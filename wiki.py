#! /usr/bin/env python3

# Created by Hans Schülein (Kamik423 contact.kamik423@gmail.com)
# 2017-11-29
# inspired by @davelevitan https://twitter.com/davelevitan/status/935619980594466816
#
# https://github.com/Kamik423/wiki_to_philosophy


import argparse
import json
import re
import urllib
import requests

import bs4
import networkx as nx


# define constants
file_name = 'graph.json'

rel_link_root = '/wiki/'
url_root = 'https://{}.wikipedia.org'
random_page_search_url = 'https://{}.wikipedia.org/w/api.php?action=query&generator=random&grnnamespace=0&prop=info&inprop=url&format=json'
top_source = 'https://en.wikipedia.org/wiki/Wikipedia:Multiyear_ranking_of_most_viewed_pages#Top-100_list'

external_link_match = re.compile(r'\<a[^\>]+?href="[^"]*\..+?\/a\>')
local_link_match = re.compile(r'\<a[^\>]+?href=\"\#[^"]*.+?\/a\>')
parentheses_match = re.compile(r'\(([^()]|\([^\)]*\))*\<a([^\(\)]|\([^\)]*\))*\)')
brackets_match = re.compile(r'\[[^\]]*\]')  # re.compile(r'\[([^\[\]]|\([^\]]*\])*\<a([^\[\]]|\[[^\]]*\])*\]')

G = nx.DiGraph()


def random_page_url():
    """return the link object to a random page.
    """
    j = list(json.loads(requests.get(random_page_search_url).text)['query']['pages'].values())[0]
    link = '<a href="{}"" title="{}""></a>'.format(j['fullurl'], j['title'])
    return bs4.BeautifulSoup(link, 'html.parser').find_all('a')[0]


def load_graph():
    """Loads graph from file.
    """
    fh = open(file_name, 'r')
    G = nx.node_link_graph(json.loads(fh.read()))
    fh.close()
    print('loaded file')
    return G


def save_graph(G):
    """Saves graph to file.
    """
    fh = open(file_name, 'w')
    fh.write(json.dumps(nx.node_link_data(G), indent=4))
    fh.close()
    if save > 1 and verbose:
        print('saved')


def name(page):
    """Gets the title of the page from any link.
    """
    return page.split('wiki/')[-1].split('#')[0]


def rel_link(page):
    """relative link for webpage: format /wiki/pagename.
    """
    return rel_link_root + page


def url(rel):
    """url for relative rel_link.
    """
    return url_root + rel


def get_next_link(link):
    """gets the next link for a relative link.
    """
    source = requests.get(url(link)).text
    soup = bs4.BeautifulSoup(source, 'html.parser')
    # get only body
    content = ''.join([str(c) for c in soup.find_all('div', class_='mw-parser-output')[0].contents])
    source = str(content)
    # remove external links
    source = re.sub(external_link_match, '', source)
    # remove internal links
    source = re.sub(local_link_match, '', source)
    # remove links in parentheses
    source = re.sub(parentheses_match, '', source)
    # remove links in brackets
    source = re.sub(brackets_match, '', source)
    # recreate soup from abbreviated source
    soup = bs4.BeautifulSoup(source, 'html.parser')
    # removes all infoboxes / sidebars &c
    for sidebox in (soup.find_all(class_='vertical-navbox') +
                    soup.find_all(class_='infobox') +
                    soup.find_all(class_='thumbinner') +
                    soup.find_all(class_='metadata') +
                    soup.find_all(class_='plainlinks') +
                    soup.find_all(class_='navbox') +
                    soup.find_all(class_='floatright') +
                    soup.find_all(class_='float-right') +
                    soup.find_all(class_='toc') +
                    soup.find_all(class_='noprint') +
                    soup.find_all(class_='navigation-not-searchable') +
                    soup.find_all(class_='mw-editsection') +
                    soup.find_all(id='coordinates') +
                    soup.find_all(role='note') +
                    soup.find_all('div') +
                    soup.find_all('sup') +
                    soup.find_all('table')):
        sidebox.decompose()
    all_links = soup.find_all('a')
    if len(all_links) == 0:
        return None
    link = soup.find_all('a')[0]
    if verbose:
        print('   ', link.get_text().ljust(70), link.get('href'))
    return link.get('href')


def trace(page):
    """traces a webpage to a dead end, loop, or tree.
    """
    t0 = 0
    if time_:
        t0 = time.time()
    page_stack = []
    if verbose:
        print('{}'.format(page.get('title')))
    else:
        print(page.get('title').ljust(50), end='')

    # initiate
    previous_page = None
    current_page = urllib.parse.unquote(name(page.get('href'))).replace('_', ' ')
    # iterative search
    while current_page not in list(G.nodes) and current_page is not None:
        page_stack.append(current_page)

        G.add_node(current_page)
        if previous_page is not None:
            G.add_edge(previous_page, current_page)
        previous_page = current_page
        next_link = get_next_link(rel_link(current_page))
        if next_link is None:
            print('{}Hit dead end after {:02d} steps'.format('    ' if verbose else '', len(page_stack)))
            return
        current_page = urllib.parse.unquote(name(next_link)).replace('_', ' ')
    # finish page
    if previous_page is not None:
        G.add_edge(previous_page, current_page)
    print('{}Hit {} after {:02d} steps'.format('    ' if verbose else '', 'loop' if current_page in page_stack else 'tree', len(page_stack)), end=' ')
    if time_:
        print('{:03.1f}s/page'.format((time.time() - t0)/(len(page_stack) + 1)), end=' ')
    if current_page in page_stack:
        print()
    else:
        # further steps to root
        further_steps = 0
        search_stack = []
        search_head = current_page
        while search_head not in search_stack:
            search_stack.append(search_head)
            further_steps += 1
            search_head = list(G.successors(search_head))[0]
        print('- {:02d} further steps to loop; {:02d} in total'.format(further_steps, further_steps + len(page_stack)))
    if save > 1:
        save_graph(G)


# argparse
parser = argparse.ArgumentParser()
parser.add_argument('-c', '--count', type=int, help='amount of random pages')
parser.add_argument('-g', '--graph', help='creates graphs', action='store_true')
parser.add_argument('-l', '--load', help='use graph.json as source not web', action='store_true')
lang_group = parser.add_mutually_exclusive_group()
lang_group.add_argument('-p', '--popular', help='search most popular pages', action='store_true')
lang_group.add_argument('-i', '--international', help='search in different language [default=en]', type=str)
parser.add_argument('-r', '--root', help='search just specified page[s], separated by ","', type=str)
parser.add_argument('-s', '--save', help='saves graph to json, -ss saves at every step', action='count')
parser.add_argument('-t', '--time', help='displays the time per online step', action='store_true')
parser.add_argument('-v', '--verbose', help='print entire path', action='store_true')

# parse arguments
args = parser.parse_args()
count = args.count
graph = args.graph
load = args.load
popular = args.popular
save = args.save or 0
locale = args.international or 'en'
time_ = args.time
verbose = args.verbose
roots = args.root

# locale
url_root = url_root.format(locale)
random_page_search_url = random_page_search_url.format(locale)

# argument dependent imports
if graph:
    import os
    from networkx.drawing.nx_agraph import to_agraph
if time_:
    import time

# parse roots
if roots is not None:
    roots = [r.lstrip().rstrip() for r in roots.split(',')]

# info print
if load:
    print('loading {}'.format(file_name))
print('searching {}:'.format(', '.join(roots) if roots is not None else ('Top 100' if popular else ('{} random page{}'.format(count, 's' if count != 1 else '') if count is not None else 'Random'))))
print('---------------')
print('graph:    {}'.format(graph))
print('save:     {}'.format('False' if not save else ('End' if save == 1 else 'Step')))
print('time:     {}'.format(time_))
print('verbose:  {}'.format(verbose))
print('---------------')

# fetch data
if load:
    # load from file
    G = load_graph()

pages = []
if roots is not None:
    # selected roots
    pages = bs4.BeautifulSoup(''.join(['<a href="{}" title="{}"></a>'.format(rel_link(root), root) for root in roots]), 'html.parser').find_all('a')
elif popular:
    print('fetching Top 100 pages')
    if verbose:
        print('from {}'.format(top_source))
    # get top 100 pages
    page = requests.get(top_source)
    soup = bs4.BeautifulSoup(page.text, 'html.parser')
    top_table = None
    # find the table (Rank* in top left corner)
    for table in soup.find_all('table', class_='wikitable'):
        if type(table) == bs4.element.Tag:
            if table.find('th') is not None:
                if table.find('th').get_text() == 'Rank*':
                    top_table = table
                    break
    for tr in top_table.find_all('tr'):
        if tr.find('a'):
            # exclude meta
            if not ('Special:' in tr.get_text() or
                    'Wikipedia:' in tr.get_text() or
                    'Portal:' in tr.get_text() or
                    'Talk:' in tr.get_text()):
                # page has no rank if meta --> column 0 is empty
                if not tr.find_all('td')[0].get_text() == '':
                    pages.append(tr.find('a'))
    print('done')
    print()

# fetch webcontent
if pages != []:
    for i, page in enumerate(pages):
        print('[{}/{}]'.format(str(i + 1).rjust(len(str(len(pages)))), len(pages)), end=' ')
        trace(page)
else:
    if count is not None:
        # search for a number of random pages
        i = 0
        for i in range(count):
            print('[{}/{}]'.format(str(i + 1).rjust(len(str(count))), count), end=' ')
            trace(random_page_url())
    else:
        # search infinteley
        while True:
            trace(random_page_url())

# save
if save == 1:
    save_graph(G)

# graphs
if graph:
    A = to_agraph(G)
    # circo exceeds memory limit or crashes in different ways. feel free to add it back in.
    layouts = ['dot', 'neato', 'fdp', 'twopi', 'lefty', 'dotty', 'osage', 'patchwork', 'sfdp', 'nop', 'wc', 'acyclic', 'gvpr', 'gvcolor', 'ccomps', 'sccmap', 'tred']
    os.makedirs('graph/{}'.format(locale), exist_ok=True)
    for layout in layouts:
        try:
            A.draw('graph/{}/{}.png'.format(locale, layout), prog=layout)
            print('drew graph for', layout)
        except Exception as e:
            print("failed with layout {}{}{}".format(layout, ' - ' if verbose else '', e if verbose else ''))

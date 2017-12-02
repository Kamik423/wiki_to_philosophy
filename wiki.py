#! /usr/bin/env python3

# Created by Hans Schülein (Kamik423 contact.kamik423@gmail.com)
# 2017-11-29
# inspired by @davelevitan https://twitter.com/davelevitan/status/935619980594466816
#
# https://github.com/Kamik423/wiki_to_philosophy


import argparse
import re
import sys


# define constants
file_name = 'graph.json'

rel_link_root = '/wiki/'
url_root = 'https://en.wikipedia.org'
top_source = 'https://en.wikipedia.org/wiki/Wikipedia:Multiyear_ranking_of_most_viewed_pages#Top-100_list'

parentheses_match = re.compile('\(([^()]|\([^\)]*\))*\<a([^()]|\([^\)]*\))*\)')
external_link_match = re.compile('\<a[^\>]*wiktionary[^\>]*>[^(\/a)]*\/a\>')

known = []
next_node = {}


def name(page):
    """Gets the title of the page from any link
    """
    return page.split('/')[-1].split('#')[0]


def rel_link(page):
    """relative link for webpage: format /wiki/pagename
    """
    return rel_link_root + page


def url(rel):
    """url for relative rel_link
    """
    return url_root + rel


def get_next_link(link):
    """gets the next link for a relative link
    """
    source = requests.get(url(link)).text
    soup = bs4.BeautifulSoup(source, 'html.parser')
    # get only body
    content = soup.find_all('div', id='mw-content-text')[0]
    source = str(content)
    # remove links in parentheses
    while re.findall(parentheses_match, source):
        source = re.sub(parentheses_match, '', source)
    # remove external links
    while re.findall(external_link_match, source):
        source = re.sub(external_link_match, '', source)
    # recreate soup from abbreviated source
    soup = bs4.BeautifulSoup(source, 'html.parser')
    content = soup
    # removes all infoboxes / sidebars &c
    for sidebox in (content.find_all(class_='vertical-navbox') +
                    content.find_all(class_='infobox') +
                    content.find_all(class_='thumbinner') +
                    content.find_all(class_='metadata') +
                    content.find_all(class_='plainlinks') +
                    content.find_all(class_='navbox') +
                    content.find_all(class_='floatright') +
                    content.find_all(class_='toc') +
                    content.find_all(class_='mw-editsection') +
                    content.find_all(id='coordinates') +
                    content.find_all(role='note') +
                    content.find_all('sup') +
                    content.find_all('table', class_='vcard')):
        sidebox.decompose()
    link = content.find_all('a')[0]
    if verbose:
        print('   ', link.get_text().ljust(70), link.get('href'))
    return link.get('href')


# argparse
parser = argparse.ArgumentParser()
parser.add_argument('-g', '--graph', help='creates graphs', action='store_true')
parser.add_argument('-l', '--load', help='use graph.json as source not web', action='store_true')
parser.add_argument('-n', '--no-nx', help='do not use networkx (disables -g -l -s)', action='store_true')
parser.add_argument('-r', '--root', help='search just specified page[s], separated by ","', type=str)
parser.add_argument('-s', '--save', help='saves graph to json', action='store_true')
parser.add_argument('-t', '--time', help='displays the time per online step', action='store_true')
parser.add_argument('-v', '--verbose', help='print entire path', action='store_true')

# parse arguments
args = parser.parse_args()
graph = args.graph
load = args.load
no_nx = args.no_nx
use_nx = not no_nx
save = args.save
time_ = args.time
verbose = args.verbose
roots = args.root

# argument dependent imports
if load or save:
    import json
if not load:
    import bs4
    import requests
if graph and use_nx:
    from networkx.drawing.nx_agraph import to_agraph
if use_nx:
    import networkx as nx
if time_:
    import time

# parse roots
if roots != None:
    roots = [r.lstrip().rstrip() for r in roots.split(',')]

# info print
if load:
    print('loading {}'.format(file_name))
else:
    print('searching {}:'.format(', '.join(roots) if roots != None else 'Top 100'))
print('---------------')
if no_nx:
    print('do not use networkx')
else:
    print('networkx: {}'.format(use_nx))
    print('graph:    {}'.format(graph))
    print('save:     {}'.format(save))
print('time:     {}'.format(time_))
print('verbose:  {}'.format(verbose))
print('---------------')

# fetch data
G = None

if load and use_nx:
    # load from file
    fh = open(file_name, 'r')
    G = nx.node_link_graph(json.loads(fh.read()))
    fh.close()
    print('loaded file')
else:
    # use WikipediA as data source
    pages = []
    if roots != None:
        pages = bs4.BeautifulSoup(''.join(['<a href="{}" title="{}"></a>'.format(rel_link(root), root) for root in roots]), 'html.parser').find_all('a')
    else:
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
                if table.find('th') != None:
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
    if use_nx:
        G = nx.DiGraph()

    # fetch webcontent
    for i, page in enumerate(pages):
        t0 = 0
        if time_:
            t0 = time.time()
        page_stack = []
        if verbose:
            print('[{}/{}] {}'.format(str(i + 1).rjust(len(str(len(pages)))), len(pages), page.get('title')))
        else:
            print(page.get('title').ljust(50), end='')

        # initiate
        previous_page = None
        current_page = name(page.get('href'))
        # iterative search
        while current_page not in known:
            page_stack.append(current_page)
            known.append(current_page)

            if use_nx:
                G.add_node(current_page)
                if previous_page != None:
                    G.add_edge(previous_page, current_page)
            next_node[previous_page] = current_page
            previous_page = current_page
            current_page = name(get_next_link(rel_link(current_page)))
        # finish page
        next_node[previous_page] = current_page
        if use_nx and not previous_page == None:
            G.add_edge(previous_page, current_page)
        print('{}Hit {} after {:02d} steps'.format('    ' if verbose else '', 'loop' if current_page in page_stack else 'tree', len(page_stack)), end = ' ')
        if time_:
            print('{:03.1f}s/page'.format((time.time() - t0)/(len(page_stack) + 1)), end=' ')
        if current_page in page_stack:
            print()
        else:
            # further steps to root
            further_steps = 0
            search_stack = []
            search_head = current_page
            while search_head in next_node and search_head not in search_stack:
                search_stack.append(search_head)
                further_steps += 1
                search_head = next_node[search_head]
            print('- {:02d} further steps to loop; {:02d} in total'.format(further_steps, further_steps + len(page_stack)))
    print()

# save
if save and use_nx:
    fh = open(file_name, 'w')
    fh.write(json.dumps(nx.node_link_data(G), indent=4))
    fh.close()
    print('saved')

# graphs
if graph and use_nx:
    A = to_agraph(G)
    # circo exceeds memory limit or crashes in different ways. feel free to add it back in.
    layouts = ['dot', 'neato', 'fdp', 'twopi', 'lefty', 'dotty', 'osage', 'patchwork', 'sfdp']
    for layout in layouts:
        try:
            A.draw('graph_{}.png'.format(layout), prog=layout)
            print('drew graph for', layout)
        except:
            print("failed with layout {}".format(layout))

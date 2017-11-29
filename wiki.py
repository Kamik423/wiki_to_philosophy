#! /usr/bin/env python3

import bs4
import requests
import re
import sys
    
debug = False

def get_next_link(link):
    source = requests.get('https://en.wikipedia.org' + link).text
    soup = bs4.BeautifulSoup(source, 'html.parser')
    content = soup.find_all('div', id='mw-content-text')[0]
    source = str(content)
    while re.findall(bracketmatch, source):
        source = re.sub(bracketmatch, '', source)
    soup = bs4.BeautifulSoup(source, 'html.parser')
    content = soup
    for note in content.find_all('div', role='note'):
        note.decompose()
    for sidebox in (content.find_all(class_='vertical-navbox') +
                    content.find_all(class_='infobox') + 
                    content.find_all(class_='thumbinner') + 
                    content.find_all(class_='metadata') + 
                    content.find_all(class_='plainlinks') + 
                    content.find_all(class_='navbox') + 
                    content.find_all(class_='floatright') + 
                    content.find_all(class_='toc') + 
                    content.find_all(class_='mw-editsection') + 
                    content.find_all('table', class_='vcard')):
        sidebox.decompose()
    for citation in content.find_all('sup'):
        citation.decompose()
    link = content.find_all('a')[0]
    if debug:
        print('   ', link.get_text().ljust(70), link.get('href'))
    return link.get('href')

top_source = 'https://en.wikipedia.org/wiki/Wikipedia:Multiyear_ranking_of_most_viewed_pages#Top-100_list'

page = requests.get(top_source)
soup = bs4.BeautifulSoup(page.text, 'html.parser')
top_table = None
for table in soup.find_all('table', class_='wikitable'):
    if type(table) == bs4.element.Tag:
        if table.find('th') != None:
            if table.find('th').get_text() == 'Rank*':
                top_table = table
                break
top_pages = []
for tr in top_table.find_all('tr'):
    if tr.find('a'):
        if not ('Special:' in tr.get_text() or 
                'Wikipedia:' in tr.get_text() or
                'Portal:' in tr.get_text() or
                'Talk:' in tr.get_text()):
            if not tr.find_all('td')[0].get_text() == '':
                top_pages.append(tr.find('a'))

bracketmatch = re.compile('\([^()]*<a[^()]*\)')
for page in top_pages:
    stack = []
    n = page.get('href')
    running = True
    print(page.get('title').ljust(30), end = ' ')
    if debug:
        print()
    while n.lower() != '/wiki/philosophy' and running:
        if n in stack:
            print('loop!', end = ' ')
            if not debug:
                print('(' + n + ')')
            else:
                print()
            running = False
            break
        stack.append(n)
        try:
            n = get_next_link(n)
        except KeyboardInterrupt:
            print('aborted')
            sys.exit()
        except:
            print('broken link!', end = ' ')
            if not debug:
                print('(' + n + ')')
            running = False
    if n.lower() == '/wiki/philosophy':
        print('found:', len(stack), 'steps')
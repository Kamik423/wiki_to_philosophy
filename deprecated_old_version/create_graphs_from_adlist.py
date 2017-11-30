#! /usr/bin/env python3

import networkx as nx
import matplotlib.pyplot as plt
import traceback
from networkx.drawing.nx_agraph import to_agraph

fh = open("graph.adjlist",'rb')
G = nx.read_adjlist(fh)
A = to_agraph(G)
# circo overloads memory
layouts = ['neato', 'dot', 'twopi', 'fdp', 'nop', 'wc', 'acyclic', 'gvpr', 'gvcolor', 'ccomps', 'sccmap', 'tred', 'sfdp']
for layout in layouts:
    try:
        A.draw('graph_{}.png'.format(layout), prog=layout)
        print('drew graph for', layout)
    except Exception as e:
        print("failed with layout {}".format(layout))
        traceback.print_exc()

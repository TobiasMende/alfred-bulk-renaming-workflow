#!/usr/bin/python
from item_helpers import *

query = sys.argv[1]

items = [pattern_item('Enter or choose a pattern to match the input files', query),
         pattern_item('Match Everything Before a -', '(.*)-.*')]

show(items)

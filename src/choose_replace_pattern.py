#!/usr/bin/python
from item_helpers import *

query = sys.argv[1]

items = []

items.append(pattern_item('Enter or choose a pattern to replace the names with', query))
items.append(pattern_item('Append a serial number', '$0-{n}'))
items.append(pattern_item('Prepend current date', '{d} $0'))
items.append(pattern_item('Switch two matches', '$2$1'))

show(items)
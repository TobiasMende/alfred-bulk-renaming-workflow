#!/usr/bin/python
from item_helpers import *

query = sys.argv[1]

items = [pattern_item('Enter or choose a pattern to replace the names with', query),
         pattern_item('Append a serial number', '$0-{n}'),
         pattern_item('Prepend current date', '{d} $0'),
         pattern_item('Capitalize words', 'c/$0'),
         pattern_item('Replace dashes with spaces', 'r(-, )/$0'),
         pattern_item('Replace dashes with spaces and capitalize words', 'r(-, )/c/$0'),
         pattern_item('Switch two matches', '$2$1')]

show(items)

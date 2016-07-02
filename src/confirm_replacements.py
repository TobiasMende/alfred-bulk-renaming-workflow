#!/usr/bin/python
from item_helpers import *

argument = os.environ['mapping']
translations = json.loads(argument)

default = {'valid': True,
           'title': 'Press Enter to perform the following replacements',
           'subtitle': 'Press ESC to abort the renaming process'}

items = map(lambda pair: mapping_item(pair[0], pair[1]), translations)
items = [default] + items

show(items)

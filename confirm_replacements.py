#!/usr/bin/python
import sys
import os
import json

argument = os.environ['mapping']
translations = json.loads(argument) 

def make_item(orig, renamed):
  item = {}
  item['valid'] = False
  item['title'] = os.path.basename(orig)
  item['subtitle'] = os.path.basename(renamed)

  icon = {}
  icon['type'] = 'fileicon'
  icon['path'] = orig
  item['icon'] = icon

  alt = {}
  alt['title'] = orig
  alt['subtitle'] = renamed
  item['mods'] = {'alt' : alt}
  return item

default = {}
default['valid'] = True
default['title'] = 'Press Enter to perform the following replacements'
default['subtitle'] = 'Press ESC to abort the renaming process'

items = map(lambda pair: make_item(pair[0], pair[1]), translations)
items = [default] + items

output = {}
output['items'] = items

output_json = json.dumps(output)

sys.stdout.write(output_json)

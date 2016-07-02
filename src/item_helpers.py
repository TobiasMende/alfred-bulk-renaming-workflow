import sys
import json
import os

def pattern_item(title, pattern):
  item = {}
  item['valid'] = True
  item['title'] = title
  item['subtitle'] = pattern
  item['arg'] = pattern
  item['autocomplete'] = pattern
  return item

def mapping_item(orig, renamed):
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

def show(items):
    output = {}
    output['items'] = items
    output_json = json.dumps(output)
    sys.stdout.write(output_json)
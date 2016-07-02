import sys
import json
import os


def pattern_item(title, pattern):
    item = {'valid': True,
            'title': title,
            'subtitle': pattern,
            'arg': pattern,
            'autocomplete': pattern}
    return item


def mapping_item(orig, renamed):
    item = {'valid': False,
            'title': os.path.basename(orig),
            'subtitle': os.path.basename(renamed)}

    icon = {'type': 'fileicon',
            'path': orig}

    item['icon'] = icon

    alt = {'title': orig,
           'subtitle': renamed}
    item['mods'] = {'alt': alt}
    return item


def show(items):
    output = {'items': items}
    output_json = json.dumps(output)
    sys.stdout.write(output_json)

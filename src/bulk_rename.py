#!/usr/bin/python
import sys
import os
import json
import shutil

mapping = json.loads(os.environ['mapping'])

try:
    for pair in mapping:
        shutil.move(pair[0], pair[1])
    sys.stdout.write('File Rename Finished')
except:
    sys.stdout.write('Failed to rename files')

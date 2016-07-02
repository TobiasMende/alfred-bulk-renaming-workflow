#!/usr/bin/python
import sys
import re
import os
import json

mapping = json.loads(os.environ['mapping'])

try:
  for pair in mapping:
    os.rename(pair[0], pair[1])
  sys.stdout.write('File Rename Finished')
except:
  sys.stdout.write('Failed to rename files')
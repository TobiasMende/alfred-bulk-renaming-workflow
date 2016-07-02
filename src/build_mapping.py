#!/usr/bin/python
import json
import os
import sys

from src.algo.build_mapping import build_filename_translations

files = os.environ['files'].split('\t')
match_pattern = os.environ['match_pattern']
replace_pattern = os.environ['replace_pattern']

translations = build_filename_translations(files, match_pattern, replace_pattern)

argument = json.dumps(translations)
sys.stdout.write(argument)

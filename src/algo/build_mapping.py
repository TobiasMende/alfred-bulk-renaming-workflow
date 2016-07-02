import datetime
import os
import re


def extract_options(match_pattern_parts):
    if len(match_pattern_parts) > 1:
        return match_pattern_parts[0:-1]


def apply_options(new_name, options):
    if options is None:
        return new_name
    for option in options:
        if len(option) == 0:
            continue
        if option == 'c':
            new_name = new_name.title()
        elif option[0] == 'r':
            replace_part = option[2:-1]
            replace_parts = replace_part.split(',')
            new_name = new_name.replace(replace_parts[0], replace_parts[1])

    return new_name


def build_filename_translations(files, match_pattern, replace_pattern):
    date = datetime.datetime.now().strftime('%Y-%m-%d')
    replace_pattern_parts = replace_pattern.split('/')
    replace_pattern = replace_pattern_parts[-1]
    options = extract_options(replace_pattern_parts)
    match_regex = re.compile(match_pattern)
    serial_number = 1
    translations = []
    for file in files:
        root, ext = os.path.splitext(file)
        path = os.path.dirname(root)
        base = os.path.basename(root)

        new_name = replace_pattern.replace('{n}', str(serial_number))
        new_name = new_name.replace('{d}', str(date))
        new_name = new_name.replace('$0', base)
        serial_number += 1

        matches = match_regex.match(base)
        if matches is not None:
            groups = matches.groups()
            var_count = 1
            for group in groups:
                new_name = new_name.replace('${}'.format(var_count), group)
                var_count += 1

            for var_count in range(var_count, 10):
                new_name = new_name.replace('${}'.format(var_count), '')

        new_name = apply_options(new_name, options)

        new_name += ext
        new_path = os.path.join(path, new_name)

        translations.append((file, new_path))

    return translations
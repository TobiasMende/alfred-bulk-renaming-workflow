import datetime
import os
import re


def build_filename_translations(files, match_pattern, replace_pattern):
    date = datetime.datetime.now().strftime('%Y-%m-%d')
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
            re.su
            var_count = 1
            for group in groups:
                new_name = new_name.replace('${}'.format(var_count), group)
                var_count += 1

            for var_count in range(var_count, 10):
                new_name = new_name.replace('${}'.format(var_count), '')

        new_name += ext
        new_path = os.path.join(path, new_name)

        translations.append((file, new_path))

    return translations
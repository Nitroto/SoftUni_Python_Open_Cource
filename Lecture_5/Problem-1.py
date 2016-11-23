import os
import sys
import fnmatch

params = sys.argv

if len(sys.argv) < 3:
    print('Please provide at least 2 parameters!')
    sys.exit(0)
else:
    directory = params[1]
    full_file_name = params[2]
    file_name, file_ext = os.path.split(full_file_name)
    locations = []

    for root, dirs, files in os.walk(directory):
        for file in files:
            if fnmatch.fnmatch(file, full_file_name):
                locations.append(os.path.join(root, file))

    if len(locations) > 0:
        for match in locations:
            print(match)
    else:
        print('File was not found!')

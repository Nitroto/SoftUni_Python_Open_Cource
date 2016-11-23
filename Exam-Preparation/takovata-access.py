import re


def has_a_params(str):
    try:
        str.index('?')
        return True
    except ValueError:
        return False


file_path = input()
pages = []

with open(file_path, encoding='utf-8') as f:
    for line in f:
        m = re.search('url="(/.+?)".*resp_t="(.+?)"', line)
        if (m.group(1).find('/ws/') == -1):
            if (has_a_params(m.group(1))):
                index = m.group(1).index('?')
                current_entry = (m.group(1)[:index], m.group(2))
            else:
                current_entry = (m.group(1), m.group(2))
            pages.append(current_entry)

pages_unique = {}
for entry in pages:
    url = entry[0]
    time = entry[1]
    if (url not in pages_unique):
        pages_unique[url] = [0, 0]
    pages_unique[url][0] = pages_unique[url][0] + 1
    pages_unique[url][1] = pages_unique[url][1] + float(time)

pages_avarege_time = []
for entry in pages_unique:
    times = float(pages_unique[entry][0])
    time = float(pages_unique[entry][1])
    avg = time / times
    pages_avarege_time.append((entry, avg))

pages_avarege_time = sorted(pages_avarege_time, key=lambda tup: tup[1])
print('{}\n{:.3f}'.format(pages_avarege_time[-1][0], pages_avarege_time[-1][1]))

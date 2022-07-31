import re
pattern = re.compile("#.+")

for i, line in enumerate(open('hard_en_main.c')):
    for match in re.finditer(pattern, line):
        print('Found on line %s: %s' % (i+1, match.group()))


# for line in open('hard_en_main.c'):
#     for match in re.finditer(pattern, line):
#         print(line)
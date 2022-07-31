
import re

def file_parser(args):
    pattern = re.compile(
        r"(\s*#ifndef.*)|(\s*#if.*)|(\s*#else.*)|(\s*#endif.*)|(\s*#ifdef.*)|((static |static inline )?[a-z]+ \w+\(.*(\s*.*\s*.*\))?)")

    tab = 0

    move_right_statements = ["#if", '#ifndef', '#ifdef']
    single_move_left_statements = ["#else"]
    move_left_statements = ["#endif"]

    for i, line in enumerate(open(args.path, 'r').read().splitlines()):

        for match in re.finditer(pattern, line):
            if any(line.startswith(statement) for statement in move_right_statements):
                print('line %s' % (i + 1) + ': ' + (' ' * tab) + '%s' % (match.group()))
                tab += 4

            elif any(line.startswith(statement) for statement in single_move_left_statements):
                tab -= 4
                print('line %s' % (i + 1) + ': ' + (' ' * tab) + '%s' % (match.group()))
                tab += 4

            elif any(line.startswith(statement) for statement in move_left_statements):
                tab -= 4
                print('line %s' % (i + 1) + ': ' + (' ' * tab) + '%s' % (match.group()))

            elif tab > 0:
                print('line %s' % (i + 1) + ': ' + (' ' * tab) + '%s' % (match.group()))
                multi_line = ''

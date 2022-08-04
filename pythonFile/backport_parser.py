'''
python script that order any programing file
'''
import re

def file_parser(args):
    # My variable
    if_statements = "#if"
    else_statements = "#else"
    endif_statements = "#endif"
    func_statements = ["void", "int", "bool", "string"]

    tab = 0
    # reading loop from a programing file
    for i, line in enumerate(open(args.path, 'r').read().splitlines()):
        # searching for the regular expression that we need
        if_pattern= re.search(f"\s*{if_statements}.*", line)
        else_pattern = re.search(f"\s*{else_statements}.*", line)
        endif_pattern = re.search(f"\s*{endif_statements}.*", line)
        # check if we have any regular expression in the reading line
        if if_pattern: # have if_statements
            print('line %s' % (i + 1) + ': ' + (' ' * tab) + '%s' % (if_pattern.group()))
            tab += 4

        elif else_pattern: # have else_statements
            tab -= 4
            print('line %s' % (i + 1) + ': ' + (' ' * tab) + '%s' % (else_pattern.group()))
            tab += 4

        elif endif_pattern: # have endif_statements
            tab -= 4
            print('line %s' % (i + 1) + ': ' + (' ' * tab) + '%s' % (endif_pattern.group()))

        else: # have function_statements
            for statement in func_statements:
                func_pattern = re.search(f"\s*{statement} \w+\(.*", line)
                if func_pattern and tab > 0:
                    print('line %s' % (i + 1) + ': ' + (' ' * tab) + '%s' % (func_pattern.string))

'''
  python script that order any programing file
'''

import re

def file_parser(args):
    # My variable
    if_statements = "#if"
    else_statements = "#else"
    elif_statements = "#elif"
    endif_statements = "#endif"
    include_statements = '#include'
    func_statements = ["void", "int", "bool", "string"]

    tab = 0
    tab_size = 4
    with open('output_' + args.path, 'w') as Write_file:
        with open(args.path, 'r') as Read_file:
            # reading loop from a programing file
            for i, line in enumerate(Read_file.readlines()):

                # searching for the regular expression that we need
                if_pattern = re.search(f"\s*{if_statements}.*", line)
                elif_pattern = re.search(f"\s*{elif_statements}.*", line)
                else_pattern = re.search(f"\s*{else_statements}.*", line)
                endif_pattern = re.search(f"\s*{endif_statements}.*", line)
                include_pattern = re.search(f"\s*{include_statements}.*", line)
                # check if we have any regular expression in the reading line

                if if_pattern:  # have if_statements
                    debug_print(tab, if_pattern.group())
                    # print(f"line {i + 1}: {' ' * tab}{if_pattern.group()}")
                    Write_file.write((' ' * tab) + if_pattern.group() + '\n')
                    tab += tab_size

                elif else_pattern:  # have else_statements
                    tab -= tab_size
                    debug_print(tab, else_pattern.group())
                    # print(f"line {i + 1}: {' ' * tab}{else_pattern.group()}")
                    Write_file.write((' ' * tab) + else_pattern.group() + '\n')
                    tab += tab_size

                elif elif_pattern:  # have elif_statements
                    tab -= tab_size
                    debug_print(tab, elif_pattern.group())
                    # print(f"line {i + 1}: {' ' * tab}{elif_pattern.group()}")
                    Write_file.write((' ' * tab) + elif_pattern.group() + '\n')
                    tab += tab_size

                elif endif_pattern:  # have endif_statements
                    tab -= tab_size
                    debug_print(tab, endif_pattern.group())
                    # print(f"line {i + 1}: {' ' * tab}{endif_pattern.group()}")
                    Write_file.write((' ' * tab) + endif_pattern.group() + '\n')

                elif include_pattern:  # have include_statements
                    debug_print(tab, include_pattern.group())
                    # print(f"line {i + 1}: {' ' * tab}{include_pattern.group()}")
                    Write_file.write((' ' * tab) + include_pattern.group() + '\n')

                else:  # have function_statements
                     for statement in func_statements:
                        func_pattern = re.search(fr"(\s*{statement}) (\w+)(\()", line)
                        if func_pattern and tab > 0:
                            debug_print(tab, func_pattern.group(2))
                            # print(f"line {i + 1}: {' ' * tab}{func_pattern.group(2)}")
                            Write_file.write(f"{' ' * tab}{func_pattern.group(2)}" + '\n')

def debug_print(tabs, group):
    print(f"{' ' * tabs}{group}")
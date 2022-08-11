import backport_parser
import argparse

# Create the parser
parser = argparse.ArgumentParser(description='Automatic full file review for defines and functions order')

# Add Arguments
parser.add_argument('-p', '--path', type=str, default=False,
                    help='Set a file path to review')
parser.add_argument('-l', '--with_line_number', action='store_true',
                    help='Set a line number')
# Parse the argument
args = parser.parse_args()

backport_parser.file_parser(args)


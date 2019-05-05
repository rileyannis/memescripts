
#!/usr/bin/env python3

import argparse
from string import ascii_letters


def add_args_to_parser(parser):
    parser.add_argument('input_string', help='the string to decap')

    return parser

def build_parser_standalone():
    parser = argparse.ArgumentParser(description="decap")
    return add_args_to_parser(parser)


def main(args):

    decapitated_string = ""
    caps = True

    for c in args.input_string:

        # "hello world" should be "HeLlO wOrLd" and not "HeLlO WoRlD"
        if c not in ascii_letters:
            decapitated_string += c
        else:
            decapitated_string += c.lower() if caps else c.upper()
            caps^=True

    print(decapitated_string)

if __name__ == "__main__":
    args = build_parser_standalone().parse_args()
    main(args)

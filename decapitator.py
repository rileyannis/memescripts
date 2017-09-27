#!/usr/bin/env python3

import argparse

def get_args():
    parser = argparse.ArgumentParser(description="decap")
    parser.add_argument('input_string', help='the string to decap')

    return parser.parse_args()

def main():
    args = get_args()

    decapitated_string = ""
    index = 0

    for c in args.input_string:
        if index % 2 == 0:
            decapitated_string += c.upper()
        else:
            decapitated_string += c.lower()
        index += 1

    print(decapitated_string)

if __name__ == "__main__":
    main()
#!/usr/bin/env python3

import argparse

def add_args_to_parser(parser):
    parser.add_argument('input_string', help='the string to rot13')
    return parser

def build_parser_standalone():
    parser = argparse.ArgumentParser(description="rot13")
    return add_args_to_parser(parser)

normal = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
encrypted = "nopqrstuvwxyzabcdefghijklmNOPQRSTUVWXYZABCDEFGHIJKLM"

ENCRYPTDICT = {plain: cipher for plain, cipher in zip(normal, encrypted)}


def encrypt(x):
    return ENCRYPTDICT.get(x, x)

def main(args):
    unencryptedString = args.input_string
    encryptedString = "".join([encrypt(x) for x in unencryptedString])

    print(encryptedString)

if __name__ == "__main__":
    args = build_parser_standalone().parse_args()
    main(args)

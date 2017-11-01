#!/usr/bin/env python3

import argparse
import os

def main():
    parser = argparse.ArgumentParser(description="decap")
    parser.add_argument('meme', help='the script to run')
    parser.add_argument('cla', help='arg to provide the script')
    args = parser.parse_args()

    for f in os.listdir("."):
        print(f)
        if f.endswith(".py"):
            print(f)
            if f[:-3] == args.meme:
                print(f)
            exec("import " + args.meme)
            print(args.cla)
            eval(args.meme + ".main(\"" + args.cla + "\")")
            return
    else:
        print(args.meme + " is not a valid memescript m'dude!")
    

if __name__ == "__main__":
    main()

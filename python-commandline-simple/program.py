#!/usr/bin/env python
"""
{{Program name}}: {{Program description}}
"""
import argparse
import sys

#import support_modules


def main():
    """
    primary function for command-line execution. return an exit status integer
    or a bool type (where True indicates successful exection)
    """
    argp = argparse.ArgumentParser(description=(
        "{{Program description}}"))
    argp.add_argument('inputfiles', nargs="+", help=(
        "{{Description of input files}}"))
    argp.add_argument('-d', '--debug', action="store_true", help=(
        "enable debugging output"))
    args = argp.parse_args()

    # do things

    return True


if __name__ == '__main__':
    RESULT = main()
    sys.exit(int(not RESULT if isinstance(RESULT, bool) else RESULT))

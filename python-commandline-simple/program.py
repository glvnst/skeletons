#!/usr/bin/env python
"""
{{Program name}}: {{Program description}}
"""
import argparse
import sys
import datetime


def main():
    """
    direct program entry point
    return an exit status integer suitable for use with sys.exit
    """
    argp = argparse.ArgumentParser(
        description=(
            "{{Program description}}"),
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    argp.add_argument('inputfiles', nargs="+", help=(
        "{{Description of input files}}"))
    argp.add_argument('-d', '--debug', action="store_true", help=(
        "enable debugging output"))
    args = argp.parse_args()

    # do things

    return 0


def warn(message):
    """
    Print the given message to stderr, with timestamp prepended and newline
    appended, return the message unchanged
    """
    sys.stderr.write("{} {}\n".format(datetime.datetime.now(), message))
    return message


if __name__ == '__main__':
    try:
        RESULT = main()
    except KeyboardInterrupt:
        sys.stderr.write("\n")
        RESULT = 1
    sys.exit(RESULT)

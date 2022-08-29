import argparse
import sys

from genericformat.genericformat import format


def main():
    parser = argparse.ArgumentParser(description="format some code with a formatter")
    parser.add_argument("code", type=str, help="the code to format")
    parser.add_argument(
        "--formatter",
        dest="formatter",
        required=True,
        help="path to the formatter to run",
    )

    args = parser.parse_args()
    formatted = format(formatter=args.formatter, code=args.code)

    if formatted:
        sys.stdout.write(formatted)


if __name__ == "__main__":
    main()

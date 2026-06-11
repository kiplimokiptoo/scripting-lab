import argparse

from lib.generate_log import generate_log


def main():
    parser = argparse.ArgumentParser(description="Write log entries to a dated text file.")
    parser.add_argument("entries", nargs="*", help="Log entries to write.")
    args = parser.parse_args()
    generate_log(args.entries)


if __name__ == "__main__":
    main()

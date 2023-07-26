"""Console script for pytfcreds."""
import argparse
import sys

import pytfcreds.pytfcreds as creds


def main():
    """Console script for pytfcreds."""
    parser = argparse.ArgumentParser()
    parser.add_argument("command", choices=["get", "store", "forget"])
    parser.add_argument("--host", required=True)
    parser.add_argument("--user", required=True)
    args = parser.parse_args()

    func = getattr(creds, args.command)
    return func(args.host, args.user)


if __name__ == "__main__":
    sys.exit(main())  # pragma: no cover

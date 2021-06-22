import argparse
import sys

from base45 import b45decode, b45encode


def main() -> None:
    """Main function"""

    parser = argparse.ArgumentParser(description="Base45 encoder/decoder")
    parser.add_argument(
        "--encode",
        action="store_true",
        help="Encode data",
    )
    parser.add_argument(
        "--decode",
        action="store_true",
        help="Decode data",
    )
    args = parser.parse_args()

    if args.encode:
        data = sys.stdin.buffer.read()
        sys.stdout.write(b45encode(data).decode())
    elif args.decode:
        data = sys.stdin.buffer.read()
        sys.stdout.buffer.write(b45decode(data.decode()))
    else:
        parser.print_help()
        sys.exit(1)


if __name__ == "__main__":
    main()

import argparse


parser = argparse.ArgumentParser(description="My own wc implementation")


parser.add_argument("file", type=str, help="file to count")
parser.add_argument("-l", "--lines", action="store_true", help="count lines")
parser.add_argument("-w", "--words", action="store_true", help="count words")
parser.add_argument("-c", "--bytes", action="store_true", help="count bytes")
parser.add_argument("-m", "--chars", action="store_true", help="count chars")

args = parser.parse_args()

file = args.file
lines = args.lines
words = args.words
bytes = args.bytes
chars = args.chars

with open(file, "r") as f:
    content = f.read()
    lines_count = len(content.split("\n"))
    words_count = len(content.split())
    bytes_count = len(content.encode("utf-8"))
    chars_count = len(content)

    if lines:
        print(f"lines count: {lines_count} in {file}")
    elif words:
        print(f"words count: {words_count} in {file}")
    elif bytes:
        print(f"bytes count: {bytes_count} in {file}")
    elif chars:
        print(f"chars count: {chars_count} in {file}")
    else:
        print(
            f"lines count: {lines_count}, \nwords count: {words_count}, \nbytes count: {bytes_count}, \nchars count: {chars_count} in {file}"
        )

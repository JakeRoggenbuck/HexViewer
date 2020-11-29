import argparse
import string
import mmap



def main(input_file):
    with open(input_file, "r+b") as file:
        mm = mmap.mmap(file.fileno(), 0)
        y = 0
        for x in range(1000):
            print("".join(
                chr(mm[y+x]) if chr(mm[y+x]) in string.printable
                else "."
                for x in range(16)
            ))
            y += 16


def maino(input_file):
    with open(input_file, "r+b") as file:
        mm = mmap.mmap(file.fileno(), 0)
        y = 0
        for x in range(1000):
            layer = ""
            for x in range(16):
                if (char := chr(mm[y+x])) in string.printable:
                    layer += char
                else:
                    layer += "."
            y += 16
            print(layer)


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("-i", help="Input video file")
    return parser.parse_args()


if __name__ == "__main__":
    args = parse_args()
    main(args.i)

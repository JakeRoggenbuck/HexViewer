import argparse
import string
import mmap
import os
from termcolor import colored


class HexEditor:
    def __init__(self, input_file: str):
        self.input_file = input_file

    def render(self, start: int, buff: int):
        self.start = start
        self.buff = buff
        self.end = start + buff

        for x in self.get_hex():
            print(x)

    def get_hex(self) -> list:
        with open(self.input_file, "r+b") as file:
            mm = mmap.mmap(file.fileno(), 0)
            pointer = self.start

            for layer_num in range(self.start, self.end):
                pre_layer = ""
                layer = ""
                for x in range(16):
                    pre_layer += hex(mm[pointer+x])[2:].ljust(2) + " "
                    if (char := chr(mm[pointer+x])) in string.printable:
                        layer += colored(char, "red")
                    else:
                        layer += "."
                pointer += 16
                yield pre_layer + " " + layer


def main(args):
    start = 0
    buff = 20
    he = HexEditor(args.i)
    he.render(start, buff)

    while 1:
        check = input("> ")
        os.system("clear")
        if check == "j":
            start -= 16
            he.render(start, buff)
        if check == "k":
            start += 16
            he.render(start, buff)


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("-i", help="Input video file")
    return parser.parse_args()


if __name__ == "__main__":
    args = parse_args()
    main(args)

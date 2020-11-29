import argparse
import string
import mmap
import os


class Foo:
    def __init__(self, input_file: str):
        self.input_file = input_file

    def render(self, start: int = 0, buff: int = 10):
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
                layer = ""
                for x in range(16):
                    if (char := chr(mm[pointer+x])) in string.printable:
                        layer += char
                    else:
                        layer += "."
                pointer += 16
                yield layer

def main(args):
    foo = Foo(args.i)
    foo.render()

    start = 0
    buff = 10
    while 1:
        check = input("> ")
        os.system("clear")
        if check == "j":
            start -= 16
            foo.render(start, buff)
        if check == "k":
            start += 16
            foo.render(start, buff)


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("-i", help="Input video file")
    return parser.parse_args()


if __name__ == "__main__":
    args = parse_args()
    main(args)

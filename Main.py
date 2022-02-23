import tkinter as tk
import sys
import argparse

from DataType import ImageController

class MainWindow:

    def __init__(self, root, inputDirectory):
        self.root = root
        self.root.title("Dalli Klick")

        self.root.attributes('-fullscreen', True)
        self.root.bind('<Escape>', self.toggle_fullscreen)
        self.root.bind('<Return>', self.next_image)
        self.root.bind("<space>", self.next_tile)

        self.canvas = tk.Canvas(root, bg='white', highlightthickness=0)
        self.canvas.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

        self.canvas.create_text((100,100), text='Dalli Klick')
        self.imageController = ImageController(self.root, self.canvas, inputDirectory)

    def toggle_fullscreen(self, event):
        state = False if self.root.attributes('-fullscreen') else True
        self.root.attributes('-fullscreen', state)
        if not state:
            self.root.geometry('1024x768+50+50')

    def next_image(self, event):
        self.imageController.next_image()

    def next_tile(self, event):
        self.imageController.next_tile()


def create_arg_parser():
    parser = argparse.ArgumentParser(description='"Dalli Klick" Desktop App.')
    parser.add_argument('inputDirectory', help='Path to the input directory.')
    return parser

def main():

    arg_parser = create_arg_parser()
    parsed_args = arg_parser.parse_args(sys.argv[1:])

    root = tk.Tk()
    app = MainWindow(root, parsed_args.inputDirectory)
    root.mainloop()

if __name__ == '__main__':
    main()
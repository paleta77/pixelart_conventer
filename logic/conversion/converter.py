from PIL import Image
from PIL.Image import Palette
from numpy import array
from .block import Block


class Converter:

    def __init__(self, image_path) -> None:
        self.image_path = image_path

    def load_image_as_array(self, path):
        image = Image.open(path)
        return array(image)

    def convert(self, block_size, number_of_colors):
        image = self.load_image_as_array(self.image_path)

        columns, rows, _ = image.shape
        for row in range(0, rows, block_size):
            for column in range(0, columns, block_size):
                column_start = column
                column_end = column + block_size

                row_start = row
                row_end = row + block_size
                block = Block(
                    image[column_start:column_end, row_start:row_end]
                    )
                block.set_average_color_of_block()

        return Image.fromarray(image, mode="RGB").convert("P", palette=Image.ADAPTIVE, colors=number_of_colors)

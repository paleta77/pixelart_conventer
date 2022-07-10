from PIL import Image
from numpy import array
from conversion.block import Block


class Conventer():

    def __init__(self, image_path, block_size) -> None:
        self.image_path = image_path
        self.block_size = block_size

    def load_image_as_array(self, path):
        image = Image.open(path)
        return array(image)

    def convert(self):
        image = self.load_image_as_array(self.image_path)

        columns, rows, _ = image.shape
        for row in range(0, rows, self.block_size):
            for column in range(0, columns, self.block_size):
                column_start = column
                column_end = column + self.block_size

                row_start = row
                row_end = row + self.block_size
                block = Block(
                    image[column_start:column_end, row_start:row_end]
                    )
                block.set_avarage_color_of_block()

        return Image.fromarray(image, mode="RGB")

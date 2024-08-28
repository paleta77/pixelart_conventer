import numpy


class Block():

    def __init__(self, pixels) -> None:
        self.pixels = pixels

    def _set_color_of_block(self, red, green, blue):
        columns, rows, _ = self.pixels.shape
        for row in range(0, rows):
            for column in range(0, columns):
                self.pixels[column][row] = [red, green, blue]

    def _get_average_color_of_block(self):
        average_rows = numpy.average(self.pixels, axis=0)
        average = numpy.average(average_rows, axis=0)
        return average

    def set_average_color_of_block(self):
        red, green, blue = self._get_average_color_of_block()
        self._set_color_of_block(red, green, blue)

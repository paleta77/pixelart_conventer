from conversion import converter


def main():
    image_path = "image.jpg"
    block_size = 16

    pixel_converter = converter.Converter(image_path, block_size)

    converted_image = pixel_converter.convert()
    converted_image.save("converted.png")


if __name__ == "__main__":
    main()

from conversion import conventer


def main():
    image_path = "image.jpg"
    block_size = 8

    pixel_conventer = conventer.Conventer(image_path, block_size)

    converted_image = pixel_conventer.convert()
    converted_image.save("converted.png")


if __name__ == "__main__":
    main()

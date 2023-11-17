# run: python shirt.py before1.jpg after1.jpg
from PIL import Image, ImageOps
import sys

def main():
    if len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")
    else:
        first_file = sys.argv[1]
        second_file = sys.argv[2]
        first_file_ext = first_file.lower().split(".")[-1]
        second_file_ext = second_file.lower().split(".")[-1]
        if second_file_ext not in ["jpg", "png"]:
            sys.exit("Invalid output")
        if first_file_ext != second_file_ext:
            sys.exit("Input and output have different extensions")
        try:
            # Open image files
            first_file_img = Image.open(first_file)
            shirt_img = Image.open("./shirt.png")

            # Use ImageOps.fit to crop and resize the image to fit within the bounding box
            # Crop the before image so that it fits with the shirt image
            fit_first_file_img = ImageOps.fit(first_file_img, shirt_img.size)#, centering=(1.0,0.0))

            fit_first_file_img.paste(shirt_img, box=(0,0), mask=shirt_img)#, (90, 600))

            # Display or save the resulting image
            # first_file_img.show()
            # fit_first_file_img.show()
            fit_first_file_img.save(second_file)
            return 0
        except FileNotFoundError:
            sys.exit(f"Input does not exist")
        except Exception as e:
            sys.exit(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
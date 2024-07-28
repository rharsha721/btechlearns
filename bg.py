from PIL import Image
import time
img_path = input("Enter image name/path: ")
img_path = img_path.replace('\\', '/')
try:
    img = Image.open(img_path)
    box = (100, 100, 400, 400)
    region = img.crop(box)

    # Display the original image
    img.show()
    time.sleep(5) #3 seconds delay
    # Display the cropped region
    region.show()
    region = region.transpose(Image.Transpose.ROTATE_180)
    img.paste(region, box)
except FileNotFoundError:
    print("Image name not found")
except OSError:
    print("Image path is not found")

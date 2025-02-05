from PIL import Image
import os

# Provide the full path to the image
image_file = "./wolf.avif"  # Or use the absolute path, e.g., "/Users/yourname/images/wolf.avif"

# Debug: Print out the full path
print(f"Full path to image: {os.path.abspath(image_file)}")

# Try opening the image
try:
    img = Image.open(image_file)
    print(f"Image format: {img.format}")  # Should print "AVIF"
    img.show()  # This should display the image in your default image viewer
except Exception as e:
    print(f"Error opening image: {e}")

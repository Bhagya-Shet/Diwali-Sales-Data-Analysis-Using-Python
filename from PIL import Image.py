from PIL import Image
import matplotlib.pyplot as plt

# Load the uploaded image
image_path = "/mnt/data/WhatsApp Image 2025-08-14 at 6.20.42 PM.jpeg"
img = Image.open(image_path)

# Display the original image
plt.figure(figsize=(8, 10))
plt.imshow(img)
plt.axis('off')
plt.title("Original Image")
plt.show()
from PIL import Image, ImageDraw
import cv2
import numpy as np

# Load the image
img_path = "WhatsApp Image 2025-08-14 at 6.20.42 PM.jpeg"
img = cv2.imread(img_path)

# Convert to RGB for PIL compatibility
img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
pil_img = Image.fromarray(img_rgb)

# Create a drawing context
draw = ImageDraw.Draw(pil_img)

# Example area to paint over the hand (you'll need to adjust this manually based on the image)
# Format: (x1, y1, x2, y2)
hand_area = (180, 100, 270, 250)
dress_sleeve_color = (152, 84, 112)  # Sample color to blend with the dress

# Paint over the hand
draw.rectangle(hand_area, fill=dress_sleeve_color)

# Save or show the result
pil_img.save("edited_image.jpg")
pil_img.show()

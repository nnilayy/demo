from PIL import Image

# Create a transparent 1x1 PNG
img = Image.new("RGBA", (1, 1), (0, 0, 0, 0))  # fully transparent
img.save("pixel.png", "PNG")

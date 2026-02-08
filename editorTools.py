# =========================
# editorTools.py
# =========================

from PIL import Image, ImageDraw
from datetime import datetime


def stamp_creation_time(img: Image.Image) -> Image.Image:
    """
    Adds the current date and time to the bottom-left corner of the image.
    """
    # Create a drawing context
    draw = ImageDraw.Draw(img)

    # Format current date and time
    text = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    # Padding from image edges
    padding = 10
    x = padding
    y = img.height - padding - 15  # Position text slightly above bottom edge

    # Draw shadow for readability
    draw.text((x + 1, y + 1), text, fill="black")
    # Draw main text
    draw.text((x, y), text, fill="white")

    return img


def add_overlay(
    img: Image.Image,
    overlay_name: str,
    stickers_folder: str = "Stickers"
) -> Image.Image:
    """
    Adds a sticker image to the bottom-right corner of the image.
    """
    # If no overlay was chosen, return the image unchanged
    if overlay_name == "":
        return img

    overlay_path = f"{stickers_folder}/{overlay_name}"

    try:
        # Load overlay and ensure transparency support
        overlay = Image.open(overlay_path).convert("RGBA")
    except Exception as e:
        print(f"\nCould not load overlay: {e}")
        return img

    # Convert base image to RGBA for proper compositing
    base = img.convert("RGBA")

    # Scale overlay to 20% of the image width
    target_width = int(base.width * 0.20)
    scale = target_width / overlay.width
    new_height = int(overlay.height * scale)
    overlay = overlay.resize((target_width, new_height))

    # Position overlay with padding from edges
    padding = 10
    x = base.width - overlay.width - padding
    y = base.height - overlay.height - padding

    # Paste overlay using its alpha channel
    base.paste(overlay, (x, y), overlay)

    # Convert back to RGB for saving
    return base.convert("RGB")

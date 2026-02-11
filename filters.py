from PIL import Image, ImageFilter, ImageEnhance, ImageOps

def ensure_rgb(img):
    """
    Ensures the image is in RGB mode.
    Some filters require RGB images to work correctly.
    """
    if img.mode != "RGB":
        return img.convert("RGB")
    return img


def apply_calm(img, style):
    """
    Applies a calm visual effect using reduced color and soft blur.
    """
    img = ensure_rgb(img)

    if style == "intense":
        img = ImageEnhance.Color(img).enhance(0.55)
        img = img.filter(ImageFilter.GaussianBlur(radius=2.2))
    else:
        img = ImageEnhance.Color(img).enhance(0.75)
        img = img.filter(ImageFilter.GaussianBlur(radius=1.2))

    return img


def apply_angry(img, style):
    """
    Applies an angry effect using high contrast and red tint.
    """
    img = ensure_rgb(img)

    base = ImageEnhance.Contrast(img).enhance(1.35 if style == "soft" else 1.7)

    gray = base.convert("L")
    red_tint = ImageOps.colorize(
        gray,
        black="#250000",
        white="#ff5a5a"
    ).convert("RGB")

    if style == "intense":
        return Image.blend(base, red_tint, 0.55)

    return Image.blend(base, red_tint, 0.35)


def apply_nostalgic(img, style):
    # TODO 4: Feeling Nostalgic
    """
    Complete a function that applies a nostalgic (sepia-style) filter to an image. The function should convert the
    image to RGB, turn it grayscale, apply sepia tones, and then adjust contrast and blur based on the selected style
    (more intense vs. subtle). Finally, return the modified image so it can continue through the editing pipeline.
    """
    return None

def apply_dreamy(img, style):
    """
    Applies a dreamy effect using brightness and blur blending.
    """
    img = ensure_rgb(img)

    bright = ImageEnhance.Brightness(img).enhance(
        1.12 if style == "soft" else 1.22
    )

    blurred = bright.filter(
        ImageFilter.GaussianBlur(
            radius=2.0 if style == "soft" else 3.2
        )
    )

    return Image.blend(
        bright,
        blurred,
        0.28 if style == "soft" else 0.40
    )

def apply_chaotic(img, style):
    """
    Applies a chaotic effect with extreme visual distortion.
    """
    img = ensure_rgb(img)

    if style == "intense":
        poster = ImageOps.posterize(img, bits=3)
        edges = poster.filter(ImageFilter.FIND_EDGES)
        edges = ImageEnhance.Contrast(edges).enhance(1.6)
        return edges
    else:
        inv = ImageOps.invert(img)
        inv = inv.filter(ImageFilter.SHARPEN)
        return ImageEnhance.Contrast(inv).enhance(1.15)

# TODO 6: The Invert
def apply_invert(img, style):
    """
    Inverts the image colors.
    Soft = normal invert
    Intense = invert + higher contrast
    """
    return None

# TODO 7: Do a Flip
def apply_mirror(img, style):
    """
    Flips the image like a mirror.
    Soft = left/right flip
    Intense = top/bottom flip
    """
    return None

def apply_mood(img, mood, style):
    """
    Routes the image to the correct mood filter.
    """
    if mood == "calm":
        return apply_calm(img, style)
    elif mood == "angry":
        return apply_angry(img, style)
    elif mood == "nostalgic":
        return apply_nostalgic(img, style)
    elif mood == "dreamy":
        return apply_dreamy(img, style)
    elif mood == "chaotic":
        return apply_chaotic(img, style)
    elif mood == "invert":
        return apply_invert(img, style)
    elif mood == "mirror":
        return apply_mirror(img, style)
    else:
        return apply_calm(img, "soft")


def square_crop(img):
    # TODO 3: A little square cropping
    """
    Implement a function that center-crops an image into a perfect square by using the smaller image dimension,
    calculating the excess space evenly on all sides, and cropping accordingly. You’ll be working directly with
    the image, so refer to the Pillow documentation for guidance.
    """
    return None

def wide_crop(img):
    """
    Crops the image to a centered 16:9 aspect ratio.
    """
    w, h = img.size
    target_h = int(w * 9 / 16)

    if target_h <= h:
        top = (h - target_h) // 2
        return img.crop((0, top, w, top + target_h))

    target_w = int(h * 16 / 9)
    left = (w - target_w) // 2
    return img.crop((left, 0, left + target_w, h))

def portrait_crop(img):
    """
    Crops the image to a centered 4:5 portrait ratio.
    """
    w, h = img.size
    target_w = int(h * 4 / 5)

    if target_w <= w:
        left = (w - target_w) // 2
        return img.crop((left, 0, left + target_w, h))

    target_h = int(w * 5 / 4)
    top = (h - target_h) // 2
    return img.crop((0, top, w, top + target_h))

def apply_frame(img, frame):
    """
    Applies the selected frame crop to the image.
    """
    if frame == "square":
        return square_crop(img)
    elif frame == "wide":
        return wide_crop(img)
    elif frame == "portrait":
        return portrait_crop(img)
    else:
        return img
def auto_resize(img):
    """
    Resizes the image to a standard resolution based on its orientation.
    """
    w, h = img.size
    if w == h:
        return img.resize((900, 900))
    elif w > h:
        return img.resize((1280, 720))
    else:
        return img.resize((720, 1280))


# TODO 5: Create your own Mood
"""
Create a new custom mood filter (any vibe you choose) that noticeably changes the image using tools like brightness, 
contrast, blur, sharpen, invert, or colorize. It must support soft (subtle) and intense (stronger) styles. 
Then update the mood menu and routing logic so the user can select your new mood and it gets applied when the program 
runs and saves the final image. **YOU HAVE TO CREATE A NEW FUNCTION FOR THIS!**
"""

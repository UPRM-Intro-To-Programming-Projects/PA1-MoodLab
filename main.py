from PIL import Image
from editorUI import (
    pick_mood, pick_style, pick_frame, pick_overlay,
    guardrails, build_output_name
)
from editorTools import stamp_creation_time, add_overlay
from filters import apply_mood, apply_frame, auto_resize

def main():
    print("================================")
    print("        MoodLab Image Editor    ")
    print("================================")

    # Get input image filename
    filename = input("\nEnter image filename (ex: cat.jpg): ").strip()
    image_path = "Images/" + filename

    # Try to open the image
    try:
        img = Image.open(image_path)
    except Exception as e:
        print(f"\nCould not open image: {e}")
        return

    # User selections
    mood = pick_mood()
    style = pick_style()
    frame = pick_frame()
    overlay_name = pick_overlay()

    # Apply rule-based adjustments
    mood, style, frame = guardrails(mood, style, frame)

    # TODO 2: Processing Pipeline Problem
    """
        Restore the image processing pipeline by applying the steps in order: apply the frame, crop the image, 
        resize it to the correct resolution, then apply the mood effect using the chosen mood and style.
    """
    # Add timestamp and overlay
    img = stamp_creation_time(img)
    img = add_overlay(img, overlay_name, stickers_folder="Stickers")

    # Build output path
    out_name = build_output_name(filename, mood, style, frame)
    out_path = "results/" + out_name

    # Save final image
    try:
        img.save(out_path)
        print(f"\nSaved: {out_path}")
    except Exception as e:
        print(f"\nCould not save image: {e}")

if __name__ == "__main__":
    main()
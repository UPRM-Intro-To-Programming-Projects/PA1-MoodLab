# =========================
# editorUI.py
# =========================

def pick_mood() -> str:
    # Display mood options
    print("\nPick a mood:")
    print("1) Calm")
    print("2) Angry")
    print("3) Nostalgic")
    print("4) Dreamy")
    print("5) Chaotic")

    choice = input("> ").strip()

    # Return selected mood
    if choice == "1":
        return "calm"
    elif choice == "2":
        return "angry"
    elif choice == "3":
        return "nostalgic"
    elif choice == "4":
        return "dreamy"
    elif choice == "5":
        return "chaotic"
    else:
        # Default fallback
        print("Invalid mood. Defaulting to Calm.")
        return "calm"


def pick_style() -> str:
    # Display style options
    print("\nPick a style:")
    print("1) Soft")
    print("2) Intense")

    choice = input("> ").strip()

    # Return selected style
    if choice == "2":
        return "intense"
    elif choice == "1":
        return "soft"
    else:
        print("Invalid style. Defaulting to Soft.")
        return "soft"


def pick_frame() -> str:
    # Display frame options
    print("\nPick a frame:")
    print("1) None")
    print("2) Square (1:1)")
    print("3) Wide (16:9)")
    print("4) Portrait (4:5)")

    choice = input("> ").strip()

    # Return selected frame
    if choice == "2":
        return "square"
    elif choice == "3":
        return "wide"
    elif choice == "4":
        return "portrait"
    elif choice == "1":
        return "none"
    else:
        print("Invalid frame. Defaulting to None.")
        return "none"


def pick_overlay() -> str:
    # Ask user if they want an overlay
    print("\nOverlay image?")
    print("1) None")
    print("2) Add overlay")

    choice = input("> ").strip()

    # If yes, ask for filename
    if choice == "2":
        return input("Enter overlay filename (ex: sticker.png): ").strip()

    return ""


def guardrails(mood: str, style: str, frame: str) -> tuple[str, str, str]:
    """
    Enforces simple rules to avoid bad combinations.
    """
    # Calm mood should not be intense
    if mood == "calm" and style == "intense":
        print("\nRule: Calm doesn't support Intense. Switching style -> Soft.")
        style = "soft"

    # Warn user about harsh visual combo
    if mood == "chaotic" and frame == "portrait":
        print("\nWarning: Chaotic + Portrait can look harsh.")

    return mood, style, frame


def build_output_name(input_path: str, mood: str, style: str, frame: str) -> str:
    """
    Generates a descriptive output filename.
    """
    lower = input_path.lower()

    # Detect file extension
    if lower.endswith(".jpeg"):
        base = input_path[:-5]
        ext = ".jpeg"
    elif lower.endswith(".jpg"):
        base = input_path[:-4]
        ext = ".jpg"
    elif lower.endswith(".png"):
        base = input_path[:-4]
        ext = ".png"
    else:
        base = input_path
        ext = ".png"

    # Build final filename
    return f"{base}_{mood}_{style}_{frame}{ext}"

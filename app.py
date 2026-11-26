import random


def generate_prompt(scene):
    camera_movements = [
        "slow cinematic dolly-in",
        "smooth tracking shot",
        "dramatic aerial shot",
        "slow orbit camera movement",
        "wide-angle establishing shot"
    ]

    lighting = [
        "soft natural lighting",
        "dramatic cinematic lighting",
        "golden hour lighting",
        "neon atmospheric lighting",
        "volumetric lighting"
    ]

    styles = [
        "photorealistic",
        "Hollywood cinematic",
        "futuristic sci-fi",
        "documentary style",
        "high-end commercial"
    ]

    camera = random.choice(camera_movements)
    light = random.choice(lighting)
    style = random.choice(styles)

    return (
        f"{scene}, {camera}, {light}, "
        f"{style}, realistic motion, "
        "high detail, cinematic composition, "
        "4K resolution, 24 fps."
    )


def main():
    print("=== Cinematic Prompt Generator ===")

    while True:
        scene = input("\nDescribe your scene: ").strip()

        if scene.lower() == "exit":
            break

        if not scene:
            print("Please enter a scene description.")
            continue

        prompt = generate_prompt(scene)

        print("\nGenerated cinematic prompt:")
        print(prompt)


if __name__ == "__main__":
    main()

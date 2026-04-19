import os

IMAGE_EXTS = (".png", ".jpg", ".jpeg", ".gif", ".bmp")


def generate_latex_commands(image_directory, output_file):
    image_files = [
        f for f in os.listdir(image_directory) if f.lower().endswith(IMAGE_EXTS)
    ]
    with open(output_file, "w") as f:
        for image in image_files:
            f.write(f"\\includegraphics[width=0.75\\textwidth]{{{image}}}\n")


if __name__ == "__main__":
    image_directory = "../Collected_PNGs"
    output_file = "pngLatex.txt"
    generate_latex_commands(image_directory, output_file)
    print(f"LaTeX commands have been written to {output_file}")

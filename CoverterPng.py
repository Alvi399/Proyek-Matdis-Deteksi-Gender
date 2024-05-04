import os
from graphviz import Source

def convert_dot_to_image(dot_file, image_format='png'):
    """
    Convert a .dot file to an image file.

    Parameters:
        dot_file (str): Path to the .dot file.
        image_format (str): Output image format (default is 'png').
    """
    image_file = os.path.splitext(dot_file)[0] + '.' + image_format
    Source.from_file(dot_file, format=image_format).render(image_file)
    print(f"Converted {dot_file} to {image_file}")
# Example usage:
dot_file = "./RandomForestTree_1.dot"  # Example dot file name
convert_dot_to_image(dot_file, image_format='png')
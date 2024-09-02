# File: /auto-manhua-editor/auto-manhua-editor/src/utils/helpers.py

"""
This module contains utility functions used throughout the project.
"""

import os
import cv2
import pytesseract
from svgwrite import Drawing

def load_image(image_path):
    """
    Load an image from the given file path.

    Args:
        image_path (str): The path to the image file.

    Returns:
        numpy.ndarray: The loaded image as a NumPy array.
    """
    return cv2.imread(image_path)

def save_image(image, save_path):
    """
    Save an image to the given file path.

    Args:
        image (numpy.ndarray): The image to be saved.
        save_path (str): The path to save the image file.
    """
    cv2.imwrite(save_path, image)

def extract_text_from_image(image):
    """
    Extract text from the given image using Tesseract-OCR.

    Args:
        image (numpy.ndarray): The image to extract text from.

    Returns:
        str: The extracted text.
    """
    return pytesseract.image_to_string(image)

def create_svg_file(svg_elements, save_path):
    """
    Create an SVG file with the given SVG elements and save it to the specified path.

    Args:
        svg_elements (list): A list of SVG elements to be included in the SVG file.
        save_path (str): The path to save the SVG file.
    """
    drawing = Drawing(save_path)
    for element in svg_elements:
        drawing.add(element)
    drawing.save()

# Other utility functions can be added here as needed
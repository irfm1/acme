# /auto-manhua-editor/auto-manhua-editor/src/svg/svg_export.py

"""
This module exports functions for exporting the finalized image as a vector file (.svg) using SVGWrite.
"""

import svgwrite

def create_svg_element(tag, attributes=None):
    """
    Create an SVG element with the given tag and attributes.

    Args:
        tag (str): The tag name of the SVG element.
        attributes (dict, optional): The attributes of the SVG element. Defaults to None.

    Returns:
        svgwrite.Element: The created SVG element.
    """
    element = svgwrite.Element(tag)
    if attributes:
        element.update(attributes)
    return element

def set_svg_attributes(element, attributes):
    """
    Set the attributes of an SVG element.

    Args:
        element (svgwrite.Element): The SVG element.
        attributes (dict): The attributes to set.
    """
    element.update(attributes)

def save_svg_file(svg_element, file_path):
    """
    Save the SVG element as an SVG file.

    Args:
        svg_element (svgwrite.Element): The SVG element to save.
        file_path (str): The file path to save the SVG file.
    """
    svg_document = svgwrite.Drawing(file_path)
    svg_document.add(svg_element)
    svg_document.save()

# This file is intentionally left blank.
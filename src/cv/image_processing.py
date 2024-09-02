# /auto-manhua-editor/auto-manhua-editor/src/cv/image_processing.py

import cv2

def analyze_image(image_path):
    """
    Analyzes the original raw image using computer vision techniques.
    
    Args:
        image_path (str): The path to the original raw image.
    
    Returns:
        analyzed_image (numpy.ndarray): The analyzed image.
    """
    # Load the image
    image = cv2.imread(image_path)
    
    # Perform image processing operations
    # ...
    
    # Return the analyzed image
    analyzed_image = image
    return analyzed_image

def extract_speech_bubbles(analyzed_image):
    """
    Extracts speech bubbles from the analyzed image using computer vision techniques.
    
    Args:
        analyzed_image (numpy.ndarray): The analyzed image.
    
    Returns:
        speech_bubbles (list): A list of speech bubble regions.
    """
    speech_bubbles = []
    # Perform speech bubble extraction
    # ...
    
    # Return the speech bubbles
    
    return speech_bubbles

def extract_floating_texts(analyzed_image):
    """
    Extracts floating texts from the analyzed image using computer vision techniques.
    
    Args:
        analyzed_image (numpy.ndarray): The analyzed image.
    
    Returns:
        floating_texts (list): A list of floating text regions.
    """
    floating_texts = []
    # Perform floating text extraction
    # ...
    
    # Return the floating texts
    return floating_texts

def extract_onomatopoeias(analyzed_image):
    """
    Extracts onomatopoeias from the analyzed image using computer vision techniques.
    
    Args:
        analyzed_image (numpy.ndarray): The analyzed image.
    
    Returns:
        onomatopoeias (list): A list of onomatopoeia regions.
    """
    onomatopoeias = []
    # Perform onomatopoeia extraction
    # ...
    
    # Return the onomatopoeias
    return onomatopoeias
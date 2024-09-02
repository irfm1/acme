# /auto-manhua-editor/auto-manhua-editor/src/cv/text_extraction.py

import cv2
import pytesseract

def extract_text_from_speech_bubbles(image):
    # TODO: Implement speech bubble detection and text extraction using computer vision techniques
    pass

def extract_text_from_floating_texts(image):
    # TODO: Implement floating text detection and text extraction using computer vision techniques
    pass

def extract_text_from_onomatopoeias(image):
    # TODO: Implement onomatopoeia detection and text extraction using computer vision techniques
    pass

def extract_text_from_image(image):
    # TODO: Implement overall text extraction by combining the above functions
    speech_bubbles_text = extract_text_from_speech_bubbles(image)
    floating_texts_text = extract_text_from_floating_texts(image)
    onomatopoeias_text = extract_text_from_onomatopoeias(image)
    
    return speech_bubbles_text, floating_texts_text, onomatopoeias_text

def main():
    # TODO: Implement main function for testing the text extraction functions
    image = cv2.imread("path/to/image.jpg")
    speech_bubbles_text, floating_texts_text, onomatopoeias_text = extract_text_from_image(image)
    print("Speech Bubbles Text:", speech_bubbles_text)
    print("Floating Texts Text:", floating_texts_text)
    print("Onomatopoeias Text:", onomatopoeias_text)

if __name__ == "__main__":
    main()
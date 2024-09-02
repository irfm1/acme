# Auto Manhua Editor

This project is an auto manhua editor that uses computer vision techniques to analyze raw webcomics/Manhua/manwah files and perform various editing tasks. It utilizes PyQt5 for the user interface, OpenCV for image processing, Tesseract-OCR for text extraction, SVGWrite for exporting the finalized image as an SVG file, and an existing AI API for text correction and translation.

## Project Structure

The project has the following file structure:

```
auto-manhua-editor
├── src
│   ├── main.py
│   ├── ui
│   │   └── main_window.py
│   ├── cv
│   │   ├── image_processing.py
│   │   ├── text_extraction.py
│   │   └── text_redraw.py
│   ├── ai
│   │   └── translation_api.py
│   ├── svg
│   │   └── svg_export.py
│   └── utils
│       └── helpers.py
├── requirements.txt
├── README.md
└── .gitignore
```

- `src/main.py`: This file is the entry point of the application. It initializes the PyQt5 application and creates an instance of the main window.

- `src/ui/main_window.py`: This file exports a class `MainWindow` which represents the main window of the application. It sets up the user interface using PyQt5 and connects the necessary signals and slots.

- `src/cv/image_processing.py`: This file exports functions for image processing using OpenCV. It includes functions for analyzing the original raw image, extracting speech bubbles, floating texts, and onomatopoeias using computer vision techniques.

- `src/cv/text_extraction.py`: This file exports functions for extracting text from the analyzed image using Tesseract-OCR. It includes functions for detecting and extracting text from speech bubbles, floating texts, and onomatopoeias.

- `src/cv/text_redraw.py`: This file exports functions for removing and redrawing imperfections in the extracted text using an existing AI API. It includes functions for sending the extracted text to the AI API, receiving the corrected text, and redrawing it on the image.

- `src/ai/translation_api.py`: This file exports functions for translating the extracted text to the desired language using an AI translation API. It includes functions for sending the extracted text to the translation API and receiving the translated text.

- `src/svg/svg_export.py`: This file exports functions for exporting the finalized image as a vector file (.svg) using SVGWrite. It includes functions for creating SVG elements, setting attributes, and saving the SVG file.

- `src/utils/helpers.py`: This file exports utility functions that are used throughout the project. It includes functions for file handling, image manipulation, and other helper functions.

- `requirements.txt`: This file lists the dependencies required for the project. It includes the necessary packages such as PyQt5, OpenCV, Tesseract-OCR, and SVGWrite.

- `README.md`: This file contains the documentation for the project, providing instructions on how to set up and use the auto manhua editor.

- `.gitignore`: This file specifies which files and directories should be ignored by Git version control. It typically includes files such as compiled binaries, temporary files, and sensitive information.

## Getting Started

To get started with the auto manhua editor, follow these steps:

1. Clone the repository:

```
git clone <repository_url>
```

2. Install the required dependencies:

```
pip install -r requirements.txt
```

3. Run the application:

```
python src/main.py
```

4. Use the user interface to open a raw webcomic/Manhua/manwah file.

5. Analyze the image to extract speech bubbles, floating texts, and onomatopoeias.

6. Use the AI API to remove imperfections in the extracted text and translate it to the desired language.

7. Export the finalized image as an SVG file.

## Contributing

Contributions to the auto manhua editor are welcome. If you find any issues or have suggestions for improvements, please open an issue or submit a pull request.

## License

This project is licensed under the [MIT License](LICENSE).
```

This file provides an overview of the project, explains the project structure, and provides instructions on how to set up and use the auto manhua editor. It also includes information on contributing to the project and the project's license.
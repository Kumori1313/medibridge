import cv2
import pytesseract


def scan_document(image_path):
    image = cv2.imread(image_path)

    if image is None:
        return "Could not open the image."

    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    text = pytesseract.image_to_string(gray)

    return text

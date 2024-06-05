import pytesseract
from PIL import Image
import io

def image_to_text(image: Image.Image) -> str:
    return pytesseract.image_to_string(image)

def image_to_bboxes(image: Image.Image, bbox_type: str) -> list:
    data = pytesseract.image_to_data(image, output_type=pytesseract.Output.DICT)
    n_boxes = len(data['level'])
    bboxes = []

    for i in range(n_boxes):
        (x, y, w, h) = (data['left'][i], data['top'][i], data['width'][i], data['height'][i])
        bboxes.append({
            "x_min": x,
            "y_min": y,
            "x_max": x + w,
            "y_max": y + h
        })

    return bboxes

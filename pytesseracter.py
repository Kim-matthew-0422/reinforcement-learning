import pytesseract
from pytesseract import Output
import cv2
from tesseractOCRmodel import preprocess_image_for_ocr

def extract_experience_values(game_screen):
    # Define the region of interest (ROI) containing the experience bar and its text
    x, y, w, h = 540, 140, 120, 40
    roi = game_screen[y:y+h, x:x+w]

    # Preprocess the ROI
    preprocessed_roi = preprocess_image_for_ocr(roi)


    ocr_data = pytesseract.image_to_data(preprocessed_roi, output_type=Output.DICT)
    ocr_text = pytesseract.image_to_string(preprocessed_roi)
    
    return  ocr_text




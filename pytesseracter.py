import pytesseract
from pytesseract import Output
import cv2


def extract_experience_values(game_screen):
    # Define the region of interest (ROI) containing the experience bar and its text
    
    x, y, w, h = 540, 140, 120, 40
    roi = game_screen[y:y+h, x:x+w]

    cv2.imshow('ROI', roi)
    cv2.waitKey(0)

    ocr_data = pytesseract.image_to_data(roi, output_type=Output.DICT)

    # Draw a rectangle border around the ROI on the game screen
    border_color = (0, 255, 0)
    border_thickness = 2
    cv2.rectangle(game_screen, (x, y), (x+w, y+h), border_color, border_thickness)
    cv2.imshow('game screen with exp bar rectangle', game_screen)
    cv2.imwrite("sample_roi.png", roi)
    cv2.waitKey(0)
    # Find the experience and percentage values from the OCR data
    # (Replace 'EXP_TEXT_IDENTIFIER' and 'PERCENTAGE_TEXT_IDENTIFIER' with the actual text strings that indicate experience and percentage values in the OCR data)
    experience_value = None
    percentage_value = None
    for i, text in enumerate(ocr_data['text']):
        if text == 'EXP_TEXT_IDENTIFIER':
            experience_value = int(ocr_data['text'][i+1])
        if text == 'PERCENTAGE_TEXT_IDENTIFIER':
            percentage_value = float(ocr_data['text'][i+1])

    return experience_value, percentage_value




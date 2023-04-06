import cv2
import numpy as np
from mss import mss
import time

from pytesseracter import extract_experience_values
from tesseractOCRmodel import preprocess_image_for_ocr
import pytesseract

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

fps = 1

interval = 1.0 / fps

#capture the screen
def capture_screen(region = None):
    with mss() as sct:
        if region:
            screen = sct.grab(region)
        else:
            screen = sct.grab(sct.monitors[0])
           
        return np.array(screen)
   
   
def draw_border(image, border_thickness=5, border_color=(0, 255, 0)):
    h, w, _ = image.shape
    cv2.rectangle(image, (0, 0), (w, h), border_color, border_thickness)
game_window = {
    "top": 200,
    "left": 800,
    "width": 800,
    "height": 600
}

def preprocess_image(image, target_size=(84, 84)):
    resized_image = cv2.resize(image, target_size, interpolation = cv2.INTER_AREA)
    grayscale_image = cv2.cvtColor(resized_image, cv2.COLOR_BGR2GRAY)
    normalized_image = grayscale_image.astype(np.float32) / 255.0
   
    return normalized_image

while True:
    start_time = time.time()
   
   
    game_screen = capture_screen(game_window)
   
    draw_border(game_screen, border_thickness=5, border_color=(0, 255, 0))
   
    cv2.imshow('game screen', game_screen)
    exp = extract_experience_values(game_screen)
    
    
    # Press 'q' to exit the loop.qqqqqqq
   
    time_elapsed = time.time() - start_time
   
    sleep_time = max(0, interval - time_elapsed)
   
    time.sleep(sleep_time)
    #cv2.imwrite(f"C:/Users/Administrator/Desktop/reinforcementlearning/images/game_screen_{time_elapsed}.png", game_screen)
    if cv2.waitKey(25) & 0xFF == ord('q'):
        cv2.destroyAllWindows()
        break

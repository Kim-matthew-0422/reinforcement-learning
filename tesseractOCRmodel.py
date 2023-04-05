import cv2

def preprocess_image_for_ocr(image_path):
    image = cv2.imread(image_path)
    
    # Convert the image to grayscale
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    
    # Apply binary thresholding to make the text stand out more
    _, thresholded_image = cv2.threshold(gray_image, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)
    
    # Resize the image to make the text larger and more recognizable
    resized_image = cv2.resize(thresholded_image, None, fx=3, fy=3, interpolation=cv2.INTER_CUBIC)

    return resized_image

preprocessed_image = preprocess_image_for_ocr('expbarexample.png')
cv2.imshow('Preprocessed Image', preprocessed_image)
cv2.waitKey(0)
cv2.destroyAllWindows()




import cv2
from retinaface import RetinaFace

img_path = r"path to input image"

# Detect faces with a threshold of 0.5
faces = RetinaFace.detect_faces(img_path, threshold=0.4)

# Read the image
img = cv2.imread(img_path)

# Iterate through all the detected faces
for face_info in faces.values():
    facial_area = face_info["facial_area"]
    landmarks = face_info["landmarks"]

    # Convert landmarks values to integers
    left_eye = (int(landmarks["left_eye"][0]), int(landmarks["left_eye"][1]))
    right_eye = (int(landmarks["right_eye"][0]), int(landmarks["right_eye"][1]))
    nose = (int(landmarks["nose"][0]), int(landmarks["nose"][1]))
    mouth_left = (int(landmarks["mouth_left"][0]), int(landmarks["mouth_left"][1]))
    mouth_right = (int(landmarks["mouth_right"][0]), int(landmarks["mouth_right"][1]))

    # Highlight facial area
    cv2.rectangle(img, (facial_area[0], facial_area[1]), (facial_area[2], facial_area[3]), (0, 255, 0), 1)

    # Extract facial area (optional, you can remove this if not needed)
    facial_img = img[facial_area[1]:facial_area[3], facial_area[0]:facial_area[2]]

    #Highlight the landmarks

    cv2.circle(img, left_eye, 1, (0, 0, 255), -1)
    cv2.circle(img, right_eye, 1, (0, 0, 255), -1)
    cv2.circle(img, nose, 1, (0, 0, 255), -1)
    cv2.circle(img, mouth_left, 1, (0, 0, 255), -1)
    cv2.circle(img, mouth_right, 1, (0, 0, 255), -1)

# Display the image with annotations for all detected faces
cv2.imshow('Facial Landmarks', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
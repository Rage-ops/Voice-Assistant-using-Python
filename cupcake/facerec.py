import cv2
from response import cupcakeResponse


def face_recognise(path):
    # loading the face detection classifier
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades+'haarcascade_frontalface_default.xml')
    try:
        image = cv2.imread(path)
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(
            gray,
            scaleFactor=1.1,
            minNeighbors=5,
            minSize=(30, 30),
        )
    except Exception as e:
        cupcakeResponse('An error occured ! Recheck the path of the image. The error is printed below:')
        print(e)
        return
    cupcakeResponse(f"I detected {len(faces)} faces in the image.")

    for face_location in faces:
        x, y, w, h = face_location
        cv2.rectangle(image, (x, y), (x+w, y+h), (0, 255, 0), 2)
    cv2.imshow("Faces found", image)
    cv2.waitKey(0)

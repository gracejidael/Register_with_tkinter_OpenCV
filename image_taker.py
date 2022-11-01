import cv2

# program to capture single image from webcam in python


webcam = cv2.VideoCapture(0)

try:
    check, frame = webcam.read()
    cv2.imshow("Capturing", frame)
    key = cv2.waitKey(0)
    if key == ord('s'):
        cv2.imwrite(filename='saved_img.jpg', img=frame)
        webcam.release()
        cv2.destroyAllWindows()

    elif key == ord('q'):
        print("Turning off camera.")
        webcam.release()
        print("Camera off.")
        print("Program ended.")
        cv2.destroyAllWindows()
except (KeyboardInterrupt):
    print("Turning off camera.")
    webcam.release()
    print("Camera off.")
    print("Program ended.")

    cv2.destroyAllWindows()

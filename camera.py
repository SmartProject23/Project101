import cv2

def select_camera():
    num_cameras = 0
    while True:
        cap = cv2.VideoCapture(num_cameras)
        if not cap.isOpened():
            break
        num_cameras += 1
        cap.release()

    if num_cameras == 0:
        print("No cameras found.")
        return None

    print(f"Found {num_cameras} camera(s).")
    selected_camera = int(input("Select a camera by entering its index (0 to {}): ".format(num_cameras - 1)))

    if selected_camera < 0 or selected_camera >= num_cameras:
        print("Invalid camera selection.")
        return None

    return selected_camera

def main():
    selected_camera = select_camera()
    if selected_camera is None:
        return

    cap = cv2.VideoCapture(selected_camera)

    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break

        # Process the frame here (e.g., face detection, recognition, etc.)

        cv2.imshow("Camera Feed", frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()

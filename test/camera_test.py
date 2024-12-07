import cv2

# 카메라 초기화 (장치 번호 0: 기본 USB 카메라)
cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("camera can not open")
    exit()

print("camera started. If you want to go out, press 'ESC'")

while True:
    ret, frame = cap.read()
    if not ret:
        print("can not read frame")
        break

    cv2.imshow('USB Camera', frame)
    
    # capture
    if cv2.waitKey(1) == ord('s'):  # 's' : capture
        print("pressed s")
        cv2.imwrite('/home/user/Pictures/capture.jpg', frame)
        print("image captured")

    # ESC
    if cv2.waitKey(1) == 27:  # 27 = ESC
        break

# end
cap.release()
cv2.destroyAllWindows()

import cv2

cap = cv2.VideoCapture(0)

if not cap.isOpened():

    print("無法開啟相機")
    exit()

width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
print(f"width : {width}px, height : {height}px")

ret, frame = cap.read()
if ret:
    cv2.imshow("Camera Frame", frame)
    print("按任意鍵結束視窗...")
    cv2.waitKey(0)

cap.release()
cv2.destroyAllWindows()

import cv2

cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("無法打開攝像頭！")
    exit()

print("按下 'q' 鍵可退出程式")

while True:

    ret, frame = cap.read()
    if not ret:
        print("無法讀取攝像頭影像")
        break

    cv2.imshow("Original Frame", frame)

    # 按下 'q' 鍵退出
    if cv2.waitKey(1) & 0xFF == ord('q'):
        print("退出程式中...")
        break

cap.release()
cv2.destroyAllWindows()

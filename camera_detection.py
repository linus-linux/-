from ultralytics import YOLO
import cv2

# 1. 加载模型
model = YOLO("yolov10n.pt")

# 2. 打开摄像头（0为默认，可修改为1、2等）
cap = cv2.VideoCapture(0)

while cap.isOpened():
    # 3. 读取摄像头画面
    success, frame = cap.read()
    if not success:
        break

    # 4. 模型推理（检测目标）
    results = model(frame)

    # 5. 可视化结果（标注检测框、置信度）
    annotated_frame = results[0].plot()

    # 6. 显示画面（强制弹出窗口）
    cv2.imshow("YOLOv10 Detection", annotated_frame)
    
    # 按 'q' 键退出
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

# 7. 释放资源
cap.release()
cv2.destroyAllWindows()
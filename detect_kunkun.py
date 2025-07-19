from ultralytics import YOLO
import cv2

# 1. 加载模型
model = YOLO("yolov10n.pt")

# 2. 读取视频文件（替换为你的视频路径，如"input.mp4"）
video_path = "D:\YOLOv10\kunkun_raw.mp4"  # 输入视频路径
cap = cv2.VideoCapture(video_path)

# 3. 获取视频参数（用于后续导出）
fps = cap.get(cv2.CAP_PROP_FPS)  # 帧率
width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))  # 宽度
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))  # 高度

# 4. 设置导出视频的编码器和路径
fourcc = cv2.VideoWriter_fourcc(*"mp4v")  # 编码器（生成mp4格式）
output_path = "output_video.mp4"  # 输出视频路径
out = cv2.VideoWriter(output_path, fourcc, fps, (width, height))

# 5. 逐帧处理视频
while cap.isOpened():
    success, frame = cap.read()
    if not success:
        break  # 视频读取完毕

    # 模型推理
    results = model(frame)
    # 可视化标注结果
    annotated_frame = results[0].plot()

    # 写入处理后的帧到输出视频
    out.write(annotated_frame)

    # （可选）实时显示处理过程，按'q'退出
    cv2.imshow("YOLOv10 Detection", annotated_frame)
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

# 6. 释放资源
cap.release()  # 关闭输入视频
out.release()  # 关闭输出视频
cv2.destroyAllWindows()  # 关闭窗口
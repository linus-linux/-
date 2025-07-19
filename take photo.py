import cv2
import os


def capture_and_save_images():
    # 打开默认摄像头（索引为0）
    cap = cv2.VideoCapture(0)

    # 设置摄像头分辨率
    cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)

    # 检查摄像头是否成功打开
    if not cap.isOpened():
        print("无法打开摄像头")
        return

    # 获取并打印实际的摄像头分辨率
    width = cap.get(cv2.CAP_PROP_FRAME_WIDTH)
    height = cap.get(cv2.CAP_PROP_FRAME_HEIGHT)
    print(f"摄像头分辨率: {width}x{height}")

    # 创建输出目录
    output_dir = 'output_images'
    os.makedirs(output_dir, exist_ok=True)

    img_counter = 0

    try:
        while True:
            # 读取一帧画面
            ret, frame = cap.read()

            # 如果读取失败，退出循环
            if not ret:
                print("无法获取画面")
                break

            # 显示画面
            cv2.imshow('Webcam', frame)

            # 等待按键输入（1毫秒）
            k = cv2.waitKey(1)

            # 如果按下ESC键（ASCII码27），退出循环
            if k == 27:
                print("ESC键被按下，正在退出...")
                break
            # 如果按下's'键，保存当前画面
            elif k == ord('s'):
                img_name = os.path.join(output_dir, f"opencv_frame_{img_counter}.png")
                cv2.imwrite(img_name, frame)
                print(f"已保存: {img_name}")
                img_counter += 1
    finally:
        # 释放摄像头资源
        cap.release()
        # 关闭所有窗口
        cv2.destroyAllWindows()


if __name__ == "__main__":
    capture_and_save_images()

import datetime
import cv2
import os

dt = datetime.datetime.now().strftime('%H%M%S')
img_path = "assets/img/" + dt +".jpg"
video_path = "assets/video/" + dt +".avi"
def cap_video_to_images(video_path):
    cap = cv2.VideoCapture(video_path)
    total_frames = cap.get(cv2.CAP_PROP_FRAME_COUNT)
    fps = cap.get(cv2.CAP_PROP_FPS)
    interval = 10 * fps  # capture images every 10 seconds

    count = 0
    while count < total_frames:
        cap.set(cv2.CAP_PROP_POS_FRAMES, count)
        ret, frame = cap.read()
        if ret:
            img_name = f"{os.path.splitext(video_path)[0]}_{count}.jpg"
            img_path = os.path.join(img_path, img_name)
            cv2.imwrite(img_path, frame)
        count += interval

    cap.release()

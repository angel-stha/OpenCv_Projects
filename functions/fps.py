import cv2
import datetime
import imutils

def main():
    video =cv2.VideoCapture('../inputs/input_video.webm')
    frame_width = int(video.get(3))
    frame_height = int(video.get(4))
    size = (frame_width, frame_height)
    fps_start = datetime.datetime.now()
    fps=0
    total_frames = 0
    result = cv2.VideoWriter('../output/file.avi',
                             cv2.VideoWriter_fourcc(*'MJPG'),
                             10, size)

    while True:
        return_value, frame = video.read()
        print(return_value)
        frame = cv2.resize(frame, (frame_width, frame_height))
        total_frames = total_frames + 1

        fps_end = datetime.datetime.now()
        diff_time = fps_end - fps_end

        if diff_time.seconds == 0:
            fps = 0.0
        else:
            fps = (total_frames / diff_time.seconds)

        text_fps = "FPS is: {:.2f}".format (fps)
        cv2.putText(frame, text_fps, (5,35), cv2.FONT_HERSHEY_TRIPLEX, 1, (0,255,0), 1)
        cv2.imshow("Video", frame)
        result.write(frame)
        key = cv2.waitKey(1)
        if key == ord('p'):
            break
    cv2.destroyAllWindows()

main()
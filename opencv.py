import cv2
import imutils


def function_image():
    image = cv2.imread("inputs/download.jpeg")
    while True:
        cv2.imshow("ImageHead", image)
        text = 'This is custom play text'
        # write on the image
        cv2.putText(image, text, (3, 4), cv2.FONT_ITALIC, 1, (0, 22, 255), 1)
        # draw rectangle on image
        cv2.rectangle(image, (50, 50), (100, 100), (255, 0, 0), 2)
        # save the image
        cv2.imwrite('output/output.jpg', image)
        # wait for input from user
        key = cv2.waitKey(1)
        # when 'q' key is pressed while loop is broken
        if key == ord('q'):
            break
    cv2.destroyAllWindows()


def video_func():
    video = cv2.VideoCapture('inputs/input_video.webm')
    frame_width = int(video.get(3))
    frame_height = int(video.get(4))

    size = (frame_width, frame_height)

    # Below VideoWriter object will create
    # a frame of above defined The output
    # is stored in 'filename.avi' file.
    opt = cv2.VideoWriter('output/filename.avi',
                          cv2.VideoWriter_fourcc(*'MJPG'),
                          10, size)
    while True:
        return_value, frame = video.read()
        frame = imutils.resize(frame, width=frame_width)

        text = "Entertaining"
        cv2.putText(frame, text, (5, 30), cv2.FONT_HERSHEY_COMPLEX_SMALL, 1, (0, 0, 255), 1)

        cv2.rectangle(frame, (50, 50), (500, 500), (0, 0, 255), 2)

        cv2.imshow('Video1', frame)
        opt.write(frame)
        key = cv2.waitKey(1)
        if key == ord('q'):
            break

    cv2.destroyAllWindows()


if __name__ == '__main__':
    a = int(input('Enter 1 for image and 2 for video:'))
    if a == 1:
        function_image()
    else:
        video_func()

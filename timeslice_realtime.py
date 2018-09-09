import cv2
import numpy as np
from collections import deque

# vidcap = cv2.VideoCapture('video_files/VID_20180906_195216.mp4')
# vidcap = cv2.VideoCapture('video_files/VID_20180820_192046.mp4')

cap = cv2.VideoCapture(0)

slice_q = deque()
slice_buffer = 720
slice_height = 120
slice_starts_y = 300

x = 1280
y = 720

cap.set(cv2.CAP_PROP_AUTOFOCUS, 0)
cap.set(3, x)
cap.set(4, y)

slices_image = np.zeros((slice_buffer + slice_height, x, 3), np.uint8)

while True:
    # Capture frame-by-frame
    ret, frame = cap.read()

    if ret:

        # print(frame.shape)
        # gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        cropped = frame[slice_starts_y:(slice_starts_y + slice_height), 0:x]
        averaged = np.average(cropped, axis=0)
        slice_q.appendleft(averaged)
        if len(slice_q) > slice_buffer:
            slice_q.pop()

        slices_image[0:slice_height, 0:x] = cropped

        for i in range(len(slice_q)):
            slices_image[slice_height + i, 0:x] = slice_q[i]

        # Display the resulting frame
        cv2.imshow('Slices (q to quit)', slices_image)
    else:
        print("fail?")

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()
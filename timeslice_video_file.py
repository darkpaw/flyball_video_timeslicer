import cv2

# vidcap = cv2.VideoCapture('video_files/VID_20180906_195216.mp4')
vidcap = cv2.VideoCapture('video_files/VID_20180820_192046.mp4')

success, image = vidcap.read()

import numpy as np
slices = []
slice_averages = []


count = 0
while success:  #  and count < 100:
    # cv2.imwrite("frame%d.jpg" % count, image)     # save frame as JPEG file
    success, image = vidcap.read()
    print('Frame %d: %s' % (count, success))

    if success:
        cropped = image[400:600, 0:1920]
        print('Shape ', image.shape)
        print('Cropped', cropped.shape)
        cv2.imwrite("frames/cropped_%d.jpg" % count, cropped)
        # slices.append(cropped)

        averaged = np.average(cropped, axis=0)
        slice_averages.append(averaged)
        print(averaged.shape)

    count += 1

slices_count = len(slices)
print("Have %d slices" % slices_count)

# build a new image from the whole slices
# blank_image = np.zeros((slices_count * 100, 1920, 3), np.uint8)
#
# for i in range(slices_count):
#     blank_image[i*100:(i+1)*100, 0:1920] = slices[i]
#
# cv2.imwrite("output.jpg", blank_image)


slice_avg_count = len(slice_averages)
print("Have %d slice averages" % slice_avg_count)

# build a new image from the averaged slice pixels
blank_image = np.zeros((slice_avg_count, 1920, 3), np.uint8)

for i in range(slice_avg_count):
    blank_image[i, 0:1920] = slice_averages[i]

cv2.imwrite("output_averaged.jpg", blank_image)


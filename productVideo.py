import os
import cv2
import time

"""
* objective: generate video by pictures
* input: path - pictures path
         size - size of picture and video
* output: nothing, but generate video in path
"""
def picvideo(path, size):
    # obtain all of files in the path
    filelist = os.listdir(path)

    '''
    fps:
    Frame rate: There are n pictures written in 1 second [Control a picture to stay for 5 seconds, that is, the frame rate is 1, repeat this picture 5 times]
    If there are 50 534 * 300 pictures in the folder, and set to play 5 pictures in 1 second, then the length of this video is 10 seconds
    '''
    fps = 12

    # video path
    file_path = path + "/" + str(int(time.time())) + ".mp4"
    fourcc = cv2.VideoWriter_fourcc(*'MP4V')

    video = cv2.VideoWriter(file_path, fourcc, fps, size)

    for item in sorted(filelist):
        # decide the file is jpg or not
        if item.endswith('.jpg'):
            item = path + '/' + item

            # Use opencv to read the image and directly return the numpy.ndarray object. The channel order is BGR. Note that it is BGR. The default channel value is 0-255.
            img = cv2.imread(item)

            # Write picture into video
            video.write(img)

    video.release()

if __name__ == '__main__':
    picvideo(r'/Users/wangwei/Documents/我爱学习 学习爱我/Project/2DMOT2015/train/TUD-Stadtmitte/graphs', (640, 480))
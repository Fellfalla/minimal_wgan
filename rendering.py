from cv2 import VideoWriter
import cv2
import os
import numpy as np

image_folder = 'images'
video_name = 'video.avi'
video_format = 'MJPG'
video_size = (256, 256)
framerate = 30

def draw_figure(generated_images):
    winname = "GeneratedImage"
    cv2.namedWindow(winname, cv2.WINDOW_NORMAL)
    cv2.resizeWindow(winname, 150,150)

    while True:
        if len(generated_images) > 0:  
            img = generated_images[-1]
            if img is not None:
                img = cv2.resize(img, video_size)#, fx=5.0, fy=5.0)
                cv2.imshow(winname, img)
            
        cv2.waitKey(10)

    cv2.destroyWindow(winname)
    
  
def export_video(generated_images):
    """ Exports the rendered frames in generated_images to a video """
    fourcc = cv2.VideoWriter_fourcc(*video_format)
    video = VideoWriter(video_name, fourcc, framerate, video_size, 1)
    print("Writing {} images".format(len(generated_images)))
    for image in generated_images:
        image = cv2.cvtColor(image, cv2.COLOR_GRAY2RGB)
        video.write(image)

    video.release()

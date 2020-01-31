import cv2
import numpy as np

def overlay(img_name): # input is a string of the image (ex: 'example.jpg')
    img = cv2.imread(img_name) # holds the image
    cap = cv2.VideoCapture(0)
    # the 3 and 4 are supposed to be held by constants made by openCV, but VS didn't show me that stuff so yeah
    cap.set(3, 9999) # sets width of camera screen to max
    cap.set(4, 9999) # above but for height
    v_width  = int(cap.get(3)) # gets width of cam screen
    v_height = int(cap.get(4)) # above for height
    i_height, i_width, _ = img.shape # gets height, width of 'img'

    scalar = 1.0 # how much to resize 'img' to fit the cam screen
    if float(v_height / v_width) > float(i_height / i_width): # ratio-wise, camera screen is taller than 'img'
        scalar = float(v_width / i_width)
    else:                                                     # ratio-wise, c.s. wider or equal to 'img'
        scalar = float(v_height / i_height)
    i_width  *= scalar # resizes width of 'img'
    i_height *= scalar # above for height
    img = cv2.resize(img, (int(i_width), int(i_height))) # resizes 'img'

    bg = np.ones([v_height, v_width, 3], np.uint8) # this is used as the background for 'img' bc cv2.addWeighted only works with same sized images
    x_offset = int((v_width - i_width) / 2)   # to get the 'img' in the middle of the screen
    y_offset = int((v_height - i_height) / 2) # above for height
    bg[y_offset:y_offset+img.shape[0], x_offset:x_offset+img.shape[1]] = img # puts 'img' on top of 'bg'; 'img' no longer needed as 'bg' takes its place

    while (True):
        _, frame = cap.read() # gets each frame of camera
        result = cv2.addWeighted(bg, 0.3, frame, 1, 0) # overlays 'bg' over 'frame'
        cv2.imshow('overlay', result) # shows 'result' in window 'overlay'
        if cv2.waitKey(1) & 0xFF == ord('q'): # press 'q' to quit
            break

    cap.release()
    cv2.destroyAllWindows()

import os
import cv2


os.mkdir('video_to_img')  #creating a folder to save the images 

vid=cv2.VideoCapture('Video_file.mp4')
img_count=1

while vid.isOpened():
    retention,frame=vid.read()
    
    if retention:
       Img_write=cv2.imwrite(f'video_to_img\img_{img_count}.jpeg',frame) #saves the frame in provided location
       
       if Img_write:
            print(f'img_{img_count} saved')
        
       if cv2.waitKey(5) & 0xff==ord(' '):  #stops the video when spacebar is pressed
            break
            
       img_count+=1

    else:
        break
        
vid.release()
cv2.destroyAllWindows()
        

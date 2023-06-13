import cv2
import numpy as np
import pyautogui

# Define the screen resolution
SCREEN_SIZE = (1920, 1080)

# Define the codec for the output video
fourcc = cv2.VideoWriter_fourcc(*"XVID")
output = cv2.VideoWriter("screen_recording.avi", fourcc, 20.0, SCREEN_SIZE)

# Create a loop to continuously capture frames
while True:
    # Capture the screen frame
    img = pyautogui.screenshot()
    
    # Convert the image to a numpy array representation
    frame = np.array(img)
    
    # Convert the color space from BGR to RGB
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    
    # Write the frame to the video file
    output.write(frame)
    
    # Display the resulting frame
    cv2.imshow("Screen Recording", frame)
    
    # Check for user input to stop the recording
    if cv2.waitKey(1) == ord("q"):
        break

# Release the video writer and destroy any open windows
output.release()
cv2.destroyAllWindows()

import cv2
import pyautogui
import tkinter as tk

# Define the screen resolution and output filename
SCREEN_SIZE = (1920, 1080)
OUTPUT_FILE = 'screen_recording.mp4'

# Define the codec for the output video
fourcc = cv2.VideoWriter_fourcc(*"mp4v")
out = cv2.VideoWriter(OUTPUT_FILE, fourcc, 20.0, SCREEN_SIZE)

# Initialize the screen recording
is_recording = False

def start_recording():
    global is_recording
    is_recording = True

def stop_recording():
    global is_recording
    is_recording = False

def capture_screen():
    while True:
        if is_recording:
            # Capture the screen frame
            img = pyautogui.screenshot()

            # Convert the captured image to an OpenCV format
            frame = cv2.cvtColor(np.array(img), cv2.COLOR_RGB2BGR)

            # Write the frame to the video file
            out.write(frame)

        # Update the GUI window with the captured frame
        #cv2.imshow('Screen Recording', frame)

        # Check for user input to control the recording
        key = cv2.waitKey(1)

        if key == ord('q'):
            break

# Create the GUI window
window = tk.Tk()
window.title('Screen Recorder')

# Create buttons for starting, stopping, and pausing the recording
start_button = tk.Button(window, text='Start Recording', command=start_recording)
start_button.pack()

stop_button = tk.Button(window, text='Stop Recording', command=stop_recording)
stop_button.pack()

# Start the screen capture loop when the GUI window is opened
window.after(0, capture_screen)
window.mainloop()

# Release the video writer and close OpenCV windows
out.release()
cv2.destroyAllWindows()

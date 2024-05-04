import cv2
import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk

def image_diff(images1_path, image2_path):
    # Read images
    img1 = cv2.imread(image1_path)
    img2 = cv2.imread(image2_path)

    # Convert images to grayscale
    gray_img1 = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
    gray_img2 = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)

    # Compute absolute difference between the images
    diff_img = cv2.absdiff(gray_img1, gray_img2)

    # Find contours of the differences
    contours, _ = cv2.findContours(diff_img, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # Draw rectangles around the contours
    for contour in contours:
        x, y, w, h = cv2.boundingRect(contour)
        cv2.rectangle(img1, (x, y), (x + w, y + h), (0, 0, 255), 2)

    # Convert image to RGB format
    img_rgb = cv2.cvtColor(img1, cv2.COLOR_BGR2RGB)
    img_pil = Image.fromarray(img_rgb)

    # Display the result using Tkinter
    root = tk.Tk()
    root.title("Image Difference")

    # Convert PIL image to Tkinter format and display
    tk_image = ImageTk.PhotoImage(img_pil)
    label = tk.Label(root, image=tk_image)
    label.pack()

    # Function to close the window
    def close_window():
        root.destroy()

    # Button to close the window
    close_button = tk.Button(root, text="Close", command=close_window)
    close_button.pack()

    root.mainloop()

# Function to open file dialog and get image paths
def open_file_dialog():
    file_path = filedialog.askopenfilename()
    return file_path

# Get input image paths using file dialogs
print("Select the first image:")
image1_path = open_file_dialog()
print("Select the second image:")
image2_path = open_file_dialog()

# Call image_diff function with user input image paths
image_diff(image1_path, image2_path)

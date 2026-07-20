import tkinter as tk
from tkinter import filedialog
from PIL import Image
import os

def convert_png_to_jpg(png_path, jpg_path):
    try:
        # Open the PNG image
        png_image = Image.open(png_path)

        # Convert PNG to JPG
        if png_image.mode != 'RGB':
            png_image = png_image.convert('RGB')
        png_image.save(jpg_path)

        result_label.config(text=f"Conversion successful: {png_path} -> {jpg_path}")
    except Exception as e:
        result_label.config(text=f"Conversion failed: {e}")

def browse_file():
    filename = filedialog.askopenfilename(filetypes=[("PNG files", "*.png")])
    input_entry.delete(0, tk.END)
    input_entry.insert(0, filename)

def convert():
    input_path = input_entry.get()
    if not input_path:
        result_label.config(text="Please select a PNG file.")
        return

    output_path = os.path.splitext(input_path)[0] + ".jpg"
    convert_png_to_jpg(input_path, output_path)

root = tk.Tk()
root.title("PNG to JPG Converter")

input_label = tk.Label(root, text="Input PNG File:")
input_label.grid(row=0, column=0, padx=5, pady=5)

input_entry = tk.Entry(root, width=40)
input_entry.grid(row=0, column=1, padx=5, pady=5)

browse_button = tk.Button(root, text="Browse", command=browse_file)
browse_button.grid(row=0, column=2, padx=5, pady=5)

convert_button = tk.Button(root, text="Convert", command=convert)
convert_button.grid(row=1, column=1, padx=5, pady=5)

result_label = tk.Label(root, text="")
result_label.grid(row=2, column=0, columnspan=3, padx=5, pady=5)

root.mainloop()

import tkinter as tk
from tkinter import filedialog
import fitz  # PyMuPDF
import os

def convert_pdf_to_jpg(pdf_path, output_dir):
    try:
        # Open the PDF file
        pdf_document = fitz.open(pdf_path)

        # Iterate through each page and convert it to JPG
        for i in range(len(pdf_document)):
            page = pdf_document[i]
            image = page.get_pixmap()
            jpg_path = os.path.join(output_dir, f"page_{i+1}.jpg")
            image.save(jpg_path)

        result_label.config(text=f"Conversion successful: {pdf_path} -> {output_dir}")
    except Exception as e:
        result_label.config(text=f"Conversion failed: {e}")

def browse_file():
    filename = filedialog.askopenfilename(filetypes=[("PDF files", "*.pdf")])
    input_entry.delete(0, tk.END)
    input_entry.insert(0, filename)

def browse_directory():
    directory = filedialog.askdirectory()
    output_entry.delete(0, tk.END)
    output_entry.insert(0, directory)

def convert():
    input_path = input_entry.get()
    output_dir = output_entry.get()
    if not input_path:
        result_label.config(text="Please select a PDF file.")
        return
    if not output_dir:
        result_label.config(text="Please select an output directory.")
        return

    convert_pdf_to_jpg(input_path, output_dir)

root = tk.Tk()
root.title("PDF to JPG Converter")

input_label = tk.Label(root, text="Input PDF File:")
input_label.grid(row=0, column=0, padx=5, pady=5)

input_entry = tk.Entry(root, width=40)
input_entry.grid(row=0, column=1, padx=5, pady=5)

browse_button = tk.Button(root, text="Browse", command=browse_file)
browse_button.grid(row=0, column=2, padx=5, pady=5)

output_label = tk.Label(root, text="Output Directory:")
output_label.grid(row=1, column=0, padx=5, pady=5)

output_entry = tk.Entry(root, width=40)
output_entry.grid(row=1, column=1, padx=5, pady=5)

output_button = tk.Button(root, text="Browse", command=browse_directory)
output_button.grid(row=1, column=2, padx=5, pady=5)

convert_button = tk.Button(root, text="Convert", command=convert)
convert_button.grid(row=2, column=1, padx=5, pady=5)

result_label = tk.Label(root, text="")
result_label.grid(row=3, column=0, columnspan=3, padx=5, pady=5)

root.mainloop()

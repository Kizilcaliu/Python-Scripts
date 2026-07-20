import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image
import imageio.v3 as iio

class HEICtoJPGConverter:
    def __init__(self, master):
        self.master = master
        master.title("HEIC to JPG Converter")

        # Set window size
        master.geometry("400x150")

        self.label = tk.Label(master, text="Select HEIC file:")
        self.label.pack()

        self.select_button = tk.Button(master, text="Select", command=self.select_file)
        self.select_button.pack()

    def select_file(self):
        file_path = filedialog.askopenfilename(filetypes=[("HEIC files", "*.heic")])
        if file_path:
            self.convert_to_jpg(file_path)

    def convert_to_jpg(self, file_path):
        try:
            # Read the HEIC file using imageio
            image = iio.imread(file_path)

            # Convert to a Pillow image
            pil_image = Image.fromarray(image)

            jpg_path = file_path[:-5] + ".jpg"  # Replace .heic extension with .jpg
            pil_image.save(jpg_path, "JPEG")
            self.show_conversion_message(jpg_path)
        except FileNotFoundError:
            self.show_error_message("File Not Found", "The selected file does not exist.")
        except Exception as e:
            self.show_error_message("Error Converting File", str(e))

    def show_conversion_message(self, jpg_path):
        message = f"Conversion successful! JPG file saved at:\n{jpg_path}"
        messagebox.showinfo("Conversion Complete", message)

    def show_error_message(self, title, message):
        messagebox.showerror(title, message)

def main():
    root = tk.Tk()
    converter = HEICtoJPGConverter(root)
    root.mainloop()

if __name__ == "__main__":
    main()

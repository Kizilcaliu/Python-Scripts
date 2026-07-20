import tkinter as tk
from tkinter import filedialog, messagebox
from ics import Calendar
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
import os

def read_ics(file_path):
    with open(file_path, 'r') as file:
        calendar = Calendar(file.read())
    events = calendar.events
    return events

def save_as_txt(events, save_path):
    with open(save_path, 'w') as file:
        for event in events:
            file.write(f"Event: {event.name}\n")
            file.write(f"Start: {event.begin}\n")
            file.write(f"End: {event.end}\n")
            file.write(f"Description: {event.description}\n")
            file.write(f"Location: {event.location}\n")
            file.write("\n\n")

def save_as_pdf(events, save_path):
    pdf = canvas.Canvas(save_path, pagesize=letter)
    width, height = letter
    pdf.setFont("Helvetica", 12)
    y_position = height - 40

    for event in events:
        pdf.drawString(30, y_position, f"Event: {event.name}")
        y_position -= 20
        pdf.drawString(30, y_position, f"Start: {event.begin}")
        y_position -= 20
        pdf.drawString(30, y_position, f"End: {event.end}")
        y_position -= 20
        pdf.drawString(30, y_position, f"Description: {event.description}")
        y_position -= 20
        pdf.drawString(30, y_position, f"Location: {event.location}")
        y_position -= 40
        if y_position < 40:
            pdf.showPage()
            y_position = height - 40

    pdf.save()

def open_file():
    file_path = filedialog.askopenfilename(filetypes=[("ICS Files", "*.ics")])
    if file_path:
        events = read_ics(file_path)
        format_choice = format_var.get()
        save_path = filedialog.asksaveasfilename(defaultextension=f".{format_choice.lower()}", filetypes=[(f"{format_choice.upper()} Files", f"*.{format_choice.lower()}")])
        if save_path:
            if format_choice == "txt":
                save_as_txt(events, save_path)
            elif format_choice == "pdf":
                save_as_pdf(events, save_path)
            messagebox.showinfo("Success", f"File saved as {save_path}")

root = tk.Tk()
root.title("ICS to Readable Format Converter")

frame = tk.Frame(root, padx=10, pady=10)
frame.pack(padx=10, pady=10)

format_var = tk.StringVar(value="txt")
txt_radio = tk.Radiobutton(frame, text="TXT", variable=format_var, value="txt")
txt_radio.grid(row=0, column=0, padx=5, pady=5)
pdf_radio = tk.Radiobutton(frame, text="PDF", variable=format_var, value="pdf")
pdf_radio.grid(row=0, column=1, padx=5, pady=5)

open_button = tk.Button(frame, text="Open ICS File", command=open_file)
open_button.grid(row=1, column=0, columnspan=2, pady=10)

root.mainloop()

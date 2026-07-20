import tkinter as tk
from tkinter import messagebox
import openpyxl
from openpyxl import Workbook
import os

# Function to get the desktop path
def get_desktop_path():
    return os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop')

# Function to get the full path of the Excel file on the desktop
def get_excel_file_path():
    return os.path.join(get_desktop_path(), 'IT_Equipment_Purchases.xlsx')

# Function to append data to the local Excel file
def append_to_excel(ticket_id, subject, description, agent, created_time, requestor):
    file_path = get_excel_file_path()
    try:
        # Load the workbook if it exists, otherwise create a new one
        try:
            wb = openpyxl.load_workbook(file_path)
            ws = wb.active
        except FileNotFoundError:
            wb = Workbook()
            ws = wb.active
            # Add headers if creating a new file
            ws.append(["Ticket ID", "Subject", "Description", "Agent", "Created Time", "Requestor"])
        
        # Append the new row of data
        ws.append([ticket_id, subject, description, agent, created_time, requestor])
        
        # Save the workbook
        wb.save(file_path)
        
        # Show success message
        messagebox.showinfo("Success", f"Data has been successfully saved to {file_path}")
        
    except Exception as e:
        messagebox.showerror("Error", f"Failed to save data: {e}")

# Function to handle the form submission
def submit_form():
    ticket_id = entry_ticket_id.get()
    subject = entry_subject.get()
    description = entry_description.get()
    agent = entry_agent.get()
    created_time = entry_created_time.get()
    requestor = entry_requestor.get()
    
    if not ticket_id or not subject or not description or not agent or not created_time or not requestor:
        messagebox.showwarning("Input Error", "All fields are required!")
        return
    
    append_to_excel(ticket_id, subject, description, agent, created_time, requestor)
    
    # Clear the form
    entry_ticket_id.delete(0, tk.END)
    entry_subject.delete(0, tk.END)
    entry_description.delete(0, tk.END)
    entry_agent.delete(0, tk.END)
    entry_created_time.delete(0, tk.END)
    entry_requestor.delete(0, tk.END)

# Create the main window
root = tk.Tk()
root.title("IT Equipment Purchase Tracker")

# Create and place the form labels and entries
tk.Label(root, text="Ticket ID:").grid(row=0, column=0, padx=10, pady=5)
entry_ticket_id = tk.Entry(root)
entry_ticket_id.grid(row=0, column=1, padx=10, pady=5)

tk.Label(root, text="Subject:").grid(row=1, column=0, padx=10, pady=5)
entry_subject = tk.Entry(root)
entry_subject.grid(row=1, column=1, padx=10, pady=5)

tk.Label(root, text="Description:").grid(row=2, column=0, padx=10, pady=5)
entry_description = tk.Entry(root)
entry_description.grid(row=2, column=1, padx=10, pady=5)

tk.Label(root, text="Agent:").grid(row=3, column=0, padx=10, pady=5)
entry_agent = tk.Entry(root)
entry_agent.grid(row=3, column=1, padx=10, pady=5)

tk.Label(root, text="Created Time:").grid(row=4, column=0, padx=10, pady=5)
entry_created_time = tk.Entry(root)
entry_created_time.grid(row=4, column=1, padx=10, pady=5)

tk.Label(root, text="Requestor:").grid(row=5, column=0, padx=10, pady=5)
entry_requestor = tk.Entry(root)
entry_requestor.grid(row=5, column=1, padx=10, pady=5)

# Create and place the submit button
submit_button = tk.Button(root, text="Submit", command=submit_form)
submit_button.grid(row=6, column=0, columnspan=2, pady=10)

# Run the Tkinter main loop
root.mainloop()

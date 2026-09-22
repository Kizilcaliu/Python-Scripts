import requests
import json
import csv
import tkinter as tk
from tkinter import simpledialog, messagebox, filedialog

# Zabbix API URL and headers
url = "https://<your-zabbix-domain>/zabbix/api_jsonrpc.php"
headers = {'Content-Type': 'application/json'}
auth_token = None

def authenticate(username, password):
    global auth_token

    data = {
        "jsonrpc": "2.0",
        "method": "user.login",
        "params": {
            "user": username,
            "password": password
        },
        "id": 1
    }

    response = requests.post(url, headers=headers, data=json.dumps(data), verify=False)
    result = response.json()
    if 'result' in result:
        auth_token = result['result']
        return True
    else:
        messagebox.showerror("Authentication Failed", result.get('error', 'No error message provided'))
        return False

def get_hosts():
    data = {
        "jsonrpc": "2.0",
        "method": "host.get",
        "params": {
            "output": ["hostid", "host"],
            "selectInterfaces": ["ip"]
        },
        "auth": auth_token,
        "id": 2
    }

    response = requests.post(url, headers=headers, data=json.dumps(data), verify=False)
    result = response.json()
    if 'result' in result:
        hosts = result['result']
        return [(host['host'], interface['ip']) for host in hosts for interface in host['interfaces']]
    else:
        messagebox.showerror("Error", result.get('error', 'No error message provided'))
        return []

def export_to_csv(data, path):
    with open(path, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["Host Name", "IP Address"])
        writer.writerows(data)
    messagebox.showinfo("Success", f"Data exported to {path}")

def login():
    username = simpledialog.askstring("Username", "Enter your Zabbix username:")
    password = simpledialog.askstring("Password", "Enter your Zabbix password:", show='*')
    
    if username and password:
        if authenticate(username, password):
            save_path = filedialog.asksaveasfilename(defaultextension=".csv", filetypes=[("CSV files", "*.csv")])
            if save_path:
                host_data = get_hosts()
                if host_data:
                    export_to_csv(host_data, save_path)
            else:
                messagebox.showwarning("No Path Selected", "Export path not selected.")
        else:
            messagebox.showerror("Login Failed", "Invalid username or password.")

# Setup the Tkinter root window
root = tk.Tk()
root.withdraw()  # Hide the root window

login()  # Show the login dialog

root.mainloop()  # Run the Tkinter main loop

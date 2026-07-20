# \# Personal Python Tool Suite

# 

# A collection of private, GUI-driven utility applications designed for IT administration, system integrations, and document/data format processing.

# 

# \## 🛠️ Application Catalog

# 

# \### 1. Zabbix Host Exporter

# \* \*\*Folder:\*\* `Zabbix-HostExporter/`

# \* \*\*Description:\*\* Connects via API to an internal Zabbix monitoring server, authenticates the agent, and extracts all monitored hostnames alongside their matching IP addresses into a downloadable CSV spreadsheet.

# \* \*\*Libraries Used:\*\* `requests`, `json`, `csv`, `tkinter`

# 

# \### 2. IT Equipment Purchase Tracker

# \* \*\*Folder:\*\* `IT-Purchase-Tracker/`

# \* \*\*Description:\*\* A manual entry form that appends technical asset purchases directly into a tracking spreadsheet.

# \* \*\*⚠️ Environment Constraint:\*\* This tool is strictly built for \*\*local, single-user operation\*\*. It targets the active Windows logged-in user profile (`%USERPROFILE%\\Desktop`) and writes locally to `IT\_Equipment\_Purchases.xlsx`. It is \*not\* a multi-user cloud tool. For team collaboration, the backend logic must be updated to target a shared UNC network path, a synced OneDrive directory, or an external SQL database.

# \* \*\*Libraries Used:\*\* `openpyxl`, `os`, `tkinter`

# 

# \### 3. ICS Calendar to Document Converter

# \* \*\*Folder:\*\* `ICS-Calendar-Converter/`

# \* \*\*Description:\*\* Imports raw universal calendar feeds (`.ics` files) exported from outlook/Google, extracts schedule data points, and neatly reformats them into human-readable plaintext logs or polished PDF schedule sheets.

# \* \*\*Libraries Used:\*\* `ics`, `reportlab`, `tkinter`

# 

# \### 4. HEIC to JPG Image Converter

# \* \*\*Folder:\*\* `HEIC-to-JPG/`

# \* \*\*Description:\*\* A batch processing image utility that strips Apple mobile compression formatting (`.heic`) and converts image directories into globally compatible `.jpg` formats. Supports compiled deployment configurations.

# \* \*\*Libraries Used:\*\* `imageio`, `Pillow`, `tkinter`, `pyinstaller`

# 

# \## ⚙️ Compilation Note for Portability

# To deploy any of these visual utilities as standalone desktop applications (`.exe`) on a new workstation without installing raw Python, navigate to the specific project directory containing a `.spec` blueprint file and execute:

# 

# ```cmd

# pip install pyinstaller

# pyinstaller \[App\_Filename].spec

# ```




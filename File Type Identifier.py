import tkinter as tk
from tkinter import filedialog, messagebox
import os

# Magic number signatures
FILE_SIGNATURES = {
    b"\x25\x50\x44\x46": "PDF Document",
    b"\x89\x50\x4E\x47\x0D\x0A\x1A\x0A": "PNG Image",
    b"\xFF\xD8\xFF": "JPEG Image",
    b"\x50\x4B\x03\x04": "ZIP Archive",
    b"\x52\x61\x72\x21\x1A\x07\x00": "RAR Archive",
    b"\x4D\x5A": "Windows Executable (EXE)",
    b"\x7F\x45\x4C\x46": "Linux Executable (ELF)",
    b"\x49\x44\x33": "MP3 Audio",
    b"\x1F\x8B": "GZIP Archive"
}

def identify_file_type(file_path):
    try:
        with open(file_path, "rb") as f:
            header = f.read(16)

        for sig, ftype in FILE_SIGNATURES.items():
            if header.startswith(sig):
                return ftype

        return "Unknown / Unsupported file type"
    except Exception as e:
        return f"Error: {e}"

def select_file():
    file_path = filedialog.askopenfilename()
    if not file_path:
        return

    detected_type = identify_file_type(file_path)
    file_name = os.path.basename(file_path)
    extension = os.path.splitext(file_path)[1] or "None"

    result_text = (
        f"File Name       : {file_name}\n"
        f"File Extension  : {extension}\n"
        f"Detected Type   : {detected_type}\n"
    )

    if detected_type != "Unknown / Unsupported file type":
        if extension != "None" and detected_type.lower().split()[0] not in extension.lower():
            result_text += "\nWARNING: Extension does NOT match actual file type!"

    output_box.config(state="normal")
    output_box.delete(1.0, tk.END)
    output_box.insert(tk.END, result_text)
    output_box.config(state="disabled")

# GUI setup
root = tk.Tk()
root.title("File Type Identifier – Security Tool")
root.geometry("520x300")
root.resizable(False, False)

title_label = tk.Label(
    root,
    text="File Type Identifier (Magic Number Analysis)",
    font=("Segoe UI", 12, "bold")
)
title_label.pack(pady=10)

select_button = tk.Button(
    root,
    text="Select File",
    command=select_file,
    width=20,
    height=2
)
select_button.pack(pady=10)

output_box = tk.Text(
    root,
    width=60,
    height=8,
    state="disabled",
    font=("Consolas", 10)
)
output_box.pack(padx=10, pady=10)

root.mainloop()

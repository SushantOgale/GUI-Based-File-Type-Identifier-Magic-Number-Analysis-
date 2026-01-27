import tkinter as tk
from tkinter import filedialog
import os



FILE_TYPES = {
    b"%PDF": ("PDF Document", [".pdf"]),
    b"\x89PNG\r\n\x1a\n": ("PNG Image", [".png"]),
    b"\xFF\xD8\xFF": ("JPEG Image", [".jpg", ".jpeg"]),
    b"GIF87a": ("GIF Image", [".gif"]),
    b"GIF89a": ("GIF Image", [".gif"]),
    b"\x50\x4B\x03\x04": ("ZIP / Office Document", [".zip", ".docx", ".xlsx", ".pptx"]),
    b"Rar!\x1A\x07\x00": ("RAR Archive", [".rar"]),
    b"\x1F\x8B": ("GZIP Archive", [".gz"]),
    b"MZ": ("Windows Executable (EXE)", [".exe", ".dll"]),
    b"\x7FELF": ("Linux Executable (ELF)", [".elf"]),
    b"ID3": ("MP3 Audio", [".mp3"]),
    b"OggS": ("OGG Audio", [".ogg"]),
    b"RIFF": ("WAV / AVI Media", [".wav", ".avi"]),
}

def detect_file_type(path):
    with open(path, "rb") as f:
        data = f.read(1024)

    # Primary detection (strict)
    for signature, (ftype, extensions) in FILE_TYPES.items():
        if data.startswith(signature):
            return ftype, extensions, "SAFE"

    # Secondary detection (embedded PDF)
    if b"%PDF" in data:
        return "PDF Document (Embedded / Malformed)", [".pdf"], "SUSPICIOUS"

    return "Unknown / Suspicious File", [], "DANGER"



def select_file():
    file_path = filedialog.askopenfilename()
    if not file_path:
        return

    detected_type, valid_exts, risk = detect_file_type(file_path)
    file_ext = os.path.splitext(file_path)[1].lower() or "None"

    output.config(state="normal")
    output.delete("1.0", tk.END)

    output.insert(tk.END, f"File Name      : {os.path.basename(file_path)}\n")
    output.insert(tk.END, f"File Extension : {file_ext}\n")
    output.insert(tk.END, f"Detected Type  : {detected_type}\n\n")



    if risk == "DANGER":
        output.insert(
            tk.END,
            "HIGH RISK: Unknown or potentially malicious file detected.\n",
            "danger"
        )

    elif risk == "SUSPICIOUS":
        output.insert(
            tk.END,
            "SUSPICIOUS: Embedded or malformed file detected.\n",
            "warning"
        )

    elif file_ext not in valid_exts:
        output.insert(
            tk.END,
            "WARNING: Extension does NOT match detected file type.\n",
            "danger"
        )

    else:
        output.insert(
            tk.END,
            "SAFE: File extension matches detected file type.\n",
            "safe"
        )

    output.config(state="disabled")



root = tk.Tk()
root.title("File Type Identifier – Security Tool")
root.geometry("900x550")
root.resizable(False, False)

title = tk.Label(
    root,
    text="File Type Identifier (Magic Number Analysis)",
    font=("Segoe UI", 14, "bold")
)
title.pack(pady=10)

btn = tk.Button(
    root,
    text="Select File",
    width=20,
    height=2,
    command=select_file
)
btn.pack(pady=10)

output = tk.Text(
    root,
    width=100,
    height=18,
    font=("Consolas", 11),
    state="disabled"
)
output.pack(padx=10, pady=10)


output.tag_config("danger", foreground="red")
output.tag_config("warning", foreground="orange")
output.tag_config("safe", foreground="green")

root.mainloop()

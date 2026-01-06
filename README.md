# GUI Based File Type Identifier Magic Number Analysis
A pyhtone based GUI security tool which help us identify the type of the file using the magic number, Magic number is also called as file signature this a unique sequence of bytes at the beginning of a file that identifies its formata unique sequence of bytes at the beginning of a file that identifies its format

Project Overview

File extensions can be easily spoofed (e.g., invoice.pdf.exe).
This tool analyzes the raw file header bytes to determine the true file format, helping detect:

Malware disguised as documents

Renamed executables

Suspicious or unknown files

The application provides a simple GUI built with Tkinter, making it usable without command-line knowledge.

✨ Features

🔍 File type identification using magic numbers

🖥️ User-friendly GUI interface

⚠️ Detects extension mismatch (spoofing alert)

📁 Works on any file type

🌐 Cross-platform (Windows, Linux, macOS)

🔒 Offline & lightweight (no external APIs)

🧠 How It Works

User selects a file via GUI

Tool reads the first few bytes of the file

Compares bytes against known file signatures

Displays:

File name

File extension

Actual detected file type

Warns if extension does not match the real file type

🧪 Example

File name:

resume.pdf


Detected signature:

4D 5A


Result:

Windows Executable (EXE)
⚠ WARNING: Extension does NOT match actual file type!


➡ Indicates potential malware masquerading as a PDF

🛠️ Technologies Used

Python 3

Tkinter (GUI)

Magic number / file signature analysis

📂 Project Structure
file-type-identifier/
│
├── file_identifier_gui.py
├── README.md

▶️ How to Run
1. Clone the repository
git clone [https://github.com/your-username/file-type-identifier.git](https://github.com/SushantOgale/GUI-Based-File-Type-Identifier-Magic-Number-Analysis-.git)
cd file-type-identifier

2. Run the application
python file_identifier_gui.py

📚 Use Cases

Malware analysis

Digital forensics

Secure file upload validation

SOC alert triage

Cybersecurity labs & assignments

Learning file internals

🎓 Academic & Resume Value

You can describe this project as:

“A GUI-based file type identification tool using magic number analysis to detect extension spoofing and disguised malware.”

This project demonstrates:

Security fundamentals

Low-level file analysis

Practical defensive security skills

🔮 Future Enhancements

Hash generation (MD5 / SHA256)

VirusTotal API integration

Batch folder scanning

Drag-and-drop GUI

Threat severity scoring

PE / ELF deep analysis

Flask-based web dashboard

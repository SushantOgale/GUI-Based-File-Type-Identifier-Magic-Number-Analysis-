# GUI File Type Identifier (Magic Number Analysis)
A pyhtone based GUI security tool which help us identify the type of the file using the magic number, Magic number is also called as file signature this a unique sequence of bytes at the beginning of a file that identifies its formata unique sequence of bytes at the beginning of a file that identifies its format

Project Overview

File extensions can be easily spoofed (e.g., invoice.pdf.exe).
This tool analyzes the raw file header bytes to determine the true file format, helping detect:

Malware disguised as documents

Renamed executables

Suspicious or unknown files

The application provides a simple GUI built with Tkinter, making it usable without command-line knowledge.


 
FEATURES

1.File type identification using magic numbers

2.User-friendly GUI interface

3.Detects extension mismatch (spoofing alert)

4.Works on any file type

5.Cross-platform (Windows, Linux, macOS)

6.Offline & lightweight (no external APIs)



HOW IT WORK

1.User selects a file via GUI

2.Tool reads the first few bytes of the file

3.Compares bytes against known file signatures


Displays:

-File name

-File extension

-Actual detected file type

-Warns if extension does not match the real file type



HOW TO USE

1. Clone the repository
git clone [https://github.com/your-username/file-type-identifier.git](https://github.com/SushantOgale/GUI-Based-File-Type-Identifier-Magic-Number-Analysis-.git)


2. Run the application
python File Type Identifier.py



TOOL CAN BE USED IN-

1.Malware analysis 

2.Digital forensics

3.Secure file upload validation

4.SOC alert triage

5.Cybersecurity labs & assignments



project as:

“A GUI-based file type identification tool using magic number analysis to detect extension spoofing and disguised malware.”

This project demonstrates:
1.Security fundamentals
       
2.Low-level file analysis
   
3.Practical defensive security skills

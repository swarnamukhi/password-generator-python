🔐 Python Password Generator

A beginner‑to‑advanced project built during the Oasis Infobyte internship.It provides two ways to generate secure passwords:

Interface

File

Highlights

Command‑line (CLI)

password_console.py

Interactive prompts for length & character sets

Graphical (GUI)

password_gui.py

Tkinter window with check‑boxes and 1‑click Copy to Clipboard

✨ Features

Random password generation using Python’s random module

User‑selectable character types: uppercase, lowercase, digits, symbols

Length range 4 – 128 characters (default = 12)

Clipboard integration in GUI (via pyperclip)

Modular core logic in password_core.py reused by both interfaces

📂 Project Structure

password_generator/
├── password_console.py      # CLI version
├── password_gui.py          # Tkinter GUI version
├── password_core.py         # Shared generate_password() logic
└── README.md                # You are here

🚀 Quick Start

Prerequisite: Python ≥ 3.9 installed

# 1️⃣ Clone the repository
$ git clone https://github.com/swarnamukhi/password-generator-python.git
$ cd password-generator-python

# 2️⃣ (Recommended) create a virtual environment
$ python -m venv venv
$ source venv/Scripts/activate      # Windows

# 3️⃣ Install clipboard library (optional for GUI)
$ pip install pyperclip

▶️ Run the CLI version

python password_console.py

Follow the prompts to choose length and character sets.

▶️ Run the GUI version

python password_gui.py

Use the window controls, click Generate Password, then Copy Password.

🛠  Technologies Used

Python 3.11

Tkinter (built‑in GUI library)

pyperclip for clipboard support

Git / GitHub for version control


📚 Learning Highlights (Oasis Task Requirements)

Randomization: random.choice & random.choices

Input Validation: ensured positive length & at least one character type

Character‑Set Handling: string.ascii_uppercase, string.digits, string.punctuation

GUI Layout: Tkinter grid() manager, BooleanVar, IntVar

🤝 Contributing

Pull requests are welcome. Please open an issue first to discuss your idea.

📄 License

This project is licensed under the MIT License. See LICENSE for details.

🙋‍♀️ Author

B. Swarnamukhi — Always learning, one project at a time.LinkedIn: https://www.linkedin.com/in/swarnamukhibandi/


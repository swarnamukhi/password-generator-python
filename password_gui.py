import  tkinter as tk
from tkinter import ttk
import string
import random
import pyperclip

root = tk.Tk()
root.title("pass word generator")
root.geometry("400x300")

length_label = ttk.Label(root,text ="passwod_length")
length_label.grid(row=0, column=0, sticky="w", padx=10, pady=5)

length_var  = tk.IntVar(value=12)   # control variable

length_spin = ttk.Spinbox(
    root,
    from_=4, to=128,
    textvariable=length_var,
    width=5
)
length_spin.grid(row=0, column=1, sticky="w", padx=10, pady=5)


uppercase_var = tk.BooleanVar(value=False)  # default: checked
uppercase_check = ttk.Checkbutton(root,text="Include UPPERCASE (A–Z)",variable=uppercase_var)
uppercase_check.grid(row=1, column=0,  sticky="w", padx=10, pady=5)

lowercasevar = tk.BooleanVar(value= True)
lowercase_check = ttk.Checkbutton(root,text="Include lower case(a to z)",variable=lowercasevar)
lowercase_check.grid(row=2,column=0,sticky="w", padx=10, pady=5)

digitsvar = tk.BooleanVar(value=True)
digit_check = ttk.Checkbutton(root,text= "include digits from 0 to 9",variable=digitsvar)
digit_check.grid(row=3,column=0,sticky="w",padx=10,pady=10)

specialcharvar = tk.BooleanVar(value=True)
specialcharcheck = ttk.Checkbutton(root,text=" include special char ' @ # $ % )?'",variable=specialcharvar)
specialcharcheck.grid(row=4,column=0,sticky="w",padx=10,pady=10)


def generate_password():
    pool = ""
    
    if uppercase_var.get():
        pool += string.ascii_uppercase
    if lowercasevar.get():
        pool += string.ascii_lowercase
    if digitsvar.get():
        pool += string.digits
    if specialcharvar.get():
        pool += string.punctuation
    
    if not pool:
        result_label.config(text="❌ Select at least one character set.")
        return

    length = length_var.get()
    password = "".join(random.choices(pool, k=length))
    result_label.config(text=f"✅ {password}")


def copy_to_clipboard():
    password = result_label.cget("text").replace("✅ ", "")
    if password:
        pyperclip.copy(password)
        result_label.config(text=f"✅ {password}  (📋 Copied!)")

generate_button = tk.Button(root,text="Genarate password",command=generate_password)
generate_button.grid(row=5, column=0, columnspan=2, pady=10)


result_label = ttk.Label(root, text="")
result_label.grid(row=6, column=0, columnspan=2, pady=5)

copy_button = ttk.Button(root, text="Copy Password", command=copy_to_clipboard)
copy_button.grid(row=7, column=0, columnspan=2, pady=5)

   
root.mainloop()


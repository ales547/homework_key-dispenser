import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import os
from datetime import datetime


directory_path = "./unused/"
log_directory_path = "./used/"


def get_files():
    files = []
    for file_name in os.listdir(directory_path):
        if file_name.endswith(".txt"):
            files.append(file_name)
    return files


def write_log(log_file_name, code):
    log_file = open(log_directory_path + log_file_name, "a")
    user_name = os.getlogin()
    current_date = datetime.now().isoformat(" ", "seconds")
    report = code + " - " + user_name + " - " + current_date + os.linesep
    log_file.write(report)


def get_key(file_name):
    key_file = open(directory_path + file_name, "r")
    keys = key_file.readlines()
    key_file.close()
    if len(keys) > 0:
        first_code = keys[0].strip()
        other_codes = keys[1:]
        key_file = open(directory_path + file_name, "w")
        key_file.writelines(other_codes)
        key_file.close()
        write_log(file_name, first_code)
        return first_code


def button1_callback():
    listbox1.delete(0, tk.END)
    key = get_key(combo1.get())
    if key:
        listbox1.insert(0, key)
    else:
        messagebox.showerror("Error", "No keys remaining in the file")


def button2_callback():
    app.destroy()


app = tk.Tk(className="key dispenser")

label1 = tk.Label(app, text="Keys Batch:")
label1.grid(column=0, row=0, padx=10, pady=5)

combo1 = ttk.Combobox(
    app, values=get_files(), state="readonly")
combo1.grid(column=1, row=0, columnspan=2, padx=5)
combo1.current(0)

button1 = tk.Button(
    app, text="Get Key", command=button1_callback)
button1.grid(column=1, row=1, pady=5)

button2 = tk.Button(
    app, text="Cancel", command=button2_callback)
button2.grid(column=2, row=1)

listbox1 = tk.Listbox(app, height=2)
listbox1.grid(column=0, row=2, columnspan=3,
              pady=5, padx=5, sticky="WE")


def main():
    app.mainloop()


if __name__ == "__main__":
    main()

import tkinter as tk
from tkinter.filedialog import askopenfilename, asksaveasfilename
def openFile():
    filepath = askopenfilename(filetypes=[("Text Files", "*.txt"), ("All files", "*.*")])

    if not filepath:
        return
    with open(filepath, "r") as input_file:
        text = input_file.read()
        txt_edit.delete("1.0", tk.END)
        txt_edit.insert(tk.END, text)
    window.title(f"Text Editor - {filepath}")
    return

def saveFile():
    filepath = asksaveasfilename(
        defaultextension="txt",
        filetypes=[("Text Files", "*.txt"), ("All files", "*.*")],
    )
    if not filepath:
        return
    with open(filepath, "w") as output_file:
        text = txt_edit.get("1.0", tk.END)
        output_file.write(text)
    return
window = tk.Tk()
window.title("Text Editor")

window.rowconfigure(0, minsize=600)
window.columnconfigure(1, minsize=600)
txt_edit = tk.Text(window)
frameButtons = tk.Frame(window, relief=tk.RAISED)
openButton = tk.Button(frameButtons, text="Open", command=openFile)
saveButton = tk.Button(frameButtons, text="Save", command=saveFile)
openButton.grid(row=0, column=0, sticky="ew")
saveButton.grid(row=1, column=0, sticky="ew")
frameButtons.grid(row=0, column=0, sticky="nw")
txt_edit.grid(row=0, column=1, sticky="nsew")
window.mainloop()

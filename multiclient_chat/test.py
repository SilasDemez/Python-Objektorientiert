import tkinter as tk

window = tk.Tk()
text = tk.Text(state='normal')
text.grid(column=0, row=0)

text.insert(tk.END, "test")
window.mainloop()

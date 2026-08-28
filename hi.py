import tkinter as tk

root = tk.Tk()
root.title("bb8therobot")
root.geometry("300x150")
root.configure(bg="#0d0d0d")

label = tk.Label(root, text="hi", font=("Arial", 48, "bold"), fg="#ff2e63", bg="#0d0d0d")
label.pack(expand=True)

root.mainloop()

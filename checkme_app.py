import tkinter as tk

# create window
root = tk.Tk()
root.title("CheckMe")

# add simple text
label = tk.Label(root, text="Welcome to CheckMe")
label.pack()

# run app
root.mainloop()
import tkinter as tk

# create window
root = tk.Tk()
root.title("CheckMe")
root.geometry("400x250")

# add simple text
label = tk.Label(root, text="Welcome to CheckMe", font=("Arial", 18))
label.pack(pady=80)

# run app
root.mainloop()
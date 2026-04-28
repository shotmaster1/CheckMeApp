import tkinter as tk

# create window
root = tk.Tk()
root.title("CheckMe")
root.geometry("400x300")

# title
title = tk.Label(root, text="Daily Mental Health Check-In", font=("Arial", 16))
title.pack(pady=10)

# variables for checkboxes
stress_var = tk.IntVar()
sleep_var = tk.IntVar()
mood_var = tk.IntVar()

# checklist questions
tk.Checkbutton(root, text="I feel low stress today", variable=stress_var).pack(anchor="w", padx=20)
tk.Checkbutton(root, text="I slept well last night", variable=sleep_var).pack(anchor="w", padx=20)
tk.Checkbutton(root, text="I feel positive today", variable=mood_var).pack(anchor="w", padx=20)

# run app
root.mainloop()
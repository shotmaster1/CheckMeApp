import tkinter as tk

# create window
root = tk.Tk()
root.title("CheckMe")
root.geometry("400x350")

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

# function for submit
def submit():
    score = 0

    if stress_var.get() == 1:
        score += 1
    if sleep_var.get() == 1:
        score += 1
    if mood_var.get() == 1:
        score += 1

    if score == 3:
        result = "You're doing great today!"
    elif score == 2:
        result = "You're doing okay, take care of yourself."
    else:
        result = "You may need rest or support today."

    result_label.config(text=result)

# submit button
submit_btn = tk.Button(root, text="Submit", command=submit)
submit_btn.pack(pady=10)

# result label
result_label = tk.Label(root, text="", font=("Arial", 12))
result_label.pack(pady=10)

# run app
root.mainloop()
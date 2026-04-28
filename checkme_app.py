import tkinter as tk

# create window
root = tk.Tk()
root.title("CheckMe")
root.geometry("450x400")

# title
title = tk.Label(root, text="Daily Mental Health Check-In", font=("Arial", 16))
title.pack(pady=10)

# instructions
instructions = tk.Label(root, text="Check each statement that feels true today.")
instructions.pack(pady=5)

# variables for checkboxes
stress_var = tk.IntVar()
sleep_var = tk.IntVar()
mood_var = tk.IntVar()

# checklist questions
tk.Checkbutton(root, text="I feel low stress today", variable=stress_var).pack(anchor="w", padx=30)
tk.Checkbutton(root, text="I slept well last night", variable=sleep_var).pack(anchor="w", padx=30)
tk.Checkbutton(root, text="I feel positive today", variable=mood_var).pack(anchor="w", padx=30)

# function for submit
def submit():
    score = 0

    if stress_var.get() == 1:
        score += 1
    if sleep_var.get() == 1:
        score += 1
    if mood_var.get() == 1:
        score += 1

    score_label.config(text="Score: " + str(score) + "/3")

    if score == 3:
        result = "You're doing great today. Keep your routine going."
    elif score == 2:
        result = "You're doing okay. Take a short break and check in later."
    else:
        result = "You may need rest or support today. Try one small healthy step."

    result_label.config(text=result)

# submit button
submit_btn = tk.Button(root, text="Submit Check-In", command=submit)
submit_btn.pack(pady=10)

# score and result labels
score_label = tk.Label(root, text="Score: --/3", font=("Arial", 12))
score_label.pack(pady=5)

result_label = tk.Label(root, text="", font=("Arial", 12), wraplength=350)
result_label.pack(pady=10)

# run app
root.mainloop()
import tkinter as tk

root = tk.Tk()
root.title("CheckMe")
root.geometry("560x600")
root.configure(bg="#e8f4ff")

title = tk.Label(
    root,
    text="CheckMe Daily Mental Health Check-In",
    font=("Arial", 18, "bold"),
    bg="#e8f4ff",
    fg="#0b3954"
)
title.pack(pady=15)

quote = tk.Label(
    root,
    text='"Small steps still move you forward."',
    font=("Arial", 12, "italic"),
    bg="#e8f4ff",
    fg="#3d5a80",
    wraplength=470
)
quote.pack(pady=5)

instructions = tk.Label(
    root,
    text="Answer today’s check-in by selecting each statement that feels true.",
    font=("Arial", 12),
    bg="#e8f4ff",
    fg="#222222",
    wraplength=470
)
instructions.pack(pady=10)

checklist_frame = tk.Frame(root, bg="white", padx=20, pady=18)
checklist_frame.pack(pady=10)

stress_var = tk.IntVar()
sleep_var = tk.IntVar()
mood_var = tk.IntVar()
exercise_var = tk.IntVar()
hydration_var = tk.IntVar()
support_var = tk.IntVar()

questions = [
    ("I feel like my stress level is manageable today.", stress_var),
    ("I got enough sleep or rest to function well today.", sleep_var),
    ("My mood feels mostly positive or stable today.", mood_var),
    ("I exercised, stretched, walked, or moved my body today.", exercise_var),
    ("I drank enough water and took care of my basic needs today.", hydration_var),
    ("I talked to someone, asked for help, or felt supported today.", support_var),
]

for question, variable in questions:
    tk.Checkbutton(
        checklist_frame,
        text=question,
        variable=variable,
        bg="white",
        fg="#222222",
        font=("Arial", 11),
        wraplength=460,
        justify="left"
    ).pack(anchor="w", pady=4)

def submit():
    score = 0

    if stress_var.get() == 1:
        score += 1
    if sleep_var.get() == 1:
        score += 1
    if mood_var.get() == 1:
        score += 1
    if exercise_var.get() == 1:
        score += 1
    if hydration_var.get() == 1:
        score += 1
    if support_var.get() == 1:
        score += 1

    score_label.config(text="Score: " + str(score) + "/6")

    if score >= 5:
        result = "Great check-in. You seem to be doing well today. Keep protecting your routine."
    elif score >= 3:
        result = "You are doing okay, but there is room to care for yourself more today. Try one small healthy action."
    else:
        result = "Today may be a heavier day. Consider resting, reaching out to someone, or doing one small thing to reset."

    result_label.config(text=result)

def reset():
    stress_var.set(0)
    sleep_var.set(0)
    mood_var.set(0)
    exercise_var.set(0)
    hydration_var.set(0)
    support_var.set(0)
    score_label.config(text="Score: --/6")
    result_label.config(text="")

button_frame = tk.Frame(root, bg="#e8f4ff")
button_frame.pack(pady=10)

submit_btn = tk.Button(
    button_frame,
    text="Submit Check-In",
    command=submit,
    bg="#0077b6",
    fg="white",
    font=("Arial", 12, "bold"),
    padx=14,
    pady=7
)
submit_btn.pack(side="left", padx=8)

reset_btn = tk.Button(
    button_frame,
    text="Reset",
    command=reset,
    bg="#0077b6",
    fg="white",
    font=("Arial", 12, "bold"),
    padx=14,
    pady=7
)
reset_btn.pack(side="left", padx=8)

score_label = tk.Label(
    root,
    text="Score: --/6",
    font=("Arial", 13, "bold"),
    bg="#e8f4ff",
    fg="#0b3954"
)
score_label.pack(pady=10)

result_label = tk.Label(
    root,
    text="",
    font=("Arial", 12),
    bg="#e8f4ff",
    fg="#222222",
    wraplength=470
)
result_label.pack(pady=10)

root.mainloop()
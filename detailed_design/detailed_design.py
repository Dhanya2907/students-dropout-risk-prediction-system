import tkinter as tk

root = tk.Tk()

root.title("Detailed Design")
root.geometry("1100x700")
root.configure(bg="#F4F7FB")

tk.Label(
    root,
    text="DETAILED DESIGN",
    font=("Times New Roman", 24, "bold"),
    bg="#172554",
    fg="white",
    pady=20
).pack(fill="x")

modules = [
    (
        "Student Data Module",
        "Input:\nStudent information\n\n"
        "Process:\nValidate fields\nCheck duplicate ID\n\n"
        "Output:\nValid student record",
        "#2563EB"
    ),
    (
        "Prediction Module",
        "Input:\nAcademic features\n\n"
        "Process:\nLoad Random Forest\nPredict risk\n\n"
        "Output:\nLOW / MEDIUM / HIGH",
        "#EA580C"
    ),
    (
        "Score Module",
        "Input:\nAcademic performance\n\n"
        "Process:\nNormalize values\nCalculate weighted score\n\n"
        "Output:\nScore / 100",
        "#16A34A"
    ),
    (
        "Recommendation Module",
        "Input:\nRisk and weak areas\n\n"
        "Process:\nAnalyse performance\nGenerate suggestions\n\n"
        "Output:\nPersonalized recommendations",
        "#DC2626"
    )
]

frame = tk.Frame(root, bg="#F4F7FB")
frame.pack(fill="both", expand=True, padx=30, pady=25)

for i, (title, description, color) in enumerate(modules):

    card = tk.Frame(
        frame,
        bg="white",
        highlightbackground="#E2E8F0",
        highlightthickness=1
    )

    card.grid(
        row=i // 2,
        column=i % 2,
        padx=10,
        pady=10,
        sticky="nsew"
    )

    frame.columnconfigure(i % 2, weight=1)
    frame.rowconfigure(i // 2, weight=1)

    tk.Label(
        card,
        text=title,
        font=("Times New Roman", 16, "bold"),
        bg="white",
        fg=color
    ).pack(pady=(20, 10))

    tk.Label(
        card,
        text=description,
        font=("Times New Roman", 11),
        bg="white",
        fg="#172033",
        justify="left"
    ).pack(
        anchor="w",
        padx=25,
        pady=15
    )

root.mainloop()
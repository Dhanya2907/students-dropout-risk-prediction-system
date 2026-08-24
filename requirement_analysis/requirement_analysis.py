import tkinter as tk

root = tk.Tk()
root.title("Requirement Analysis")
root.geometry("1000x650")
root.configure(bg="#F4F7FB")

tk.Label(
    root,
    text="REQUIREMENT ANALYSIS",
    font=("Times New Roman", 24, "bold"),
    bg="#172554",
    fg="white",
    pady=20
).pack(fill="x")

requirements = [
    ("Functional Requirements",
     "• Student registration\n"
     "• Student data storage\n"
     "• Dropout risk prediction\n"
     "• Performance score calculation\n"
     "• Risk classification\n"
     "• Recommendation generation\n"
     "• n8n notification"),

    ("Input Requirements",
     "• Student ID\n"
     "• Student Name\n"
     "• Attendance\n"
     "• Study Hours\n"
     "• Internal Marks\n"
     "• Assignment Marks\n"
     "• Previous Semester GPA\n"
     "• Number of Backlogs"),

    ("Software Requirements",
     "• Python\n"
     "• Tkinter\n"
     "• OpenPyXL\n"
     "• Scikit-learn\n"
     "• Joblib\n"
     "• Requests\n"
     "• n8n"),

    ("Output Requirements",
     "• LOW Risk\n"
     "• MEDIUM Risk\n"
     "• HIGH Risk\n"
     "• Performance Score\n"
     "• Prediction Probability\n"
     "• Recommendations")
]

container = tk.Frame(root, bg="#F4F7FB")
container.pack(fill="both", expand=True, padx=30, pady=30)

for index, (title, text) in enumerate(requirements):

    card = tk.Frame(
        container,
        bg="white",
        highlightbackground="#E2E8F0",
        highlightthickness=1
    )

    card.grid(
        row=index // 2,
        column=index % 2,
        padx=10,
        pady=10,
        sticky="nsew"
    )

    container.columnconfigure(index % 2, weight=1)
    container.rowconfigure(index // 2, weight=1)

    tk.Label(
        card,
        text=title,
        font=("Times New Roman", 16, "bold"),
        bg="white",
        fg="#2563EB"
    ).pack(pady=(20, 10))

    tk.Label(
        card,
        text=text,
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
import tkinter as tk
from tkinter import ttk

BG = "#F4F7FB"
WHITE = "#FFFFFF"
SIDEBAR = "#172554"
PRIMARY = "#2563EB"
TEXT = "#172033"
GRAY = "#64748B"
GREEN = "#16A34A"
ORANGE = "#EA580C"
RED = "#DC2626"
LIGHT_BLUE = "#EFF6FF"
LIGHT_GREEN = "#F0FDF4"
LIGHT_ORANGE = "#FFF7ED"
LIGHT_RED = "#FEF2F2"
BORDER = "#E2E8F0"

root = tk.Tk()

root.title(
    "System Design - Student Dropout Risk Prediction System"
)

root.geometry("1200x750")
root.minsize(1000, 650)
root.configure(bg=BG)

header = tk.Frame(
    root,
    bg=SIDEBAR,
    height=80
)

header.pack(fill="x")
header.pack_propagate(False)

tk.Label(
    header,
    text="SYSTEM DESIGN",
    font=("Times New Roman", 24, "bold"),
    bg=SIDEBAR,
    fg=WHITE
).pack(
    side="left",
    padx=30
)

tk.Label(
    header,
    text="Smart Student Dropout Risk Prediction System",
    font=("Times New Roman", 13),
    bg=SIDEBAR,
    fg="#BFDBFE"
).pack(side="left")

main = tk.Frame(
    root,
    bg=BG
)

main.pack(
    fill="both",
    expand=True,
    padx=25,
    pady=20
)

tk.Label(
    main,
    text="System Architecture",
    font=("Times New Roman", 22, "bold"),
    bg=BG,
    fg=TEXT
).pack(anchor="w")

tk.Label(
    main,
    text=(
        "The system is designed using modular components "
        "for student data management, machine learning "
        "prediction and automated notification."
    ),
    font=("Times New Roman", 12),
    bg=BG,
    fg=GRAY
).pack(
    anchor="w",
    pady=(5, 20)
)

architecture = tk.Frame(
    main,
    bg=WHITE,
    highlightbackground=BORDER,
    highlightthickness=1
)

architecture.pack(fill="x")


def create_module(
    parent,
    row,
    column,
    title,
    description,
    color,
    background
):

    frame = tk.Frame(
        parent,
        bg=background,
        highlightbackground=BORDER,
        highlightthickness=1
    )

    frame.grid(
        row=row,
        column=column,
        padx=15,
        pady=15,
        sticky="nsew"
    )

    parent.columnconfigure(
        column,
        weight=1
    )

    tk.Label(
        frame,
        text=title,
        font=("Times New Roman", 14, "bold"),
        bg=background,
        fg=color
    ).pack(pady=(15, 8))

    tk.Label(
        frame,
        text=description,
        font=("Times New Roman", 10),
        bg=background,
        fg=TEXT,
        justify="center",
        wraplength=220
    ).pack(
        padx=15,
        pady=(0, 15)
    )

    return frame


create_module(
    architecture,
    0,
    0,
    "1. User Interface",
    "Tkinter GUI\n\n"
    "Student details entry\n"
    "Dashboard\n"
    "Student list\n"
    "Risk prediction",
    PRIMARY,
    LIGHT_BLUE
)

create_module(
    architecture,
    0,
    1,
    "2. Data Storage",
    "Excel Database\n\n"
    "student_details.xlsx\n\n"
    "Stores student information "
    "and academic details.",
    GREEN,
    LIGHT_GREEN
)

create_module(
    architecture,
    0,
    2,
    "3. Machine Learning",
    "Random Forest Model\n\n"
    "dropout_risk_model.pkl\n\n"
    "Predicts LOW, MEDIUM "
    "or HIGH dropout risk.",
    ORANGE,
    LIGHT_ORANGE
)

create_module(
    architecture,
    0,
    3,
    "4. Risk Analysis",
    "Performance Score\n\n"
    "Attendance\n"
    "Study Hours\n"
    "Internal Marks\n"
    "Assignment Marks\n"
    "GPA & Backlogs",
    RED,
    LIGHT_RED
)

tk.Label(
    main,
    text="System Flow",
    font=("Times New Roman", 20, "bold"),
    bg=BG,
    fg=TEXT
).pack(
    anchor="w",
    pady=(25, 10)
)

flow = tk.Frame(
    main,
    bg=WHITE,
    highlightbackground=BORDER,
    highlightthickness=1
)

flow.pack(fill="x")


def flow_step(
    parent,
    column,
    number,
    title,
    description
):

    frame = tk.Frame(
        parent,
        bg=WHITE
    )

    frame.grid(
        row=0,
        column=column,
        padx=10,
        pady=18,
        sticky="nsew"
    )

    parent.columnconfigure(
        column,
        weight=1
    )

    tk.Label(
        frame,
        text=str(number),
        font=("Times New Roman", 15, "bold"),
        bg=PRIMARY,
        fg=WHITE,
        width=3
    ).pack(pady=(0, 8))

    tk.Label(
        frame,
        text=title,
        font=("Times New Roman", 11, "bold"),
        bg=WHITE,
        fg=TEXT
    ).pack()

    tk.Label(
        frame,
        text=description,
        font=("Times New Roman", 9),
        bg=WHITE,
        fg=GRAY,
        justify="center",
        wraplength=150
    ).pack(pady=(5, 0))


flow_step(
    flow,
    0,
    1,
    "Student Input",
    "Enter academic and attendance details"
)

tk.Label(
    flow,
    text="→",
    font=("Arial", 22, "bold"),
    bg=WHITE,
    fg=PRIMARY
).grid(row=0, column=1)

flow_step(
    flow,
    2,
    2,
    "Validation",
    "Validate input values and ranges"
)

tk.Label(
    flow,
    text="→",
    font=("Arial", 22, "bold"),
    bg=WHITE,
    fg=PRIMARY
).grid(row=0, column=3)

flow_step(
    flow,
    4,
    3,
    "Data Storage",
    "Save student details into Excel"
)

tk.Label(
    flow,
    text="→",
    font=("Arial", 22, "bold"),
    bg=WHITE,
    fg=PRIMARY
).grid(row=0, column=5)

flow_step(
    flow,
    6,
    4,
    "ML Prediction",
    "Random Forest predicts dropout risk"
)

tk.Label(
    flow,
    text="→",
    font=("Arial", 22, "bold"),
    bg=WHITE,
    fg=PRIMARY
).grid(row=0, column=7)

flow_step(
    flow,
    8,
    5,
    "Recommendation",
    "Generate improvement suggestions"
)

tk.Label(
    flow,
    text="→",
    font=("Arial", 22, "bold"),
    bg=WHITE,
    fg=PRIMARY
).grid(row=0, column=9)

flow_step(
    flow,
    10,
    6,
    "n8n Notification",
    "Send prediction data to automation workflow"
)

tk.Label(
    main,
    text="Input – Process – Output Design",
    font=("Times New Roman", 20, "bold"),
    bg=BG,
    fg=TEXT
).pack(
    anchor="w",
    pady=(25, 10)
)

io_frame = tk.Frame(
    main,
    bg=BG
)

io_frame.pack(fill="x")

input_card = tk.Frame(
    io_frame,
    bg=WHITE,
    highlightbackground=BORDER,
    highlightthickness=1
)

input_card.pack(
    side="left",
    fill="both",
    expand=True,
    padx=(0, 8)
)

tk.Label(
    input_card,
    text="INPUT",
    font=("Times New Roman", 15, "bold"),
    bg=WHITE,
    fg=PRIMARY
).pack(pady=(15, 8))

tk.Label(
    input_card,
    text=(
        "• Student ID\n"
        "• Student Name\n"
        "• Attendance\n"
        "• Study Hours\n"
        "• Internal Marks\n"
        "• Assignment Marks\n"
        "• Previous Semester GPA\n"
        "• Number of Backlogs"
    ),
    font=("Times New Roman", 10),
    bg=WHITE,
    fg=TEXT,
    justify="left"
).pack(
    anchor="w",
    padx=25,
    pady=(0, 15)
)

process_card = tk.Frame(
    io_frame,
    bg=WHITE,
    highlightbackground=BORDER,
    highlightthickness=1
)

process_card.pack(
    side="left",
    fill="both",
    expand=True,
    padx=8
)

tk.Label(
    process_card,
    text="PROCESS",
    font=("Times New Roman", 15, "bold"),
    bg=WHITE,
    fg=ORANGE
).pack(pady=(15, 8))

tk.Label(
    process_card,
    text=(
        "• Input Validation\n"
        "• Data Storage\n"
        "• Feature Processing\n"
        "• Random Forest Prediction\n"
        "• Performance Score Calculation\n"
        "• Risk Classification\n"
        "• Recommendation Generation"
    ),
    font=("Times New Roman", 10),
    bg=WHITE,
    fg=TEXT,
    justify="left"
).pack(
    anchor="w",
    padx=25,
    pady=(0, 15)
)

output_card = tk.Frame(
    io_frame,
    bg=WHITE,
    highlightbackground=BORDER,
    highlightthickness=1
)

output_card.pack(
    side="left",
    fill="both",
    expand=True,
    padx=(8, 0)
)

tk.Label(
    output_card,
    text="OUTPUT",
    font=("Times New Roman", 15, "bold"),
    bg=WHITE,
    fg=GREEN
).pack(pady=(15, 8))

tk.Label(
    output_card,
    text=(
        "• Dropout Risk Level\n"
        "• Performance Score\n"
        "• Prediction Probability\n"
        "• Student Performance Details\n"
        "• Personalized Recommendations\n"
        "• n8n Workflow Notification"
    ),
    font=("Times New Roman", 10),
    bg=WHITE,
    fg=TEXT,
    justify="left"
).pack(
    anchor="w",
    padx=25,
    pady=(0, 15)
)

tk.Label(
    root,
    text="System Design Phase | Smart Student Dropout Risk Prediction System",
    font=("Times New Roman", 9),
    bg=SIDEBAR,
    fg="#BFDBFE"
).pack(
    fill="x",
    ipady=8
)

root.mainloop()
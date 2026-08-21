import tkinter as tk
from tkinter import ttk, messagebox
import openpyxl
import os


# ============================================================
# CONFIGURATION
# ============================================================

FILE_NAME = "student_details.xlsx"

BG = "#F4F7FB"
SIDEBAR = "#172554"
SIDEBAR_HOVER = "#1E3A8A"

WHITE = "#FFFFFF"
PRIMARY = "#2563EB"
PRIMARY_DARK = "#1D4ED8"

TEXT = "#172033"
GRAY = "#64748B"
LIGHT_GRAY = "#E2E8F0"

GREEN = "#16A34A"
ORANGE = "#EA580C"
RED = "#DC2626"

LIGHT_GREEN = "#DCFCE7"
LIGHT_ORANGE = "#FFEDD5"
LIGHT_RED = "#FEE2E2"


# ============================================================
# MAIN WINDOW
# ============================================================

root = tk.Tk()

root.title("Smart Student Dropout Risk Prediction System")
root.geometry("1200x750")
root.minsize(1000, 650)
root.configure(bg=BG)

is_maximized = False


# ============================================================
# GLOBAL VARIABLES
# ============================================================

student_id_entry = None
student_name_entry = None
attendance_entry = None
study_hours_entry = None
internal_entry = None
assignment_entry = None
gpa_entry = None
backlog_entry = None

student_list_tree = None
student_dropdown = None

prediction_result_frame = None


# ============================================================
# WINDOW CONTROLS
# ============================================================

def toggle_maximize():

    global is_maximized

    if is_maximized:

        root.state("normal")
        root.geometry("1200x750")

        is_maximized = False

        maximize_button.config(text="□")

    else:

        root.state("zoomed")

        is_maximized = True

        maximize_button.config(text="❐")


def exit_application():

    answer = messagebox.askyesno(
        "Exit Application",
        "Are you sure you want to exit?"
    )

    if answer:
        root.destroy()


# ============================================================
# CONTENT CLEAR
# ============================================================

def clear_content():

    for widget in content.winfo_children():
        widget.destroy()


# ============================================================
# EXCEL FILE
# ============================================================

def create_excel_file():

    if not os.path.exists(FILE_NAME):

        workbook = openpyxl.Workbook()

        sheet = workbook.active

        sheet.title = "Student Details"

        sheet.append([
            "Student ID",
            "Student Name",
            "Attendance",
            "Study Hours",
            "Internal Marks",
            "Assignment Marks",
            "Previous Semester GPA",
            "Backlogs"
        ])

        workbook.save(FILE_NAME)

        workbook.close()


# ============================================================
# LOAD ALL STUDENTS
# ============================================================

def load_students():

    create_excel_file()

    workbook = openpyxl.load_workbook(FILE_NAME)

    sheet = workbook.active

    students = []

    for row in sheet.iter_rows(
        min_row=2,
        values_only=True
    ):

        if row[0] is not None:

            student = {
                "id": str(row[0]),
                "name": str(row[1]),
                "attendance": float(row[2]),
                "study_hours": float(row[3]),
                "internal": float(row[4]),
                "assignment": float(row[5]),
                "gpa": float(row[6]),
                "backlogs": int(row[7])
            }

            students.append(student)

    workbook.close()

    return students


# ============================================================
# SAVE STUDENT
# ============================================================

def save_student():

    try:

        student_id = student_id_entry.get().strip()

        student_name = student_name_entry.get().strip()

        attendance = float(
            attendance_entry.get()
        )

        study_hours = float(
            study_hours_entry.get()
        )

        internal = float(
            internal_entry.get()
        )

        assignment = float(
            assignment_entry.get()
        )

        gpa = float(
            gpa_entry.get()
        )

        backlogs = int(
            backlog_entry.get()
        )


        # ----------------------------------------------------
        # VALIDATION
        # ----------------------------------------------------

        if student_id == "":
            raise ValueError(
                "Please enter Student ID."
            )

        if student_name == "":
            raise ValueError(
                "Please enter Student Name."
            )

        if not 0 <= attendance <= 100:
            raise ValueError(
                "Attendance must be between 0 and 100."
            )

        if study_hours < 0:
            raise ValueError(
                "Study hours cannot be negative."
            )

        if not 0 <= internal <= 100:
            raise ValueError(
                "Internal marks must be between 0 and 100."
            )

        if not 0 <= assignment <= 100:
            raise ValueError(
                "Assignment marks must be between 0 and 100."
            )

        if not 0 <= gpa <= 10:
            raise ValueError(
                "GPA must be between 0 and 10."
            )

        if backlogs < 0:
            raise ValueError(
                "Backlogs cannot be negative."
            )


        # ----------------------------------------------------
        # CREATE / OPEN EXCEL
        # ----------------------------------------------------

        create_excel_file()

        workbook = openpyxl.load_workbook(
            FILE_NAME
        )

        sheet = workbook.active


        # ----------------------------------------------------
        # DUPLICATE CHECK
        # ----------------------------------------------------

        for row in sheet.iter_rows(
            min_row=2,
            values_only=True
        ):

            existing_id = str(row[0])

            if existing_id == student_id:

                workbook.close()

                messagebox.showwarning(
                    "Duplicate Student",
                    "This Student ID already exists."
                )

                return


        # ----------------------------------------------------
        # SAVE
        # ----------------------------------------------------

        sheet.append([
            student_id,
            student_name,
            attendance,
            study_hours,
            internal,
            assignment,
            gpa,
            backlogs
        ])

        workbook.save(FILE_NAME)

        workbook.close()


        messagebox.showinfo(
            "Success",
            f"Student '{student_name}' saved successfully."
        )


        clear_student_form()

        show_student_list()


    except ValueError as error:

        messagebox.showerror(
            "Invalid Input",
            str(error)
        )


# ============================================================
# CLEAR STUDENT FORM
# ============================================================

def clear_student_form():

    fields = [
        student_id_entry,
        student_name_entry,
        attendance_entry,
        study_hours_entry,
        internal_entry,
        assignment_entry,
        gpa_entry,
        backlog_entry
    ]

    for field in fields:

        if field is not None:
            field.delete(0, tk.END)


# ============================================================
# CREATE FIELD
# ============================================================

def create_field(
    parent,
    row,
    column,
    label_text
):

    frame = tk.Frame(
        parent,
        bg=WHITE
    )

    frame.grid(
        row=row,
        column=column,
        padx=25,
        pady=10,
        sticky="ew"
    )

    label = tk.Label(
        frame,
        text=label_text,
        font=("Arial", 10, "bold"),
        bg=WHITE,
        fg=GRAY
    )

    label.pack(
        anchor="w"
    )

    entry = tk.Entry(
        frame,
        font=("Arial", 12),
        bg="#F8FAFC",
        fg=TEXT,
        bd=0,
        highlightbackground=LIGHT_GRAY,
        highlightthickness=1
    )

    entry.pack(
        fill="x",
        ipady=8,
        pady=(5, 0)
    )

    return entry


# ============================================================
# DASHBOARD
# ============================================================

def show_dashboard():

    clear_content()

    students = load_students()

    total_students = len(students)

    high_risk = 0
    medium_risk = 0
    low_risk = 0

    for student in students:

        score = calculate_score(student)

        if score < 50:
            high_risk += 1

        elif score < 75:
            medium_risk += 1

        else:
            low_risk += 1


    # --------------------------------------------------------
    # TITLE
    # --------------------------------------------------------

    tk.Label(
        content,
        text="Dashboard",
        font=("Arial", 27, "bold"),
        bg=BG,
        fg=TEXT
    ).pack(
        anchor="w",
        pady=(5, 5)
    )


    tk.Label(
        content,
        text="Smart Student Dropout Risk Analytics",
        font=("Arial", 11),
        bg=BG,
        fg=GRAY
    ).pack(
        anchor="w",
        pady=(0, 25)
    )


    # --------------------------------------------------------
    # STAT CARDS
    # --------------------------------------------------------

    cards = tk.Frame(
        content,
        bg=BG
    )

    cards.pack(
        fill="x"
    )


    create_stat_card(
        cards,
        "👨‍🎓",
        "TOTAL STUDENTS",
        total_students,
        PRIMARY
    )


    create_stat_card(
        cards,
        "🔴",
        "HIGH RISK",
        high_risk,
        RED
    )


    create_stat_card(
        cards,
        "🟠",
        "MEDIUM RISK",
        medium_risk,
        ORANGE
    )


    create_stat_card(
        cards,
        "🟢",
        "LOW RISK",
        low_risk,
        GREEN
    )


    # --------------------------------------------------------
    # WELCOME CARD
    # --------------------------------------------------------

    welcome = tk.Frame(
        content,
        bg=WHITE,
        highlightbackground=LIGHT_GRAY,
        highlightthickness=1
    )

    welcome.pack(
        fill="x",
        pady=30
    )


    tk.Label(
        welcome,
        text="Welcome to Smart Student Analytics 🎓",
        font=("Arial", 19, "bold"),
        bg=WHITE,
        fg=TEXT
    ).pack(
        anchor="w",
        padx=30,
        pady=(25, 10)
    )


    tk.Label(
        welcome,
        text=(
            "Save student information first. Saved students will "
            "appear in the Student List and can then be selected "
            "for dropout risk prediction."
        ),
        font=("Arial", 11),
        bg=WHITE,
        fg=GRAY,
        wraplength=850,
        justify="left"
    ).pack(
        anchor="w",
        padx=30,
        pady=(0, 25)
    )


# ============================================================
# STAT CARD
# ============================================================

def create_stat_card(
    parent,
    icon,
    title,
    value,
    color
):

    card = tk.Frame(
        parent,
        bg=WHITE,
        highlightbackground=LIGHT_GRAY,
        highlightthickness=1
    )

    card.pack(
        side="left",
        fill="both",
        expand=True,
        padx=6,
        ipady=15
    )


    tk.Label(
        card,
        text=icon,
        font=("Arial", 22),
        bg=WHITE
    ).pack(
        anchor="w",
        padx=20
    )


    tk.Label(
        card,
        text=title,
        font=("Arial", 9, "bold"),
        bg=WHITE,
        fg=GRAY
    ).pack(
        anchor="w",
        padx=20
    )


    tk.Label(
        card,
        text=str(value),
        font=("Arial", 22, "bold"),
        bg=WHITE,
        fg=color
    ).pack(
        anchor="w",
        padx=20
    )


# ============================================================
# STUDENT DETAILS PAGE
# ============================================================

def show_student_details():

    clear_content()

    global student_id_entry
    global student_name_entry
    global attendance_entry
    global study_hours_entry
    global internal_entry
    global assignment_entry
    global gpa_entry
    global backlog_entry


    tk.Label(
        content,
        text="Student Details",
        font=("Arial", 27, "bold"),
        bg=BG,
        fg=TEXT
    ).pack(
        anchor="w"
    )


    tk.Label(
        content,
        text="Enter student information and save it to the student database.",
        font=("Arial", 11),
        bg=BG,
        fg=GRAY
    ).pack(
        anchor="w",
        pady=(5, 20)
    )


    card = tk.Frame(
        content,
        bg=WHITE,
        highlightbackground=LIGHT_GRAY,
        highlightthickness=1
    )

    card.pack(
        fill="x"
    )


    tk.Label(
        card,
        text="Student Information",
        font=("Arial", 16, "bold"),
        bg=WHITE,
        fg=TEXT
    ).grid(
        row=0,
        column=0,
        columnspan=3,
        sticky="w",
        padx=25,
        pady=(25, 15)
    )


    for col in range(3):
        card.columnconfigure(
            col,
            weight=1
        )


    student_id_entry = create_field(
        card,
        1,
        0,
        "Student ID"
    )


    student_name_entry = create_field(
        card,
        1,
        1,
        "Student Name"
    )


    attendance_entry = create_field(
        card,
        1,
        2,
        "Attendance (%)"
    )


    study_hours_entry = create_field(
        card,
        2,
        0,
        "Study Hours / Day"
    )


    internal_entry = create_field(
        card,
        2,
        1,
        "Internal Marks"
    )


    assignment_entry = create_field(
        card,
        2,
        2,
        "Assignment Marks"
    )


    gpa_entry = create_field(
        card,
        3,
        0,
        "Previous Semester GPA"
    )


    backlog_entry = create_field(
        card,
        3,
        1,
        "Number of Backlogs"
    )


    button_frame = tk.Frame(
        card,
        bg=WHITE
    )

    button_frame.grid(
        row=4,
        column=0,
        columnspan=3,
        pady=25
    )


    tk.Button(
        button_frame,
        text="💾  SAVE STUDENT",
        font=("Arial", 11, "bold"),
        bg=GREEN,
        fg=WHITE,
        bd=0,
        padx=25,
        pady=12,
        cursor="hand2",
        command=save_student
    ).pack(
        side="left",
        padx=8
    )


    tk.Button(
        button_frame,
        text="↻  CLEAR",
        font=("Arial", 11, "bold"),
        bg=LIGHT_GRAY,
        fg=TEXT,
        bd=0,
        padx=25,
        pady=12,
        cursor="hand2",
        command=clear_student_form
    ).pack(
        side="left",
        padx=8
    )


# ============================================================
# STUDENT LIST PAGE
# ============================================================

def show_student_list():

    clear_content()

    tk.Label(
        content,
        text="List of Students",
        font=("Arial", 27, "bold"),
        bg=BG,
        fg=TEXT
    ).pack(
        anchor="w"
    )


    tk.Label(
        content,
        text="Only students saved in student_details.xlsx are displayed here.",
        font=("Arial", 11),
        bg=BG,
        fg=GRAY
    ).pack(
        anchor="w",
        pady=(5, 20)
    )


    card = tk.Frame(
        content,
        bg=WHITE,
        highlightbackground=LIGHT_GRAY,
        highlightthickness=1
    )

    card.pack(
        fill="both",
        expand=True
    )


    # --------------------------------------------------------
    # TREEVIEW
    # --------------------------------------------------------

    columns = (
        "id",
        "name",
        "attendance",
        "study",
        "internal",
        "assignment",
        "gpa",
        "backlogs"
    )


    tree = ttk.Treeview(
        card,
        columns=columns,
        show="headings"
    )


    headings = {
        "id": "Student ID",
        "name": "Name",
        "attendance": "Attendance",
        "study": "Study Hours",
        "internal": "Internal",
        "assignment": "Assignment",
        "gpa": "GPA",
        "backlogs": "Backlogs"
    }


    widths = {
        "id": 100,
        "name": 160,
        "attendance": 100,
        "study": 100,
        "internal": 100,
        "assignment": 100,
        "gpa": 100,
        "backlogs": 90
    }


    for col in columns:

        tree.heading(
            col,
            text=headings[col]
        )

        tree.column(
            col,
            width=widths[col],
            anchor="center"
        )


    scrollbar = ttk.Scrollbar(
        card,
        orient="vertical",
        command=tree.yview
    )

    tree.configure(
        yscrollcommand=scrollbar.set
    )


    tree.pack(
        side="left",
        fill="both",
        expand=True,
        padx=15,
        pady=15
    )


    scrollbar.pack(
        side="right",
        fill="y",
        pady=15
    )


    # --------------------------------------------------------
    # LOAD SAVED STUDENTS
    # --------------------------------------------------------

    students = load_students()


    for student in students:

        tree.insert(
            "",
            "end",
            values=(
                student["id"],
                student["name"],
                student["attendance"],
                student["study_hours"],
                student["internal"],
                student["assignment"],
                student["gpa"],
                student["backlogs"]
            )
        )


# ============================================================
# CALCULATE SCORE
# ============================================================

def calculate_score(student):

    study_score, gpa_score, backlog_score = normalize_values(
        student["study_hours"],
        student["gpa"],
        student["backlogs"]
    )


    score = (
        student["attendance"] * 0.20 +
        study_score * 0.15 +
        student["internal"] * 0.20 +
        student["assignment"] * 0.15 +
        gpa_score * 0.20 +
        backlog_score * 0.10
    )


    return round(score, 2)


# ============================================================
# PREDICTION PAGE
# ============================================================

def show_prediction():

    clear_content()

    global student_dropdown
    global prediction_result_frame


    tk.Label(
        content,
        text="Risk Prediction",
        font=("Arial", 27, "bold"),
        bg=BG,
        fg=TEXT
    ).pack(
        anchor="w"
    )


    tk.Label(
        content,
        text="Select a saved student to predict dropout risk.",
        font=("Arial", 11),
        bg=BG,
        fg=GRAY
    ).pack(
        anchor="w",
        pady=(5, 20)
    )


    students = load_students()


    if not students:

        empty_card = tk.Frame(
            content,
            bg=WHITE,
            highlightbackground=LIGHT_GRAY,
            highlightthickness=1
        )

        empty_card.pack(
            fill="x",
            pady=30
        )


        tk.Label(
            empty_card,
            text="No Saved Students",
            font=("Arial", 20, "bold"),
            bg=WHITE,
            fg=RED
        ).pack(
            pady=(35, 10)
        )


        tk.Label(
            empty_card,
            text=(
                "Please go to Student Details and save a student "
                "before making a prediction."
            ),
            font=("Arial", 11),
            bg=WHITE,
            fg=GRAY
        ).pack(
            pady=(0, 35)
        )


        return


    # --------------------------------------------------------
    # SELECT STUDENT
    # --------------------------------------------------------

    selection_card = tk.Frame(
        content,
        bg=WHITE,
        highlightbackground=LIGHT_GRAY,
        highlightthickness=1
    )

    selection_card.pack(
        fill="x"
    )


    tk.Label(
        selection_card,
        text="Select Saved Student",
        font=("Arial", 13, "bold"),
        bg=WHITE,
        fg=TEXT
    ).pack(
        anchor="w",
        padx=30,
        pady=(25, 8)
    )


    student_options = [
        f'{student["id"]} - {student["name"]}'
        for student in students
    ]


    student_dropdown = ttk.Combobox(
        selection_card,
        values=student_options,
        state="readonly",
        font=("Arial", 12),
        width=50
    )


    student_dropdown.pack(
        anchor="w",
        padx=30,
        pady=5
    )


    student_dropdown.current(0)


    tk.Button(
        selection_card,
        text="🔍  PREDICT SELECTED STUDENT",
        font=("Arial", 11, "bold"),
        bg=PRIMARY,
        fg=WHITE,
        bd=0,
        padx=25,
        pady=12,
        cursor="hand2",
        command=perform_selected_prediction
    ).pack(
        anchor="w",
        padx=30,
        pady=25
    )


    # --------------------------------------------------------
    # RESULT FRAME
    # --------------------------------------------------------

    prediction_result_frame = tk.Frame(
        content,
        bg=WHITE,
        highlightbackground=LIGHT_GRAY,
        highlightthickness=1
    )

    prediction_result_frame.pack(
        fill="x",
        pady=25
    )


    tk.Label(
        prediction_result_frame,
        text="Prediction Result",
        font=("Arial", 14, "bold"),
        bg=WHITE,
        fg=TEXT
    ).pack(
        pady=(25, 10)
    )


    tk.Label(
        prediction_result_frame,
        text="Select a student and click Predict.",
        font=("Arial", 12),
        bg=WHITE,
        fg=GRAY
    ).pack(
        pady=(0, 25)
    )


# ============================================================
# PREDICT SELECTED SAVED STUDENT
# ============================================================

def perform_selected_prediction():

    selected = student_dropdown.get()


    if not selected:

        messagebox.showwarning(
            "Select Student",
            "Please select a student."
        )

        return


    student_id = selected.split(" - ")[0]


    students = load_students()


    selected_student = None


    for student in students:

        if student["id"] == student_id:

            selected_student = student

            break


    if selected_student is None:

        messagebox.showerror(
            "Error",
            "Student data could not be found."
        )

        return


    # --------------------------------------------------------
    # CALCULATE
    # --------------------------------------------------------

    score = calculate_score(
        selected_student
    )


    # --------------------------------------------------------
    # RISK
    # --------------------------------------------------------

    if score >= 75:

        risk = "LOW DROPOUT RISK"

        color = GREEN

    elif score >= 50:

        risk = "MEDIUM DROPOUT RISK"

        color = ORANGE

    else:

        risk = "HIGH DROPOUT RISK"

        color = RED


    # --------------------------------------------------------
    # CLEAR OLD RESULT
    # --------------------------------------------------------

    for widget in prediction_result_frame.winfo_children():

        widget.destroy()


    # --------------------------------------------------------
    # STUDENT NAME
    # --------------------------------------------------------

    tk.Label(
        prediction_result_frame,
        text=(
            f'{selected_student["name"]} '
            f'({selected_student["id"]})'
        ),
        font=("Arial", 18, "bold"),
        bg=WHITE,
        fg=TEXT
    ).pack(
        pady=(25, 5)
    )


    # --------------------------------------------------------
    # SCORE
    # --------------------------------------------------------

    tk.Label(
        prediction_result_frame,
        text=f"{score}",
        font=("Arial", 48, "bold"),
        bg=WHITE,
        fg=PRIMARY
    ).pack()


    tk.Label(
        prediction_result_frame,
        text=risk,
        font=("Arial", 20, "bold"),
        bg=WHITE,
        fg=color
    ).pack(
        pady=10
    )


    # --------------------------------------------------------
    # STUDENT DATA
    # --------------------------------------------------------

    data_text = (
        f'Attendance       : {selected_student["attendance"]}%\n'
        f'Study Hours      : {selected_student["study_hours"]}\n'
        f'Internal Marks   : {selected_student["internal"]}\n'
        f'Assignment Marks : {selected_student["assignment"]}\n'
        f'Previous GPA     : {selected_student["gpa"]}\n'
        f'Backlogs         : {selected_student["backlogs"]}'
    )


    tk.Label(
        prediction_result_frame,
        text=data_text,
        font=("Arial", 11),
        bg=WHITE,
        fg=GRAY,
        justify="left"
    ).pack(
        pady=10
    )


    # --------------------------------------------------------
    # IMPROVEMENTS
    # --------------------------------------------------------

    improvements = []


    if selected_student["attendance"] < 75:

        improvements.append(
            "Improve attendance"
        )


    if selected_student["study_hours"] < 3:

        improvements.append(
            "Increase daily study hours"
        )


    if selected_student["internal"] < 50:

        improvements.append(
            "Improve internal marks"
        )


    if selected_student["assignment"] < 50:

        improvements.append(
            "Complete assignments regularly"
        )


    if selected_student["gpa"] < 6:

        improvements.append(
            "Improve previous semester GPA"
        )


    if selected_student["backlogs"] > 0:

        improvements.append(
            "Clear pending backlogs"
        )


    if not improvements:

        improvements.append(
            "Student performance is satisfactory."
        )


    tk.Label(
        prediction_result_frame,
        text="💡 Areas to Improve",
        font=("Arial", 13, "bold"),
        bg=WHITE,
        fg=TEXT
    ).pack(
        anchor="w",
        padx=30,
        pady=(20, 8)
    )


    tk.Label(
        prediction_result_frame,
        text="\n".join(
            "• " + item
            for item in improvements
        ),
        font=("Arial", 11),
        bg=WHITE,
        fg=GRAY,
        justify="left"
    ).pack(
        anchor="w",
        padx=30,
        pady=(0, 25)
    )


# ============================================================
# SIDEBAR BUTTON
# ============================================================

def sidebar_button(
    parent,
    text,
    command
):

    button = tk.Button(
        parent,
        text=text,
        font=("Arial", 11, "bold"),
        bg=SIDEBAR,
        fg=WHITE,
        activebackground=SIDEBAR_HOVER,
        activeforeground=WHITE,
        bd=0,
        anchor="w",
        padx=25,
        pady=14,
        cursor="hand2",
        command=command
    )

    button.pack(
        fill="x",
        padx=8,
        pady=2
    )


# ============================================================
# TOP BAR
# ============================================================

topbar = tk.Frame(
    root,
    bg=SIDEBAR,
    height=65
)

topbar.pack(
    side="top",
    fill="x"
)

topbar.pack_propagate(False)


tk.Label(
    topbar,
    text="🎓",
    font=("Arial", 22),
    bg=SIDEBAR,
    fg=WHITE
).pack(
    side="left",
    padx=(25, 10)
)


tk.Label(
    topbar,
    text="SMART STUDENT ANALYTICS",
    font=("Arial", 16, "bold"),
    bg=SIDEBAR,
    fg=WHITE
).pack(
    side="left"
)


# ------------------------------------------------------------
# EXIT BUTTON
# ------------------------------------------------------------

tk.Button(
    topbar,
    text="✕  EXIT",
    font=("Arial", 10, "bold"),
    bg=RED,
    fg=WHITE,
    bd=0,
    padx=15,
    cursor="hand2",
    command=exit_application
).pack(
    side="right",
    padx=10,
    pady=15
)


# ------------------------------------------------------------
# MAXIMIZE BUTTON
# ------------------------------------------------------------

maximize_button = tk.Button(
    topbar,
    text="□",
    font=("Arial", 13, "bold"),
    bg="#334155",
    fg=WHITE,
    bd=0,
    width=4,
    cursor="hand2",
    command=toggle_maximize
)

maximize_button.pack(
    side="right",
    pady=15
)


# ============================================================
# SIDEBAR
# ============================================================

sidebar = tk.Frame(
    root,
    bg=SIDEBAR,
    width=235
)

sidebar.pack(
    side="left",
    fill="y"
)

sidebar.pack_propagate(False)


tk.Label(
    sidebar,
    text="MAIN MENU",
    font=("Arial", 10, "bold"),
    bg=SIDEBAR,
    fg="#93C5FD"
).pack(
    anchor="w",
    padx=25,
    pady=(30, 15)
)


sidebar_button(
    sidebar,
    "🏠   Dashboard",
    show_dashboard
)


sidebar_button(
    sidebar,
    "👤   Student Details",
    show_student_details
)


sidebar_button(
    sidebar,
    "📋   List of Students",
    show_student_list
)


sidebar_button(
    sidebar,
    "📊   Risk Prediction",
    show_prediction
)


# ============================================================
# CONTENT
# ============================================================

content = tk.Frame(
    root,
    bg=BG
)

content.pack(
    side="left",
    fill="both",
    expand=True,
    padx=30,
    pady=20
)


# ============================================================
# START
# ============================================================

show_dashboard()


# ============================================================
# RUN
# ============================================================

root.mainloop()
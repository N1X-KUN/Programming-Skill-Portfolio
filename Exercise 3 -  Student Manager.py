import tkinter as tk  # Import the tkinter library for GUI creation
from tkinter import messagebox  # Import messagebox for displaying error messages

root = tk.Tk()  # Create the main window
root.title("Student Manager || Exercise 3")  # Title for Exercise 3
root.geometry("600x500")                     # Set the size of the window
root.resizable(False, False)                 # Disable resizing of the window
root.configure(bg="#f6b26b")                 # Set the background color of the window
root.option_add("*Font", "Arial 12")         # Set global font for all widgets

students = []  # List to hold student data

# Read student data from file
def load_student_data():
    # Load student data from a specified file and store it in the students list.
    with open("studentMarks.txt") as file:
        lines = file.readlines()
        for line in lines[1:]:  
            parts = line.strip().split(',')    # Split each line into parts
            code, name = parts[0], parts[1]    # Extract student code and name
            marks = list(map(int, parts[2:]))  # Convert mark strings to integers
            coursework_total = sum(marks[:3])  # Calculate total coursework marks
            exam_mark = marks[3]               # Extract exam mark
            overall_percentage = (coursework_total + exam_mark) / 160 * 100  # Calculate percentage
            grade = calculate_grade(overall_percentage)  
            students.append({                  # Appends the student data to the list
                "code": code,
                "name": name,
                "coursework": coursework_total,
                "exam": exam_mark,
                "percentage": overall_percentage,
                "grade": grade
            })

def calculate_grade(percentage):
    if percentage >= 70:
        return 'A'
    elif percentage >= 60:
        return 'B'
    elif percentage >= 50:
        return 'C'
    elif percentage >= 40:
        return 'D'
    else:
        return 'F'

def display_all_students(order="Ascending"):
    textbox.delete(1.0, tk.END)  # Clear the text box before displaying new data
    sorted_students = sorted(students, key=lambda s: s['percentage'], reverse=(order == "Ascending"))  # Sort students by percentage

    total_percentage = sum(student['percentage'] for student in sorted_students)  
    for student in sorted_students:  # Loop through sorted students to display their info
        info = f"Name: {student['name']}\nCode: {student['code']}\n" \
               f"Coursework: {student['coursework']}\nExam: {student['exam']}\n" \
               f"Percentage: {student['percentage']:.2f}%\nGrade: {student['grade']}\n\n"
        textbox.insert(tk.END, info)  # Insert student info into the text box

    # Calculate and display total students and average percentage
    avg_percentage = total_percentage / len(students) if students else 0
    textbox.insert(tk.END, f"Total students: {len(students)}\nAverage percentage: {avg_percentage:.2f}%")

def open_sorting_options():
    sort_window = tk.Toplevel(root)  
    sort_window.title("Sort Student Records")  
    sort_window.geometry("250x150")  
    sort_window.configure(bg="#f8ff00")  

    # Label and buttons for sorting options
    tk.Label(sort_window, text="Choose sorting order:", bg="#f8ff00").pack(pady=10)
    asc_button = tk.Button(sort_window, text="Ascending (Highest to Lowest)", bg="#fccf60", 
                           command=lambda: display_all_students("Ascending"))  # Sort in ascending order
    asc_button.pack(pady=5, fill="x")
    desc_button = tk.Button(sort_window, text="Descending (Lowest to Highest)", bg="#fccf60",
                            command=lambda: display_all_students("Descending"))  # Sort in descending order
    desc_button.pack(pady=5, fill="x")

def display_individual_record(student):
    # Display a single student's record in the text box.
    info = f"Name: {student['name']}\nCode: {student['code']}\n" \
           f"Coursework: {student['coursework']}\nExam: {student['exam']}\n" \
           f"Percentage: {student['percentage']:.2f}%\nGrade: {student['grade']}"
    textbox.delete(1.0, tk.END)   # Clear the text box
    textbox.insert(tk.END, info)  # Insert individual student info onto the text box

def open_individual_record_window():
    window = tk.Toplevel(root) 
    window.title("Select Student")  
    window.geometry("400x230")  
    window.configure(bg="#000000")  

    num_columns = 2  # Number of columns
    for index, student in enumerate(students):
        btn = tk.Button(window, text=student["name"], bg="#ffd966", fg="#000000",
                        command=lambda s=student: display_individual_record(s))          # Display selected student's record
        btn.grid(row=index // num_columns, column=index % num_columns, padx=10, pady=5)  # Place button in grid
    for col in range(num_columns):
        window.grid_columnconfigure(col, weight=1)

def display_highest_score():
    # Display the record of the student with the highest score.
    if students:
        highest_student = max(students, key=lambda s: s['percentage'])  
        display_individual_record(highest_student)  

def display_lowest_score():
    # Display the record of the student with the lowest score.
    if students:
        lowest_student = min(students, key=lambda s: s['percentage'])  
        display_individual_record(lowest_student)  

load_student_data()  # Call function to load student data from the file

header = tk.Label(root, text="STUDENT MANAGER", bg="#000000", fg="#f8ff00", font=("Arial", 15, "bold","underline"))
header.grid(row=0, column=0, columnspan=2, pady=20)  # Place header in the grid

def view_all_students():
    open_sorting_options()

def view_highest_score():
    display_highest_score()

def view_lowest_score():
    display_lowest_score()

def view_individual_record():
    open_individual_record_window()

button1 = tk.Button(root, text="View all Student Records", command=view_all_students, width=30, height=2, bg="#393030", fg="#ffe599")
button2 = tk.Button(root, text="Highest Student Score", command=view_highest_score, width=30, height=2, bg="#393030", fg="#ffe599")
button3 = tk.Button(root, text="Lowest Student Score", command=view_lowest_score, width=30, height=2, bg="#393030", fg="#ffe599")
button4 = tk.Button(root, text="Individual Student Record", command=view_individual_record, width=30, height=2, bg="#393030", fg="#ffe599")

def log_off():
    root.quit()  # Exit the Tkinter program

# Acts as the Quit Program or Terminate Window
log_off_button = tk.Button(root, text="Log Off", command=log_off, width=30, height=2, bg="#393030", fg="#ffe599")
log_off_button.grid(row=4, column=0, columnspan=2, padx=10, pady=10) 

# Place buttons in the grid layout
button1.grid(row=1, column=0, padx=10, pady=10)
button2.grid(row=1, column=1, padx=10, pady=10)
button3.grid(row=2, column=0, padx=10, pady=10)
button4.grid(row=2, column=1, padx=10, pady=10)

# Textbox for displaying student records
textbox = tk.Text(root, wrap="word", width=40, height=10)
textbox.grid(row=3, column=0, columnspan=2, padx=10, pady=10)

root.mainloop()  # Start the Tkinter event loop
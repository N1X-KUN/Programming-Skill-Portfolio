from tkinter import *  # Pull in everything from tkinter to build our GUI
import random  # Bring in random functions for question generation

root = Tk()
root.title('Math Quiz || Exercise 1')  # Title for Exercise 1
root.geometry('400x400')               # Setting a standard size for the quiz window
root.resizable(False, False)           # Locking the window size for consistency
root.configure(bg='black')             # Dark theme background for simplicity and focus
root.option_add("*Font", "Arial 16")   # Applying a standard font across widgets

# Set initial values
score = 0  # Starting score at zero
question_count = 0  # No questions answered yet
level = 1  # Begin with the easy level
quiz_bg_color = 'black'  # Background color that will shift by difficulty

def Menu():
    # Main menu for choosing quiz level
    menu_frame = Frame(root, bg='black')
    menu_frame.pack(pady=50)

    Label(menu_frame, text="Choose level", bg='black', fg='white', font=("bold")).pack()

    # Buttons to select difficulty level
    Button(menu_frame, text="Easy", width=20, height=2, bg='blue', fg='white', command=setEasy).pack(pady=5)
    Button(menu_frame, text="Moderate", width=20, height=2, bg='purple', fg='white', command=setModerate).pack(pady=5)
    Button(menu_frame, text="Hard", width=20, height=2, bg='red', fg='white', command=setHard).pack(pady=5)

def setEasy():
    # Setting the game to easy mode
    setlevel(1, 'blue')

def setModerate():
    # Adjusting game to moderate mode
    setlevel(2, 'purple')

def setHard():
    # Adjusting game to hard mode
    setlevel(3, 'red')

def setlevel(new_level, bg_color):
    # Update global difficulty level and background color
    global level, quiz_bg_color
    level = new_level
    quiz_bg_color = bg_color
    root.configure(bg=quiz_bg_color)  # Refresh background color

    # Clear previous widgets, start fresh for quiz questions
    for widget in root.winfo_children():
        widget.destroy()
    nextQuestion()

def randomInt():
    # Generate numbers suited to each difficulty level
    if level == 1:
        return random.randint(1, 9)  # Numbers that are easier to handle
    elif level == 2:
        return random.randint(10, 99)  # Moderate challenge
    else:
        return random.randint(1000, 9999)  # Higher challenge with big numbers

def operation():
    # Decide randomly between addition or subtraction
    return random.choice(['+', '-'])

def Problem():
    # Create a math problem based on the level
    num1 = randomInt()
    num2 = randomInt()
    operation_type = operation()

    # Make sure subtraction doesn't give negative results
    if operation_type == '-' and num1 < num2:
        num1, num2 = num2, num1

    question = f"{num1} {operation_type} {num2} = "
    return question, eval(question[:-2])  # Evaluate question to get the answer

def submitAnswer():
    # Check answer with the first attempt
    checkAnswer(1)

def retryAnswer():
    # Check answer on the second try
    checkAnswer(2)

def checkAnswer(attempt):
    """Check if the submitted answer is correct and update the score."""
    global score
    try:
        user_input = int(user_answer.get())
        if user_input == correct_answer:
            if attempt == 1:
                score += 10                               # Grants 10 Points for first time attempt
            else:
                score += 5                                # Grants only half for second chance
            comments.config(text="Correct Answer! \t Well done studying!", fg='white')
            submit_btn.after(2000, nextQuestion)          # Gives 2 second before it moves to the next 
        else:
            if attempt == 1:
                comments.config(text="Its not that hard, Try again :3", fg='black')
                submit_btn.config(command=retryAnswer)    # Goes to checkAswer(2)
            else:
                comments.config(text=f"Tsk Tsk, Minus Point! \n The correct answer was {correct_answer}.", fg='black')
                submit_btn.after(3500, nextQuestion)      # Gives the user 3.5 seconds to see the correct answer before moving to the next part
    except ValueError:
        comments.config(text="Refrain from using text or symbols... \n Input a Valid Number Only", fg='black')

def nextQuestion():
    # Load a new question or finish if we're at the end
    global question_count, user_answer, correct_answer, comments, submit_btn
    if question_count < 10:  # Less than 10 questions means we continue
        question_count += 1  # Increment question count
        question, correct_answer = Problem()  # Create new problem

        # Clear old content for new question display
        for widget in root.winfo_children():
            widget.destroy()

        question_frame = Frame(root, bg=quiz_bg_color)
        question_frame.pack(pady=50)

        Label(question_frame, text=f"Question {question_count}", bg=quiz_bg_color, fg='white').pack()
        Label(question_frame, text=question, bg=quiz_bg_color, fg='white').pack(pady=10)

        user_answer = Entry(question_frame)
        user_answer.pack(pady=10)

        comments = Label(question_frame, text="", bg=quiz_bg_color, fg='black')
        comments.pack(pady=5)

        submit_btn = Button(question_frame, text="Submit", command=submitAnswer)
        submit_btn.pack(pady=10)
        quit_btn = Button(question_frame, text="Give Up", command=quitQuiz, bg='black', fg='white')
        quit_btn.pack(pady=10)

    else:
        Results()  # Display results if all questions are completed

def quitQuiz():
    # Exit the quiz program
    root.destroy()

def Results():
    # Calculate final score and rank after finishing quiz
    for widget in root.winfo_children():
        widget.destroy()

    result_frame = Frame(root, bg='black')
    result_frame.pack(pady=50)

    Label(result_frame, text=f"Your final score is: {score}/100", bg='black', fg='white').pack()

    # If condition that operates according to the grades user gets
    if score >= 90:
        rank = "A+ \n Outstanding Grade! Keep at it!"
    elif score >= 80:
        rank = "B \n  Well done studying!"
    elif score >= 70:
        rank = "C \n  Effort are seen, Keep practicing!"
    elif score >= 60:
        rank = "D \n  At least you didn't use Chat Gpt."
    elif score >= 50:
        rank = "E \n  You won your 50/50 chances..."
    else:
        rank = "F \n  See me after class time..."

    Label(result_frame, text=f"Your rank is: {rank}", bg='black', fg='white').pack()
    Button(result_frame, text="Play Again", command=restartQuiz, width=15, height=2, bg='green', fg='white').pack(pady=10)

def restartQuiz():
    # Reset everything and return to the main menu
    global score, question_count
    score = 0
    question_count = 0
    for widget in root.winfo_children():
        widget.destroy()
    Menu()

Menu()  # Start with the main menu
root.mainloop()  # Run the app

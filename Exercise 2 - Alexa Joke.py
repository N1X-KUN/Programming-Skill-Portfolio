import random          # Import the random module to randomly select jokes
from tkinter import *  # Import all classes and functions from the tkinter module

# Set up the main window
root = Tk()  # Create the main window
root.title("Hey Alexa, Tell me a Joke || Exercise 2")  # Title for Exercise 2
root.geometry("500x200")                               # Set the size of the window
root.configure(bg="#f2f2f2")                           # Set the background color of the window
root.option_add("*Font", "Arial 16")                   # Set the default font for all widgets

def load_jokes(filename):
    # Load jokes from the specified file and return as a list of setups and punchlines.
    with open(filename, 'r') as file:
        return [line.strip().split('?') for line in file]  # Split each line into setup and punchline

def show_suggestion():
    # Don't know what to type? This suggestion pops up
    suggestion_label.config(text="Suggestion: Try typing 'Alexa tell me a joke'.")
    root.after(2000, clear_suggestion)  # Clear suggestion after 2 seconds

def clear_suggestion():
    # Clears the suggestion label.
    suggestion_label.config(text="")  # Reset the suggestion label text

def process_input(event=None):
    # Process user input and show a joke if the correct phrase is detected.
    user_input = input_entry.get().strip().lower()  # Get and normalize user input
    if "alexa tell me a joke" in user_input:        # Check if the input matches the command
        open_joke_window()                         
    else:
        show_suggestion()       # Show suggestion if the command is incorrect
    input_entry.delete(0, END)  # Clear the input entry for the next command

def open_joke_window():
    global setup, punchline, joke_window     # Declare global variables for setup, punchline, and the joke window
    setup, punchline = random.choice(jokes)  # Randomly select a joke from the loaded jokes

    # Create the joke window if it doesn't already exist
    if not hasattr(root, 'joke_window') or not joke_window.winfo_exists():  # Check if the joke window is already open
        joke_window = Toplevel(root)                                        # Create a new top-level window for the joke
        joke_window.title("Alexa's Joke")  
        joke_window.geometry("600x200") 
        joke_window.configure(bg="#93acff")  

    # Clear previous contents of the joke window
    for widget in joke_window.winfo_children():
        widget.destroy()  # Remove all existing widgets from the joke window

    # Display the joke setup and a button to show the punchline
    Label(joke_window, text=setup + "?").pack(pady=20) 
    punchline_button = Button(joke_window, text="Show Punchline", command=show_punchline)  # Button to reveal the punchline
    punchline_button.pack(pady=10) 

def show_punchline():
    # Show the punchline in the joke window with options to see another joke or quit.
    for widget in joke_window.winfo_children():
        widget.destroy()  

    Label(joke_window, text=punchline).pack(pady=20)  # Show the punchline
    Button(joke_window, text="Tell Another Joke", command=tell_another_joke).pack(side=LEFT, padx=20, pady=10)  # Button for another joke
    Button(joke_window, text="Quit", command=joke_window.destroy, bg="red").pack(side=RIGHT, padx=20, pady=10)  # Button to close the joke window

def tell_another_joke():
    open_joke_window()  # Open a new joke window with a different joke

jokes = load_jokes("randomJokes.txt")  # Load jokes into the global variable

# Entry widget for user input
input_entry = Entry(root, width=40)          # Create an entry box for user input
input_entry.pack(pady=5)                     # Add padding around the entry box
input_entry.bind("<Return>", process_input)  # Bind the Return key to process the input

# Label for suggestions if the input is incorrect
suggestion_label = Label(root, text="", fg="red", bg="#f2f2f2")  # Create a label for displaying suggestions
suggestion_label.pack(pady=5)  # Add padding around the suggestion label

# Quit button for the main window
Button(root, text="Quit", command=root.quit, bg="red").pack(pady=10)  # Button to quit the application

root.mainloop()  # Start the Tkinter main loop
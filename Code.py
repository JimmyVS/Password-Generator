# Password Generator GUI

# Description:
# This Python script, created by Jim Grysmpolakis that utilizes the Tkinter library to create a 
# graphical user interface (GUI) for generating random passwords with customizable settings. 
# Users can choose the password length, complexity, and include/exclude character sets. 
# Additionally, there is an option to save generated passwords to a text file.

# License:
# MIT License. Please do not claim as yours.

import os
from datetime import date
import random
from tkinter import ttk
from tkinter import *
from ttkthemes import ThemedTk

# Create a themed Tkinter window
screen = ThemedTk("breeze")
screen.set_theme("breeze")
screen.title("Password Generator")
screen.geometry("490x210")

# Define character sets for password generation
UpperCaseLetters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P",
                    "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]

LowerCaseLetters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p",
                    "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]

Numbers = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]

Symbols = [
    '!', '"', '#', '$', '%', '&', "'", '(', ')', '*', '+', ',', '-', '.', '/', ':', ';', '<', '=', '>',
    '?', '@', '[', ']', '^', '_', '`', '{', '|', '}', '~'
]

def generate():
    # Declare global variables to modify them within the function
    global PasswordLength
    global password
    
    # Reset password entry widget
    PasswordEntry.configure(state=NORMAL)
    PasswordEntry.configure(foreground="black")
    PasswordEntry.delete(0, END)
    
    # Initialize variables
    PasswordLength = 0
    Complexity = Difficulty.get()
    string = []
    
    # Retrieve user preferences
    CheckCapitalLetters = IncludeCapitalLetters.get()
    CheckLowerCaseLetters = IncludeLetters.get()
    CheckNumbers = IncludeNumbers.get()
    CheckSymbols = IncludeSymbols.get()
    CheckSpaces = IncludeSpaces.get()
    
    # Determine password length
    if LengthPicker.get() == 'Random':
        PasswordLength = random.randint(6, 12)
    else:
        try:
            PasswordLength = int(LengthPicker.get())
        except:
            PasswordEntry.insert(0, "Please enter a number, not text, not decimal, not symbols...")
    
    # Build the character set based on user preferences
    if CheckCapitalLetters == True:
        string.extend(UpperCaseLetters)
    if CheckLowerCaseLetters == True:
        string.extend(LowerCaseLetters)
    if CheckNumbers == True:
        string.extend("".join(Numbers))
    if CheckSymbols == True:
        if Complexity == "Strong":
            string.extend(Symbols)
        elif Complexity == "Medium":
            MediumSymbols = ["!", "_", "-", "/", "+", "*"]
            string.extend(MediumSymbols)
        elif Complexity == "Simple":
            string.extend("!")
    if CheckSpaces == True:
        string.append(" ")
    
    # Display an error message if no character set is selected
    if CheckCapitalLetters == False and CheckLowerCaseLetters == False and CheckNumbers == False and \
    CheckSymbols == False and CheckSpaces == False:
        PasswordEntry.insert(0, "Please select the contents of the password.")
    
    # Generate and display the password
    password = "".join(random.sample(string, PasswordLength))
    PasswordEntry.insert(0, password)
    PasswordEntry.configure(foreground="black")
    PasswordEntry.configure(state="readonly")

def save():
    # Get the current date
    today = date.today()
    day = today.strftime("%B %d, %Y")
    
    # Get the script directory and create the file path
    script_directory = os.path.dirname(os.path.abspath(__file__))
    file = os.path.join(script_directory, 'passwords.txt')

    try:
        # Save password to file if it's not empty
        if password != "" and password != " ":
            with open(file, 'a') as f:
                f.write("date: " + day + " | password:  " + password + "\n")
        else:
            # Display an error message if no password is generated
            PasswordEntry.configure(state=NORMAL)
            PasswordEntry.insert(0, "Couldn't save file, because no password is generated.")
            PasswordEntry.configure(state="readonly")
    except:
        # Display an error message if the file couldn't be saved
        PasswordEntry.configure(state=NORMAL)
        PasswordEntry.insert(0, "Couldn't save file, because no password is generated.")
        PasswordEntry.configure(state="readonly")

# Create Tkinter widgets for the GUI
PasswordLabel = ttk.Label(screen, text="Password: ", font=("Helvetica", 13, "bold"), foreground="black")
PasswordLabel.place(x=10, y=10)
PasswordEntry = ttk.Entry(screen, width=20, state=NORMAL, background="white")
PasswordEntry.configure(state="readonly")
PasswordEntry.place(x=110, y=5)
GenerateButton = ttk.Button(screen, text="Generate", command=generate)
GenerateButton.place(x=285, y=6)

SaveButton = ttk.Button(screen, text="Save", command=save)
SaveButton.place(x=385, y=6)

SettingsLabel = ttk.Label(screen, text="Settings: ", font=("Helvetica", 13, "bold"), foreground="black")
SettingsLabel.place(x=10, y=50)
LengthPicker = ttk.Combobox(screen, width=20, values=["Random", "6", "7", "8", "9", "10", "11", "12"])
LengthPicker.current(0)
LengthPicker.place(x=110, y=45)

NamesLabelLength = ttk.Label(screen, text="Length", font=("Helvetica", 9), foreground="gray")
NamesLabelLength.place(x=110, y=85)
NamesLabelComplexity = ttk.Label(screen, text="Complexity", font=("Helvetica", 9), foreground="gray")
NamesLabelComplexity.place(x=275, y=85)

Difficulty = StringVar(screen, "Medium")
DifficultyRadiobuttonLow = ttk.Radiobutton(screen, variable=Difficulty, value="Simple", text="Simple")
DifficultyRadiobuttonMedium = ttk.Radiobutton(screen, variable=Difficulty, value="Medium", text="Medium")
DifficultyRadiobuttonStrong = ttk.Radiobutton(screen, variable=Difficulty, value="Strong", text="Strong")
DifficultyRadiobuttonLow.place(x=275, y=48)
DifficultyRadiobuttonMedium.place(x=345, y=48)
DifficultyRadiobuttonStrong.place(x=420, y=48)

BreakUp = ttk.Label(screen, text="________________________________________________________________" \
                    "_____________________________________________________", font=("Helvetica", 7), foreground="black")
BreakUp.place(x=0, y=175)
CredentialLabel = ttk.Label(screen, text="Made by Jim Grysmpolakis", font=("Helvetica", 9), foreground="black")
CredentialLabel.place(x=170, y=190)

BreakUp2 = ttk.Label(screen, text="________________________________________________________________" \
                    "_____________________________________________________", font=("Helvetica", 7), foreground="black")
BreakUp2.place(x=0, y=100)

IncludeLabel = ttk.Label(screen, text="Include: ", font=("Helvetica", 13, "bold"), foreground="black")
IncludeLabel.place(x=10, y=140)

# BooleanVar for checkboxes
IncludeLetters = BooleanVar(value=1)
IncludeCapitalLetters = BooleanVar(value=0)
IncludeSymbols = BooleanVar(value=1)
IncludeNumbers = BooleanVar(value=1)
IncludeSpaces = BooleanVar(value=0)

# Checkboxes for character set inclusion
LettersCheckBox = ttk.Checkbutton(screen, text='Lower Case letters', variable=IncludeLetters, onvalue=1, offvalue=0)
CapitalLettersCheckBox = ttk.Checkbutton(screen, text='Upper Case letters', variable=IncludeCapitalLetters, onvalue=1, offvalue=0)
SymbolsCheckBox = ttk.Checkbutton(screen, text='Symbols', variable=IncludeSymbols, onvalue=1, offvalue=0)
NumbersCheckBox = ttk.Checkbutton(screen, text='Numbers', variable=IncludeNumbers, onvalue=1, offvalue=0)
SpacesCheckBox = ttk.Checkbutton(screen, text='Spaces', variable=IncludeSpaces, onvalue=1, offvalue=0)

# Place checkboxes on the screen
LettersCheckBox.place(x=107, y=119)
CapitalLettersCheckBox.place(x=249, y=119)
SymbolsCheckBox.place(x=390, y=119)
NumbersCheckBox.place(x=210, y=150)
SpacesCheckBox.place(x=295, y=150)

# Start the Tkinter main event loop
screen.mainloop()

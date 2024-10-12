from tkinter import *  
from tkinter import font as tkfont  

# Initialize an empty expression  
expression = ""  

# Function to update the expression when a button is pressed  
def press(num):  
    global expression  
    expression += str(num)  # Append the pressed number to the expression  
    equation.set(expression)  # Update the display  

# Function to evaluate the expression when '=' is pressed  
def equalpress():  
    try:  
        global expression  
        total = str(eval(expression))  # Evaluate the expression  
        equation.set(total)  # Display the result  
        expression = str(total)  # Update the expression with the result  
    except:  
        equation.set(" ERROR! ")  # Display error on invalid expression  
        expression = ""  # Reset expression  

# Function to clear the expression and display  
def clear():  
    global expression  
    expression = ""  
    equation.set("")  # Clear the display  

# Function to handle keyboard inputs  
def key_press(event):  
    key = event.char  
    if key in '0123456789+-*/':  # Check if the key is a number or operator  
        press(key)  # Update the expression  
    elif key == '\r':  # Handle the Enter key  
        equalpress()  # Evaluate the expression  
    elif key.lower() == 'c':  # Handle the 'C' key for clear  
        clear()  # Clear the display  

# Create the main window  
root = Tk()  
root.config(bg="black")  # Set background color  
root.title("ANITA CALCULATOR")  # Set window title  
root.geometry("520x580")  # Set window size  

# Create a StringVar to hold the expression  
equation = StringVar()  
button_font = tkfont.Font(size=30)  # Font for buttons  
text_font = tkfont.Font(size=35)  # Font for entry field  

# Create an entry field for displaying the expression  
expression_field = Entry(root, textvariable=equation, font=text_font, bg="#34495e", fg="white", bd=10, insertwidth=4, width=14, borderwidth=4)  
expression_field.grid(columnspan=4, ipadx=10, padx=10, pady=10, sticky='ew')  

# Define the layout of buttons  
buttons = [  
    ['7', '8', '9', '/'],  
    ['4', '5', '6', '*'],  
    ['1', '2', '3', '-'],  
    ['C', '0', '=', '+']  
]  

# Create buttons and add them to the grid  
for i, row in enumerate(buttons):  
    for j, button in enumerate(row):  
        if button == 'C':  
            btn_command = clear  # Command for clear button  
        elif button == '=':  
            btn_command = equalpress  # Command for equal button  
        else:  
            btn_command = lambda x=button: press(x)  # Command for number/operator buttons  
        
        # Create and place the button on the grid  
        Button(root, text=button, fg="white", bg="orange", command=btn_command, font=button_font).grid(row=i+2, column=j, padx=5, pady=5, sticky='nsew')  

# Configure grid layout for responsive resizing  
for i in range(4):  
    root.grid_columnconfigure(i, weight=1)   

for i in range(2, 6):  
    root.grid_rowconfigure(i, weight=1)   

# Bind keyboard inputs to the key_press function  
root.bind("<Key>", key_press)  

# Start the main event loop  
root.mainloop()
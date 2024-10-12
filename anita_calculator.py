from tkinter import *  
from tkinter import font as tkfont  

# Initialize an empty expression for the calculator  
expression = ""  

# Function to append the pressed number/button to the expression  
def press(num):  
    global expression  
    expression += str(num)  
    equation.set(expression)  # Update the display with the current expression  

# Function to calculate the result of the expression  
def equalpress():  
    try:  
        global expression  
        total = str(eval(expression))  # Evaluate the expression  
        equation.set(total)  # Display the result  
        expression = str(total)  # Store the result for further calculations  
    except:  
        equation.set(" ERROR! ")  # Display an error if evaluation fails  
        expression = ""  # Reset the expression  

# Function to clear the current expression  
def clear():  
    global expression  
    expression = ""  
    equation.set("")  # Clear the display  

# Function to handle key presses for calculations  
def key_press(event):  
    key = event.char  
    if key in '0123456789+-*/':  
        press(key)  # Call press function if a number or operator is pressed  
    elif key == '\r':  
        equalpress()  # Call equalpress if Enter is pressed  
    elif key.lower() == 'c':  
        clear()  # Call clear if 'c' is pressed  

# Create the main window  
root = Tk()  
root.config(bg="black")   
root.title("ANITA'S CALCULATOR")  
root.geometry("520x580")  

# String variable to hold the current equation  
equation = StringVar()  
button_font = tkfont.Font(size=30)   
text_font = tkfont.Font(size=35)   

# Create the entry field for the calculator display  
expression_field = Entry(root, textvariable=equation, font=text_font, bg="#34495e", fg="white", bd=10, insertwidth=4, width=14, borderwidth=4)  
expression_field.grid(columnspan=4, ipadx=10, padx=10, pady=10, sticky='ew')  

# Define the calculator buttons layout  
buttons = [  
    ['7', '8', '9', '/'],  
    ['4', '5', '6', '*'],  
    ['1', '2', '3', '-'],  
    ['C', '0', '=', '+']  
]  

# Create buttons and assign their functionality  
for i, row in enumerate(buttons):  
    for j, button in enumerate(row):  
        # Determine the command and color based on the button text  
        if button == 'C':  
            btn_command = clear  
            button_color = "black"  
            button_fg = "white"  
        elif button == '=':  
            btn_command = equalpress  
            button_color = "orange"  
            button_fg = "black"    
        elif button in ['+', '/', '*', '-']:  
            btn_command = lambda x=button: press(x)  
            button_color = "orange"  
            button_fg = "black"   
        elif button in ['7', '8', '9']:  
            btn_command = lambda x=button: press(x)  
            button_color = "gray"  
            button_fg = "white"  
        else:  
            btn_command = lambda x=button: press(x)  
            button_color = "black"  
            button_fg = "white"   

        # Create and place the button on the grid  
        Button(root, text=button, fg=button_fg, bg=button_color, command=btn_command, font=button_font).grid(row=i+2, column=j, padx=5, pady=5, sticky='nsew')  

# Configure grid columns and rows for proper spacing  
for i in range(4):  
    root.grid_columnconfigure(i, weight=1)   

for i in range(2, 6):  
    root.grid_rowconfigure(i, weight=1)   

# Bind keypress events to the key_press function  
root.bind("<Key>", key_press)  

# Start the main event loop  
root.mainloop()
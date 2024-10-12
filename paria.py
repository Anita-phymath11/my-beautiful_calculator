from tkinter import *  
from tkinter import font as tkfont  

# Initialize an empty expression for the calculator  
expression = ""  

def press(num):  
    global expression  
    expression += str(num)  # Append the pressed number to the expression  
    equation.set(expression)  # Update the display  

def equalpress():  
    try:  
        global expression  
        total = str(eval(expression))  # Calculate the total using eval  
        equation.set(total)  # Show the result on the display  
        expression = str(total)  # Update the expression to the result  
    except:  
        equation.set(" ERROR! ")  # Show an error if the expression is invalid  
        expression = ""  # Reset the expression  

def clear():  
    global expression  
    expression = ""  # Clear the expression  
    equation.set("")  # Clear the display  

def key_press(event):  
    key = event.char  # Get the character of the pressed key  
    if key in '0123456789+-*/':  
        press(key)  # If it's a number or operator, call press  
    elif key == '\r':  
        equalpress()  # If Enter is pressed, calculate the result  
    elif key.lower() == 'c':  
        clear()  # If 'c' is pressed, clear the expression  

root = Tk()  
root.config(bg="#f3c6d0")  # Change background color  
root.title("Daughter's Calculator")  # Set the title of the window  
root.geometry("520x580")  # Set the size of the window  

equation = StringVar()  # Create a StringVar to hold the display value  
button_font = tkfont.Font(size=30)  # Set font size for buttons  
text_font = tkfont.Font(size=35)  # Set font size for entry field  

# Create entry field for displaying the expression/result  
expression_field = Entry(root, textvariable=equation, font=text_font, bg="#f9e5e7", fg="#d5006d", bd=10, insertwidth=4, width=14, borderwidth=4)  
expression_field.grid(columnspan=4, ipadx=10, padx=10, pady=10, sticky='ew')  

# Define buttons layout  
buttons = [  
    ['7', '8', '9', '/'],  
    ['4', '5', '6', '*'],  
    ['1', '2', '3', '-'],  
    ['C', '0', '=', '+']  
]  

# Create buttons and attach their functions  
for i, row in enumerate(buttons):  
    for j, button in enumerate(row):  
        if button == 'C':  
            btn_command = clear  # Assign clear function to 'C' button  
        elif button == '=':  
            btn_command = equalpress  # Assign equal function to '=' button  
        else:  
            btn_command = lambda x=button: press(x)  # Assign press function to other buttons  
        
        Button(root, text=button, fg="white", bg="#d5006d", command=btn_command, font=button_font).grid(row=i+2, column=j, padx=5, pady=5, sticky='nsew')  

# Configure grid weights for layout responsiveness  
for i in range(4):  
    root.grid_columnconfigure(i, weight=1)   

for i in range(2, 6):  
    root.grid_rowconfigure(i, weight=1)   

root.bind("<Key>", key_press)  # Bind keyboard press to the key_press function  

root.mainloop()  # Start the Tkinter main loop
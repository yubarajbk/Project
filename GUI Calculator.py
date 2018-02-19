from tkinter import *

#Creating window frame
frame = Tk()
frame.title("GUI Calculator")
frame.resizable(width = False, height = False)

txt_Input = StringVar()
store =""


#Defining functions
def NumberInput(num):
    global store
    store = store + str(num)
    txt_Input.set(store)

def clrScreen():
    global store
    store = ""
    txt_Input.set(0)

def bckSpace():
    global store
    back = str(store[:-1])
    txt_Input.set(back)
    store = back

def calcPercent():
    global store
    try:
        store = float(eval(store))
        txt_Input.set(store*100)
    except:
        txt_Input.set("ERROR")
        store = ""


def Result():
    global store
    try:
        store = str(eval(store))
        txt_Input.set(store)
    except:
        txt_Input.set("ERROR")
        store = ""


#Creating Entry Box    
Display = Entry(frame, font = ('arial', 20, 'bold'), textvariable = txt_Input, bd = 15, insertwidth = 4,
               bg = 'powder blue', justify = 'right')
Display.grid(columnspan = 4)


#Creating and Positioning Buttons

#Clear Button
Clear = Button(frame, padx = 14, bd = 8, fg = 'black', font = ('arial', 20, 'bold'),
              text = "C", bg = 'powder blue', command = clrScreen)
Clear.grid(row = 1, column = 0)


#Backspace Button
Backspace = Button(frame, padx = 14, bd = 8, fg = 'black', font = ('arial', 20, 'bold'),
              text = "<-", bg = 'powder blue', command = bckSpace)
Backspace.grid(row = 1, column = 1)

#Percentage Button
Percent = Button(frame, padx = 14, bd = 8, fg = 'black', font = ('arial', 20, 'bold'),
              text = "%", bg = 'powder blue', command = calcPercent)
Percent.grid(row = 1, column = 2)


#Division Button
Division = Button(frame, padx = 16, bd = 8, fg = 'black', font = ('arial', 20, 'bold'),
              text = "/", bg = 'powder blue', command = lambda:NumberInput("/"))
Division.grid(row = 1, column = 3)


#Multiply Button
Multiply = Button(frame, padx = 16, bd = 8, fg = 'black', font = ('arial', 20, 'bold'),
              text = "*", bg = 'powder blue', command = lambda:NumberInput("*"))
Multiply.grid(row = 2, column = 3)


#Subtraction Button
Subtract = Button(frame, padx = 16, bd = 8, fg = 'black', font = ('arial', 20, 'bold'),
              text = "-", bg = 'powder blue', command = lambda:NumberInput("-"))
Subtract.grid(row = 3, column = 3)
             

#NumberInput 7 Button
btn7 = Button(frame, padx = 16, bd = 8, fg = 'black', font = ('arial', 20, 'bold'),
              text = '7', bg = 'powder blue', command = lambda:NumberInput(7))
btn7.grid(row = 2, column = 0)


#NumberInput 8 Button
btn8 = Button(frame, padx = 16, bd = 8, fg = 'black', font = ('arial', 20, 'bold'),
              text = '8', bg = 'powder blue', command = lambda:NumberInput(8))
btn8.grid(row = 2, column = 1)


#NumberInput 9 Button
btn9 = Button(frame, padx = 16, bd = 8, fg = 'black', font = ('arial', 20, 'bold'),
              text = '9', bg = 'powder blue', command = lambda:NumberInput(9))
btn9.grid(row = 2, column = 2)


#Addition Button
Add = Button(frame, padx = 16, bd = 8, fg = 'black', font = ('arial', 20, 'bold'),
              text = "+", bg = 'powder blue', command = lambda:NumberInput("+"))
Add.grid(row = 4, column = 3)


#NumberInput 4 Button
btn4 = Button(frame, padx = 16, bd = 8, fg = 'black', font = ('arial', 20, 'bold'),
              text = '4', bg = 'powder blue', command = lambda:NumberInput(4))
btn4.grid(row = 3, column = 0)


#NumberInput 5 Button
btn5 = Button(frame, padx = 16, bd = 8, fg = 'black', font = ('arial', 20, 'bold'),
              text = '5', bg = 'powder blue', command = lambda:NumberInput(5))
btn5.grid(row = 3, column = 1)


#NumberInput 6 Button
btn6 = Button(frame, padx = 16, bd = 8, fg = 'black', font = ('arial', 20, 'bold'),
              text = '6', bg = 'powder blue', command = lambda:NumberInput(6))
btn6.grid(row = 3, column = 2)


#NumberInput 1 Button
btn1 = Button(frame, padx = 16, bd = 8, fg = 'black', font = ('arial', 20, 'bold'),
              text = '1', bg = 'powder blue', command = lambda:NumberInput(1))
btn1.grid(row = 4, column = 0)

#NumberInput 2 Button
btn2 = Button(frame, padx = 16, bd = 8, fg = 'black', font = ('arial', 20, 'bold'),
              text = '2', bg = 'powder blue', command = lambda:NumberInput(2))
btn2.grid(row = 4, column = 1)


#NumberInput 3 Button
btn3 = Button(frame, padx = 16, bd = 8, fg = 'black', font = ('arial', 20, 'bold'),
              text = '3', bg = 'powder blue', command = lambda:NumberInput(3))
btn3.grid(row = 4, column = 2)


#Equals Button
Equals = Button(frame, padx = 60, bd = 8, fg = 'black', font = ('arial', 20, 'bold'),
              text = "=", bg = 'powder blue', command = Result)
Equals.grid(row = 5, column = 2, columnspan = 2)


#NumberInput 0 Button
btn0 = Button(frame, padx = 16 , bd = 8, fg = 'black', font = ('arial', 20, 'bold'),
              text = '0', bg = 'powder blue', command = lambda:NumberInput(0))
btn0.grid(row = 5, column = 0)


#Dot Button
Dot = Button(frame, padx = 18 , bd = 8, fg = 'black', font = ('arial', 20, 'bold'),
              text = ".", bg = 'powder blue', command = lambda:NumberInput("."))
Dot.grid(row = 5, column = 1)


frame.mainloop()


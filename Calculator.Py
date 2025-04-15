from tkinter import *

BUTTON_BG = "#3B3B3B"
BUTTON_FG = "white"

#Pressing The Button
def button_press(num):
  global equation_text
  equation_text = equation_text + str(num)
  equation_label.set(equation_text)

#Calculate The Result
def equals():
  global equation_text
  try:
    total = str(eval(equation_text))
    equation_label.set(total)
    equation_text = total
  except ZeroDivisionError:
    equation_label.set("Arithmetic Error")
    equation_text = ""
  except SyntaxError:
    equation_label.set("Syntax Error")
    equation_text = ""
  except NameError:
    equation_label.set("Syntax Error")
    equation_text = ""

#Clear The Screen
def clear():
  global equation_text
  equation_label.set("")
  equation_text = ""

#BackSpace One Char
def delete():
    global equation_text
    equation_text = equation_text[0:len(equation_text)-1]
    equation_label.set(equation_text)

#Getting Keys From KeyBoard
def keys(event):
  global equation_text
  num_list = ["0", "1", "2", "3", "4" ,"5", "6", "7", "8", "9"]
  for key in num_list:
    if key == event.keysym:
      button_press(key)
  if event.keysym == "period":
    button_press(".")
  elif event.keysym == "plus":
    button_press("+")
  elif event.keysym == "minus":
    button_press("-")
  elif event.keysym == "asterisk":
    button_press("*")
  elif event.keysym == "slash":
    button_press("/")
  elif event.keysym == "parenleft":
    button_press("(")
  elif event.keysym == "parenright":
    button_press(")")
  elif event.keysym == "equal" or event.keysym == "Return":
    equals()
  elif event.keysym == "BackSpace":
    delete()
  elif event.keysym == "Escape":
    clear()
  else:
    return

#Intiate The Window
window = Tk()
window.title("Calculator By Ziad")
window.geometry("364x500")
window.resizable(False, False)

equation_text = ""
equation_label = StringVar()

#Screen Where The Equation Display
label = Label(window, textvariable=equation_label ,font=("consolas", 20,),
              fg=BUTTON_FG, bg="#202020", width=24, height=2)
label.pack()

#Frame To Collect Buttons
frame = Frame(window)
frame.pack()

#Create Buttons
button_0 = Button(frame, text=0, height=4 , width=9,font=35, fg=BUTTON_FG, bg=BUTTON_BG,
                  activeforeground=BUTTON_FG, activebackground=BUTTON_BG,command= lambda:button_press(0))
button_0.grid(row=4, column=0)

button_1 = Button(frame, text=1, height=4 , width=9,font=35, fg=BUTTON_FG, bg=BUTTON_BG,
                  activeforeground=BUTTON_FG, activebackground=BUTTON_BG, command= lambda:button_press(1))
button_1.grid(row=3, column=0)

button_2 = Button(frame, text=2, height=4 , width=9,font=35, fg=BUTTON_FG, bg=BUTTON_BG,
                  activeforeground=BUTTON_FG, activebackground=BUTTON_BG, command= lambda:button_press(2))
button_2.grid(row=3, column=1)

button_3 = Button(frame, text=3, height=4 , width=9, font=35, fg=BUTTON_FG, bg=BUTTON_BG,
                  activeforeground=BUTTON_FG, activebackground=BUTTON_BG,command= lambda:button_press(3))
button_3.grid(row=3, column=2)

button_4 = Button(frame, text=4, height=4 , width=9, font=35, fg=BUTTON_FG, bg=BUTTON_BG,
                  activeforeground=BUTTON_FG, activebackground=BUTTON_BG, command= lambda:button_press(4))
button_4.grid(row=2, column=0)

button_5 = Button(frame, text=5, height=4 , width=9, font=35, fg=BUTTON_FG, bg=BUTTON_BG,
                  activeforeground=BUTTON_FG, activebackground=BUTTON_BG, command= lambda:button_press(5))
button_5.grid(row=2, column=1)

button_6 = Button(frame, text=6, height=4 , width=9, font=35, fg=BUTTON_FG, bg=BUTTON_BG,
                  activeforeground=BUTTON_FG, activebackground=BUTTON_BG, command= lambda:button_press(6))
button_6.grid(row=2, column=2)

button_7 = Button(frame, text=7, height=4 , width=9, font=35, fg=BUTTON_FG, bg=BUTTON_BG,
                  activeforeground=BUTTON_FG, activebackground=BUTTON_BG, command= lambda:button_press(7))
button_7.grid(row=1, column=0)

button_8 = Button(frame, text=8, height=4 , width=9, font=35, fg=BUTTON_FG, bg=BUTTON_BG,
                  activeforeground=BUTTON_FG, activebackground=BUTTON_BG, command= lambda:button_press(8))
button_8.grid(row=1, column=1)

button_9 = Button(frame, text=3, height=4 , width=9, font=35, fg=BUTTON_FG, bg=BUTTON_BG,
                  activeforeground=BUTTON_FG, activebackground=BUTTON_BG, command= lambda:button_press(9))
button_9.grid(row=1, column=2)

button_decimal = Button(frame, text=".", height=4 , width=9, font=35, fg=BUTTON_FG, bg=BUTTON_BG,
                        activeforeground=BUTTON_FG, activebackground=BUTTON_BG, command= lambda:button_press("."))
button_decimal.grid(row=4, column=1)

button_plus = Button(frame, text="+", height=4 , width=9, font=35, fg=BUTTON_FG, bg=BUTTON_BG,
                    activeforeground=BUTTON_FG, activebackground=BUTTON_BG, command= lambda:button_press("+"))
button_plus.grid(row=1, column=4)

button_minus = Button(frame, text="-", height=4 , width=9, font=35, fg=BUTTON_FG, bg=BUTTON_BG,
                      activeforeground=BUTTON_FG, activebackground=BUTTON_BG, command= lambda:button_press("-"))
button_minus.grid(row=2, column=4)

button_multiply = Button(frame, text="*", height=4 , width=9, font=35, fg=BUTTON_FG, bg=BUTTON_BG,
                        activeforeground=BUTTON_FG, activebackground=BUTTON_BG, command= lambda:button_press("*"))
button_multiply.grid(row=3, column=4)

button_divided = Button(frame, text="/", height=4 , width=9, font=35, fg=BUTTON_FG, bg=BUTTON_BG,
                        activeforeground=BUTTON_FG, activebackground=BUTTON_BG, command= lambda:button_press("/"))
button_divided.grid(row=4, column=4)

button_left_bracket = Button(frame, text="(", height=4, width=9, font=35, fg=BUTTON_FG, bg=BUTTON_BG,
                            activeforeground=BUTTON_FG, activebackground=BUTTON_BG, command= lambda:button_press("("))
button_left_bracket.grid(row=0, column=0)

button_right_bracket = Button(frame, text=")", height=4, width=9, font=35, fg=BUTTON_FG, bg=BUTTON_BG,
                              activeforeground=BUTTON_FG, activebackground=BUTTON_BG, command= lambda:button_press(")"))
button_right_bracket.grid(row=0, column=1)

button_equal = Button(frame, text="=", height=4 , width=9, font=35, fg=BUTTON_FG, bg=BUTTON_BG,
                      activeforeground=BUTTON_FG, activebackground=BUTTON_BG, command= equals)
button_equal.grid(row=4, column=2)

button_delete = Button(frame, text="DEL", height=4 , width=9, font=35, fg=BUTTON_FG, bg=BUTTON_BG,
                      activeforeground=BUTTON_FG, activebackground=BUTTON_BG, command=delete)
button_delete.grid(row=0, column=2)

button_clear = Button(frame, text="Clear", height=4 , width=9, font=35, fg=BUTTON_FG, bg=BUTTON_BG,
                      activeforeground=BUTTON_FG, activebackground=BUTTON_BG, command= clear)
button_clear.grid(row=0, column=4)

#Binding The KeyBoard
window.bind("<Key>", keys)

window.mainloop()

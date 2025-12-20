# from tkinter import *
# first=""
# second=""
# first_set=False
# sign=''
# root=Tk()
# ans=" "
# root.title("Graphical User Interface Calculator")
# root.geometry("700x600")
# root.minsize(width=700,height=600)

# mainframe=Frame(root,bg='black',width=600,height=500,bd=10,borderwidth=10)
# mainframe.pack(pady=100)
# mainframe.pack_propagate(0)

# display=Frame(mainframe,bg='lightgrey',width=550,height=100)
# display.pack(pady=5)
# display.pack_propagate(0)

# numbers=Frame(mainframe,bg='lightgrey',width=300,height=350)
# numbers.pack(padx=15,side='left')
# numbers.grid_propagate(0)

# menus=Frame(mainframe,bg='lightgrey',width=250,height=350)
# menus.pack(padx=15,side='right')
# menus.grid_propagate(0)

# screen=Label(display,text='0',width=530,height=80,bg='white',font=('Arial',50),anchor="e")
# screen.pack()

# def press(value):
#     global first_set
#     global first
#     global second
#     global sign
#     global ans
#     current=screen['text']
#     if(value=="AC"):
#         screen.config(text="")
#         first_set=False
#         second=""
#         first=""
#         sign=""
#     elif(value=="DEL"):
#         if not ans=="":
#             pass
#         elif not first_set:
#             first=first[:-1]
#             screen.config(text=first)
#         else :
#             second=second[:-1]
#             screen.config(text=second)
#     elif(value=="+"):
#         first_set=True
#         sign="+"
#         screen.config(text="")
#         # print("first val: ",first)
#         # print("second val : ",second)
#     elif(value=="-"):
#         first_set=True
#         sign="-"
#         screen.config(text="")
#     elif(value=="*"):
#         first_set=True
#         sign="*"
#         screen.config(text="")
#     elif(value=="/"):
#         first_set=True
#         sign="/"
#         screen.config(text="")
#     elif(value=="="):
#         if not (first == "" or second=="" or sign==""):
#             ans=eval(first+sign+second)
#             # print(type(ans))
#             first=str(ans)
#             print(first)
#             print(second)
#             second=""
#             screen.config(text=str(ans))
#             ans=""

#     elif current == "0" or current=="":
#         screen.config(text=str(value))
#         if not first_set:
#            first=str(value)
#         #    screen.config(text=str(value))

#         else:
#             second=str(value)
#             # screen.config(text=str(value))

#     else:
#         if not first_set:
#            first=first+str(value)
#            screen.config(text=current + str(value))
#         else:               
#             second=second+str(value)
#             screen.config(text=current + str(value))

           


# r = 0
# col=0
# for i in range(1,10,1):
#     if(col>2 ):
#         r+=1
#         col=0

#     Button(numbers,text=i,command=lambda x=i: press(x),width=6,height=3).grid(row=r,column=col,padx=20,pady=10)
#     col+=1
# Button(numbers,text="0",command=lambda : press(0),width=32,height=3).grid(row=3,column=0,columnspan=3)
# Button(menus,text="Delete",command=lambda : press("DEL"),width=15,height=2).grid(row=0,column=0)
# Button(menus,text="All Clear",command=lambda : press("AC"),width=15,height=2).grid(row=0,column=1)


# Button(menus,text="+",command=lambda : press("+"),width=15,height=4).grid(row=1,column=0,padx=2,pady=2)
# Button(menus,text="-",command=lambda : press("-"),width=15,height=4).grid(row=1,column=1,padx=2,pady=2)
# Button(menus,text="*",command=lambda : press("*"),width=15,height=4).grid(row=2,column=0,padx=2,pady=2)
# Button(menus,text="/",command=lambda : press("/"),width=15,height=4).grid(row=2,column=1,padx=2,pady=2)
# Button(menus,text="=",command=lambda : press("="),width=30,height=4).grid(row=3,column=0,padx=2,pady=2,columnspan=2)

# root.mainloop()
from tkinter import *

class Calculator:
    def __init__(self, root):
        self.expression = ""     # holds full expression
        self.current = ""        # holds current number
        self.result_shown = False

        root.title("Improved Calculator")
        root.geometry("400x500")
        root.config(bg="black")

        # Display
        self.screen = Label(root, text="0", anchor="e",
                            bg="white", fg="black",
                            font=("Arial", 40), bd=10,
                            relief="sunken")
        self.screen.pack(fill="both", padx=10, pady=10, ipady=20)

        # Buttons Frame
        btn_frame = Frame(root, bg="black")
        btn_frame.pack()

        # Layout of buttons
        buttons = [
            ["AC", "DEL", "/", "*"],
            ["7", "8", "9", "-"],
            ["6", "5", "4", "+"],
            ["3", "2", "1", "="],
            ["0", ".", "", ""]
        ]

        for r, row in enumerate(buttons):
            for c, char in enumerate(row):
                if char != "":
                    Button(btn_frame, text=char, width=6, height=3,
                           font=("Arial", 18),
                           command=lambda x=char: self.press(x)).grid(
                        row=r, column=c, padx=5, pady=5
                    )

    # -----------------------------------------
    #              MAIN LOGIC
    # -----------------------------------------
    def press(self, value):
        if value == "AC":
            self.expression = ""
            self.current = ""
            self.result_shown = False
            self.update_screen("0")
            return

        if value == "DEL":
            if self.current and not self.result_shown:
                self.current = self.current[:-1]
                self.update_screen(self.current if self.current else "0")
            return

        # If result is shown and a number is pressed → start new calculation
        if self.result_shown and value.isdigit():
            self.expression = ""
            self.current = value
            self.result_shown = False
            self.update_screen(self.current)
            return

        # Numbers
        if value.isdigit():
            self.current += value
            self.update_screen(self.current)
            return

        # Decimal
        if value == ".":
            if "." not in self.current:
                self.current += "."
                self.update_screen(self.current)
            return

        # Operators (+ - * /)
        if value in "+-*/":
            if self.current == "":
                return  # avoid double operators

            self.expression += self.current + value
            self.current = ""
            self.update_screen(value)
            return

        # Equals (=)
        if value == "=":
            if self.current == "":
                return

            self.expression += self.current
            try:
                result = str(eval(self.expression))
                self.update_screen(result)
                self.current = result
                self.expression = ""
                self.result_shown = True
            except Exception:
                self.update_screen("Error")
                self.current = ""
                self.expression = ""

    def update_screen(self, value):
        self.screen.config(text=value)


root = Tk()
Calculator(root)
root.mainloop()

from tkinter import *
first=""
second=""
first_set=False
sign=''
root=Tk()

root.title("Graphical User Interface Calculator")
root.geometry("700x600")
root.minsize(width=700,height=600)

mainframe=Frame(root,bg='black',width=600,height=500,bd=10,borderwidth=10)
mainframe.pack(pady=100)
mainframe.pack_propagate(0)

display=Frame(mainframe,bg='lightgrey',width=550,height=100)
display.pack(pady=5)
display.pack_propagate(0)

numbers=Frame(mainframe,bg='lightgrey',width=300,height=350)
numbers.pack(padx=15,side='left')
numbers.grid_propagate(0)

menus=Frame(mainframe,bg='lightgrey',width=250,height=350)
menus.pack(padx=15,side='right')
menus.grid_propagate(0)

screen=Label(display,text='0',width=530,height=80,bg='white',font=('Arial',50),anchor="e")
screen.pack()

def press(value):
    global first_set
    global first
    global second
    global sign
    current=screen['text']
    if(value=="+"):
        first_set=True
        sign="+"
        screen.config(text="")
        # print("first val: ",first)
        # print("second val : ",second)
    elif(value=="-"):
        first_set=True
        sign="-"
        screen.config(text="")
    elif(value=="*"):
        first_set=True
        sign="*"
        screen.config(text="")
    elif(value=="/"):
        first_set=True
        sign="/"
        screen.config(text="")
    elif(value=="="):
        if not (first == "" or second=="" or sign==""):
            ans=eval(first+sign+second)
            # print(type(ans))
            first=str(ans)
            print(first)
            print(second)
            second=""
            screen.config(text=str(ans))

    elif current == "0" or current=="":
        screen.config(text=str(value))
        if not first_set:
           first=str(value)
        #    screen.config(text=str(value))

        else:
            second=str(value)
            # screen.config(text=str(value))

    else:
        if not first_set:
           first=first+str(value)
           screen.config(text=current + str(value))
        else:               
            second=second+str(value)
            screen.config(text=current + str(value))

           


r = 0
col=0
for i in range(1,10,1):
    if(col>2 ):
        r+=1
        col=0

    Button(numbers,text=i,command=lambda x=i: press(x),width=6,height=3).grid(row=r,column=col,padx=20,pady=10)
    col+=1
Button(numbers,text="0",command=lambda : press(0),width=32,height=3).grid(row=3,column=0,columnspan=3)

Button(menus,text="+",command=lambda : press("+"),width=15,height=5).grid(row=1,column=0)
Button(menus,text="-",command=lambda : press("-"),width=15,height=5).grid(row=1,column=1)
Button(menus,text="*",command=lambda : press("*"),width=15,height=5).grid(row=2,column=0)
Button(menus,text="/",command=lambda : press("/"),width=15,height=5).grid(row=2,column=1)
Button(menus,text="=",command=lambda : press("="),width=30,height=5).grid(row=3,column=0,columnspan=2)

root.mainloop()
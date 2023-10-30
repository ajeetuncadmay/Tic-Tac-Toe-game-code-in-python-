from tkinter import *
from tkinter import messagebox
import random as r
def button(frame):          #Function to define a button
    b=Button(frame,padx=0,bg="papaya whip",width=3,text="   ",font=('Helvetica',50,'bold'), bd=1)
    return b
def change_a():             #Function to change the operand for the next player
    global a
    for i in ['O','X']:
        if not(i==a):
            a=i
            break

def reset():                #Resets the game
    global a
    for i in range(3):
        for j in range(3):
                b[i][j]["text"]=" "
                b[i][j]["state"]=NORMAL
    a=r.choice(['X','O'])

def check():                #Checks for victory or Draw
    for i in range(3):
            if(b[i][0]["text"]==b[i][1]["text"]==b[i][2]["text"]==a or b[0][i]["text"]==b[1][i]["text"]==b[2][i]["text"]==a ):
                    messagebox.showinfo("Congrats!!","'"+a+"' Congrats 😀jit gaye ")
                    reset()
    if(b[0][0]["text"]==b[1][1]["text"]==b[2][2]["text"]==a or b[0][2]["text"]==b[1][1]["text"]==b[2][0]["text"]==a):
        messagebox.showinfo("Congrats!!","'"+a+"' Congrats 😀win😃")
        reset()   
    elif(b[0][0]["state"]==b[0][1]["state"]==b[0][2]["state"]==b[1][0]["state"]==b[1][1]["state"]==b[1][2]["state"]==b[2][0]["state"]==b[2][1]["state"]==b[2][2]["state"]==DISABLED):
        messagebox.showinfo("Tied!!","match drow ho gya ")
        reset()
def click(row,col):
        b[row][col].config(text=a,state=DISABLED,disabledforeground=colour[a])
        check() 
        change_a()
        label.config(text=a+"'s Ajeet") 
         


###############   Main Program #################
root=Tk()                   #Window defined
root.title("Tic-Tac-Toe game") 
root.resizable(False,False)
root.geometry("800x500+400+100")
  #Title given
a=r.choice(['O','X'])       #Two operators defined
colour={'O':"deep sky blue",'X':"lawn green"}
b=[[],[],[]]
for i in range(3):
        for j in range(3):
                b[i].append(button(root))
                b[i][j].config(command= lambda row=i,col=j:click(row,col))
                b[i][j].grid(row=i,column=j)
label=Label(text=a+"'s Chance",font=('arial',20,'bold'))
label.grid(row=3,column=0,columnspan=3)
bgimage=PhotoImage(file="i.png")
bgLabel=Label(root,image=bgimage,width=400,height=550,bg="deep sky blue")
bgLabel.place(x=400,y=0)
lbl=Label(root,text="Playing Tic-Tac-Toe game ",fg="black",font=("Arial 20 bold"),bg="deep sky blue")
lbl.place(x=450,y=100)
lbl=Label(root,text="Welcome ",fg="black",font=("Arial 50 bold"),bg="deep sky blue")
lbl.place(x=450,y=0)
root.config(bg="deep sky blue")

root.mainloop()
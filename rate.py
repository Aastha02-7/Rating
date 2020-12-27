from tkinter import *
from tkinter import messagebox
root=Tk()
root.title("Rate my sketches")
root.geometry("800x800")

count=0
def incre():
    global count
    if count<10:
        count+=1
        lm.config(text=str(count))

def show():
    pass

def show1():
    pass

def stop():
    answer=messagebox.askyesno(title="Quitting",message="All done want to quit!")
    if answer == True:
        root.destroy()

l0=Label(root,text="Hello User! Please rate my sketches",font="Arial 15 bold",bg="black",fg="white")
l0.grid(row=0,column=3)

draw1=PhotoImage(file="C:/Users/aasth/Desktop/1st.png")
l1=Label(root,image=draw1)
draw2=PhotoImage(file="C:/Users/aasth/Desktop/2nd.png")
l2=Label(root,image=draw2)
draw3=PhotoImage(file="C:/Users/aasth/Desktop/3rd.png")
l3=Label(root,image=draw3)
draw4=PhotoImage(file="C:/Users/aasth/Desktop/4th.png")
l4=Label(root,image=draw4)

l1.grid(row=1,column=0)
l2.grid(row=2,column=0)
l3.grid(row=3,column=0)
l4.grid(row=4,column=0)

l5=Label(root,text="Click the button to rate between 0 to 10",font="Arial 12 bold")
l6=Label(root,text="Choose one",font="Arial 12 bold")
l7=Label(root,text="Choose one or more",font="Arial 12 bold")
l8=Label(root,text="Adjust the scale :)",font="Arial 12 bold")

l5.grid(row=1,column=2)
l6.grid(row=2,column=2)
l7.grid(row=3,column=2)
l8.grid(row=4,column=2)

lm=Label(root,text="0",font="Arial 11 bold")
b1=Button(root,text="0-10",command=incre,font="Arial 11 bold")

b1.grid(row=1,column=4)
lm.grid(row=1,column=5)

x=IntVar()
rb1=Radiobutton(root,text="Like it",command=show,variable=x,value=1,font="Arial 11 bold")
rb2=Radiobutton(root,text="Don't like it",command=show,variable=x,value=2,font="Arial 11 bold")
rb3=Radiobutton(root,text="Love it",command=show,variable=x,value=3,font="Arial 11 bold")

rb1.grid(row=2,column=4)
rb2.grid(row=2,column=5)
rb3.grid(row=2,column=6)

a=IntVar()
b=IntVar()
c=IntVar()
cb1=Checkbutton(root,text="Woww",command=show1,variable=a,font="Arial 11 bold")
cb2=Checkbutton(root,text="Awesome",command=show1,variable=b,font="Arial 11 bold")
cb3=Checkbutton(root,text="Beautiful",command=show1,variable=c,font="Arial 11 bold")

cb1.grid(row=3,column=4)
cb2.grid(row=3,column=5)
cb3.grid(row=3,column=6)

sb=Scale(root,from_=0,to=100,orient=HORIZONTAL,font="Arial 11 bold")
sb.grid(row=4,column=4)

b5=Button(root,text="All done!!!",command=stop,font="Arial 14 bold")
b5.grid(row=5,column=3)

root.mainloop()
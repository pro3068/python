from tkinter import*

root=Tk()

root.title("Pro")
root.geometry("500x500+50+50")

labl1=Label(root,text="Label1",font=("times new roman",30,"bold"))

#labl1.pack(side=LEFT)

#labl1.grid(row=0,column=0)

#labl1.place(x=50,y=100)

entry=Entry(root,width=100)
entry.pack(padx=50,pady=20)

def clickl():
    lbl=Label(root,text="Hi"+entry.get())
    lbl.pack()
 

Mybutton=Button(root,text="Click me",command=clickl)
Mybutton.pack()


root=mainloop()
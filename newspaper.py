from tkinter import *
from PIL import Image, ImageTk

#creating the root window 
root=Tk() 
root.title("Macleans Newspaper")
root.geometry("1180x644")
root.minsize(width=300, height=300)



#creating the header
Header = Frame(root,bg="#333",borderwidth=5, relief=SUNKEN)
Header.pack(side=TOP, fill=X)
headerlabel = Label(Header, text="Macleans Newspaper")
headerlabel.pack(side=LEFT, padx=10) 



 #news 1 
f1 = Frame(root, bg="lightblue", borderwidth=5, relief=SUNKEN)
f1.pack(side=TOP, fill=X)
p1 = Image.open("img/auckland.jpg")
p1 = ImageTk.PhotoImage(p1)
l1 = Label(f1, image=p1, width=100, height = 100)
l1.pack(side=LEFT) 
l2= Label (f1, text= "Macleans college newspaper").pack() 


f3 = Frame(root, bg="lightblue", borderwidth=5, relief=SUNKEN)
f3.pack(side=TOP, fill=X)
p3 = Image.open("img/auckland.jpg")
p3 = ImageTk.PhotoImage(p3)
l3 = Label(f3, image=p3, width=100, height = 100)
l3.pack(side=LEFT)
l4= Label (f3, text="Macleans college").pack()

f4 = Frame(root, bg="lightblue", borderwidth=5, relief=SUNKEN)
f4.pack(side=TOP, fill=X)
p4 = Image.open("img/auckland.jpg")
p4 = ImageTk.PhotoImage(p4)
l4 = Label(f4, image=p4, width=100, height = 100)
l4.pack(side=LEFT) 
l5= Label (f4, text= "Macleans college").pack()

f5 = Frame(root, bg="lightblue", borderwidth=5, relief=SUNKEN)
f5.pack(side=TOP, fill=X)
p5 = Image.open("img/auckland.jpg")
p5 = ImageTk.PhotoImage(p5)
l5 = Label(f5, image=p4, width=100, height = 100)
l5.pack(side=LEFT) 
l6= Label (f5, text="Macleans college").pack()



root.mainloop()
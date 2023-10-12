from tkinter import *
base=Tk()
base.geometry("500x500")
base.title("Registraction form")

base.maxsize(500,500)
lb0= Label(base, text="Registraction form", width=40, font=("arial",12),fg="red")
lb0.place(x=50, y=70)

lb1 = Label(base, text="Enter name", width=40, font=("arial",12),fg="red")
lb1.place(x=20, y=120)
en1=Entry(base)
en1.place(x=200, y=120)

lb2= Label(base, text="Enter Email", width=10, font=("arial",12))
lb2.place(x=19, y=160)
en2=Entry(base)
en2.place(x=200, y=160)

lb3= Label(base, text="Enter ConatatNo", width=13, font=("arial",12))
lb3.place(x=19, y=200)
en3=Entry(base)
en3.place(x=200, y=200)


lb4= Label(base, text="Select Gender", width=15, font=("arial",12))
lb4.place(x=5, y=240)
vars=IntVar()
Radiobutton(base, text="Male", padx=5,variable=vars,value=1).place(x=180, y=240)
Radiobutton(base, text="FeMale", padx=10,variable=vars,value=2).place(x=240, y=240)

lb5= Label(base,text="Enter Password",width=13,font=("arial",12))
lb5.place(x=19, y=300)
en5= Entry(base, show='*')
en5.place(x=200, y=300)

lb6= Label(base,text="Re-Enter Password",width=15,font=("arial",12))
lb6.place(x=21, y=340)
en6= Entry(base, show='*')
en6.place(x=200, y=340)

Button(base,text="Register", width=10).place(x=200, y=400)
base.mainloop()





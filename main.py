from tkinter import*

kal = Tk()
kal.title('Kalkulator')
operator = ""
Text_Input = StringVar()

txtDisplay = Entry(kal, font=("FreeSerif", 20), textvariable=Text_Input, bd=20, insertwidth=4, bg="CadetBlue2", justify="right").grid(columnspan=5)

btn7=Button(kal, padx=14, bd=7, fg="black", font=("FreeSerif", 20), text="7").grid(row=1, column=0)
btn8=Button(kal, padx=14, bd=7, fg="black", font=("FreeSerif", 20), text="8").grid(row=1, column=1)
btn9=Button(kal, padx=14, bd=7, fg="black", font=("FreeSerif", 20), text="9").grid(row=1, column=2)

btn_dodawanie=Button(kal, padx=14, bd=7, fg="black", font=("FreeSerif", 20), text="+").grid(row=1, column=3)
kal.mainloop()
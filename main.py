from tkinter import*

def btnClick(numbers):
    global operator
    operator += str(numbers)
    Text_Input.set(operator)

def btnWynik():
    global operator
    suma=str(eval(operator))
    Text_Input.set(suma)
    operator=""

def btnComma():
    global operator
    comma=float(operator)
    Text_Input.set(comma)

def btnClearDisplay():
    global operator
    operator=""
    Text_Input.set("")

kal = Tk()
kal.title('Kalkulator')
operator = ""
Text_Input = StringVar()

txtDisplay = Entry(kal, font=("FreeSerif", 20), textvariable=Text_Input, bd=20, insertwidth=8, bg="CadetBlue2", justify="right").grid(columnspan=5)
#row 1
btn7=Button(kal, padx=15, pady=12, bd=7, fg="black", font=("FreeSerif", 20), text="7", bg="CadetBlue2", command=lambda:btnClick(7)).grid(row=1, column=0)
btn8=Button(kal, padx=15, pady=12, bd=7, fg="black", font=("FreeSerif", 20), text="8", bg="CadetBlue2", command=lambda:btnClick(8)).grid(row=1, column=1)
btn9=Button(kal, padx=15, pady=12, bd=7, fg="black", font=("FreeSerif", 20), text="9", bg="CadetBlue2", command=lambda:btnClick(9)).grid(row=1, column=2)
btn_dzielenie=Button(kal, padx=16, pady=12, bd=7, fg="black", font=("FreeSerif", 20), text="/", command=lambda:btnClick("/")).grid(row=1, column=3)


#row 2

btn4=Button(kal, padx=15, pady=12, bd=7, fg="black", font=("FreeSerif", 20), text="4", bg="CadetBlue2", command=lambda:btnClick(4)).grid(row=2, column=0)
btn5=Button(kal, padx=15, pady=12, bd=7, fg="black", font=("FreeSerif", 20), text="5", bg="CadetBlue2", command=lambda:btnClick(5)).grid(row=2, column=1)
btn6=Button(kal, padx=15, pady=12, bd=7, fg="black", font=("FreeSerif", 20), text="6", bg="CadetBlue2", command=lambda:btnClick(6)).grid(row=2, column=2)

btn_mnozenie=Button(kal, padx=14, pady=12, bd=7, fg="black", font=("FreeSerif", 20), text="*", command=lambda:btnClick("*")).grid(row=2, column=3)


#row 3
btn1=Button(kal, padx=15, pady=12, bd=7, fg="black", font=("FreeSerif", 20), text="1", bg="CadetBlue2", command=lambda:btnClick(1)).grid(row=3, column=0)
btn2=Button(kal, padx=15, pady=12, bd=7, fg="black", font=("FreeSerif", 20), text="2", bg="CadetBlue2", command=lambda:btnClick(2)).grid(row=3, column=1)
btn3=Button(kal, padx=15, pady=12, bd=7, fg="black", font=("FreeSerif", 20), text="3", bg="CadetBlue2", command=lambda:btnClick(3)).grid(row=3, column=2)

btn_odejmowanie=Button(kal, padx=15, pady=12, bd=7, fg="black", font=("FreeSerif", 20), text="-", command=lambda:btnClick("-")).grid(row=3, column=3)

#row 4

btn_clear=Button(kal, padx=13,pady=12, bd=7, fg="black", font=("FreeSerif", 20), text="C", bg="CadetBlue2", command=btnClearDisplay).grid(row=4, column=0)
btn0=Button(kal, padx=15, pady=12, bd=7, fg="black", font=("FreeSerif", 20), text="0", bg="CadetBlue2", command=lambda:btnClick(0)).grid(row=4, column=1)
btn_comma=Button(kal, padx=17, pady=12, bd=7, fg="black", font=("FreeSerif", 20), text=",", bg="CadetBlue2", command=lambda:btnComma()).grid(row=4, column=2)
btn_dodawanie=Button(kal, padx=11, pady=12, bd=7, fg="black", font=("FreeSerif", 20), text="+", command=lambda:btnClick("+")).grid(row=4, column=3)

#row 5

btn_wynik=Button(kal, padx=137, pady=12, bd=7, fg="black", font=("FreeSerif", 20), text="=", bg="CadetBlue2", command=btnWynik).grid(row=5, column=0, columnspan=4)





kal.mainloop()
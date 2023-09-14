from tkinter import *

window= Tk()
window.title("Distance Converter")
# window.minsize(width=300, height=200)
window.config(padx=25, pady=25)

equal= Label(text="is equal to")
equal.grid(column=0, row=1)
# equal.config(padx=25, pady=25)

text_input= Entry(width=15)
text_input.grid(column=1, row=0)
# text_input.config(padx=5, pady=25)

km_result= Label(text="0")
km_result.grid(column=1, row=1)

def calculate():
    miles= float(text_input.get())
    km=round(miles* 1.609)
    km_result.config(text= f"{km}")
    
    

button= Button(text="Calculate", command=calculate)
button.grid(column=1, row=2)

Miles= Label(text="Miles")
Miles.grid(column=2, row=0)

Km= Label(text="Km")
Km.grid(column=2, row=1)


window.mainloop()
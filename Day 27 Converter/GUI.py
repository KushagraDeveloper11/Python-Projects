from tkinter import *

window = Tk()
window.title("My first Tkinter")
window.minsize(width=500, height=400)
window.config(padx= 20, pady=20)

my_label= Label(text= "I love Tkinter", font= ("Arial", 16, "bold"))
my_label.grid(column=0, row=0)

my_label["text"]= "New text"
my_label.config(text="New Text")

def button_clicked():
    new_text= imp.get()
    my_label.config(text= new_text)

button= Button(text= "CLick Me", command=button_clicked)
button.grid(column=1, row=1)

imp= Entry(width=10)
imp.grid(column=4, row= 3)

new_button = Button(text="New")
new_button.grid(column=3, row=0)


window.mainloop()
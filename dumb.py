import tkinter, random

window= tkinter.Tk()
window.title("R U DUMB")
window.geometry("300x300")

def no():
    btn2.place(x=random.randint(40, 200), y=random.randint(130, 200))
def si():
    frm["text"]="I knew it :p"
    btn.destroy()
    btn2.destroy()
frm = tkinter.Label(window, text="Are You Dumb!", font="Arial 30 bold") 
frm.place(x=10, y=30)

btn=tkinter.Button(window, text="Yes", padx=5, pady=5, relief=tkinter.GROOVE, font="Arial 20", command=si)
btn.place(x=30, y=130)

btn2=tkinter.Button(window, text="No", padx=5, pady=5, relief=tkinter.GROOVE, font="Arial 20", command=no)
btn2.place(x=200, y=130)

window.mainloop()

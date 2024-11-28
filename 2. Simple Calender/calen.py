# ======================= Imoprts =======================

from tkinter import *
from tkinter import ttk
import calendar

# ===================== Main Program ====================

def show_calen():
    calen = Toplevel(root)
    calen.title("Calendar")
    calen.geometry("550x600")
    calen.config(bg= "tan")
    calen.resizable(0,0)

    fetch_year = int(E1.get())
    content = calendar.calendar(fetch_year)
    cal_year = Label(calen, text = content, font = "Consolas 10 bold")
    cal_year.grid(row = 5, column = 1, padx = 20)
    calen.mainloop()

# ===================== GUI Creation ====================

root = Tk()
root.title("Calendar")
root.config(bg= "coral")
root.geometry("550x450")
root.resizable(0,0)

# ======================= Labels =======================

L1 = Label(root, text= "Calendar",font= ("Eras Light ITC",35, "bold"))
L1.config(bg = 'coral', fg= 'black')
L1.place(x=180, y= 20 )

L2 = Label(root, text= "Select Your Year",font= ("Bradley Hand ITC",35, "bold"))
L2.config(bg = 'coral', fg= 'black')
L2.place(x=100, y= 100 )

# ======================= Entry =======================

E1 = Entry(root,font = ("Eras Light ITC",20,'bold'))
E1.place(x= 120, y=170)

# ======================= Button =======================

B1= Button(root,text= "Show",font=("Eras Light ITC",25),command=show_calen,bg= "spring green",fg= 'black')
B1.place(x= 160,y= 250)

B2= Button(root,text= "Exit",font=("Eras Light ITC",25),command=exit,bg= "red",fg= 'black')
B2.place(x= 300,y= 250)

root.mainloop()

# ==================== End of Program ====================
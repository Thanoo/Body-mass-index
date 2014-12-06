'''
Body mass index v.1
NUI & TUKTA
'''
from Tkinter import *

class Menu():
    '''Class Menu'''
    def __init__(self):
        '''Main'''
        self.master = Tk()
        self.master.geometry("500x400+500+100")
        self.master.title("Body mass index")
        self.master.resizable(width=FALSE, height=FALSE)
        
        #Background Color
        self.master.configure(bg = '#ffffff')
        
        #Logo
        Label(self.master, bg = '#ffffff', text = 'Body mass index', font=("Helvetica", 30)).place(x=110, y=30)

        #Menu Button
        #Calculate Your BMI
        '''b1 = PhotoImage(file = "testbut.gif")'''
        b_menu1 = Button(self.master, text = 'Calculate Your BMI', bg = '#ffffff', command = self.calculate, font=("Helvetica", 15), relief=GROOVE)
        b_menu1.place(x=30, y=145, width = 190)
        #About
        b_menu2 = Button(self.master, text = 'About', bg = '#ffffff', command = self.about, font=("Helvetica", 15), relief=RIDGE)
        b_menu2.place(x=30, y=200, width = 190)
        #Exit
        b_menu3 = Button(self.master, text = 'Exit', bg = '#ffffff', command = self.exits, font=("Helvetica", 15), relief=RIDGE)
        b_menu3.place(x=30, y=255, width = 190)
        
        self.master.mainloop()
    def calculate(self):
        self.master.destroy()
        Calculate()
    def about(self):
        self.master.destroy()
        About()
    def exits(self):
        self.master.destroy()

class Calculate():
    def __init__(self):
        self.master = Tk()
        self.master.geometry("700x600+500+100")
        self.master.title("Body mass index ~ Calculate Your BMI")
        self.master.resizable(width=FALSE, height=FALSE)
        
        #Background Color
        self.master.configure(bg = '#ffffff')
        
        #Logo
        logo = Label(self.master, text='Calculate Your BMI', font=("Helvetica", 30), bg = '#ffffff')
        logo.place(x=30, y=20)

        #Back to menu
        b_back = Button(self.master, text="Menu", width=10, command=self.back, relief=RIDGE)
        b_back.place(x=30, y=550)

        #Exit
        b_exit = Button(self.master, text = 'Exit', command = self.exits, relief=RIDGE)
        b_exit.place(x=130, y=550, width = 80)

        #Input Weight & String
        self.weight = Entry(self.master)
        self.weight.place(x=130, y=403)
        label_weight = Label(self.master, text='weight (Kg)', font=("Helvetica", 12), bg = '#ffffff')
        label_weight.place(x=30, y=400)

        #Input Height & Sttring
        self.height = Entry(self.master)
        self.height.place(x=130, y=443)
        label_heigh = Label(self.master, text='height (Cm)', font=("Helvetica", 12), bg = '#ffffff')
        label_heigh.place(x=30, y=440)

        #Calculate Button
        cal = Button(self.master, text="Calculate", width=10, command=self.callback, relief=RIDGE)
        cal.place(x=110, y=480)

        #BMI label
        self.update = StringVar()
        label_bmi = Label(self.master, font=("Helvetica", 20), background='#ffffff', textvariable=self.update)
        label_bmi.place(x=160, y=345)
        label_you = Label(self.master, text='Your BMI is : ', font=("Helvetica", 15), background= '#ffffff')
        label_you.place(x=30, y=350)
        self.label_bmi1 = Label(self.master, text = '0',font=("Helvetica", 20), background='#ffffff')
        self.label_bmi1.place(x=160,y=345)

        #BMI Table
        table = PhotoImage(file = "image/bmi_table.gif")
        self.table = Label(self.master, image=table, bg='#ffffff')
        self.table.place(x=30,y=100)
        self.table1 = PhotoImage(file = "image/bmi_table(under).gif")
        self.table2 = PhotoImage(file = "image/bmi_table(normal).gif")
        self.table3 = PhotoImage(file = "image/bmi_table(risk).gif")
        self.table4 = PhotoImage(file = "image/bmi_table(moder).gif")
        self.table5 = PhotoImage(file = "image/bmi_table(sev).gif")

        self.master.mainloop()
    def callback(self):
        weight = int(self.weight.get())
        height = int(self.height.get())
        bmi = weight/((height/100.0)**2)
        self.update.set('%.2f' % bmi)
        self.label_bmi1.place_forget()
        if bmi < 18.5:
            table = Label(self.master, image=self.table1, bg='#ffffff')
            table.place(x=30,y=100)
        elif bmi >= 18.5 and bmi <= 22.9:
            table = Label(self.master, image=self.table2, bg='#ffffff')
            table.place(x=30,y=100)
        elif bmi >= 23 and bmi <= 24.9:
            table = Label(self.master, image=self.table3, bg='#ffffff')
            table.place(x=30,y=100)
        elif bmi >= 25 and bmi <= 29.9:
            table = Label(self.master, image=self.table4, bg='#ffffff')
            table.place(x=30,y=100)
        else:
            table = Label(self.master, image=self.table5, bg='#ffffff')
            table.place(x=30,y=100)
 
    def back(self):
        self.master.destroy()
        Menu()

    def exits(self):
        self.master.destroy()
class About():
    def __init__(self):
        self.maste = Tk()
        self.maste.geometry("500x400+500+100")
        self.maste.title("Body mass index")
        self.maste.resizable(width=FALSE, height=FALSE)
        
Menu()  

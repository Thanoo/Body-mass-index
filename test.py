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
        self.master.geometry("500x400+500+100")
        self.master.title("Body mass index ~ Calculate Your BMI")
        '''self.master.resizable(width=FALSE, height=FALSE)'''
        
        #Background Color
        self.master.configure(bg = '#ffffff')
        
        #Logo
        logo = Label(self.master, text='Calculate Your BMI', font=("Helvetica", 30), bg = '#ffffff')
        logo.place(x=10, y=10)

        #Input Weight & String
        self.weight = Entry(self.master)
        self.weight.place(x=110, y=105)
        label_weight = Label(self.master, text='weight (Kg)', font=("Helvetica", 12), bg = '#ffffff')
        label_weight.place(x=10, y=100)

        #Input Height & Sttring
        self.height = Entry(self.master)
        self.height.place(x=110, y=155)
        label_heigh = Label(self.master, text='height (Cm)', font=("Helvetica", 12), bg = '#ffffff')
        label_heigh.place(x=10, y=150)

        #Calculate Button
        cal = Button(self.master, text="Calculate", width=10, command=self.callback, relief=RIDGE)
        cal.place(x=70, y=200)

        #BMI label
        self.update = StringVar()
        label_bmi = Label(self.master, font=("Helvetica", 20), background='#ffffff', textvariable=self.update)
        label_you = Label(self.master, text='Your BMI is : ', font=("Helvetica", 15), background= '#ffffff')
        label_you.place(x=10, y=270)
        label_bmi.place(x=140, y=265)
        
        
        self.master.mainloop()

        
    def callback(self):
        weight = int(self.weight.get())
        height = int(self.height.get())
        bmi = weight/((height/100.0)**2)
        self.update.set('%.2f' % bmi)

        
class About():
    def __init__(self):
        self.maste = Tk()
        self.maste.geometry("500x400+500+100")
        self.maste.title("Body mass index")
        self.maste.resizable(width=FALSE, height=FALSE)
        
Menu()  

# -*- coding: utf-8 -*-
#!/usr/bin/python
'''
Body mass index v.2
NUI & TUKTA
'''
from Tkinter import *
import sqlite3
import tkMessageBox
class Menu():
      '''Class Menu'''
      def __init__(self):
            '''Main'''
            self.master = Tk()
            self.master.geometry("500x400+500+100")
            self.master.title("Body mass index")
            self.master.resizable(width=FALSE, height=FALSE)
        
            #Background Color
            self.master.configure(bg = '#b0e0e6')
            
            #Logo
            Label(self.master, fg = 'white', bg = '#b0e0e6', text = 'Body mass index', font = ("Helvetica", 30)).place(x=110, y=30)

            #Menu Button
            #Calculate Your BMI
            '''b1 = PhotoImage(file = "testbut.gif")'''
            b_menu1 = Button(self.master, text = 'Calculate Your BMI', bg = '#cef590', command = self.calculate, font = ("Helvetica", 15), relief = GROOVE)
            b_menu1.place(x=30, y=145, width = 190)
            #About
            b_menu2 = Button(self.master, text = 'About', bg = '#cef590', command = self.about, font = ("Helvetica", 15), relief = RIDGE)
            b_menu2.place(x=30, y=200, width = 190)
            #Exit
            b_menu3 = Button(self.master, text = 'Exit', bg = '#cef590', command = self.exits, font = ("Helvetica", 15), relief = RIDGE)
            b_menu3.place(x=30, y=255, width=190)
        
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
            self.master.geometry("670x600+400+70")
            self.master.title("Body mass index ~ Calculate Your BMI")
            #self.master.resizable(width=FALSE, height=FALSE)
        
            #Background Color
            self.master.configure(bg = '#b0e0e6')
            
            #Logo
            logo = Label(self.master, text = 'Calculate Your BMI', font = ("Helvetica", 30), bg = '#b0e0e6')
            logo.place(x=30, y=20)

            #Back to menu
            b_back = Button(self.master, text = "Menu", width = 10, command = self.back, relief = RIDGE)
            b_back.place(x=35, y=550)

            #Exit
            b_exit = Button(self.master, text = 'Exit', command = self.exits, relief = RIDGE)
            b_exit.place(x=135, y=550, width=80)

            #Change mode
            R1 = Button(self.master, text = "Standard", command = self.standard)
            R1.place(x=35, y=90)
            R2 = Button(self.master, text = "Metric", command = self.metric)
            R2.place(x=105, y=90)

            #Input Frame
            self.frame = Frame(self.master, width = 300, height = 130, bg = 'green')
            self.metric()


            #Result BMI label
            self.update = StringVar()
            label_bmi = Label(self.master, text = '0', font = ("Helvetica", 20), background = '#b0e0e6', textvariable = self.update)
            label_bmi.place(x=500, y=95)
            label_you = Label(self.master, text = 'Your BMI is : ', font = ("Helvetica", 15), background = '#b0e0e6')
            label_you.place(x=375, y=100)
            self.label_zero = Label(self.master, text = '0', font = ("Helvetica", 20), background = '#b0e0e6')
            self.label_zero.place(x=500, y=95)

            #BMI Table
            table = PhotoImage(file = "image/bmi_table.gif")
            self.table = Label(self.master, image = table, bg = '#ffffff')
            self.table.place(x=30, y=270)
            self.table1 = PhotoImage(file = "image/bmi_table(under).gif")
            self.table2 = PhotoImage(file = "image/bmi_table(normal).gif")
            self.table3 = PhotoImage(file = "image/bmi_table(risk).gif")
            self.table4 = PhotoImage(file = "image/bmi_table(moder).gif")
            self.table5 = PhotoImage(file = "image/bmi_table(sev).gif")           

            #BMI Picture
            pic = PhotoImage(file = "image/normal.gif")
            Label(self.master, image = pic, bg = '#ffffff').place(x=375, y=150)
            self.pic1 = PhotoImage(file = "image/under.gif")
            self.pic2 = PhotoImage(file = "image/normal.gif")
            self.pic3 = PhotoImage(file = "image/risk.gif")
            self.pic4 = PhotoImage(file = "image/moder.gif")
            self.pic5 = PhotoImage(file = "image/sev.gif")

            self.master.mainloop()

      def metric(self):
            self.frame.destroy()
            self.frame = Frame(self.master, width = 300, height = 130, bg = '#b0e0e6')
            self.frame.place(x=30, y=130)
            #Input Label
            weight_label = Label(self.frame, text = 'weight', font = ("Helvetica", 12), bg = '#b0e0e6')
            weight_label.place(x=10, y=10)
            heigh_label = Label(self.frame, text = 'height', font = ("Helvetica", 12), bg = '#b0e0e6')
            heigh_label.place(x=10, y=50)
            #Input Weight
            self.weight_entry = Entry(self.frame, bg='#ffffff')
            self.weight_entry.place(x=65, y=13)
            Label(self.frame, text = 'kg', font = ("Helvetica", 12), bg = '#b0e0e6').place(x=190, y=12)
            Label(self.frame, text = 'cm', font = ("Helvetica", 12), bg = '#b0e0e6').place(x=190, y=50)
            #Input Height
            self.height_entry = Entry(self.frame, bg = '#ffffff')
            self.height_entry.place(x=65, y=54)
            cal = Button(self.frame, text="Calculate", width = 10, command = self.cal_metric, relief = RIDGE)
            cal.place(x=80, y=90)


      def standard(self):
            self.frame.destroy()
            #Input Weight
            self.frame = Frame(self.master, width = 300, height = 130, bg = '#b0e0e6')
            self.frame.place(x=30, y=130)
            self.weight_entry = Entry(self.frame, bg = '#ffffff')
            self.weight_entry.place(x=65, y=13)
            weight_label = Label(self.frame, text = 'weight', font = ("Helvetica", 12), bg = '#b0e0e6')
            weight_label.place(x=10, y=10)
            Label(self.frame, text = 'ft', font = ("Helvetica", 12), bg = '#b0e0e6').place(x=135, y=50)
            Label(self.frame, text = 'in', font = ("Helvetica", 12), bg = '#b0e0e6').place(x=237, y=50)
            Label(self.frame, text = 'lbs', font = ("Helvetica", 12), bg = '#b0e0e6').place(x=190, y=10)
            #Input Height
            self.height_ft_entry = Entry(self.frame, width = 10, bg = '#ffffff')
            self.height_ft_entry.place(x = 65, y = 54)
            self.height_in_entry = Entry(self.frame, width = 10, bg = '#ffffff')
            self.height_in_entry.place(x = 165, y = 54)
            heigh_label = Label(self.frame, text='height', font = ("Helvetica", 12), bg = '#b0e0e6')
            heigh_label.place(x=10, y=50)
            cal = Button(self.frame, text = "Calculate", width = 10, command = self.cal_standard, relief = RIDGE)
            cal.place(x=80, y=90)
      
      def cal_metric(self):
            try:
                  weight = float(self.weight_entry.get())
                  height = float(self.height_entry.get())
                  self.bmi = weight/((height/100.0)**2)
                  self.update.set('%.2f' % self.bmi)
                  self.label_zero.place_forget()
                  self.bmi_table()
            except:
                  tkMessageBox.showerror('Error!', 'Please insert integer or float only')

      def cal_standard(self):
            try:
                  weight = float(self.weight_entry.get())
                  height_in = (float(self.height_ft_entry.get())*12) + float(self.height_in_entry.get())
                  self.bmi = (weight*703.0)/(height_in)**2
                  self.update.set('%.2f' % self.bmi)
                  self.label_zero.place_forget()
                  self.bmi_table()
            except:
                  tkMessageBox.showerror('Error!', 'Please insert integer or float only')
                  
      def bmi_table(self):
            self.table.place_forget()
            if self.bmi < 18.5:
                  table = Label(self.master, image = self.table1, bg = '#ffffff')
                  table.place(x=30, y=270)
                  pic = Label(self.master, image = self.pic1, bg = '#ffffff')
                  pic.place(x=375, y=150)
            elif self.bmi >= 18.5 and self.bmi < 23:
                  table = Label(self.master, image = self.table2, bg = '#ffffff')
                  table.place(x=30, y=270)
                  pic = Label(self.master, image = self.pic2, bg = '#ffffff')
                  pic.place(x=375, y=150)
            elif self.bmi >= 23 and self.bmi < 25:
                  table = Label(self.master, image = self.table3, bg = '#ffffff')
                  table.place(x=30, y=270)
                  pic = Label(self.master, image = self.pic3, bg = '#ffffff')
                  pic.place(x=375, y=150)
            elif self.bmi >= 25 and self.bmi < 30:
                  table = Label(self.master, image = self.table4, bg = '#ffffff')
                  table.place(x=30, y=270)
                  pic = Label(self.master, image = self.pic4, bg = '#ffffff')
                  pic.place(x=375, y=150)
            else:
                  table = Label(self.master, image = self.table5, bg = '#ffffff')
                  table.place(x=30, y=270)
                  pic = Label(self.master, image = self.pic5, bg = '#ffffff')
                  pic.place(x=375, y=150)

 
      def back(self):
            self.master.destroy()
            Menu()

      def exits(self):
            self.master.destroy()
            
class About():
      def __init__(self):
            self.master = Tk()
            self.master.geometry("500x400+500+100")
            self.master.title("Body mass index")
            self.master.resizable(width = FALSE, height = FALSE)

            #Background Color
            self.master.configure(bg = '#b0e0e6')

            #about
            text_a = Message(self.master, text="\nProvider", width=450, font = ("Helvetica", 20), background = '#b0e0e6')
            text_b = Message(self.master, text="\nThanoo    Chomyad     57070051"
                            "\nBusakorn Yuangngoen 57070062", width=450, font = ("Helvetica", 15), background = '#b0e0e6')
            text_a.pack()
            text_b.pack()

            #Menu
            f_menu = Button(self.master, text = 'Menu', bg = '#cef590', command = self.menu, font = ("Helvetica", 15), relief = RIDGE)
            f_menu.place(x=60, y=340, width=190)

            #Exit
            b_menu3 = Button(self.master, text = 'Exit', bg = '#cef590', command = self.exits, font = ("Helvetica", 15), relief = RIDGE)
            b_menu3.place(x=270, y=340, width=190)

            self.master.mainloop()

      def menu(self):
            self.master.destroy()
            Menu()

      def exits(self):
            self.master.destroy()
        
Menu()  

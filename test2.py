# -*- coding: utf-8 -*-
'''
Body mass index v.2
NUI & TUKTA
'''
from Tkinter import *
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
            Label(self.master, fg = '#FFFFFF', bg = '#b0e0e6', text = 'Body mass index', font=("Helvetica", 30)).place(x=110, y=30)

            #Menu Button
            #Calculate Your BMI
            '''b1 = PhotoImage(file = "testbut.gif")'''
            b_menu1 = Button(self.master, text = 'Calculate Your BMI', bg = '#FFFF99', command = self.calculate, font=("Helvetica", 15), relief=GROOVE)
            b_menu1.place(x=30, y=145, width = 190)
            #About
            b_menu2 = Button(self.master, text = 'About', bg = '#FFFF99', command = self.about, font=("Helvetica", 15), relief=RIDGE)
            b_menu2.place(x=30, y=200, width = 190)
            #Exit
            b_menu3 = Button(self.master, text = 'Exit', bg = '#FFFF99', command = self.exits, font=("Helvetica", 15), relief=RIDGE)
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
            self.master.geometry("715x600+400+70")
            self.master.title("Body mass index ~ Calculate Your BMI")
            self.master.resizable(width=FALSE, height=FALSE)
        
            #Background Color
            self.master.configure(bg = '#FFE4B5')
            
        
            #Logo
            logo = Label(self.master, text='Calculate Your BMI', font=("Helvetica", 30), bg = '#FFE4B5')
            logo.place(x=30, y=20)

            #Back to menu
            b_back = Button(self.master, text="Menu", width=10, command=self.back, relief=RIDGE)
            b_back.place(x=30, y=550)

            #Exit
            b_exit = Button(self.master, text = 'Exit', command = self.exits, relief=RIDGE)
            b_exit.place(x=130, y=550, width = 80)

            #Change mode
            R1 = Button(self.master, text="Standard", command=self.standard)
            R1.place(x=30, y=68)
            R2 = Button(self.master, text="Metric", command=self.metric)
            R2.place(x=100, y=68)

            #Input Weight
            self.frame = Frame(self.master, width=300, height=130, bg='green')
            self.frame.place(x=30,y=400)
            self.frame.destroy()
            #Input Weight
            self.frame = Frame(self.master, width=300, height=130, bg='#FFE4B5')
            self.frame.place(x=30,y=400)
            self.weight_entry = Entry(self.frame, bg='#FFFFFF')
            self.weight_entry.place(x=65, y=13)
            weight_label = Label(self.frame, text='weight', font=("Helvetica", 12), bg = '#FFE4B5')
            weight_label.place(x=10, y=10)
            Label(self.frame, text='kg', font=("Helvetica", 12), bg = '#FFE4B5').place(x=190, y=12)
            Label(self.frame, text='cm', font=("Helvetica", 12), bg = '#FFE4B5').place(x=190, y=50)
            #Input Height
            self.height_entry = Entry(self.frame, bg='#FFFFFF')
            self.height_entry.place(x=65, y=54)
            heigh_label = Label(self.frame, text='height', font=("Helvetica", 12), bg = '#FFE4B5')
            heigh_label.place(x=10, y=50)

            #Calculate Button
            cal = Button(self.master, text="Calculate", width=10, command=self.cal_metric, relief=RIDGE)
            cal.place(x=130, y=490)

            #BMI label
            self.update = StringVar()
            label_bmi = Label(self.master, font=("Helvetica", 20), background='#FFE4B5', textvariable=self.update)
            label_bmi.place(x=160, y=345)
            label_you = Label(self.master, text='Your BMI is : ', font=("Helvetica", 15), background= '#FFE4B5')
            label_you.place(x=30, y=350)
            self.label_bmi1 = Label(self.master, text = '0',font=("Helvetica", 20), background='#FFE4B5')
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
            

            #BMI detail
            #self.detail = PhotoImage(file = "image/1.gif")
            #self.box = Label(self.master, image=self.detail, bg='red')
            #self.box.place(x=350, y=100)
            #self.detail.set('        congratulations! Your healthy weight is well worth the effort. It reduces your risk of serious \
            #               health conditions such as high blood pressure, heart disease, stroke and diabetes. To maintain a healthy weight : \
            #               \t - Embrace healthy eating by choosing a variety of nutrient-rich foods, including fruits, vegetables and \
            #              whole grains and small amounts of energy-dense foods like olive oil, nuts and dried fruits.\
            #              \t')
            self.master.mainloop()

      def metric(self):
            self.frame.destroy()
            #Input Weight
            self.frame = Frame(self.master, width=300, height=130, bg='#FFE4B5')
            self.frame.place(x=30,y=400)
            self.weight_entry = Entry(self.frame, bg='#ffffff')
            self.weight_entry.place(x=65, y=13)
            weight_label = Label(self.frame, text='weight', font=("Helvetica", 12), bg = '#FFE4B5')
            weight_label.place(x=10, y=10)
            Label(self.frame, text='kg', font=("Helvetica", 12), bg = '#FFE4B5').place(x=190, y=12)
            Label(self.frame, text='cm', font=("Helvetica", 12), bg = '#FFE4B5').place(x=190, y=50)
            #Input Height
            self.height_entry = Entry(self.frame, bg='#ffffff')
            self.height_entry.place(x=65, y=54)
            heigh_label = Label(self.frame, text='height', font=("Helvetica", 12), bg = '#FFE4B5')
            heigh_label.place(x=10, y=50)
            cal = Button(self.master, text="Calculate", width=10, command=self.cal_metric, relief=RIDGE)
            cal.place(x=130, y=490)


      def standard(self):
            self.frame.destroy()
            #Input Weight
            self.frame = Frame(self.master, width=300, height=130, bg='#FFE4B5')
            self.frame.place(x=30,y=400)
            self.weight_entry = Entry(self.frame, bg='#FFFFFF')
            self.weight_entry.place(x=65, y=13)
            weight_label = Label(self.frame, text='weight', font=("Helvetica", 12), bg = '#FFE4B5')
            weight_label.place(x=10, y=10)
            Label(self.frame, text='ft', font=("Helvetica", 12), bg = '#FFE4B5').place(x=135, y=50)
            Label(self.frame, text='in', font=("Helvetica", 12), bg = '#FFE4B5').place(x=237, y=50)
            Label(self.frame, text='lbs', font=("Helvetica", 12), bg = '#FFE4B5').place(x=190, y=10)
            #Input Height
            self.height_ft_entry = Entry(self.frame, width=10, bg='#ffffff')
            self.height_ft_entry.place(x=65, y=54)
            self.height_in_entry = Entry(self.frame, width=10, bg='#ffffff')
            self.height_in_entry.place(x=165, y=54)
            heigh_label = Label(self.frame, text='height', font=("Helvetica", 12), bg = '#FFE4B5')
            heigh_label.place(x=10, y=50)
            cal = Button(self.master, text="Calculate", width=10, command=self.cal_standard, relief=RIDGE)
            cal.place(x=130, y=490)
      
      def cal_metric(self):
            try:
                  weight = float(self.weight_entry.get())
                  height = float(self.height_entry.get())
                  self.bmi = weight/((height/100.0)**2)
                  self.update.set('%.2f' % self.bmi)
                  self.label_bmi1.place_forget()
                  self.bmi_table()
            except:
                  tkMessageBox.showerror('Error!', 'Error')

      def cal_standard(self):
          try:
                weight = float(self.weight_entry.get())
                height_in = (float(self.height_ft_entry.get())*12) + float(self.height_in_entry.get())
                self.bmi = (weight*703.0)/(height_in)**2
                self.update.set('%.2f' % self.bmi)
                self.label_bmi1.place_forget()
                self.bmi_table()
          except:
                tkMessageBox.showerror('Error!', 'Error')
                  
      def bmi_table(self):
            if self.bmi < 18.5:
                  table = Label(self.master, image=self.table1, bg='#ffffff')
                  table.place(x=30,y=100)
                  #self.detail = PhotoImage(file = "image/1.gif")
                  #self.box = Label(self.master, image=self.detail, bg='#ffffff')
                  #self.box.place(x=350, y=100)
            elif self.bmi >= 18.5 and self.bmi <= 22.9:
                  table = Label(self.master, image=self.table2, bg='#ffffff')
                  table.place(x=30,y=100)
                  #self.detail = PhotoImage(file = "image/2.gif")
                  #self.box = Label(self.master, image=self.detail, bg='#ffffff')
                  #self.box.place(x=350, y=100)
            elif self.bmi >= 23 and self.bmi <= 24.9:
                  table = Label(self.master, image=self.table3, bg='#ffffff')
                  table.place(x=30,y=100)
                  #self.detail = PhotoImage(file = "image/3.gif")
                  #self.box = Label(self.master, image=self.detail, bg='#ffffff')
                  #self.box.place(x=350, y=100)
            elif self.bmi >= 25 and self.bmi <= 29.9:
                  table = Label(self.master, image=self.table4, bg='#ffffff')
                  table.place(x=30,y=100)
                  #self.detail = PhotoImage(file = "image/4.gif")
                  #self.box = Label(self.master, image=self.detail, bg='#ffffff')
                  #self.box.place(x=350, y=100)
            else:
                  table = Label(self.master, image=self.table5, bg='#ffffff')
                  table.place(x=30,y=100)
                  #self.detail = PhotoImage(file = "image/4.gif")
                  #self.box = Label(self.master, image=self.detail, bg='#ffffff')
                  #self.box.place(x=350, y=100)
 
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
            self.master.resizable(width=FALSE, height=FALSE)

            #Background Color
            self.master.configure(bg = '#FFFACD')

            #about
            text_a = Message(self.master, text="\n\tThe body mass index (BMI), or Quetelet index, is a measure "
                        "of relative weight based on an individual's mass and height.\n\n"
                        "\tA frequent use of the BMI is to assess how much an individual's body weight "
                        "departs from what is normal or desirable for a person of his or her height. "
                        "The weight excess or deficiency may, in part, be accounted for by body fat "
                        "(adipose tissue) although other factors such as muscularity also affect BMI "
                        "significantly (see discussion below and overweight). The WHO regards a BMI of "
                        "less than 18.5 as underweight and may indicate malnutrition, an eating disorder, "
                        "or other health problems, while a BMI greater than 25 is considered overweight and "
                        "above 30 is considered obese. These ranges of BMI values are valid only as statistical "
                        "categories\n\n", width=450, font=("Helvetica", 12), background = '#FFFACD')
            text_a.pack()

            #Menu
            f_menu = Button(self.master, text = 'Menu', bg = '#FFDEAD', command = self.menu, font=("Helvetica", 15), relief=RIDGE)
            f_menu.place(x=60, y=340, width = 190)

            #Exit
            b_menu3 = Button(self.master, text = 'Exit', bg = '#FFDEAD', command = self.exits, font=("Helvetica", 15), relief=RIDGE)
            b_menu3.place(x=270, y=340, width = 190)

            self.master.mainloop()

      def menu(self):
            self.master.destroy()
            Menu()

      def exits(self):
            self.master.destroy()
        
Menu()  

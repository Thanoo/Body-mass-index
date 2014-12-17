'''
Body mass index
NUI & TUKTA
'''
from Tkinter import *
import tkMessageBox
class Menu():
      '''Class Menu'''
      def __init__(self):
            '''Main'''
            self.master = Tk()
            self.master.geometry("500x400+500+150")
            self.master.title("Body mass index")
            self.master.configure(bg = '#8fc9ff')
            self.master.wm_iconbitmap('image/icon.ico')
            self.master.resizable(width=FALSE, height=FALSE)
            
            #Logo
            logo = PhotoImage(file = "image/Logo.gif")
            Label(self.master, fg = 'white', bg = '#8fc9ff', image = logo, font = ("Helvetica", 30)).place(x=83, y=30)

            #Menu Button
            #Calculate Your BMI
            cal = PhotoImage(file = "image/menu1.gif")
            b_menu1 = Button(self.master, image = cal, command = self.calculate, relief = FLAT)
            b_menu1.place(x=135, y=150, width=230, height=40)
            #About
            about = PhotoImage(file = "image/menu2.gif")
            b_menu2 = Button(self.master, image= about, command = self.about, relief = FLAT)
            b_menu2.place(x=135, y=210, width=230, height=40)
            #Exit
            exits = PhotoImage(file = "image/exit.gif")
            b_menu3 = Button(self.master, image= exits, command = self.exits, relief = FLAT)
            b_menu3.place(x=135, y=270, width=230, height=42)
        
            self.master.mainloop()
      def calculate(self):
            '''Go to calculate'''
            self.master.destroy()
            Calculate()
      def about(self):
            '''Go to about'''
            self.master.destroy()
            About()
      def exits(self):
            '''Exit program'''
            self.master.destroy()

class Calculate():
      def __init__(self):
            self.master = Tk()
            self.master.geometry("650x590+400+70")
            self.master.title("Body mass index ~ Calculate Your BMI")
            self.master.configure(bg = '#8fc9ff')
            self.master.wm_iconbitmap('image/icon.ico')
            self.master.resizable(width=FALSE, height=FALSE)
            #Logo
            logo2 = PhotoImage(file = "image/Logo2.gif")
            logo = Label(self.master, image = logo2, bg = '#8fc9ff')
            logo.place(x=150, y=10)

            #Back to menu
            back_pic = PhotoImage(file = "image/menu.gif")
            b_back = Button(self.master, image = back_pic, command = self.back, relief = FLAT)
            b_back.place(x=70, y=540, width=103, height=33)

            #Exit
            exit_pic = PhotoImage(file = "image/exit1.gif")
            b_exit = Button(self.master, image = exit_pic, command = self.exits, relief = FLAT)
            b_exit.place(x=185, y=540, width=103, height=33)

            #backgound Calculator
            back = PhotoImage(file = "image/back.gif")
            Label(self.master, image = back, bg = '#8fc9ff').place(x=20, y=120)

            #Change mode
            r1_photo = PhotoImage(file = "image/standard.gif")
            r1 = Button(self.master, image = r1_photo, command = self.standard, relief = FLAT)
            r1.place(x=35, y=110, width=70, height=35)
            r2_photo = PhotoImage(file = "image/metric.gif")
            r2 = Button(self.master, image = r2_photo, command = self.metric, relief = FLAT)
            r2.place(x=105, y=110, width=70, height=35)

            #Input Frame
            self.frame = Frame(self.master, width = 300, height = 130, bg = '#8fc9ff')
            self.standard()

            #Result BMI label
            back2 = PhotoImage(file = "image/back2.gif")
            Label(self.master, image = back2, fg = 'white', background = '#8fc9ff').place(x=355, y=118)
            result = PhotoImage(file = "image/result.gif")
            label_you = Label(self.master, image = result, fg = 'white', background = '#6594c0')
            label_you.place(x=375, y=138)
            self.update = StringVar()
            label_bmi = Label(self.master, text = '0', fg = 'white', font = ("Helvetica", 17), bg = '#6594c0', textvariable = self.update)
            label_bmi.place(x=517, y=145)
            self.label_zero = Label(self.master, text = '0', fg = 'white', font = ("Helvetica", 17), bg = '#6594c0')
            self.label_zero.place(x=517, y=145)
            

            #BMI Table
            table = PhotoImage(file = "image/bmi_table.gif")
            self.table = Label(self.master, image = table, bg = '#8fc9ff')
            self.table.place(x=30, y=300)
            self.table1 = PhotoImage(file = "image/bmi_table(under).gif")
            self.table2 = PhotoImage(file = "image/bmi_table(normal).gif")
            self.table3 = PhotoImage(file = "image/bmi_table(risk).gif")
            self.table4 = PhotoImage(file = "image/bmi_table(moder).gif")
            self.table5 = PhotoImage(file = "image/bmi_table(sev).gif")           

            #BMI Picture
            pic = PhotoImage(file = "image/normal.gif")
            Label(self.master, image = pic, bg = '#6594c0').place(x=400, y=180)
            self.pic1 = PhotoImage(file = "image/under.gif")
            self.pic2 = PhotoImage(file = "image/normal.gif")
            self.pic3 = PhotoImage(file = "image/risk.gif")
            self.pic4 = PhotoImage(file = "image/moder.gif")
            self.pic5 = PhotoImage(file = "image/sev.gif")
            self.master.mainloop()

      def metric(self):
            '''metric input frame'''
            self.frame.destroy()
            self.frame = Frame(self.master, width = 300, height = 130, bg = '#6893ba')
            self.frame.place(x=30, y=150)
            #Input Label
            weight_label = Label(self.frame, text = 'weight', fg = 'white', font = ("Helvetica", 12), bg = '#6893ba')
            weight_label.place(x=10, y=10)
            heigh_label = Label(self.frame, text = 'height', fg = 'white', font = ("Helvetica", 12), bg = '#6893ba')
            heigh_label.place(x=10, y=50)
            #Input Weight
            self.weight_entry = Entry(self.frame, fg= 'white', bg='#7cafde', relief = FLAT)
            self.weight_entry.place(x=65, y=13)
            Label(self.frame, text = 'kg', fg = 'white', font = ("Helvetica", 12), bg = '#6893ba').place(x=190, y=12)
            Label(self.frame, text = 'cm', fg = 'white', font = ("Helvetica", 12), bg = '#6893ba').place(x=190, y=50)
            #Input Height
            self.height_entry = Entry(self.frame, fg= 'white', bg='#7cafde', relief = FLAT)
            self.height_entry.place(x=65, y=54)
            self.cal_pic = PhotoImage(file = "image/calculate.gif")
            cal = Button(self.frame, image = self.cal_pic, command = self.cal_metric, relief = FLAT)
            cal.place(x=100, y=95, width=103, height=33)


      def standard(self):
            '''standard input frame'''
            self.frame.destroy()
            self.frame = Frame(self.master, width = 300, height = 130, bg = '#6893ba')
            self.frame.place(x=30, y=150)
            #Input Label
            weight_label = Label(self.frame, text = 'weight', fg = 'white', font = ("Helvetica", 12), bg = '#6893ba')
            weight_label.place(x=10, y=10)
            heigh_label = Label(self.frame, text='height', fg = 'white', font = ("Helvetica", 12), bg = '#6893ba')
            heigh_label.place(x=10, y=50)
            #Input Weight
            self.weight_entry = Entry(self.frame, fg= 'white', bg='#7cafde', relief = FLAT)
            self.weight_entry.place(x=65, y=13)
            Label(self.frame, text = 'ft', fg = 'white', font = ("Helvetica", 12), bg = '#6893ba').place(x=120, y=50)
            Label(self.frame, text = 'in', fg = 'white', font = ("Helvetica", 12), bg = '#6893ba').place(x=190, y=50)
            Label(self.frame, text = 'lbs', fg = 'white', font = ("Helvetica", 12), bg = '#6893ba').place(x=190, y=12)
            #Input Height
            self.height_ft_entry = Entry(self.frame, width = 8, fg= 'white', bg='#7cafde', relief = FLAT)
            self.height_ft_entry.place(x = 65, y = 54)
            self.height_in_entry = Entry(self.frame, width = 8, fg= 'white', bg='#7cafde', relief = FLAT)
            self.height_in_entry.place(x = 137, y = 54)
            self.cal_pic = PhotoImage(file = "image/calculate.gif")
            cal = Button(self.frame, image = self.cal_pic, command = self.cal_standard, relief = FLAT)
            cal.place(x=100, y=95, width=103, height=33)
      
      def cal_metric(self):
            '''Calculate metric mode'''
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
            '''Calculate standard mode'''
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
            '''All table and Picture'''
            self.table.place_forget()
            if self.bmi < 18.5:
                  table = Label(self.master, image = self.table1, bg = '#8fc9ff')
                  pic = Label(self.master, image = self.pic1, bg = '#6594c0')
                  table.place(x=30, y=300)
                  pic.place(x=400, y=180)
            elif self.bmi >= 18.5 and self.bmi < 23:
                  table = Label(self.master, image = self.table2, bg = '#8fc9ff')
                  pic = Label(self.master, image = self.pic2, bg = '#6594c0')
                  table.place(x=30, y=300)
                  pic.place(x=400, y=180)
            elif self.bmi >= 23 and self.bmi < 25:
                  table = Label(self.master, image = self.table3, bg = '#8fc9ff')
                  pic = Label(self.master, image = self.pic3, bg = '#6594c0')
                  table.place(x=30, y=300)
                  pic.place(x=400, y=180)
            elif self.bmi >= 25 and self.bmi < 30:
                  table = Label(self.master, image = self.table4, bg = '#8fc9ff')
                  pic = Label(self.master, image = self.pic4, bg = '#6594c0')
                  table.place(x=30, y=300)
                  pic.place(x=400, y=180)
            else:
                  table = Label(self.master, image = self.table5, bg = '#8fc9ff')
                  pic = Label(self.master, image = self.pic5, bg = '#6594c0')
                  table.place(x=30, y=300)
                  pic.place(x=400, y=180)

 
      def back(self):
            '''Go to menu'''
            self.master.destroy()
            Menu()

      def exits(self):
            '''Exit program'''
            self.master.destroy()
            
class About():
      def __init__(self):
            self.master = Tk()
            self.master.geometry("500x400+500+150")
            self.master.title("Body mass index")
            self.master.wm_iconbitmap('image/icon.ico')
            self.master.resizable(width = FALSE, height = FALSE)

            #about
            page = PhotoImage(file = "image/about.gif")
            text_a = Label(self.master, image = page, bg = '#8fc9ff')
            text_a.place(x=0, y=0)

            #Menu
            menu_pic = PhotoImage(file = "image/menu3.gif")
            f_menu = Button(self.master, image = menu_pic, bg = '#8fc9ff', command = self.menu, relief = FLAT)
            f_menu.place(x=20, y=340, width=230, height=40)

            #Exit
            exit_pic = PhotoImage(file = "image/exit.gif")
            b_menu3 = Button(self.master, image = exit_pic, bg = '#8fc9ff', command = self.exits, relief = FLAT)
            b_menu3.place(x=255, y=340, width=230, height=40)

            self.master.mainloop()
      def menu(self):
            '''Go to menu'''
            self.master.destroy()
            Menu()
      def exits(self):
            '''Exit program'''
            self.master.destroy()
Menu()

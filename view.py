import tkinter as tk 
import tkinter.ttk as ttk
from tkinter import *
from controller import * 
import tkinter.messagebox

class Aplication:
     def __init__(self):
         self.window    = tk.Tk()
         self.obj = PasswordController() #objeto de la clase Password Controller
         self.random_password = tk.StringVar() #creamos una variable del tipo string guarda la contrasena
         self.selected = tk.StringVar() #creamos variable que se encargue de guardar la seleccion de fortaleza
         self.labelvar = tk.StringVar()

         self.window.title("PASSWORD GENERATOR")
         self.window.geometry("550x340+675+300")
         self.window.resizable(0, 0)
         self.window.iconbitmap("./images/lock.ico")
            #Creacion de un canvas 
         self.canvas = Canvas(self.window, width = 520, height= 30)
         self.canvas.place(x= 15, y= 35)
         self.canvas.create_line(0,25,520,25, fill = 'white')

         self.t_style = ttk.Style()
         self.t_style.configure("BW.Tlabel", foreground='white', font=('Helvetica', 24))
         self.s_style = ttk.Style()
         self.s_style.configure("WB.TLabel", foreground='white', font=("Helvetica", 14))
         self.sp_style = ttk.Style()
         self.s_style.configure("GB.TLabel", foreground='blue', font=("Helvetica", 16))

         self.label1 = ttk.Label(self.window, text="Password Generator", style="BW.TLabel").place(x = 200, y = 10)
         
         
         self.rdbtn1 = ttk.Radiobutton(self.window, text="Unica", variable=self.selected, value=0).place(x = 50, y = 100)
        

         #En la sig linea se especifica el cuadro de texto que nos muestra la contrasena

         self.txtbox = ttk.Entry(self.window, textvariable = self.random_password, state= 'disable', justify = "center", font = ("Helvetica", 24)).place(x= 90, y = 180)

            #Boton de generar         
         self.btn2 = ttk.Button(text = "Generate", command = self.generate).place(x= 237, y = 280)

         self.window.mainloop()

     def generate(self):
         try:
             #self.labelvar.set("")
             #self.random_password.set("")
             value = int(self.selected.get()) #obtenemos el valor de la variable(0,1,2...) pero solo en este caso solo hay un valor
             self.random_password.set(self.obj.process_password(value))
         except:
             tkinter.messagebox.showwarning("Error", "Select a lenght")


Aplication = Aplication()




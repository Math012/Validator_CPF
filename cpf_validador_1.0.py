from tkinter import *
root = Tk()

class MainApplication():
    def __init__(self):
        self.root = root
        self.Window()
        self.WindowElements()
        root.mainloop()

    def Window(self):
        self.root.title("CPF VALIDATOR")
        self.root.configure(background='#A9A9A9')        
        self.root.geometry("300x500")
        self.root.maxsize(width=300, height=500)
        self.root.minsize(width=300, height=500)

    def WindowElements(self):
        #CREATE LABEL AND ENTRY

        #LABEL AND ENTRY THAT GET INPUT THE CPF WRITED BY USER
        self.lb_cpf = Label(self.root, text="Informe o CPF que deseja validar", bg='#A9A9A9', font=('arial',13,'bold'))
        self.lb_cpf.place(relx=0.05, rely=0.02)

        self.entry_cpf = Entry(self.root, font=('arial',15,'bold'), bd=5)
        self.entry_cpf.place(relx=0.01, rely=0.08, relwidth=0.97, relheight=0.08)

        #CREATING LABEL FOR ADD MORE INFORMATION TO USER, LIKE FORMAT THE NUMBER
        self.lb_info1 = Label(self.root, text="*Informe o CPF sem espaços ou sinais.", font=('arial',10), bg='#A9A9A9')
        self.lb_info1.place(relx=0.01, rely=0.20) 
        self.lb_info1 = Label(self.root, text="*Verifique se os 11 números foram informados.", font=('arial',9), bg='#A9A9A9')
        self.lb_info1.place(relx=0.01, rely=0.28)
        self.lb_info1 = Label(self.root, text="*Para evitar erros, antes de realizar uma consulta", font=('arial',9), bg='#A9A9A9')
        self.lb_info1.place(relx=0.01, rely=0.36)
        self.lb_info1 = Label(self.root, text="clique em reset.", font=('arial',9), bg='#A9A9A9')
        self.lb_info1.place(relx=0.01, rely=0.39)

        #CREATE THE BUTTON START AND RESET
        self.bt_start = Button(self.root, text="Validar CPF", bg='#A9A9A9', font=('arial',8), bd=4, command=self.Calc)
        self.bt_start.place(relx=0.02, rely=0.49, relwidth=0.4, relheight=0.1)

        self.reset = Button(self.root, text="Reset", bg='#A9A9A9', font=('arial',8), bd=4, command=self.Reset)
        self.reset.place(relx=0.50, rely=0.49, relwidth=0.4, relheight=0.1)

        # CREATE THE ENTRY AND LABEL RELATED THE RESULT OF PROGRAM
        self.lb_cpf = Label(self.root, text="Resultado", bg='#A9A9A9', font=('arial',13,'bold'))
        self.lb_cpf.place(relx=0.05, rely=0.70)

        self.entry_result = Entry(self.root, font=('arial',15,'bold'), bd=5)
        self.entry_result.place(relx=0.01, rely=0.75, relwidth=0.97, relheight=0.08)          

    def Calc(self):
        self.cpf = self.entry_cpf.get()
        self.lista = []
        for c in range(0, 9):
            self.lista.append(int(self.cpf[c]))

        self.a8 = self.lista[8] * 2
        self.a7 = self.lista[7] * 3
        self.a6 = self.lista[6] * 4
        self.a5 = self.lista[5] * 5
        self.a4 = self.lista[4] * 6
        self.a3 = self.lista[3] * 7
        self.a2 = self.lista[2] * 8
        self.a1 = self.lista[1] * 9
        self.a0 = self.lista[0] * 10

        self.total = (self.a0 + self.a1 + self.a2 + self.a3 + self.a4 + self.a5 + self.a6 + self.a7 + self.a8)           
        self.total = self.total % 11
        self.total = 11 - self.total

        if self.total >= 10:
            total = 0

        self.lista.append(int(self.cpf[9]))
        if self.lista[9] == self.total:
            self.b9 = self.lista[9] * 2
            self.b8 = self.lista[8] * 3
            self.b7 = self.lista[7] * 4
            self.b6 = self.lista[6] * 5
            self.b5 = self.lista[5] * 6
            self.b4 = self.lista[4] * 7
            self.b3 = self.lista[3] * 8
            self.b2 = self.lista[2] * 9
            self.b1 = self.lista[1] * 10
            self.b0 = self.lista[0] * 11            

            self.total2 = (self.b0 + self.b1 + self.b2 + self.b3 + self.b4 + self.b5 + self.b6 + self.b7 + self.b8 + self.b9) 
            self.total2 = self.total2 %  11
            self.total2 = 11 - self.total2
            if self.total2 >= 10:
                self.total2 = 0
            self.lista.append(int(self.cpf[10]))
            if self.lista[10] == self.total2:
                self.entry_result.insert(0,f"CPF VALIDO")
            else:
                self.entry_result.insert(0,f"CPF INVALIDO")                    
        else:
            self.entry_result.insert(0,f"CPF INVALIDO")
            
        pass 
    
    def Reset(self):
        self.entry_cpf.delete(0, END)
        self.entry_result.delete(0, END)
MainApplication()
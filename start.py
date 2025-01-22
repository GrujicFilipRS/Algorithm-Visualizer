import customtkinter
from load_fonts import tkinter_fonts

class StartPage:
    def __init__(self) -> None:
        pass

    def show(self) -> None:
        font = tkinter_fonts()
        window = customtkinter.CTk()
        window.title('Algorithm visualizer')
        window.geometry('800x600')

        title_label = customtkinter.CTkLabel(window, text='Algorithm visualizer', font=('Jaldi', 36))
        title_label.place(relx=0.5, rely=0.1, anchor='center')
        
        window.mainloop()
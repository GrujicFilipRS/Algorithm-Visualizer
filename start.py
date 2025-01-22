import customtkinter
from load_fonts import tkinter_fonts
from abc import abstractmethod
from display_handler import handle_pygame

class Option:
    options = []

    def __init__(self, id, name, description):
        self.id = id
        self.name = name
        self.description = description
        Option.options.append(self)
    
    @abstractmethod
    def find(id) -> 'Option':
        for option in Option.options:
            if option.id == int(id):
                return option
        else: return False

class StartPage:
    def __init__(self) -> None:
        Option(0, 'BFS', 'ddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd'),
        Option(1, 'DFS', 'DFS Desc'),
        Option(2, 'test 1', 'test 1 Desc'),

    def show(self) -> None:
        font = tkinter_fonts()
        window = customtkinter.CTk()
        window.title('Algorithm visualizer')
        window.geometry('800x700')

        title_label = customtkinter.CTkLabel(window, text='Algorithm visualizer', font=('Jaldi', 36))
        title_label.place(relx=0.5, rely=0.07, anchor='center')
        
        choose_alg_label = customtkinter.CTkLabel(window, text='Choose algorithm', font=('Jaldi', 24))
        choose_alg_label.place(relx=0.2, rely=0.2, anchor='center')

        modify_start_label = customtkinter.CTkLabel(window, text='Modify start position', font=('Jaldi', 24))
        modify_start_label.place(relx=0.5, rely=0.2, anchor='center')

        go_btn = customtkinter.CTkButton(window, text='See algorithm', font=('Jaldi', 20), command=lambda: handle_pygame(int(self.selected_option.get()), None))
        go_btn.place(relx=0.85, rely=0.5, anchor='center')

        self.selected_option = customtkinter.StringVar(value='0')
        for i, option in enumerate(Option.options):
            self.alg_option = customtkinter.CTkRadioButton(window, text=option.name, variable=self.selected_option,
                                                      value=str(option.id), font=('Jaldi', 17), command=self.change_option)
            self.alg_option.place(relx=0.16, rely=0.25+0.04*i, anchor='center')
        
        self.desc_label = customtkinter.CTkLabel(window, text=Option.find(0).description, font=('Jaldi', 14), wraplength=250)
        self.desc_label.place(relx=0.2, rely=0.97, anchor='s')

        window.mainloop()
    
    def change_option(self):
        self.desc_label.configure(text=Option.find(self.selected_option.get()).description)
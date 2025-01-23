import customtkinter
from load_fonts import tkinter_fonts
from abc import abstractmethod
from display_handler import handle_pygame

class Option:
    options = []

    def __init__(self, id, name, description, startpos):
        self.id = id
        self.name = name
        self.description = description
        self.startpos = startpos
        Option.options.append(self)
    
    @abstractmethod
    def find(id) -> 'Option':
        for option in Option.options:
            if option.id == int(id):
                return option
        else: return False

class StartPage:
    def __init__(self) -> None:
        Option(0, 'BFS', 'Breadth-First Search (BFS) is a graph traversal algorithm that explores nodes level by level, starting from a source node, using a queue to ensure the shortest path in unweighted graphs.', '[\n\t[0, 0, 1, 1, 0],\n\t[0, 0, 1, 1, 0],\n\t[1, 1, 0, 1, 1],\n\t[1, 1, 1, 0, 0]\n]'),
        Option(1, 'DFS', 'DFS Desc', 'DFS start pos'),
        Option(2, 'test 1', 'test 1 Desc', 'test1 start pos'),

    def handle_transition(self):
        startpos = self.start_pos_txtbox.get(1.0, customtkinter.END)
        status = handle_pygame(int(self.selected_option.get()), startpos)
        print(f'Status code: {status}')

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

        self.start_pos_value = customtkinter.StringVar(value=f'{Option.find(0).startpos}')

        go_btn = customtkinter.CTkButton(window, text='See algorithm', font=('Jaldi', 20), command=self.handle_transition)
        go_btn.place(relx=0.85, rely=0.5, anchor='center')

        self.selected_option = customtkinter.StringVar(value='0')
        for i, option in enumerate(Option.options):
            self.alg_option = customtkinter.CTkRadioButton(window, text=option.name, variable=self.selected_option,
                                                      value=str(option.id), font=('Jaldi', 17), command=self.change_option)
            self.alg_option.place(relx=0.16, rely=0.25+0.04*i, anchor='center')
        
        self.desc_label = customtkinter.CTkLabel(window, text=Option.find(0).description, font=('Jaldi', 12), wraplength=250)
        self.desc_label.place(relx=0.2, rely=0.97, anchor='s')

        self.start_pos_txtbox = customtkinter.CTkTextbox(window, font=('Jaldi', 14))
        self.start_pos_txtbox.place(relx=0.5, rely=0.37, anchor='center')

        self.change_option()

        window.mainloop()
    
    def change_option(self):
        self.desc_label.configure(text=Option.find(self.selected_option.get()).description)
        self.start_pos_txtbox.delete(1.0, customtkinter.END)
        self.start_pos_txtbox.insert(customtkinter.END, str(Option.find(int(self.selected_option.get())).startpos))
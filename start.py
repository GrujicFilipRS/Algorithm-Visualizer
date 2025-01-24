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
        Option(1, 'Bubble sort', 'Bubble sort repeatedly compares and swaps adjacent elements to sort a list. Smaller elements "bubble" up, while larger ones sink down. It\'s simple but slow for large datasets.', '[\n\t5, 4, 7, 3, 2, 1, 8, 6\n]'),
        Option(2, 'Insertion sort', 'Insertion sort builds a sorted list one element at a time by picking the next element and inserting it into its correct position among the already sorted elements.', '[\n\t5, 4, 7, 3, 2, 1, 8, 6\n]'),

    def handle_transition(self):
        startpos = self.start_pos_txtbox.get(1.0, customtkinter.END)
        status = handle_pygame(int(self.selected_option.get()), startpos)
        if status == 0:
            self.error_code_txt.configure(text='')
        elif status == 1:
            self.error_code_txt.configure(text='Invalid format of starting position')
        elif status == 2:
            self.error_code_txt.configure(text='Incorrect type/format of starting position')

    def show(self) -> None:
        tkinter_fonts()
        window = customtkinter.CTk()
        window.after(201, lambda :window.iconbitmap('./resources/icon.ico'))
        window.title('Algorithm visualizer')
        window.resizable(False, False)
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
            self.alg_option.place(relx=0.1, rely=0.25+0.04*i, anchor='w')
        
        self.desc_label = customtkinter.CTkLabel(window, text=Option.find(0).description, font=('Jaldi', 12), wraplength=250)
        self.desc_label.place(relx=0.2, rely=0.97, anchor='s')

        self.start_pos_txtbox = customtkinter.CTkTextbox(window, font=('Jaldi', 14))
        self.start_pos_txtbox.place(relx=0.5, rely=0.37, anchor='center')

        default_start_btn = customtkinter.CTkButton(window, text='Default', font=('Jaldi', 16), width=75, height=30, command=self.start_to_default)
        default_start_btn.place(relx=0.5, rely=0.55, anchor='center')

        self.error_code_txt = customtkinter.CTkLabel(window, text='', font=('Jaldi', 14), text_color='darkred', wraplength=250)
        self.error_code_txt.place(relx=0.5, rely=0.58, anchor='n')

        self.change_option()

        window.mainloop()
    
    def start_to_default(self):
        self.start_pos_value.set(Option.find(self.selected_option.get()).startpos)
        self.start_pos_txtbox.delete(1.0, customtkinter.END)
        self.start_pos_txtbox.insert(customtkinter.END, self.start_pos_value.get())

    def change_option(self):
        self.desc_label.configure(text=Option.find(self.selected_option.get()).description)
        self.start_pos_txtbox.delete(1.0, customtkinter.END)
        self.start_pos_txtbox.insert(customtkinter.END, str(Option.find(int(self.selected_option.get())).startpos))
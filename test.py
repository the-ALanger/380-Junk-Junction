import tkinter as tk

class MyApp(tk.Frame):

    def __init__(self, root):
    
        self.color1 = 'darkred'
        self.color2 = 'brown'

        super().__init__(
            root,
            
        )

        self.main_frame = self

        self.main_frame.pack(fill=tk.BOTH, expand=True)
        self.main_frame.columnconfigure(0, weight=1)
        self.main_frame.rowconfigure(0, weight=1)

        self.load_main_widgets()

    def load_main_widgets(self):
        self.create_page_container
        self.create_pager()

    def create_page_container(self):
        self.create_page_container - tk.Frame(
            self.main_frame,
            background=self.color1
        )

        

    def create_pager(self):
        pass


root = tk.Tk()
root.title('My App')
root.geometry('800x600')
root.resizable(width=False, height=False)
my_app_instance = MyApp(root)
root.mainloop()

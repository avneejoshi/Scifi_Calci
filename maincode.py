import tkinter as tk
import math

class ScientificCalculator(tk.Tk):
    def _init_(self):
        super()._init_()
        self.title("Scientific Calculator")
        self.geometry("400x500")
        self.result_var = tk.StringVar()
        self.create_widgets()

    def create_widgets(self):
        entry = tk.Entry(self, textvariable=self.result_var, font=('Arial', 18), bd=10, relief=tk.GROOVE, justify=tk.RIGHT)
        entry.grid(row=0, column=0, columnspan=5, pady=10, padx=10, sticky='nsew')

        buttons = [
            '7', '8', '9', '/',
            '4', '5', '6', '*',
            '1', '2', '3', '-',
            '.', '0', '+', '=',
            'sin', 'cos', 'tan', 'sqrt',
            '^', '%', 'C', '⌫'            
        ]

        row_val = 1
        col_val = 0

        for button in buttons:
            tk.Button(self, text=button, padx=20, pady=20, font=('Arial', 12), command=lambda btn=button: self.on_button_click(btn)).grid(row=row_val, column=col_val, padx=5, pady=5, sticky='nsew')
            col_val += 1
            if col_val > 3:
                col_val = 0
                row_val += 1

        # Configure row and column weights
        for i in range(1, 6):
            self.grid_rowconfigure(i, weight=1)
            self.grid_columnconfigure(i, weight=1)

    def on_button_click(self, button):
        current_value = self.result_var.get()

        if button == '=':
            try:
                result = eval(current_value)
                self.result_var.set(result)
            except Exception as e:
                self.result_var.set("Error")
        elif button == 'C':
            self.result_var.set('')
        elif button == '⌫':
            self.result_var.set(current_value[:-1])
        elif button == 'sqrt':
            self.result_var.set(math.sqrt(float(current_value)))
        elif button == '^':
            self.result_var.set(current_value + '')
        elif button in ('sin', 'cos', 'tan'):
            angle = eval(current_value)
            if button == 'sin':
                result = math.sin(math.radians(angle))
            elif button == 'cos':
                result = math.cos(math.radians(angle))
            elif button == 'tan':
                result = math.tan(math.radians(angle))
            self.result_var.set(result)
        else:
            self.result_var.set(current_value + str(button))

if _name_ == "_main_":
    app = ScientificCalculator()
    app.mainloop()

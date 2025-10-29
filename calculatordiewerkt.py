#!/usr/bin/env python3

import math
import tkinter as tk
import tkinter.messagebox as messbox

#KLEURTJES voor de rekenmachine
zwart = "#0c0c0c"
secondary_paars = "#5e0062"
primary_roze = "#7c1d5a"
grijsblauw = "#336997"
font_roze = "#af158c"

# Global variable
expr = ""

# Functies knoppen
def press(key):
    global expr
    expr += str(key)
    display.set(expr)

def equal():
    global expr

    try:
        result = str(eval(expr))
        display.set(result)
        expr = ""
    except:
        if '/0' in expr:
            display.set("Undefined: /0 in expr (press 'clear' first)")
            expr = ""
        else:
            display.set("error, (press 'clear' first)")
            expr = ""


def clear():
    global expr
    expr = ""
    display.set("")

def delete():
    global expr
    expr = expr[:-1]
    display.set(expr)

# Main Program:

if __name__ == "__main__":

    # Window
    mother = tk.Tk()
    mother.geometry("400x400")
    mother.title("Maarten's Scientific Calculator")

    # Top Frame
    top_frame = tk.Frame(mother, background = zwart)

    # Entry Field
    display = tk.StringVar()

    entryfield_label = tk.Entry(top_frame, background = secondary_paars, foreground = zwart, font = "Ubuntu 20",
                                borderwidth = 10, relief = "sunken", textvariable = display)

    # Knoppen Frame
    bottom_frame = tk.Frame(mother, background = zwart)

    knop_7 = tk.Button(bottom_frame, text = "7", background = primary_roze, foreground = grijsblauw,
                       font = "Ubuntu 20 bold", command = lambda: press(7))
    knop_8 = tk.Button(bottom_frame, text = "8", background = primary_roze, foreground = grijsblauw,
                       font = "Ubuntu 20 bold", command = lambda: press(8))
    knop_9 = tk.Button(bottom_frame, text = "9", background = primary_roze, foreground = grijsblauw,
                       font = "Ubuntu 20 bold", command = lambda: press(9))

    knop_4 = tk.Button(bottom_frame, text = "4", background = primary_roze, foreground = grijsblauw,
                       font = "Ubuntu 20 bold", command = lambda: press(4))
    knop_5 = tk.Button(bottom_frame, text = "5", background = primary_roze, foreground = grijsblauw,
                       font = "Ubuntu 20 bold", command = lambda: press(5))
    knop_6 = tk.Button(bottom_frame, text = "6", background = primary_roze, foreground = grijsblauw,
                       font = "Ubuntu 20 bold", command = lambda: press(6))

    knop_1 = tk.Button(bottom_frame, text = "1", background = primary_roze, foreground = grijsblauw,
                       font = "Ubuntu 20 bold", command = lambda: press(1))
    knop_2 = tk.Button(bottom_frame, text = "2", background = primary_roze, foreground = grijsblauw,
                       font = "Ubuntu 20 bold", command = lambda: press(2))
    knop_3 = tk.Button(bottom_frame, text = "3", background = primary_roze, foreground = grijsblauw,
                       font = "Ubuntu 20 bold", command = lambda: press(3))

    knop_0 = tk.Button(bottom_frame, text = "0", background = primary_roze, foreground = grijsblauw,
                       font = "Ubuntu 20 bold", command = lambda: press(0))
    knop_decimaal = tk.Button(bottom_frame, text = ".", background = secondary_paars, foreground = font_roze,
                              font = "Ubuntu 20 bold", command = lambda: press("."))

    knop_min = tk.Button(bottom_frame, text = "-", background = secondary_paars, foreground = font_roze,
                         font = "Ubuntu 20 bold", command = lambda: press("-"))
    knop_plus = tk.Button(bottom_frame, text = "+", background = secondary_paars, foreground = font_roze,
                          font = "Ubuntu 20 bold", command = lambda: press("+"))
    knop_enter = tk.Button(bottom_frame, text = "enter", background = secondary_paars, foreground = font_roze,
                           font = "Ubuntu 20 bold", command = equal)

    knop_vermenigvuldigen = tk.Button(bottom_frame, text = "*", background = secondary_paars, foreground = font_roze,
                                      font = "Ubuntu 20 bold", command = lambda: press("*"))
    knop_delen = tk.Button(bottom_frame, text = "/", background = secondary_paars, foreground = font_roze,
                           font = "Ubuntu 20 bold", command = lambda: press("/"))

    knop_macht = tk.Button(bottom_frame, text = "^", background = secondary_paars, foreground = font_roze,
                           font = "Ubuntu 20 bold", command = lambda: press("**"))
    knop_delete = tk.Button(bottom_frame, text = "del", background = grijsblauw, foreground = zwart,
                            font = "Ubuntu 20 bold", command = delete)
    knop_clear = tk.Button(bottom_frame, text = "clear", background = grijsblauw, foreground = zwart,
                           font = "Ubuntu 20 bold", command = clear)
    knop_haakjes_open = tk.Button(bottom_frame, text = "(", background = secondary_paars, foreground = font_roze,
                           font = "Ubuntu 20 bold", command = lambda: press("("))
    knop_haakjes_sluiten = tk.Button(bottom_frame, text = ")", background = secondary_paars, foreground = font_roze,
                           font = "Ubuntu 20 bold", command = lambda: press(")"))


    # Knoppen Frame Layout
    bottom_frame.columnconfigure(0, weight = 1, uniform = 'fred')
    bottom_frame.columnconfigure(1, weight = 1, uniform = 'fred')
    bottom_frame.columnconfigure(2, weight = 1, uniform = 'fred')
    bottom_frame.columnconfigure(3, weight = 1, uniform = 'fred')
    bottom_frame.rowconfigure(0, weight = 1, uniform = 'fred')
    bottom_frame.rowconfigure(1, weight = 1, uniform = 'fred')
    bottom_frame.rowconfigure(2, weight = 1, uniform = 'fred')
    bottom_frame.rowconfigure(3, weight = 1, uniform = 'fred')
    bottom_frame.rowconfigure(4, weight = 1, uniform = 'fred')
    bottom_frame.rowconfigure(5, weight = 1, uniform = 'fred')

    # Layout van de knoppen

    knop_haakjes_open.grid(row = 0, column = 0, sticky = 'nsew', pady = 5, padx = 5)
    knop_haakjes_sluiten.grid(row = 0, column = 1, sticky = 'nsew', pady = 5, padx = 5)
    knop_delete.grid(row = 0, column = 2, sticky = 'nsew', pady = 5, padx = 5)
    knop_clear.grid(row = 0, column = 3, sticky = 'nsew', pady = 5, padx = 5)

    knop_macht.grid(row = 1, column = 0, sticky = 'nsew', pady = 5, padx = 5)
    knop_delen.grid(row = 1, column = 1, sticky = 'nsew', pady = 5, padx = 5)
    knop_vermenigvuldigen.grid(row = 1, column = 2, sticky = 'nsew', pady = 5, padx = 5)
    knop_min.grid(row = 1, column = 3, sticky = 'nsew', pady = 5, padx = 5)

    knop_7.grid(row = 2, column = 0, sticky = 'nsew', pady = 5, padx = 5)
    knop_8.grid(row = 2, column = 1, sticky = 'nsew', pady = 5, padx = 5)
    knop_9.grid(row = 2, column = 2, sticky = 'nsew', pady = 5, padx = 5)
    knop_plus.grid(row = 2, column = 3, rowspan = 2, sticky = 'nsew', pady = 5, padx = 5)

    knop_4.grid(row = 3, column = 0, sticky = 'nsew', pady = 5, padx = 5)
    knop_5.grid(row = 3, column = 1, sticky = 'nsew', pady = 5, padx = 5)
    knop_6.grid(row = 3, column = 2, sticky = 'nsew', pady = 5, padx = 5)

    knop_1.grid(row = 4, column = 0, sticky = 'nsew', pady = 5, padx = 5)
    knop_2.grid(row = 4, column = 1, sticky = 'nsew', pady = 5, padx = 5)
    knop_3.grid(row = 4, column = 2, sticky = 'nsew', pady = 5, padx = 5)

    knop_0.grid(row = 5, column = 0, columnspan = 2, sticky = 'nsew', pady = 5, padx = 5)
    knop_decimaal.grid(row = 5, column = 2, sticky = 'nsew', pady = 5, padx = 5)
    knop_enter.grid(row = 4, column = 3, rowspan = 2, sticky = 'nsew', pady = 5, padx = 5)

    '''
    #Scientific Menu Frame
    wetenschappelijk_frame = tk.Frame(master = )

    # Wetenschappelijke Knoppen:
    knop_pi = tk.Button(wetenschappelijk_frame, text = "\u03C0")
    knop_e = tk.Button(wetenschappelijk_frame, text = "e")
    knop_log = tk.Button(wetenschappelijk_frame, text = "log")
    knop_ln = tk.Button(wetenschappelijk_frame, text = "ln")
    knop_fac = tk.Button(wetenschappelijk_frame, text = "x!")

    knop_mean = tk.Button(wetenschappelijk_frame, text = "mean(x)")
    knop_sinus = tk.Button(wetenschappelijk_frame, text = "sin")
    knop_cosinus = tk.Button(wetenschappelijk_frame, text = "cos")
    knop_tangens = tk.Button(wetenschappelijk_frame, text = "tan")
    knop_negatief = tk.Button(wetenschappelijk_frame, text = "(-)")

    knop_pro1000 = tk.Button(wetenschappelijk_frame, text = "\u2030")
    knop_arcsinus = tk.Button(wetenschappelijk_frame, text = "sin-1")
    knop_arccos = tk.Button(wetenschappelijk_frame, text = "cos-1")
    knop_arctan = tk.Button(wetenschappelijk_frame, text = "tan-1")
    knop_pro100 = tk.Button(wetenschappelijk_frame, text = "%")

    knop_exp = tk.Button(wetenschappelijk_frame, text = "*10^x")
    knop_tot_de_macht = tk.Button(wetenschappelijk_frame, text = "x^y")
 
    knop_wortel = tk.Button(wetenschappelijk_frame, text = "\u221A")
    '''

    # Mother Layout
    entryfield_label.pack(side = "top", expand = False, fill = "x")
    top_frame.pack(side = "top", expand = False, fill = "both")
    bottom_frame.pack(side = "top", expand = True, fill = "both")

    # RUN
    mother.mainloop()


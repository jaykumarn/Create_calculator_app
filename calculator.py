# -*- coding: utf-8 -*-
from tkinter import Tk, END, Entry, N, E, S, W, Button
from tkinter import font
from tkinter import Label
from functools import partial
import math


def get_input(entry, argu):
    entry.insert(END, argu)


def backspace(entry):
    input_len = len(entry.get())
    entry.delete(input_len - 1)


def clear(entry):
    entry.delete(0, END)


def calc(entry):
    from math import sin, cos, tan, asin, acos, atan, radians, degrees, sqrt, log, log10, factorial, pi, e
    input_info = entry.get()
    try:
        # Replace display symbols with Python equivalents
        expression = input_info.strip()
        expression = expression.replace('π', str(math.pi))
        expression = expression.replace('√(', 'sqrt(')
        # Use placeholders for inverse trig to avoid double replacement
        expression = expression.replace('asin(', '_ASIN_(')
        expression = expression.replace('acos(', '_ACOS_(')
        expression = expression.replace('atan(', '_ATAN_(')
        # Regular trig (degrees input)
        expression = expression.replace('sin(', '_SIN_(')
        expression = expression.replace('cos(', '_COS_(')
        expression = expression.replace('tan(', '_TAN_(')
        # Now replace placeholders with actual functions
        expression = expression.replace('_ASIN_(', 'degrees(asin(')
        expression = expression.replace('_ACOS_(', 'degrees(acos(')
        expression = expression.replace('_ATAN_(', 'degrees(atan(')
        expression = expression.replace('_SIN_(', 'sin(radians(')
        expression = expression.replace('_COS_(', 'cos(radians(')
        expression = expression.replace('_TAN_(', 'tan(radians(')
        expression = expression.replace('log(', 'log10(')
        expression = expression.replace('ln(', 'log(')
        expression = expression.replace('!(', 'factorial(')
        # Replace 'e' only when standalone
        import re
        expression = re.sub(r'(?<![a-zA-Z])e(?![a-zA-Z])', str(math.e), expression)
        
        output = str(eval(expression))
        if output.endswith('.0'):
            output = output[:-2]
    except ZeroDivisionError:
        popupmsg("Cannot divide by 0!")
        output = ""
    except ValueError as e:
        popupmsg("Math error!\n" + str(e)[:20])
        output = ""
    except Exception:
        popupmsg("Invalid expression!")
        output = ""
    clear(entry)
    entry.insert(END, output)


def popupmsg(msg="Error"):
    popup = Tk()
    popup.resizable(0, 0)
    popup.geometry("150x100")
    popup.title("Alert")
    label = Label(popup, text=msg)
    label.pack(side="top", fill="x", pady=10)
    B1 = Button(popup, text="Okay", bg="#DDDDDD", command=popup.destroy)
    B1.pack()


def cal():
    root = Tk()
    root.title("Scientific Calculator")
    root.resizable(0, 0)

    entry_font = font.Font(size=15)
    entry = Entry(root, justify="right", font=entry_font, width=28)
    entry.grid(row=0, column=0, columnspan=6, sticky=N + W + S + E, padx=5, pady=5)

    cal_button_bg = '#FF6600'
    num_button_bg = '#4B4B4B'
    other_button_bg = '#DDDDDD'
    sci_button_bg = '#2E86AB'
    text_fg = '#FFFFFF'
    button_active_bg = '#C0C0C0'

    num_button = partial(Button, root, fg=text_fg, bg=num_button_bg,
                         padx=10, pady=3, activebackground=button_active_bg, width=4)
    cal_button = partial(Button, root, fg=text_fg, bg=cal_button_bg,
                         padx=10, pady=3, activebackground=button_active_bg, width=4)
    sci_button = partial(Button, root, fg=text_fg, bg=sci_button_bg,
                         padx=5, pady=3, activebackground=button_active_bg, width=4)

    # Row 1: Scientific functions
    Button(root, text='sin', fg=text_fg, bg=sci_button_bg, padx=5, pady=3, width=4,
           command=lambda: get_input(entry, 'sin('), activebackground=button_active_bg).grid(row=1, column=0, pady=2)
    Button(root, text='cos', fg=text_fg, bg=sci_button_bg, padx=5, pady=3, width=4,
           command=lambda: get_input(entry, 'cos('), activebackground=button_active_bg).grid(row=1, column=1, pady=2)
    Button(root, text='tan', fg=text_fg, bg=sci_button_bg, padx=5, pady=3, width=4,
           command=lambda: get_input(entry, 'tan('), activebackground=button_active_bg).grid(row=1, column=2, pady=2)
    Button(root, text='log', fg=text_fg, bg=sci_button_bg, padx=5, pady=3, width=4,
           command=lambda: get_input(entry, 'log('), activebackground=button_active_bg).grid(row=1, column=3, pady=2)
    Button(root, text='ln', fg=text_fg, bg=sci_button_bg, padx=5, pady=3, width=4,
           command=lambda: get_input(entry, 'ln('), activebackground=button_active_bg).grid(row=1, column=4, pady=2)
    Button(root, text='√', fg=text_fg, bg=sci_button_bg, padx=5, pady=3, width=4,
           command=lambda: get_input(entry, '√('), activebackground=button_active_bg).grid(row=1, column=5, pady=2)

    # Row 2: More scientific functions
    Button(root, text='asin', fg=text_fg, bg=sci_button_bg, padx=5, pady=3, width=4,
           command=lambda: get_input(entry, 'asin('), activebackground=button_active_bg).grid(row=2, column=0, pady=2)
    Button(root, text='acos', fg=text_fg, bg=sci_button_bg, padx=5, pady=3, width=4,
           command=lambda: get_input(entry, 'acos('), activebackground=button_active_bg).grid(row=2, column=1, pady=2)
    Button(root, text='atan', fg=text_fg, bg=sci_button_bg, padx=5, pady=3, width=4,
           command=lambda: get_input(entry, 'atan('), activebackground=button_active_bg).grid(row=2, column=2, pady=2)
    Button(root, text='π', fg=text_fg, bg=sci_button_bg, padx=5, pady=3, width=4,
           command=lambda: get_input(entry, 'π'), activebackground=button_active_bg).grid(row=2, column=3, pady=2)
    Button(root, text='e', fg=text_fg, bg=sci_button_bg, padx=5, pady=3, width=4,
           command=lambda: get_input(entry, 'e'), activebackground=button_active_bg).grid(row=2, column=4, pady=2)
    Button(root, text='n!', fg=text_fg, bg=sci_button_bg, padx=5, pady=3, width=4,
           command=lambda: get_input(entry, '!('), activebackground=button_active_bg).grid(row=2, column=5, pady=2)

    # Row 3: Parentheses, clear, backspace
    Button(root, text='(', fg='black', bg=other_button_bg, padx=10, pady=3, width=4,
           command=lambda: get_input(entry, '('), activebackground=button_active_bg).grid(row=3, column=0, pady=2)
    Button(root, text=')', fg='black', bg=other_button_bg, padx=10, pady=3, width=4,
           command=lambda: get_input(entry, ')'), activebackground=button_active_bg).grid(row=3, column=1, pady=2)
    Button(root, text='C', bg=other_button_bg, padx=10, pady=3, width=4,
           command=lambda: clear(entry), activebackground=button_active_bg).grid(row=3, column=2, pady=2)
    Button(root, text='<-', bg=other_button_bg, padx=10, pady=3, width=4,
           command=lambda: backspace(entry), activebackground=button_active_bg).grid(row=3, column=3, pady=2)
    Button(root, text='%', fg=text_fg, bg=cal_button_bg, padx=10, pady=3, width=4,
           command=lambda: get_input(entry, '%'), activebackground=button_active_bg).grid(row=3, column=4, pady=2)
    Button(root, text='/', fg=text_fg, bg=cal_button_bg, padx=10, pady=3, width=4,
           command=lambda: get_input(entry, '/'), activebackground=button_active_bg).grid(row=3, column=5, pady=2)

    # Row 4: 7 8 9 *
    num_button(text='7', command=lambda: get_input(entry, '7')).grid(row=4, column=0, pady=2)
    num_button(text='8', command=lambda: get_input(entry, '8')).grid(row=4, column=1, pady=2)
    num_button(text='9', command=lambda: get_input(entry, '9')).grid(row=4, column=2, pady=2)
    cal_button(text='*', command=lambda: get_input(entry, '*')).grid(row=4, column=3, pady=2)
    Button(root, text='x²', fg=text_fg, bg=cal_button_bg, padx=10, pady=3, width=4,
           command=lambda: get_input(entry, '**2'), activebackground=button_active_bg).grid(row=4, column=4, pady=2)
    Button(root, text='xʸ', fg=text_fg, bg=cal_button_bg, padx=10, pady=3, width=4,
           command=lambda: get_input(entry, '**'), activebackground=button_active_bg).grid(row=4, column=5, pady=2)

    # Row 5: 4 5 6 -
    num_button(text='4', command=lambda: get_input(entry, '4')).grid(row=5, column=0, pady=2)
    num_button(text='5', command=lambda: get_input(entry, '5')).grid(row=5, column=1, pady=2)
    num_button(text='6', command=lambda: get_input(entry, '6')).grid(row=5, column=2, pady=2)
    cal_button(text='-', command=lambda: get_input(entry, '-')).grid(row=5, column=3, pady=2)
    Button(root, text='1/x', fg=text_fg, bg=cal_button_bg, padx=10, pady=3, width=4,
           command=lambda: get_input(entry, '1/('), activebackground=button_active_bg).grid(row=5, column=4, pady=2)
    Button(root, text='|x|', fg=text_fg, bg=cal_button_bg, padx=10, pady=3, width=4,
           command=lambda: get_input(entry, 'abs('), activebackground=button_active_bg).grid(row=5, column=5, pady=2)

    # Row 6: 1 2 3 +
    num_button(text='1', command=lambda: get_input(entry, '1')).grid(row=6, column=0, pady=2)
    num_button(text='2', command=lambda: get_input(entry, '2')).grid(row=6, column=1, pady=2)
    num_button(text='3', command=lambda: get_input(entry, '3')).grid(row=6, column=2, pady=2)
    cal_button(text='+', command=lambda: get_input(entry, '+')).grid(row=6, column=3, pady=2)
    Button(root, text='10ˣ', fg=text_fg, bg=cal_button_bg, padx=10, pady=3, width=4,
           command=lambda: get_input(entry, '10**'), activebackground=button_active_bg).grid(row=6, column=4, pady=2)
    Button(root, text='eˣ', fg=text_fg, bg=cal_button_bg, padx=10, pady=3, width=4,
           command=lambda: get_input(entry, 'e**'), activebackground=button_active_bg).grid(row=6, column=5, pady=2)

    # Row 7: 0 . = Quit
    num_button(text='0', command=lambda: get_input(entry, '0')).grid(row=7, column=0, pady=2)
    num_button(text='.', command=lambda: get_input(entry, '.')).grid(row=7, column=1, pady=2)
    num_button(text='±', command=lambda: toggle_sign(entry)).grid(row=7, column=2, pady=2)
    Button(root, text='=', fg=text_fg, bg=cal_button_bg, padx=10, pady=3, width=4,
           command=lambda: calc(entry), activebackground=button_active_bg).grid(row=7, column=3, pady=2)
    Button(root, text='Quit', fg='white', bg='black', padx=10, pady=3, width=4,
           command=root.quit, activebackground=button_active_bg).grid(row=7, column=4, columnspan=2, pady=2, sticky=E+W)

    root.mainloop()


def toggle_sign(entry):
    current = entry.get()
    if current:
        if current[0] == '-':
            clear(entry)
            entry.insert(END, current[1:])
        else:
            clear(entry)
            entry.insert(END, '-' + current)


if __name__ == '__main__':
    cal()

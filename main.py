from tkinter import *

root = Tk()
root.title("Compliment Color Calculator")
root.configure(background="#b3c9c3")
root.geometry('450x450')

# person will type in Hexcode for which color they want to compliment

""" Compliment colors will be calculated in this function by subtracting the input Hex code value from #FFFFFF """
title = Label(root, text='Compliment Color Calculator', bg='#4c363c', fg='white')
title.place(x=145, y=35)

# Code for input field
color1 = Entry(root)
color1.grid(row=5, column=5)
color1.place(x=60, y=300)
label1 = Label(root, text='Input hexcode values \n (no symbols):  #', relief="flat")
label1.place(x=60, y=250)

# Code for output field
color2 = Entry(root)
color2.grid(row=5, column=10)
color2.place(x=250, y=300)
label2 = Label(root, text='Compliment color hex-code', relief="flat")
label2.place(x=250, y=270)

# Label squares display the color that was input and the compliment color

color_choice = Label(root, bg='#c98c4e', relief="sunken", borderwidth=3,
                     text='Input \n Color')  # background = bg = value of input
color_choice.configure(height=5, width=20)
color_choice.place(x=50, y=100)

compliment_color = Label(root, bg='#c9524e', relief="sunken", borderwidth=3,
                         text='Compliment \n Color')  # background = bg = value of compliment color
compliment_color.configure(height=5, width=20)
compliment_color.place(x=240, y=100)


class Color(object):
    """ Class where inputs are processed to return compliment color visual and hex-code """

    def __init__(self):
        """ starting_ value saved input : holding just saves and sorts the RED, BLUE, GREEN values of hex-code : hex_output is the actual hexadecimal value of the compliment color  """
        self.starting_value = color1.get()
        self.holding = []
        self.hex_output = []

    def hex_dec(self):
        """ converts the input hexadecimal value into decimal  """
        self.holding += [int(str(self.starting_value[0:2]), 16)]
        self.holding += [int(str(self.starting_value[2:4]), 16)]
        self.holding += [int(str(self.starting_value[4:6]), 16)]

    def calculation(self):
        """ Compliment colors is found by subtracting decimal input value from 255 and reconverting into hexadecimal """
        self.hex_output += hex(255 - self.holding[0])[2:4]
        self.hex_output += hex(255 - self.holding[1])[2:4]
        self.hex_output += hex(255 - self.holding[2])[2:4]
        self.hex_output = ''.join(self.hex_output)


print(color1.get())


def pressed():  # button clicked will start up functions to calculate compliment color hex code

    c = Color()
    c.hex_dec()
    c.calculation()

    pair_tup = (color1.get(),
                c.hex_output)  # tuple retains value of the input even after the entry field is cleared which lets me continue to work with the value even after I've removed it.

    # Will clear values inside input field everytime button is clicked
    color1.delete(0, END)
    color2.delete(0, END)

    # Inserts hex numbers with pound symbol for presentation purposes
    color1.insert(0, '#')
    color1.insert(1, pair_tup[0])
    color2.insert(0, '#')
    color2.insert(1, c.hex_output)

    # Updates the colors of the large square labels to show user what they entered and what color compliments that entry
    color_choice.config(bg='#' + pair_tup[0])
    compliment_color.config(bg='#' + c.hex_output)

    pass


calculate_button = Button(root, text='calculate', relief="raised", command=pressed)
calculate_button.place(x=190, y=350)

root.mainloop()

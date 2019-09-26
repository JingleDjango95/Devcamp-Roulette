from tkinter import *
import tkinter.messagebox
from threading import Timer
import random
from ast import literal_eval as make_tuple

bet = []
counter = 20
total = 0

def roulette(number):

    master = Tk()
    master.title('Devcamp Roulette')
    master.geometry('500x300')
    
    topFrame = Frame(master, width=500, height=200)
    topFrame.pack(anchor=N)

    chip_value = number / 20

    def clicked(number):
        global bet
        global counter
        counter -= 1
        chip.config(text=f"You have {counter} chips, valued at ${chip_value:0.2f} each.")
        if counter <= 0:
            chip.config(text="You don't have any chips")
        else:
            bet.append(number)
            

    
    button_0 = Button(topFrame, text="0", fg='green', width=2, command=lambda: clicked(0))
    button_0.grid(row=0)
    button_00 = Button(topFrame, text="00", fg='green', width=2, command=lambda: clicked('00'))
    button_00.grid(row=2)

    button_3 = Button(topFrame, text="3", fg='red', width=2, command=lambda: clicked(3))
    button_3.grid(row=0, column=1)
    button_2 = Button(topFrame, text="2", width=2, command=lambda: clicked(2))
    button_2.grid(row=1, column=1)
    button_1 = Button(topFrame, text="1", fg='red', width=2, command=lambda: clicked(1))
    button_1.grid(row=2, column=1)

    button_6 = Button(topFrame, text="6", width=2, command=lambda: clicked(6))
    button_6.grid(row=0, column=2)
    button_5 = Button(topFrame, text="5", fg='red', width=2, command=lambda: clicked(5))
    button_5.grid(row=1, column=2)
    button_4 = Button(topFrame, text="4", width=2, command=lambda: clicked(4))
    button_4.grid(row=2, column=2)

    button_9 = Button(topFrame, text="9", fg='red', width=2, command=lambda: clicked(9))
    button_9.grid(row=0, column=3)
    button_8 = Button(topFrame, text="8", width=2, command=lambda: clicked(8))
    button_8.grid(row=1, column=3)
    button_7 = Button(topFrame, text="7", fg='red', width=2, command=lambda: clicked(7))
    button_7.grid(row=2, column=3)

    button_12 = Button(topFrame, text="12", fg='red', command=lambda: clicked(12))
    button_12.grid(row=0, column=4)
    button_11 = Button(topFrame, text="11", command=lambda: clicked(11))
    button_11.grid(row=1, column=4)
    button_10 = Button(topFrame, text="10", command=lambda: clicked(10))
    button_10.grid(row=2, column=4)

    button_15 = Button(topFrame, text="15", command=lambda: clicked(15))
    button_15.grid(row=0, column=5)
    button_14 = Button(topFrame, text="14", fg='red', command=lambda: clicked(14))
    button_14.grid(row=1, column=5)
    button_13 = Button(topFrame, text="13", command=lambda: clicked(13))
    button_13.grid(row=2, column=5)

    button_18 = Button(topFrame, text="18", fg='red', command=lambda: clicked(18))
    button_18.grid(row=0, column=6)
    button_17 = Button(topFrame, text="17", command=lambda: clicked(17))
    button_17.grid(row=1, column=6)
    button_16 = Button(topFrame, text="16", fg='red', command=lambda: clicked(16))
    button_16.grid(row=2, column=6)

    button_21 = Button(topFrame, text="21", fg='red', command=lambda: clicked(21))
    button_21.grid(row=0, column=7)
    button_20 = Button(topFrame, text="20", command=lambda: clicked(20))
    button_20.grid(row=1, column=7)
    button_19 = Button(topFrame, text="19", fg='red', command=lambda: clicked(19))
    button_19.grid(row=2, column=7)

    button_24 = Button(topFrame, text="24", command=lambda: clicked(24))
    button_24.grid(row=0, column=8)
    button_23 = Button(topFrame, text="23", fg='red', command=lambda: clicked(23))
    button_23.grid(row=1, column=8)
    button_22 = Button(topFrame, text="22", command=lambda: clicked(22))
    button_22.grid(row=2, column=8)

    button_27 = Button(topFrame, text="27", fg='red', command=lambda: clicked(27))
    button_27.grid(row=0, column=9)
    button_26 = Button(topFrame, text="26", command=lambda: clicked(26))
    button_26.grid(row=1, column=9)
    button_25 = Button(topFrame, text="25", fg='red', command=lambda: clicked(25))
    button_25.grid(row=2, column=9)

    button_30 = Button(topFrame, text="30", fg='red', command=lambda: clicked(30))
    button_30.grid(row=0, column=10)
    button_29 = Button(topFrame, text="29", command=lambda: clicked(29))
    button_29.grid(row=1, column=10)
    button_28 = Button(topFrame, text="28", command=lambda: clicked(28))
    button_28.grid(row=2, column=10)

    button_33 = Button(topFrame, text="33", command=lambda: clicked(33))
    button_33.grid(row=0, column=11)
    button_32 = Button(topFrame, text="32", fg='red', command=lambda: clicked(32))
    button_32.grid(row=1, column=11)
    button_31 = Button(topFrame, text="31", command=lambda: clicked(31))
    button_31.grid(row=2, column=11)

    button_36 = Button(topFrame, text="36", fg='red', command=lambda: clicked(36))
    button_36.grid(row=0, column=12)
    button_35 = Button(topFrame, text="35", command=lambda: clicked(35))
    button_35.grid(row=1, column=12)
    button_34 = Button(topFrame, text="34", fg='red', command=lambda: clicked(34))
    button_34.grid(row=2, column=12)

    button_c1 = Button(topFrame, text='2 to 1', command=lambda: clicked('c1'))
    button_c1.grid(row=0, column=13)
    button_c2 = Button(topFrame, text='2 to 1', command=lambda: clicked('c2'))
    button_c2.grid(row=1, column=13)
    button_c3 = Button(topFrame, text='2 to 1', command=lambda: clicked('c3'))
    button_c3.grid(row=2, column=13)

    button_first12 = Button(topFrame, text='1st 12', width=12, command=lambda: clicked('1st12'))
    button_first12.grid(row=3, column=1, columnspan=4)
    button_second12 = Button(topFrame, text='2nd 12', width=12, command=lambda: clicked('2nd12'))
    button_second12.grid(row=3, column=5, columnspan=4)
    button_third12 = Button(topFrame, text='3rd 12', width=12, command=lambda: clicked('3rd12'))
    button_third12.grid(row=3, column=9, columnspan=4)

    button_first18 = Button(topFrame, text='1 to 18', width=6, command=lambda: clicked('1-18'))
    button_first18.grid(row=4, column=1, columnspan=2)
    button_even = Button(topFrame, text='EVEN', width=6, command=lambda: clicked('even'))
    button_even.grid(row=4, column=3, columnspan=2)
    button_red = Button(topFrame, text='RED', width=6, fg='red', command=lambda: clicked('red'))
    button_red.grid(row=4, column=5, columnspan=2)
    button_black = Button(topFrame, text='BLACK', width=6, command=lambda: clicked('black'))
    button_black.grid(row=4, column=7, columnspan=2)
    button_odd = Button(topFrame, text='ODD', width=6, command=lambda: clicked('odd'))
    button_odd.grid(row=4, column=9, columnspan=2)
    button_last18 = Button(topFrame, text='19 to 36', width=6, command=lambda: clicked('19-36'))
    button_last18.grid(row=4, column=11, columnspan=2)
    
    buttons = [button_0, button_00, button_1, button_2, button_3, button_4, button_5, button_6, button_7, button_8, button_9, button_10, button_11, button_12, button_13, button_14, button_15, button_16, button_17, button_18, button_19, button_20, button_21, button_22, button_23, button_24, button_25, button_26, button_27, button_28, button_29, button_30, button_31, button_32, button_33, button_34, button_35, button_36, button_c1, button_c2, button_c3, button_first12, button_second12, button_third12, button_first18, button_last18, button_even, button_odd, button_red, button_black]

    border = Canvas(master, width=500, height=10)
    border.pack(anchor=CENTER)

    borderLine = border.create_line(0, 10, 500, 10)

    bottomFrame = Frame(master, width=500, height=190)
    bottomFrame.pack_propagate(0)
    bottomFrame.pack(anchor=S)

    chip = Label(bottomFrame, text=f"You have {counter} chips, valued at ${chip_value:0.2f}")
    chip.grid(row=0, columnspan=4)

    tkvar1 = StringVar(master)
    tkvar2 = StringVar(master)
    tkvar3 = StringVar(master)
    tkvar4 = StringVar(master)


    split_choices = ['NONE', [0, 00], [0, 1], [0, 2], [00, 2], [00, 3], [1, 4], [1, 2], [2, 5], [2, 3], [3, 6], [4, 7], [4, 5], [5, 8], [5, 6], [6, 9], [7, 8], [7, 10], [8, 9], [8, 11], [9, 12], [13, 14], [13, 16], [13, 14], [14, 17], [14, 15], [15, 18], [19, 22], [19, 20], [20, 23], [20, 21], [21, 24], [25, 28], [25, 26], [26, 29], [26, 27], [27, 30], [31, 34], [31, 32], [32, 35], [32, 33], [33, 36]]
    streen_choices = ['NONE', '1-3', '4-6', '7-9', '10-12', '13-15', '16-18', '19-21', '22-24', '25-27', '28-30', '31-33', '34-36']
    corner_choices = ['NONE', [1, 2, 4, 5], [2, 3, 5, 6], [4, 5, 7, 8], [5, 6, 8, 9], [7, 8, 10, 11], [8, 9, 11, 12], [10, 11, 13, 14], [11, 12, 14, 15], [13, 14, 16, 17], [14, 15, 17, 18], [16, 17, 19, 20], [17, 18, 20, 21], [19, 20, 22, 23], [20, 21, 23, 24], [22, 23, 25, 26], [23, 24, 26, 27], [25, 26, 28, 29], [26, 27, 29, 30], [28, 29, 31, 32], [29, 30, 32, 33], [31, 32, 34, 35], [32, 33, 35, 36]]
    six_choices = ['NONE', '1-6', '7-12', '13-18', '19-24', '25-30', '31-36']

    tkvar1.set('NONE')
    tkvar2.set('NONE')
    tkvar3.set('NONE')
    tkvar4.set('NONE')

    split_menu = OptionMenu(bottomFrame, tkvar1, *split_choices)
    Label(bottomFrame, text='Split Bets').grid(row=1, column=0)
    split_menu.grid(row=2, column=0)

    street_menu = OptionMenu(bottomFrame, tkvar2, *streen_choices)
    Label(bottomFrame, text='Street Bets').grid(row=1, column=1)
    street_menu.grid(row=2, column=1)

    corner_menu = OptionMenu(bottomFrame, tkvar3, *corner_choices)
    Label(bottomFrame, text='Corner Bets').grid(row=1, column=2)
    corner_menu.grid(row=2, column=2)

    six_menu = OptionMenu(bottomFrame, tkvar4, *six_choices)
    Label(bottomFrame, text='Six-Number Bets').grid(row=1, column=3)
    six_menu.grid(row=2, column=3)

    menus = [split_menu, street_menu, corner_menu, six_menu]

    cash_out = Button(master, text="Cash Out", command=lambda: cashOut(total, chip_value))
    cash_out.pack(anchor=CENTER, side=RIGHT, padx=80)
    keep_playing = Button(master, text="Keep Playing", command=lambda: keepPlaying(total, chip_value, cash_out, keep_playing))
    keep_playing.pack(anchor=CENTER, side=LEFT, padx=80)

    def change_dropdown1(*args):
        global counter
        global bet
        counter -= 1
        split_bet = tkvar1.get()
        bet.append(split_bet)

    tkvar1.trace('w', change_dropdown1)

    def change_dropdown2(*args):
        global counter
        global bet
        counter -= 1
        street_bet = tkvar2.get()
        bet.append(street_bet)

    tkvar2.trace('w', change_dropdown2)

    def change_dropdown3(*args):
        global counter
        global bet
        counter -= 1
        corner_bet = tkvar3.get()
        bet.append(corner_bet)

    tkvar3.trace('w', change_dropdown3)

    def change_dropdown4(*args):
        global counter
        global bet
        counter -= 1
        six_bet = tkvar4.get()
        bet.append(six_bet)
        
    tkvar4.trace('w', change_dropdown4)

    def end_of_bets(chip_value):
        chip.config(text="Please, no more bets")
        for button in buttons:
            button.config(state='disabled')
        for menu in menus:
            menu.config(state='disabled')
        random_number(chip_value)

    def random_number(chip_value):
        choice = [0, '00', 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36]
        r_number = random.choice(choice)
        chip.config(text=f'And the number is: {r_number}')
        t = Timer(2.0, lambda: win_query(r_number, chip_value))
        t.start()
        
    def keepPlaying(total, chip_value, cash_out, keep_playing):
        global counter
        global bet
        counter += total
        chip.config(text=f"You have {counter} chips, valued at ${chip_value:0.2f} each.")
        bet = []
        t = Timer(20.0, lambda: end_of_bets(chip_value))
        for button in buttons:
            button.config(state='normal')
        for menu in menus:
            menu.config(state='normal')
        t.start()

    def cashOut(total, chip_value):
        global counter
        counter += total
        counter *= chip_value
        total *= chip_value
        chip.config(text=f"You won ${total:0.2f}. You cashed out ${counter:0.2f}. Thanks for playing!")
        

    def win_query(random, chip_value):
        global counter
        global total
        col1 = [3,6,9,12,15,18,21,24,27,30,33,36]
        col2 = [2,5,8,11,14,17,20,23,26,29,32,35]
        col3 = [1,4,7,10,13,16,19,22,25,28,31,34]
        red = [1,3,5,7,9,12,14,16,18,19,21,23,25,27,30,32,34,36]
        black = [2,4,6,8,10,11,13,15,17,20,22,24,26,28,29,31,33,35]
        even = [2,4,6,8,10,12,14,16,18,20,22,24,26,28,30,32,34,36]
        odd = [1,3,5,7,9,11,13,15,17,19,21,23,25,27,29,31,33,35]
        fst12 = [1,2,3,4,5,6,7,8,9,10,11,12]
        sec12 = [13,14,15,16,17,18,19,20,21,22,23,24]
        thi12 = [25,26,27,28,29,30,31,32,33,34,35,36]
        fst18 = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18]
        lst18 = [19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36]
        split_choices = [[0, 00], [0, 1], [0, 2], [00, 2], [00, 3], [1, 4], [1, 2], [2, 5], [2, 3], [3, 6], [4, 7], [4, 5], [5, 8], [5, 6], [6, 9], [7, 8], [7, 10], [8, 9], [8, 11], [9, 12], [13, 14], [13, 16], [13, 14], [14, 17], [14, 15], [15, 18], [19, 22], [19, 20], [20, 23], [20, 21], [21, 24], [25, 28], [25, 26], [26, 29], [26, 27], [27, 30], [31, 34], [31, 32], [32, 35], [32, 33], [33, 36]]
        streen_choices = [[1,2,3], [4,5,6], [7,8,9], [10,11,12], [13,14,15], [16,17,18], [19,20,21], [22,23,24], [25,26,27], [28,29,30], [31,32,33], [34,35,36]]
        corner_choices = [[1, 2, 4, 5], [2, 3, 5, 6], [4, 5, 7, 8], [5, 6, 8, 9], [7, 8, 10, 11], [8, 9, 11, 12], [10, 11, 13, 14], [11, 12, 14, 15], [13, 14, 16, 17], [14, 15, 17, 18], [16, 17, 19, 20], [17, 18, 20, 21], [19, 20, 22, 23], [20, 21, 23, 24], [22, 23, 25, 26], [23, 24, 26, 27], [25, 26, 28, 29], [26, 27, 29, 30], [28, 29, 31, 32], [29, 30, 32, 33], [31, 32, 34, 35], [32, 33, 35, 36]]
        six_choices = [[1,2,3,4,5,6], [7,8,9,10,11,12], [13,14,15,16,17,18], [19,20,21,22,23,24], [25,26,27,28,29,30], [31,32,33,34,35,36]]
        for item in bet:
            if item == random:
                total += 35
            elif item == 'c1':
                for number in col1:
                    if number == random:
                        total += 2
            elif item == 'c2':
                for number in col2:
                    if number == random:
                        total += 2
            elif item == 'c3':
                for number in col3:
                    if number == random:
                        total += 2
            elif item == 'red':
                for number in red:
                    if number == random:
                        total += 1
            elif item == 'black':
                for number in black:
                    if number == random:
                        total += 1
            elif item == 'even':
                for number in even:
                    if number == random:
                        total += 1
            elif item == 'odd':
                for number in odd:
                    if number == random:
                        total += 1
            elif item == '1st12':
                for number in fst12:
                    if number == random:
                        total += 2
            elif item == '2nd12':
                for number in sec12:
                    if number == random:
                        total += 2
            elif item == '3rd12':
                for number in thi12:
                    if number == random:
                        total += 2
            elif item == '1-18':
                for number in fst18:
                    if number == random:
                        total += 1
            elif item == '19-36':
                for number in lst18:
                    if number == random:
                        total += 1
            elif item == '(0, 00)' or item == '(0, 1)' or item == '(0, 2)' or item == '(00, 2)' or item == '(00, 3)' or item == '(1, 4)' or item == '(1, 2)' or item == '(2, 5)' or item == '(2, 3)' or item == '(3, 6)' or item == '(4, 7)' or item == '(4, 5)' or item == '(5, 8)' or item == '(5, 6)' or item == '(6, 9)' or item == '(7, 8)' or item == '(7, 10)' or item == '(8, 9)' or item == '(8, 11)' or item == '(9, 12)' or item == '(13, 14)' or item == '(13, 16)' or item == '(13, 14)' or item == '(14, 17)' or item == '(14, 15)' or item == '(15, 18)' or item == '(19, 22)' or item == '(19, 20)' or item == '(20, 23)' or item == '(20, 21)' or item == '(21, 24)' or item == '(25, 28)' or item == '(25, 26)' or item == '(26, 29)' or item == '(26, 27)' or item == '(27, 30)' or item == '(31, 34)' or item == '(31, 32)' or item == '(32, 35)' or item == '(32, 33)' or item == '(33, 36)':
                for lst in split_choices:
                    for item in lst:
                        if item == random:
                            total += 17
            elif item == '(1, 2, 3)' or item == '(4, 5, 6)' or item == '(7, 8, 9)' or item == '(10, 11, 12)' or item == '(13, 14, 15)' or item == '(16, 17, 18)' or item == '(19, 20, 21)' or item == '(22, 23, 24)' or item == '(25, 26, 27)' or item == '(28, 29, 30)' or item == '(31, 32, 33)' or item == '(34, 35, 36)':
                for lst in streen_choices:
                    for item in lst:
                        if item == random:
                            total += 11
            elif item == '(1, 2, 4, 5)' or item == '(2, 3, 5, 6)' or item == '(4, 5, 7, 8)' or item == '(5, 6, 8, 9)' or item == '(7, 8, 10, 11)' or item == '(8, 9, 11, 12)' or item == '(10, 11, 13, 14)' or item == '(11, 12, 14, 15)' or item == '(13, 14, 16, 17)' or item == '(14, 15, 17, 18)' or item == '(16, 17, 19, 20)' or item == '(17, 18, 20, 21)' or item == '(19, 20, 22, 23)' or item == '(20, 21, 23, 24)' or item == '(22, 23, 25, 26)' or item == '(23, 24, 26, 27)' or item == '(25, 26, 28, 29)' or item == '(26, 27, 29, 30)' or item == '(28, 29, 31, 32)' or item == '(29, 30, 32, 33)' or item == '(31, 32, 34, 35)' or item == '(32, 33, 35, 36)':
                for lst in corner_choices:
                    for item in lst:
                        if item == random:
                            total += 8
            elif item == '(1, 2, 3, 4, 5, 6)' or item == '(7, 8, 9, 10, 11, 12)' or item == '(13, 14, 15, 16, 17, 18)' or item == '(19, 20, 21, 22, 23, 24)' or item == '(25, 26, 27, 28, 29, 30)' or item == '(31, 32, 33, 34, 35, 36)':
                for lst in six_choices:
                    for item in lst:
                        if item == random:
                            total += 6
        if total <= 0:
            chip.config(text="I'm sorry, you didn't win anything.")
            if counter == 0:
                t = Timer(3.0, master.destroy)
                t.start
            else:
                chip.config(text="Cash out or keep playing?")
        else:
            chip.config(text=f"You won {total} chips! Cash out or keep playing?")
            
        

    t = Timer(30.0, lambda: end_of_bets(chip_value))
    t.start()
    master.mainloop()


buy_in = Tk()
buy_in.title("Buy In")
buy_in.geometry('250x150')

tkinter.messagebox.showinfo("Welcome to Roulette!",
"Welcome to Roulette!, the rules are simple, guess the number \
 and you win! There are several bets you can make: \
 straight bets: which is one number, split bets: which is between \
 two adjacent numbers, street bets: which is between three adjacent \
 numbers, corner bets: which are between four adjacent numbers, \
 a six number bet: which is any row of six numbers, and if you don't want to \
 risk it all, you can make safer bets with black, red, even odd, the numbers \
 1-18, or 19-36, which dozen will win, and which column will win. Good luck, and have fun!")

buy_in_message = Label(buy_in, text="How much are you buying in for?")
buy_in_message.pack(anchor=N)

buy_in_button1 = Button(buy_in, text="$1")
buy_in_button1.pack(anchor=CENTER)
buy_in_button10 = Button(buy_in, text="$10")
buy_in_button10.pack(anchor=CENTER)
buy_in_button100 = Button(buy_in, text="$100")
buy_in_button100.pack(anchor=CENTER)
buy_in_button1000 = Button(buy_in, text="$1000")
buy_in_button1000.pack(anchor=CENTER)

def initiate_roulette_with_1(event):
    buy_in.destroy()
    game1 = roulette(1)

def initiate_roulette_with_10(event):
    buy_in.destroy()
    game2 = roulette(10)

def initiate_roulette_with_100(event):
    buy_in.destroy()
    game3 = roulette(100)

def initiate_roulette_with_1000(event):
    buy_in.destroy()
    game4 = roulette(1000)

buy_in_button1.bind('<Button-1>', initiate_roulette_with_1)
buy_in_button10.bind('<Button-1>', initiate_roulette_with_10)
buy_in_button100.bind('<Button-1>', initiate_roulette_with_100)
buy_in_button1000.bind('<Button-1>', initiate_roulette_with_1000)

buy_in.mainloop()
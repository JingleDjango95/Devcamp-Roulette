# We are building a casino!
# You are to build one casino game, black jack, slots, roulette, etc, ( these are the ones I have seen built out before.)
# requirements
# Build the game.
# Push individual commits to github.
# In addition,
# the player will have a wallet, they can add money to the wallet, any winnings they get will be added to the wallet.
# If the wallet goes empty they must add more money or they have to stop playing.
# They need to be able to stop playing and cash out the wallet at anytime. (bonus if the cash out proccess tells them if they made a profit or not)
# let the player set the dollar/cents amount of the bet (in the game).
# let them continue playing as long as they have money or decide to cash out.

# 0 and 00 are green
# 1 - 10 evens are black, odds are red
# 11 - 18 evens are red, odds are black
# 19 - 28 evens are black, odds are red
# 29 - 36 evens are red, odds are black

# rules

# inside bets

# straight bet = 36:1 win
# split bet = 17:1 win
# street bet = 11:1 win
# corner bet = 8:1 win
# five number bet (0, 00, 1, 2, 3 corner bet) = 6:1 win
# six line bet = 6:1 win

# outside bets

# red = 1:1 win
# black = 1:1 win
# even = 1:1 win
# odd = 1:1 win
# low bet (1-18) = 1:1 win
# high bet (19-36) = 1:1 win
# dozen bet = 2:1 win
# column bet = 2:1 win


# random number generator


# wins determined, wheel goes again

from tkinter import *
import tkinter.messagebox

global counter
counter = 20

def roulette(number):

    master = Tk()
    master.title('Devcamp Roulette')
    master.geometry('500x500')

    topFrame = Frame(master, width=500, height=200)
    topFrame.pack(anchor=N)

    buttonFrame = Frame(topFrame, width=2, height=2)

    chip_value = number // 20

    def clicked():
        global counter
        counter -= 1
        chip.config(text=f"You have {counter} chips, valued at ${chip_value:0.2f}")
        if counter <= 0:
            chip.config(text="You don't have any chips")
            end_of_bets()

    button_0 = Button(topFrame, text="0", fg='green', width=2, command=clicked).grid(row=0)
    button_00 = Button(topFrame, text="00", fg='green', width=2).grid(row=2)

    button_3 = Button(topFrame, text="3", fg='red', width=2).grid(row=0, column=1)
    button_2 = Button(topFrame, text="2", width=2).grid(row=1, column=1)
    button_1 = Button(topFrame, text="1", fg='red', width=2).grid(row=2, column=1)

    button_6 = Button(topFrame, text="6", width=2).grid(row=0, column=2)
    button_5 = Button(topFrame, text="5", fg='red', width=2).grid(row=1, column=2)
    button_4 = Button(topFrame, text="4", width=2).grid(row=2, column=2)

    button_9 = Button(topFrame, text="9", fg='red', width=2).grid(row=0, column=3)
    button_8 = Button(topFrame, text="8", width=2).grid(row=1, column=3)
    button_7 = Button(topFrame, text="7", fg='red', width=2).grid(row=2, column=3)

    button_12 = Button(topFrame, text="12", fg='red').grid(row=0, column=4)
    button_11 = Button(topFrame, text="11").grid(row=1, column=4)
    button_10 = Button(topFrame, text="10").grid(row=2, column=4)

    button_15 = Button(topFrame, text="15").grid(row=0, column=5)
    button_14 = Button(topFrame, text="14", fg='red').grid(row=1, column=5)
    button_13 = Button(topFrame, text="13").grid(row=2, column=5)

    button_18 = Button(topFrame, text="18", fg='red').grid(row=0, column=6)
    button_17 = Button(topFrame, text="17").grid(row=1, column=6)
    button_16 = Button(topFrame, text="16", fg='red').grid(row=2, column=6)

    button_21 = Button(topFrame, text="21", fg='red').grid(row=0, column=7)
    button_20 = Button(topFrame, text="20").grid(row=1, column=7)
    button_19 = Button(topFrame, text="19", fg='red').grid(row=2, column=7)

    button_24 = Button(topFrame, text="24").grid(row=0, column=8)
    button_23 = Button(topFrame, text="23", fg='red').grid(row=1, column=8)
    button_22 = Button(topFrame, text="22").grid(row=2, column=8)

    button_27 = Button(topFrame, text="27", fg='red').grid(row=0, column=9)
    button_26 = Button(topFrame, text="26").grid(row=1, column=9)
    button_25 = Button(topFrame, text="25", fg='red').grid(row=2, column=9)

    button_30 = Button(topFrame, text="30", fg='red').grid(row=0, column=10)
    button_29 = Button(topFrame, text="29").grid(row=1, column=10)
    button_28 = Button(topFrame, text="28").grid(row=2, column=10)

    button_33 = Button(topFrame, text="33").grid(row=0, column=11)
    button_32 = Button(topFrame, text="32", fg='red').grid(row=1, column=11)
    button_31 = Button(topFrame, text="31").grid(row=2, column=11)

    button_36 = Button(topFrame, text="36", fg='red').grid(row=0, column=12)
    button_35 = Button(topFrame, text="35").grid(row=1, column=12)
    button_34 = Button(topFrame, text="34", fg='red').grid(row=2, column=12)

    button_c1 = Button(topFrame, text='2 to 1').grid(row=0, column=13)
    button_c2 = Button(topFrame, text='2 to 1').grid(row=1, column=13)
    button_c3 = Button(topFrame, text='2 to 1').grid(row=2, column=13)

    button_first12 = Button(topFrame, text='1st 12', width=12).grid(row=3, column=1, columnspan=4)
    button_second12 = Button(topFrame, text='2nd 12', width=12).grid(row=3, column=5, columnspan=4)
    button_third12 = Button(topFrame, text='3rd 12', width=12).grid(row=3, column=9, columnspan=4)

    button_first18 = Button(topFrame, text='1 to 18', width=6).grid(row=4, column=1, columnspan=2)
    button_even = Button(topFrame, text='EVEN', width=6).grid(row=4, column=3, columnspan=2)
    button_red = Button(topFrame, text='RED', width=6, fg='red').grid(row=4, column=5, columnspan=2)
    button_black = Button(topFrame, text='BLACK', width=6).grid(row=4, column=7, columnspan=2)
    button_odd = Button(topFrame, text='ODD', width=6).grid(row=4, column=9, columnspan=2)
    button_last18 = Button(topFrame, text='19 to 36', width=6).grid(row=4, column=11, columnspan=2)

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


    split_choices = ['0, 00', '0, 1', '0, 2', '00, 2', '00, 3', '1, 4', '1, 2', '2, 5', '2, 3', '3, 6', '4, 7', '4, 5', '5, 8', '5, 6', '6, 9', '7, 8', '7, 10', '8, 9', '8, 11', '9, 12', '13, 14', '13, 16', '13, 14', '14, 17', '14, 15', '15, 18', '19, 22', '19, 20', '20, 23', '20, 21', '21, 24', '25, 28', '25, 26', '26, 29', '26, 27', '27, 30', '31, 34', '31, 32', '32, 35', '32, 33', '33, 36']
    streen_choices = ['1-3', '4-6', '7-9', '10-12', '13-15', '16-18', '19-21', '22-24', '25-27', '28-30', '31-33', '34-36']
    corner_choices = ['1, 2, 4, 5', '2, 3, 5, 6', '4, 5, 7, 8', '5, 6, 8, 9', '7, 8, 10, 11', '8, 9, 11, 12', '10, 11, 13, 14', '11, 12, 14, 15', '13, 14, 16, 17', '14, 15, 17, 18', '16, 17, 19, 20', '17, 18, 20, 21', '19, 20, 22, 23', '20, 21, 23, 24', '22, 23, 25, 26', '23, 24, 26, 27', '25, 26, 28, 29', '26, 27, 29, 30', '28, 29, 31, 32', '29, 30, 32, 33', '31, 32, 34, 35', '32, 33, 35, 36']
    six_choices = ['1-6', '7-12', '13-18', '19-24', '25-30', '31-36']

    tkvar1.set('0, 00')
    tkvar2.set('1-3')
    tkvar3.set('1, 2, 4, 5')
    tkvar4.set('1-6')

    split_menu = OptionMenu(bottomFrame, tkvar1, split_choices[0], *split_choices)
    Label(bottomFrame, text='Split Bets').grid(row=1, column=0)
    split_menu.grid(row=2, column=0)

    street_menu = OptionMenu(bottomFrame, tkvar2, streen_choices[0], *streen_choices)
    Label(bottomFrame, text='Street Bets').grid(row=1, column=1)
    street_menu.grid(row=2, column=1)

    corner_menu = OptionMenu(bottomFrame, tkvar3, corner_choices[0], *corner_choices)
    Label(bottomFrame, text='Corner Bets').grid(row=1, column=2)
    corner_menu.grid(row=2, column=2)

    six_menu = OptionMenu(bottomFrame, tkvar4, six_choices[0], *six_choices)
    Label(bottomFrame, text='Six-Number Bets').grid(row=1, column=3)
    six_menu.grid(row=2, column=3)

    def change_dropdown1(*args):
        split_bet = tkvar1.get()

    tkvar1.trace('w', change_dropdown1)

    def change_dropdown2(*args):
        steet_bet = tkvar2.get()

    tkvar2.trace('w', change_dropdown2)

    def change_dropdown3(*args):
        corner_bet = tkvar3.get()

    tkvar3.trace('w', change_dropdown3)

    def change_dropdown4(*args):
        six_bet = tkvar4.get()

    tkvar4.trace('w', change_dropdown4)

    def end_of_bets():
        pass

    master.mainloop()


buy_in = Tk()
buy_in.title("Buy In")
buy_in.geometry('200x100')

tkinter.messagebox.showinfo("Welcome to Roulette!",
"Welcome to Roulette!, the rules are simple, guess the number \
 and you win! There are several bets you can make: \
 straight bets: which is one number, split bets: which is between \
 two adjacent numbers, street bets: which is between three adjacent \
 numbers, corner bets: which are between four adjacent numbers, \
 the lucky five-number bet: which is only 00, 0, 1, 2, and 3, a six \
 number bet: which is any row of six numbers, and if you don't want to \
 risk it all, you can make safer bets with black, red, even odd, the numbers \
 1-18, or 19-36, which dozen will win, and which column will win. Good luck, and have fun!")

buy_in_message = Label(buy_in, text="How much are you buying in for?")
buy_in_message.pack()

def close_window():
    buy_in.destroy()

buy_in_button1 = Button(buy_in, text="$1")
buy_in_button1.pack(side=LEFT)
buy_in_button10 = Button(buy_in, text="$10")
buy_in_button10.pack(side=LEFT)
buy_in_button100 = Button(buy_in, text="$100")
buy_in_button100.pack(side=LEFT)
buy_in_button1000 = Button(buy_in, text="$1000")
buy_in_button1000.pack(side=LEFT)

def initiate_roulette_with_1(event):
    close_window()
    game1 = roulette(1)

def initiate_roulette_with_10(event):
    close_window()
    game2 = roulette(10)

def initiate_roulette_with_100(event):
    close_window()
    game3 = roulette(100)

def initiate_roulette_with_1000(event):
    close_window()
    game4 = roulette(1000)

buy_in_button1.bind('<Button-1>', initiate_roulette_with_1)
buy_in_button10.bind('<Button-1>', initiate_roulette_with_10)
buy_in_button100.bind('<Button-1>', initiate_roulette_with_100)
buy_in_button1000.bind('<Button-1>', initiate_roulette_with_1000)

buy_in.mainloop()

# def buy_in():
#     # player inputs buy in amount and is given the chips for it
#     player_money = input('How much are you buying in today?\n')
#     x = re.findall("[0-9]", player_money)
#     player_money = ''.join(x)
#     player_money = int(player_money)
#     white = 0
#     if player_money > 0:
#         white += 20
#         player_money /= 20
#         print(f'You have {white} chips worth ${player_money:0.2f}.')
#     else:
#         print("I'm sorry, you don't have enough money.")
#         exit()
#     bet_query(white)

# # place bets

# def bet_query(white):
#     empty = []
#     bet = input(f'How many chips are you betting?\n')
#     bet= int(bet)
#     white = white - bet
#     empty.append(bet)
#     bet_place(empty)

# def bet_place(empty):
#     bet = []
#     for element in empty:
#         if element != 0:
#             bet_placing = input("What's your bet? Inside or outside?\n")
#             bet_placing = bet_placing.lower()
#             if bet_placing == 'inside':
#                 number = input("Which number(s) are you betting on?\n")
#                 bet.append((number))
#             elif bet_placing == 'outside':
#                 outer = input("")
#             else:
#                 print("I didn't quite get that. Please try again.")
#                 bet_place(empty)
#         else:
#             cash_out: input("Would you like to cash out?\n")
#             cash_check()

# def inner_winnings():
#     pass

# def outer_winnings():
#     pass
    
# def cash_check():
#     pass

# start()
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

def roulette(number):

    master = Tk()
    master.title('Devcamp Roulette')

    topFrame = Frame(master, width=1080, height=540)
    topFrame.pack()
    bottomFrame = Frame(master, width=1080, height=540)
    bottomFrame.pack(side=BOTTOM)

    button_0 = Button(topFrame, text="0", fg='green').grid(row=0)
    button_00 = Button(topFrame, text="00", fg='green').grid(row=2)
    button_1 = Button(topFrame, text="1", fg='red').grid(row=0, column=1)
    button_2 = Button(topFrame, text="2").grid(row=1, column=1)
    button_3 = Button(topFrame, text="3", fg='red').grid(row=2, column=1)
    button_4 = Button(topFrame, text="4").grid(row=0, column=2)
    button_5 = Button(topFrame, text="5", fg='red').grid(row=1, column=2)
    button_6 = Button(topFrame, text="6").grid(row=2, column=2)
    button_7 = Button(topFrame, text="7", fg='red').grid(row=0, column=3)
    button_8 = Button(topFrame, text="8").grid(row=1, column=3)
    button_9 = Button(topFrame, text="9", fg='red').grid(row=2, column=3)
    button_10 = Button(topFrame, text="10").grid(row=0, column=4)
    button_11 = Button(topFrame, text="11").grid(row=1, column=4)
    button_12 = Button(topFrame, text="12", fg='red').grid(row=2, column=4)
    button_13 = Button(topFrame, text="13").grid(row=0, column=5)
    button_14 = Button(topFrame, text="14", fg='red').grid(row=1, column=5)
    button_15 = Button(topFrame, text="15").grid(row=2, column=5)
    button_16 = Button(topFrame, text="16", fg='red').grid(row=0, column=6)
    button_17 = Button(topFrame, text="17").grid(row=1, column=6)
    button_18 = Button(topFrame, text="18", fg='red').grid(row=2, column=6)
    button_19 = Button(topFrame, text="19", fg='red').grid(row=0, column=7)
    button_20 = Button(topFrame, text="20").grid(row=1, column=7)
    button_21 = Button(topFrame, text="21", fg='red').grid(row=2, column=7)
    button_22 = Button(topFrame, text="22").grid(row=0, column=8)
    button_23 = Button(topFrame, text="23", fg='red').grid(row=1, column=8)
    button_24 = Button(topFrame, text="24").grid(row=2, column=8)
    button_25 = Button(topFrame, text="25", fg='red').grid(row=0, column=9)
    button_26 = Button(topFrame, text="26").grid(row=1, column=9)
    button_27 = Button(topFrame, text="27", fg='red').grid(row=2, column=9)
    button_28 = Button(topFrame, text="28").grid(row=0, column=10)
    button_29 = Button(topFrame, text="29").grid(row=1, column=10)
    button_30 = Button(topFrame, text="30", fg='red').grid(row=2, column=10)
    button_31 = Button(topFrame, text="31").grid(row=0, column=11)
    button_32 = Button(topFrame, text="32", fg='red').grid(row=1, column=11)
    button_33 = Button(topFrame, text="33").grid(row=2, column=11)
    button_34 = Button(topFrame, text="34", fg='red').grid(row=0, column=12)
    button_35 = Button(topFrame, text="35").grid(row=1, column=12)
    button_36 = Button(topFrame, text="36", fg='red').grid(row=2, column=12)

    master.mainloop()


buy_in = Tk()
buy_in.title("Buy In")

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
# import re

# def start():
#     print(' --------------')
#     print('/   0   |  00  \\')
#     print('----------------')
#     print('| 1  | 2  | 3  |')
#     print('----------------')
#     print('| 4  | 5  | 6  |')
#     print('----------------')
#     print('| 7  | 8  | 9  |')
#     print('----------------')
#     print('| 10 | 11 | 12 |')
#     print('----------------')
#     print('| 13 | 14 | 15 |')
#     print('----------------')
#     print('| 16 | 17 | 18 |')
#     print('----------------')
#     print('| 19 | 20 | 21 |')
#     print('----------------')
#     print('| 22 | 23 | 24 |')
#     print('----------------')
#     print('| 25 | 26 | 27 |')
#     print('----------------')
#     print('| 28 | 29 | 30 |')
#     print('----------------')
#     print('| 31 | 32 | 33 |')
#     print('----------------')
#     print('| 34 | 35 | 36 |')
#     print('----------------')
#     print("\nWelcome to Roulette!, the rules are simple, guess the number \
# and you win! There are several bets you can make, there are \
# straight bets, which is one number, split bets, which is between \
# two adjacent numbers, street bets, which is between three adjacent \
# numbers, corner bets, which are between four adjacent numbers, \
# the lucky five-number bet, which is only 00, 0, 1, 2, and 3, a six \
# number bet, which is any row of six numbers, and if you don't want to \
# risk it all, you can make safer bets with black, red, even odd, the numbers \
# 1-18, or 19-36, which dozen will win, and which column will win.\n")
#     buy_in()

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
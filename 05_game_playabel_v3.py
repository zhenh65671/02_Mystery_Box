from tkinter import *
from functools import partial  # To prevent unwanted windows
import random


class Start:
    def __init__(self, parent):
        # GUI to get starting balance and stakes
        self.start_frame = Frame(padx=10, pady=10)
        self.start_frame.grid()

        self.push_me_button = Button(text="Push Me", command=self.to_game)
        self.push_me_button.grid(row=0, pady=10)

    def to_game(self):
        # retrieve starting balance
        starting_balance = 50
        stakes = 2

        Game(self, stakes, starting_balance)

        # hide start up window
        self.start_frame.destroy()


class Game:
    def __init__(self, partner, stakes, starting_balance):
        print(stakes)
        print(starting_balance)

        # Initialise variables
        self.balance = IntVar()

        # Set starting balance to amount entered by user at the start of the game
        self.balance.set(starting_balance)

        # Get value of stakes (use it as a multiplier when calculating winnings
        self.multiplier = IntVar()
        self.multiplier.set(stakes)

        # GUI Setup
        self.game_box = Toplevel()

        # If user press cross at top, game quits
        self.game_boxprotocol('WM_DELETE_WINDOW',self.to_quit)

        self.game_frame = Frame(self.game_box)
        self.game_frame.grid()



        # Heading Row
        self.heading_label = Label(self.game_frame, text="Play...",
                                   font="Arial 24 bold", padx=10,
                                   pady=10)
        self.heading_label.grid(row=0)

        # Instructions Label
        self.instructions_label = Label(self.game_frame, wrap=300, justify=LEFT,
                                        text="Press <enter> or click the Open "
                                             "Boxes' button to reveal the "
                                             "contents of the mystery boxes.",
                                        font="Arial 10 bold", pady=10, padx=10)
        self.instructions_label.grid(row=1)

        # Boxes go here (row 2)
        box_text = "Arial 16 bold"
        box_back = "#b9ea96"  # light green
        box_width = 5
        self.box_frame = Frame(self.game_frame)
        self.box_frame.grid(row=2, pady=10)

        self.prize1_label = Label(self.box_frame, text="?\n", font=box_text,
                                  bg=box_back, width=box_width, padx=10, pady=10)
        self.prize1_label.grid(row=0, column=0)

        self.prize2_label = Label(self.box_frame, text="?\n", font=box_text,
                                  bg=box_back, width=box_width, padx=10, pady=10)
        self.prize2_label.grid(row=0, column=1, padx=10)

        self.prize3_label = Label(self.box_frame, text="?\n", font=box_text,
                                  bg=box_back, width=box_width, padx=10, pady=10)
        self.prize3_label.grid(row=0, column=2)

        # Play Button goes here (row 3)
        self.play_button = Button(self.game_frame, text="Open Boxes",
                                  bg="#FFFF33", font="Arial 15 bold", width=20,
                                  padx=10, pady=10, cpmm,a)

        # bind button to <enter> (user can push enter to reveal the boxes)


        # Balance Label (row 4)

        start_text = "Game Cost: ${} \n "" \nHow much " \
                     "will you win?".format(stakes * 5)

        self.balance_label = Label(self.game_frame, font="Arial 12 bold", fg="green",
                                   text=start_text, wrap=288,
                                   justify=LEFT)
        self.balance_label.grid(row=4, pady=10)

        # Help and Game stats button (row 5)
        self.help_export_frame = Frame(self.game_frame)
        self.help_export_frame.grid(row=5, padx=10)

        self.help_button = Button(self.help_export_frame, text="Help / Rules",
                                  font="Arial 15 bold",
                                  bg="#808080", fg="white")
        self.help_button.grid(row=5, column=0, padx=20)

        self.stats_button = Button(self.help_export_frame, text="Game Stats...",
                                   font="Arial 15 bold",
                                   bg="#003366", fg="white")
        self.stats_button.grid(row=5, column=1, padx=2)

        # Quit Button
        self.quit_button = Button(self.game_frame, text="Quit", fg="white",
                                  bg="#660000", font="Arial 15 bold", width=20,
                                  command=self.to_quit, padx=10, pady=10)
        self.quit_button.grid(row=6, pady=10)

    def reveal_boxes(self):
        # retrieve the balance from the initial function...
        current_balance = self.balance.get()
        stakes_multiplier = self.multiplier.get()

        round_winnings = 0
        prizes = []
        background = []
        for item in range(0, 3):
            prize_num = random.randint(1, 100)

            if 0 < prize_num <= 5:
                prize = "gold\n(${})".format(5 * stakes_multiplier)
                back_color = "#CEA935"  # Gold Colour
                round_winnings += 5 * stakes_multiplier
            elif 5 < prize_num <= 25:
                prize = "silver\n(${})".format(2 * stakes_multiplier)
                back_color = "#B7B7B5"  # Silver Colour
                round_winnings += 2 * stakes_multiplier
            elif 25 < prize_num <= 65:
                prize = "copper\n(${})".format(1 * stakes_multiplier)
                back_color = "BC7F61"   # Copper colour
                round_winnings += 1 * stakes_multiplier
            else:
                prize = "lead\n($0)"
                back_color = "#595E71"  # Lead colour

            prizes.append(prize)
            background.append(back_color)

            # Display prizes...
            self.prize1_label.config(text=prizes[0])
            self.prize2_label.config(text=prizes[1])
            self.prize3_label.config(text=prizes[2])

            # Deduct cost of games
            current_balance -= 5 * stakes_multiplier

            # Add winnings
            current_balance += round_winnings

            # Set balance to new balance
            self.balance.set(current_balance)

            balance_statement = "Game Cost: ${}\npayback: ${} \n" \
                                "Current Balance: ${}".format(5 * stakes_multiplier,
                                                              round_winnings,
                                                              current_balance)

            # Edit label so user can see their balance
            self.balance_label.configure(text=balance_statement)

            if current_balance < 5 * stakes_multiplier:
                self.play_button.config(state=DISABLED)
                self.game_box.focus()
                self.play_button.config(text="Game Over")

                balance_statement = "current Balance: ${}\n" \
                                    "Your balance is too low. You can only quit" \
                                    "or view your stats. Sorry about that.".format(current_balance)
                self.balance_label.config(fg="#660000", font="Arial 10 bold",
                                          text=balance_statement)

    def to_quit(self):
        root.destroy()


# main routine
if __name__ == "__main__":
    root = Tk()
    root.title("Mystery Box Game")
    something = Start(root)
    root.mainloop()
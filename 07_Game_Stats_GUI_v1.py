from tkinter import *
from functools import partial   # To prevent unwanted windows

import random


class Game:
    def __init__(self):

        # Formatting variables...
        self.game_stats_list = [50, 6]

        # In actual program this is blank and is populated with user calculations
        self.round_stats_list = [
            'silver ($4) | silver ($4) | lead ($0) - Cost: $10 | Payback: $8 | Current Balance: $48',
            'lead ($0) | silver ($4) | gold ($10) - Cost: $10 | Payback: $14 | Current Balance: $52',
            'lead ($0) | lead ($0) | copper ($2) - Cost: $10 | Payback: $2 | Current Balance: $44',
            'copper ($2) | lead ($0) | copper ($2) - Cost: $10 | Payback: $4 | Current Balance: $38',
            'lead ($0) | lead ($0) | lead ($0) - Cost: $10 | Payback: $0 | Current Balance: $28',
            'lead ($0) | lead ($0) | silver ($4) - Cost: $10 | Payback: $4 | Current Balance: $22',
            'silver ($4) | silver ($4) | silver ($4) - Cost: $10 | Payback: $12 | Current Balance: $24',
            'copper ($2) | silver ($4) | lead ($0) - Cost: $10 | Payback: $6 | Current Balance: $20',
            'lead ($0) | lead ($0) | copper ($2) - Cost: $10 | Payback: $2 | Current Balance: $12',
            'copper ($2) | copper ($2) | silver ($4) - Cost: $10 | Payback: $8 | Current Balance: $10',
            'copper ($2) | silver ($4) | silver ($4) - Cost: $10 | Payback: $10 | Current Balance: $10',
            'copper ($2) | lead ($0) | silver ($4) - Cost: $10 | Payback: $6 | Current Balance: $6']

        self.game_frame = Frame()
        self.game_frame.grid()

        # Heading Row
        self.heading_label = Label(self.game_frame, text="play...",
                                   font="Arial 19 bold", padx=10,
                                   pady=10)
        self.heading_label.grid(row=0)

        # help Button (row 1)
        self.stats_button = Button(self.game_frame,
                                   text="Arial 14", padx=10, pady=10,
                                   command=lambda: self.to_stats(self.round_stats_list))
        self.stats_button.grid(row=1)

    def to_stats(self, game_help, game_stats):
        GameStats(self, game_help, game_stats)


class GameStats:
    def __init__(self, partner, game_help, game_stats):

        print(game_help)

        # disable help button
        partner.stats_button.config(state=DISABLED)

        heading = "Arial 12 bold"
        content = "Arial 12"

        # If users press cross at top, closes help and 'releases' help button
        self.help_box.protocol('WM_DELETE_WINDOW', partial(self.close_help, partner))

        # Set up GUI Frame
        self.help_frame = Frame(self.help_box, width=300, bg=background)
        self.help_frame.grid()

        # Set up help heading (row 0)
        self.how_heading = Label(self.help_frame, text="help / Instruction",
                                 font="arial 10 bold", bg=background)
        self.how_heading.grid(row=0)
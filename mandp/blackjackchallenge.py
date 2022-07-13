import random

try:
    import tkinter
except ImportError:
    import Tkinter as tkinter


def loadimages(card_images):
    suits = ['heart', 'club', 'diamond', 'spade']
    face_cards = ['jack', 'queen', 'king']

    if tkinter.TkVersion >= 8.6:
        extension = 'ppm'
    else:
        extension = 'ppm'

    # for each suit retrieve the image for the cards,
    for suit in suits:
        # first number cards 1 - 10
        for card in range(1, 11):
            name = 'cards/{}_{}.{}'.format(str(card), suit, extension)
            image = tkinter.PhotoImage(file=name)
            card_images.append((card, image))

        # next the face cards
        for card in face_cards:
            name = 'cards/{}_{}.{}'.format(str(card), suit, extension)
            card_images.append((10, image))


def deal_card(frame):
    # pop the next card
    next_card = deck.pop(0)
    tkinter.Label(frame, image=next_card[1], relief='raised').pack(side='left')
    deck.append(next_card)
    return next_card


def score_hand(hand):
    score = 0
    ace = False
    for next_card in hand:
        card_value = next_card[0]
        if card_value == 1 and not ace:
            ace = True
            card_value = 11
        score += card_value
        if score > 21 and ace:
            score -= 10
            ace = False
    return score


def deal_dealer():
    global dealer_wins_inc
    global player_wins_inc
    global dealer_wins_label
    global player_wins_label

    dealer_score = score_hand(dealer_hand)
    while 0 < dealer_score < 17:
        dealer_hand.append(deal_card(dealer_card_frame))
        dealer_score = score_hand(dealer_hand)
        dealer_score_label.set(dealer_score)

    player_score = score_hand(player_hand)
    if player_score > 21:
        result_text.set("Dealer wins!")
        dealer_wins_inc += 1
        dealer_wins_label.set(dealer_wins_inc)
    elif dealer_score > 21 or dealer_score < player_score:
        result_text.set("Player wins!")
        player_wins_inc += 1
        player_wins_label.set(player_wins_inc)
    elif dealer_score > player_score:
        result_text.set("Dealer wins!")
        dealer_wins_inc += 1
        dealer_wins_label.set(dealer_wins_inc)
    else:
        result_text.set("Draw!")


def deal_player():
    global dealer_wins_inc
    global player_wins_inc
    global dealer_wins_label
    global player_wins_label

    player_hand.append(deal_card(player_card_frame))
    player_score = score_hand(player_hand)

    player_score_label.set(player_score)
    if player_score > 21:
        result_text.set("Dealer Wins!")
        dealer_wins_inc += 1
        dealer_wins_label.set(dealer_wins_inc)


def init_deal():
    deal_player()
    dealer_hand.append(deal_card(dealer_card_frame))
    dealer_score_label.set(score_hand(dealer_hand))
    result_text.set("")
    deal_player()

def new_game():
    global dealer_card_frame
    global player_card_frame
    global dealer_hand
    global player_hand
    global dealer_wins
    global player_wins
    dealer_hand = []
    player_hand = []

    dealer_card_frame.destroy()
    player_card_frame.destroy()

    tkinter.Label(card_frame, text="Dealer", background="green", fg="white").grid(row=0, column=0)
    tkinter.Label(card_frame, textvariable=dealer_score_label, background="green", fg="white").grid(row=1, column=0)

    dealer_card_frame = tkinter.Frame(card_frame, background="green")
    dealer_card_frame.grid(row=0, column=1, sticky='ew', rowspan=2)

    player_card_frame = tkinter.Frame(card_frame, background="green")
    player_card_frame.grid(row=2, column=1, sticky='ew', rowspan=2)

    init_deal()

def play():
    init_deal()
    mainWindow.mainloop()

cards = []
player_wins_inc = 0
dealer_wins_inc = 0

mainWindow = tkinter.Tk()

# set up the screen and frames
mainWindow.title("Blackjack")
mainWindow.geometry("640x480")
mainWindow.configure(background="Green")

result_text = tkinter.StringVar()
result = tkinter.Label(mainWindow, textvariable=result_text)
result.grid(row=0, column=0, columnspan=2)

playerpanel = tkinter.Frame(mainWindow, relief="sunken", borderwidth=1)
playerpanel.grid(row=0, column=1, columnspan=5)

player_tally = tkinter.Label(playerpanel, text="Player Score:")
player_tally.grid(row=0, column=0, columnspan=2)

player_wins_label = tkinter.IntVar()
tkinter.Label(playerpanel, textvariable=player_wins_label).grid(row=0, column=2, columnspan=2, sticky='w')

dealerpanel = tkinter.Frame(mainWindow, relief="sunken", borderwidth=1)
dealerpanel.grid(row=0, column=3, columnspan=5)

dealer_tally = tkinter.Label(dealerpanel, text="Dealer Score:")
dealer_tally.grid(row=0, column=0, columnspan=2)

dealer_wins_label = tkinter.IntVar()
tkinter.Label(dealerpanel, textvariable=dealer_wins_label).grid(row=0, column=2, columnspan=2, sticky='w')

card_frame = tkinter.Frame(mainWindow, relief="sunken", borderwidth=1, background="green")
card_frame.grid(row=1, column=0, sticky='ew', columnspan=3, rowspan=2)

dealer_score_label = tkinter.IntVar()
tkinter.Label(card_frame, text="Dealer", background="green", fg="white").grid(row=0, column=0)
tkinter.Label(card_frame, textvariable=dealer_score_label, background="green", fg="white").grid(row=1, column=0)

# embedded frame to hold the card images
dealer_card_frame = tkinter.Frame(card_frame, background="green")
dealer_card_frame.grid(row=0, column=1, sticky='ew', rowspan=2)

player_score_label = tkinter.IntVar()
player_score = 0
player_ace = False

tkinter.Label(card_frame, text="Player", background="green", fg="white")
tkinter.Label(card_frame, textvariable=player_score_label, background="green", fg="white").grid(row=3, column=0)

# embedded frame to hold the card images
player_card_frame = tkinter.Frame(card_frame, background="green")
player_card_frame.grid(row=2, column=1, sticky='ew', rowspan=2)

button_frame = tkinter.Frame(mainWindow)
button_frame.grid(row=3, column=0, columnspan=3, sticky='w')

dealer_button = tkinter.Button(button_frame, text="Dealer", command=deal_dealer)
dealer_button.grid(row=0, column=0)

player_button = tkinter.Button(button_frame, text="Player", command=deal_player)
player_button.grid(row=0, column=1)

reset_button = tkinter.Button(button_frame, text="Reset Game", command=new_game)
reset_button.grid(row=0, column=2)

# load cards
loadimages(cards)
print(cards)

# creata a new deck of card and shuffle them
deck = list(cards)

random.shuffle(deck)

dealer_hand = []
player_hand = []

deal_player()
dealer_hand.append(deal_card(dealer_card_frame))
dealer_score_label.set(score_hand(dealer_hand))
deal_player()

if __name__ == "__main__":
    play()


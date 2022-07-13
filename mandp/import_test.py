import blackjack

g = sorted(globals())

for x in g:
    print(x)

blackjack._deal_card(blackjack.dealer_card_frame)
# print(__name__)
# blackjack._deal_card(blackjack.dealer_card_frame)
blackjack.play()
# print(blackjack.cards)


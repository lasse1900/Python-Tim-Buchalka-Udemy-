# from blackjack import *
import blackjack

# from command line: python -m blackjack
# print(__name__)
#
# blackjack._deal_card(blackjack.dealer_card_frame)
# blackjack.play()
# print(blackjack.cards)

# g = sorted(globals())
#
# for x in g:
#     print(x)

blackjack._deal_card(blackjack.dealer_card_frame)
blackjack.play()

# Just example:
personal_details = ("Tim", 24, "Austria")

name, _, country = personal_details
print(name, country)
print(_)
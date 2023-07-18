import random

user = input(
    "Do you want to play a game of blackjack? Type 'y' for yes and 'n' for no: "
)
"""should_continue= True
if user=="n":
    should_continue= False"""


def deal_cards():
    #returns a random card
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    d_card = random.choice(cards)
    return d_card


def calculations(card):
    for i in range(len(card)):
        total = int(sum((card[i])))
        i += 1
    if i == 2:
        if total == 21:
            print("Win")
            return (0)
        if 11 in card and total > 21:
            card.remove(11)
            card.append(1)
        if total>21:
          print("the end")
        else:
            return (total)


user_card = []
user_card.append(deal_cards())
user_card.append(deal_cards())
print(f"Your cards: {user_card}")

computer_card = []
computer_card.append(deal_cards())
print(f"computer's card: ", computer_card)
computer_card.append(deal_cards())
print(calculations(user_card),calculations(computer_card))

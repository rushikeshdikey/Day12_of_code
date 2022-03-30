# start to python day-12 code
# starting code is basics learned
# main project code at end

# Author: Rushikesh Dikey
# Date: 30-03-2022
import random
import art
print(art.logo)


cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

card = random.choice(cards)
print(card)

deal_cards = {}

user_cards = []
computer_cards = []

for _ in range(2):
    user_cards.append(deal_cards)
    computer_cards.append(deal_cards)

print(user_cards)
print(computer_cards)
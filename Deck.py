import random
deck=[]
suits = ["C", "D", "S", "H"] # clubs, diamond, spade, heart
ranks = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
# this is so I can do the probabilities
card_rank = {
    '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10,
    'J': 11, 'Q': 12, 'K': 13, 'A': 14
}
card_suit = {
    'C': 1, 'D': 2, 'H': 3, 'S': 4
}
def card2rank(card):
    rank = card[:-1]  # Get the rank (e.g., "J" from "JH")
    return card_rank[rank]

def card2suit(card):
    suit = card[-1]  # Get the suit (e.g., "H" from "JH")
    return card_suit[suit]
                                    # How prints in different place effect it
for suit in suits:                  # same indentation as this line will give me the finished product
    for rank in ranks:              # same indentation as this line will give me it to me suit by suit
        card = rank + suit          # same indentation as this line will give me it to me card by card
        deck.append(card)
print(len(deck))
random.shuffle(deck)

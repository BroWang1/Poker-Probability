import random
deck=[]
suits = ["C", "D", "S", "H"] # clubs, diamond, spade, heart
ranks = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
# this is so I can do the probabilities
card_rank = {
    '2': 1, '3': 2, '4': 3, '5': 4, '6': 5, '7': 6, '8': 7, '9': 8, '10': 9,
    'J': 12, 'Q': 11, 'K': 12, 'A': 13
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

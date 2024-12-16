deck=[]
suits = ["C", "D", "S", "H"] # clubs, diamond, spade, heart
ranks = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
                                    # How prints in different place effect it
for suit in suits:                  # same indentation as this line will give me the finished product
    for rank in ranks:              # same indentation as this line will give me it to me suit by suit
        card = rank + suit          # same indentation as this line will give me it to me card by card
        deck.append(card)

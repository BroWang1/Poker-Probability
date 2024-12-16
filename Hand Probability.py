from Deck import deck # I wanted to test out how this import works from different .py files
import random
import math

random.shuffle(deck)
# this is so I can do the probabilities
card_values = {
    '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10,
    'J': 11, 'Q': 12, 'K': 13, 'A': 14
}

num_players = input("How many players are playing? (Please give numerical values)" + "\n")
user_input = input("Enter Hand(EX.JH,AC - Jack of hearts, Ace of Clubs):"+ "\n")

user_hand = user_input.replace(" ", "").split(",")# cleaning/normalizing the answers
print(user_hand)

def card2value(card):
    rank = card[:-1]  # Get the rank (e.g., "J" from "JH")
    return card_values[rank]

for card in user_hand: # this is to remove the hand from the deck
    if card in deck:
        deck.remove(card)
    #print(len(deck))

other_cards = (int(num_players)-1)*2 # every player has 2 cards
for cr in range(other_cards):   # CR=cards removed; Now it is time to randomly remove the number of cards in the other players hand
    randomly_rem = random.choice(deck)
    deck.remove(randomly_rem)
#print(len(deck))

value_hand = [card2value(card) for card in user_hand]
#print(value_hand)
#value_community_cards = [card2value(card) for card in input_community_cards]
def high_card(value_hand,other_cards):
    all = math.comb(50,other_cards)# the denominator
    higher = 14 - max(value_hand)
    if higher == 0:
        if value_hand == ['14', '14']:
            amt_higher = 2
        elif 14 in value_hand:
            amt_higher = 3
    else:
        amt_higher = higher * 4
    high_card = math.comb(50-amt_higher,other_cards)/all
    return high_card
print(high_card(value_hand,other_cards,))
print(f'The chances the opponent has a higher card than you:{1-high_card(value_hand,other_cards)}')
# def evaluate_hand(value_hand, value_community_cards):
#
#         cards = value_hand + value_community_cards # This allows them to be seen as a group
#         return {
#             "high_card": high_card(value_hand,other_cards),
#             "pairs": pairs(cards),
#             "three_of_a_kind": trips(cards),
#             "straight": straight(cards),
#             "flush": flush(cards),
#             "full_house": full_house(cards),
#             "four_of_a_kind": quads(cards),
#             "straight_flush": str_flush(cards),
#         }
#









    # pair =
    # two_pair =
    # trips =
    # quads =
    # straight =
    # flush =
    # full_house =
    # str_flush =
    # roy_flush =
    #
    # total_prob = high_card + pair + two_pair + trips + quads + straight + flush + full_house + str_flush + roy_flush

input_community_cards = input("What are the first 3 community cards?(EX.2H,8C,7D)")
community_cards = user_input.replace(" ", "").split(",")# cleaning/normalizing the answers
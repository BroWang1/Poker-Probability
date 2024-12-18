from Deck import deck, card2rank,card2suit          #i wanted to test out how this import works from different .py files
import math

community_cards = []
suit_community_cards = []
rank_community_cards = []

                                                    #to get initial info like players and hand
num_players = input("How many players are playing? (Please give numerical values)" + "\n")
otherp_cards = (int(num_players)-1)*2                                # every player has 2 cards
user_input = input("Enter Hand(EX.6H,5C - Six of Hearts, 5 of Clubs):" + "\n").upper()
user_hand = user_input.replace(" ", "").split(",")      # cleaning/normalizing the answers
print(user_hand)

for card in user_hand:                                              # this is to remove the hand from the deck
    if card in deck:
        deck.remove(card)
print(len(deck))

suit_hand = [card2suit(card) for card in user_hand]
print(suit_hand)
rank_hand = [card2rank(card) for card in user_hand]
print(rank_hand)

unseen_cards = len(deck) - len(community_cards)
total_combo = math.comb(unseen_cards, otherp_cards)  # the denominator
num_cardHigher = 14 - max(rank_hand)

amt_higher = 0
if num_cardHigher == 0:  # if there are aces
    if rank_hand == ['14', '14']:  # if there are pocket aces need to change this
        amt_higher = 2
    elif rank_hand.count(14) == 1:  # if there is a ace in hand
        amt_higher = 3
else:
    amt_higher = num_cardHigher * 4 #4 suits per higher card

rank_board = rank_hand + rank_community_cards
suit_board = suit_hand + suit_community_cards

lowerC_deck = len(deck) - amt_higher
def high_card(rank_hand, suit_community_cards, rank_community_cards):
    rank_board = rank_hand + rank_community_cards
    suit_board = suit_hand + suit_community_cards
    if any(rank_board.count(rank) >= 2 for rank in set(rank_board)):      #Checking for pairs, trips, quads
        print('0% - Better Hand Available')
        return
    elif any(suit_board.count(card) >= 5 for card in suit_board):      #Checking for flushes
        print('0% - Better Hand Available')
        return
    elif len(rank_board) >= 5:
        sort = sorted(rank_board)
        if any(
                sort[i + 1] == sort[i] + 1 and
                sort[i + 2] == sort[i] + 2 and
                sort[i + 3] == sort[i] + 3 and
                sort[i + 4] == sort[i] + 4
            for i in range(len(rank_board) - 4)
            ):
            print('0% - Better Hand Available')
            return

    high_rankin_hand = max(rank_hand)  # highest card in hand
    num_higherCC = sum(1 for rank in rank_community_cards if rank > high_rankin_hand)
    num_lowerCC = len(rank_community_cards) - num_higherCC
    possible_lowerC = math.comb((lowerC_deck - num_lowerCC + num_higherCC), otherp_cards)
    high_card = possible_lowerC / total_combo
    return high_card

#def pair(rank_hand, suit_community_cards, rank_community_cards):
#def two_pair(rank_hand, suit_community_cards, rank_community_cards):                 # give them the length two win
#def trips(rank_hand, suit_community_cards, rank_community_cards):
#def quads(rank_hand, suit_community_cards, rank_community_cards):
#def straight(rank_hand, suit_community_cards, rank_community_cards):                 # give them the length two win
#def flush(rank_hand, suit_community_cards, rank_community_cards):                    # give them the length two win
#def full_house(rank_hand, suit_community_cards, rank_community_cards):               # give them the length two win
#def str_flush(rank_hand, suit_community_cards, rank_community_cards):                # give them the length two win
#def roy_flush(rank_hand, suit_community_cards, rank_community_cards):                # give them the length two win
def evaluate_hand(rank_hand,suit_community_cards, rank_community_cards):
    return {
             "high_card": high_card(rank_hand,suit_community_cards, rank_community_cards),
#             "pairs": pairs(cards),
#             "two_pairs": two_pairs(cards),
#             "three_of_a_kind": trips(cards),
#             "straight": straight(cards),
#             "flush": flush(cards),
#             "full_house": full_house(cards),
#             "four_of_a_kind": quads(cards),
#             "straight_flush": str_flush(cards),
         }

    # total_prob = high_card + pair + two_pair + trips + quads + straight + flush + full_house + str_flush + roy_flush

preflop = evaluate_hand(rank_hand,suit_community_cards, rank_community_cards)
print(preflop)
def update_community_cards(input_cards, community_cards, deck):     #this grabs the new cards and normalizes them and put the in the community cards
    new_cards = input_cards.replace(" ", "").split(",")
    community_cards += new_cards
    for card in new_cards:      # this is to change the length of the board and remove the known cars
        if card in deck:
            deck.remove(card)
    return community_cards, deck

input_community_cards = input("Enter the first 3 community cards (e.g., 9H, 8C, 7D): " + "\n").upper()
community_cards, deck = update_community_cards(input_community_cards, community_cards, deck)

suit_community_cards = [card2suit(card) for card in community_cards]
rank_community_cards = [card2rank(card) for card in community_cards]

postflop_high_card = high_card(rank_hand, suit_community_cards, rank_community_cards)
print(postflop_high_card)

# Repeat for 4th and 5th cards
for round_num in range(4, 6):
    input_card = input(f"Enter the {round_num}th community card: " + "\n").upper()
    community_cards, deck = update_community_cards(input_card, community_cards, deck)

    suit_community_cards = [card2suit(card) for card in community_cards]
    rank_community_cards = [card2rank(card) for card in community_cards]

    probability = high_card(rank_hand, suit_community_cards, rank_community_cards)
    print(probability)
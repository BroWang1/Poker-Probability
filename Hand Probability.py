from Deck import deck, card2rank,card2suit          #i wanted to test out how this import works from different .py files
import random
import math

                                                    #to get initial info like players and hand
num_players = input("How many players are playing? (Please give numerical values)" + "\n")
otherp_cards = (int(num_players)-1)*2                                # every player has 2 cards
user_input = input("Enter Hand(EX.QH,5C - Queen of Hearts, 5 of Clubs):" + "\n").upper()
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

community_cards = []
suit_community_cards = []
rank_community_cards = []

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

lowerC_deck = (len(deck) - amt_higher)
def high_card(rank_hand, community_cards, rank_community_cards):
    if not community_cards:     #preflop
        high_card = math.comb((lowerC_deck), otherp_cards) / total_combo
        return high_card
    # comb1 = math.comb(lowerC_deck, otherp_cards) # combo number of cards lower to the number of other players cards
    # comb2 = math.comb(lowerC_deck - otherp_cards, 5 - len(community_cards))


    elif community_cards:       #postflop
        high_rankin_hand = max(rank_hand) # highest card in hand
        num_higherCC = sum(1 for rank in rank_community_cards if rank > high_rankin_hand)
        num_lowerCC = len(rank_community_cards) - num_higherCC
        if any(rank_board.count(card) > 1 for card in rank_board):                    #using a comprehension would make it better
            print('0% - Better Hand Available')
        else:
            high_card = math.comb((len(deck) - num_lowerCC - amt_higher + num_higherCC), otherp_cards - num_higherCC) / total_combo
            return high_card



print(high_card(rank_hand,community_cards, rank_community_cards))


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
input_community_cards = input("What are the first 3 community cards?(EX.2H,8C,7D)" + "\n").upper()
community_cards = input_community_cards.replace(" ", "").split(",")
for knownC in range(len(community_cards)):                                       # known cards in the community
     randomly_rem = random.choice(deck)
     deck.remove(randomly_rem)
print(len(deck))


rank_community_cards = [card2rank(card) for card in community_cards]# cleaning/normalizing the answers
postflop_high_card = high_card(rank_hand,community_cards, rank_community_cards)
print(postflop_high_card)
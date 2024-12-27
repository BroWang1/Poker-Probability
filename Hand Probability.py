from Deck import deck, card2rank, card2suit#, card_rank, card_suit          # I wanted to test out how this import works from different .py files
import math
#import sys


community_cards = []
suit_community_cards = []
rank_community_cards = []

# to get initial info like players and hand
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
num_cardHigher = 13 - max(rank_hand)

amt_higher = 0
if num_cardHigher == 0:  # if there are aces
    if rank_hand == ['13', '13']:  # if there are pocket aces need to change this
        amt_higher = 2
    elif rank_hand.count(13) == 1:  # if there is an ace in hand
        amt_higher = 3
else:
    amt_higher = num_cardHigher * 4     # 4 suits per higher card


def high_card(rank_hand, suit_community_cards, rank_community_cards):
    lowerC_deck = len(deck) - amt_higher
    totalunseen_combo = math.comb(unseen_cards, otherp_cards)  # the denominator
    rank_board = rank_hand + rank_community_cards
    suit_board = suit_hand + suit_community_cards
    if any(rank_board.count(rank) >= 2 for rank in set(rank_board)):      # Checking for pairs, trips, quads
        return '0% - Better Hand Available'
    elif any(suit_board.count(card) >= 5 for card in suit_board):      # Checking for flushes
        return '0% - Better Hand Available'
    elif len(rank_board) >= 5:
        sort = sorted(rank_board)
        if any(
                sort[i + 1] == sort[i] + 1 and
                sort[i + 2] == sort[i] + 2 and
                sort[i + 3] == sort[i] + 3 and
                sort[i + 4] == sort[i] + 4
            for i in range(len(rank_board) - 4)
            ):
            return '0% - Better Hand Available'

    high_rankin_hand = max(rank_hand)  # highest card in hand
    num_higherCC = sum(1 for rank in rank_community_cards if rank >= high_rankin_hand)
    num_lowerCC = sum(1 for rank in rank_community_cards if rank < high_rankin_hand)
    possible_lowerC = math.comb((lowerC_deck - num_lowerCC + num_higherCC), otherp_cards)
    high_card_prob = possible_lowerC / totalunseen_combo
    return high_card_prob


def pair(rank_hand, suit_community_cards, rank_community_cards):
    rank_board = rank_hand + rank_community_cards
    suit_board = suit_hand + suit_community_cards
    if any(rank_board.count(rank) >= 3 for rank in set(rank_board)):    # Checking for trips, quads
        return '0% - Better Hand Available'
    elif any(suit_board.count(card) >= 5 for card in suit_board):       # Checking for flushes
        return '0% - Better Hand Available'
    elif len(rank_board) >= 5:                                          # Checking for Straight
        sort = sorted(rank_board)
        if any(
                sort[i + 1] == sort[i] + 1 and
                sort[i + 2] == sort[i] + 2 and
                sort[i + 3] == sort[i] + 3 and
                sort[i + 4] == sort[i] + 4
            for i in range(len(rank_board) - 4)
            ):
            return '0% - Better Hand Available'
    if rank_hand[0] == rank_hand[1]:
        print(rank_hand[0])
        higher_pockets = (13 - rank_hand[0]) * math.comb(4, 2)
        print(higher_pockets)
        lowerpair = ((1 - (higher_pockets / math.comb(len(deck), 2))) ** (int(num_players) - 1))
        if lowerpair == 0:
            lowerpair = 1
        return lowerpair

    pairs = 0
    for user_card in rank_hand:
        for cc_card in rank_community_cards:
            if user_card == cc_card:
                pairs += 1
    if pairs == 1:
        matches = [user_card for user_card in rank_hand if user_card in rank_community_cards]
        if matches:
            matching_card = matches[0]
            num_higherCC = sum(1 for rank in rank_community_cards if rank >= matching_card)
            num_lowerCC = sum(1 for rank in rank_community_cards if rank < matching_card)
            higher = (13 - rank_hand[0])
            if higher == 0:
                higher = 1
                higherpairs = higher * math.comb(4, 2) - (3 * num_lowerCC) + (3 * num_higherCC)
                print(higherpairs)
                pair = ((1 - (higherpairs / math.comb(len(deck), 2))) ** (int(num_players) - 1))  # there is a 3 because the difference between C(4,2) and C(3,2) is 3
                return pair
            if higher > 0:
                higherpairs = higher * math.comb(4, 2) - (3 * num_lowerCC)  + (3 * num_higherCC)
                print(higherpairs)
                pair_prob = ((1 - (higherpairs / math.comb(len(deck), 2))) ** (int(num_players) - 1)) # there is a 3 because the difference between C(4,2) and C(3,2) is 3
                return pair_prob
    elif pairs == 2:
        return '0% - Better Hand Available'


def two_pair(rank_hand, suit_community_cards, rank_community_cards):
    rank_board = rank_hand + rank_community_cards
    suit_board = suit_hand + suit_community_cards
    if any(rank_board.count(rank) >= 3 for rank in set(rank_board)):  # Checking for trips, quads
        return '0% - Better Hand Available'
    elif any(suit_board.count(card) >= 5 for card in suit_board):  # Checking for flushes
        return '0% - Better Hand Available'
    elif len(rank_board) >= 5:  # Checking for Straight
        sort = sorted(rank_board)
        if any(
                sort[i + 1] == sort[i] + 1 and
                sort[i + 2] == sort[i] + 2 and
                sort[i + 3] == sort[i] + 3 and
                sort[i + 4] == sort[i] + 4
                for i in range(len(rank_board) - 4)
        ):
            return '0% - Better Hand Available'
    #for pairs in rank_board:
        ##this is for when you have a pair in hand and the board gets a flop

    pairs = 0 # this is for if both of your cards get a pair from the board
    for user_card in rank_hand:
        for cc_card in rank_community_cards:
            if user_card == cc_card:
                pairs += 1
    if pairs == 2:
        matches = [user_card for user_card in rank_hand if user_card in rank_community_cards]
        if matches:
            matching_card = max(matches)
            num_higherCC = sum(1 for rank in rank_community_cards if rank >= matching_card)
            num_lowerCC = sum(1 for rank in rank_community_cards if rank < matching_card)
            highertwopairs = (num_higherCC * 3) * (num_lowerCC * 3) # the number of chances some player might have a higher hand
            two_pair_prob = ((1 - (highertwopairs / math.comb(len(deck), 2))) ** (int(num_players) - 1))
            return two_pair_prob


def trips(rank_hand, suit_community_cards, rank_community_cards):
    rank_board = rank_hand + rank_community_cards
    suit_board = suit_hand + suit_community_cards
    if any(rank_board.count(rank) >= 4 for rank in set(rank_board)):  # Checking for quads
        return '0% - Better Hand Available'
    elif any(suit_board.count(card) >= 5 for card in suit_board):  # Checking for flushes
        return '0% - Better Hand Available'
    elif len(rank_board) >= 5:  # Checking for Straight
        sort = sorted(rank_board)
        if any(
                sort[i + 1] == sort[i] + 1 and
                sort[i + 2] == sort[i] + 2 and
                sort[i + 3] == sort[i] + 3 and
                sort[i + 4] == sort[i] + 4
                for i in range(len(rank_board) - 4)
        ):
            return '0% - Better Hand Available'
    rank_counts = [rank_board.count(rank) for rank in set(rank_board)]
    if 3 in rank_counts and 2 in rank_counts:   # checking for full house
        return '0% - Better Hand Available'
    triple_rank = None
    for rank in set(rank_board):
        if rank_board.count(rank) == 3:
            triple_rank = rank
            break
    if triple_rank is not None:
        num_higherCC = sum(1 for rank in rank_community_cards if rank > triple_rank)
        num_lowerCC = sum(1 for rank in rank_community_cards if rank < triple_rank)
        highertrips = num_higherCC * math.comb(4,3)
        if highertrips == 0 and max(rank_hand) == 13:
            highertrips = 1
        else:
            highertrips = num_higherCC * math.comb(4, 3)
        print(highertrips)
        trips_prob = ((1 - (highertrips / math.comb(len(deck), 2))) ** (int(num_players) - 1))       # there is a 3 because the difference between C(4,2) and C(3,2) is 3
        return trips_prob


def straight(rank_hand, suit_community_cards, rank_community_cards):
    rank_board = rank_hand + rank_community_cards
    suit_board = suit_hand + suit_community_cards
    if any(suit_board.count(card) >= 5 for card in suit_board):  # Checking for any straight flushes
        if len(rank_board) >= 5:
            sort = sorted(rank_board)
            if any(
                    sort[i + 1] == sort[i] + 1 and
                    sort[i + 2] == sort[i] + 2 and
                    sort[i + 3] == sort[i] + 3 and
                    sort[i + 4] == sort[i] + 4
                    for i in range(len(rank_board) - 4)
            ):
                return '0% - Better Hand Available'
    if any(rank_board.count(rank) >= 4 for rank in set(rank_board)):  # Checking for quads
        return '0% - Better Hand Available'
    elif any(suit_board.count(card) >= 5 for card in suit_board):  # Checking for flushes
        return '0% - Better Hand Available'


    community_card_ranks = {}               # To know where each card is coming from
    for rank in rank_community_cards:
        community_card_ranks[rank] = "community"
    user_ranks = {}
    for rank in rank_hand:
        user_ranks[rank] = "user"
    rank_board = list(community_card_ranks.keys()) + list(user_ranks.keys())
    #print(rank_board)
    if 13 in rank_board and {2, 3, 4, 5}.intersection(rank_board):
        adjusted_rank_board = [0 if rank == 13 else rank for rank in rank_board]
    else:
        adjusted_rank_board = rank_board
    sorted_board_rank = sorted(adjusted_rank_board)
    #print(sorted_board_rank)
    for i in range(len(sorted_board_rank) - 4):
        if sorted_board_rank[i + 4] - sorted_board_rank[i] == 4:
            straight_cards = sorted_board_rank[i:i + 5]
            highest_community_card = max([card for card in straight_cards if community_card_ranks.get(card, None) == "community"], default=None)
            #print(highest_community_card)
            highest_user_card = max([card for card in straight_cards if user_ranks.get(card, None) == "user"], default = None)
            #print(highest_user_card)
            if highest_user_card - highest_community_card == 2:
                return 1
            if highest_user_card - highest_community_card == 1:
                numhighercombo = math.comb(4,1)
                straight_prob = ((1 - (numhighercombo / math.comb(len(deck), 2))) ** (int(num_players) - 1))
                return straight_prob
            if highest_user_card - highest_community_card < 0:
                numhighercombo = math.comb(4,1) ** 2
                straight_prob = ((1 - (numhighercombo / math.comb(len(deck), 2))) ** (int(num_players) - 1))
                return straight_prob
            if 13 in rank_board and {9, 10, 11, 12}.intersection(rank_board):
                numhighercombo = math.comb(3, 1)
                straight_prob = ((1 - (numhighercombo / math.comb(len(deck), 2))) ** (int(num_players) - 1))
                return straight_prob



def flush(suit_hand, rank_hand, suit_community_cards, rank_community_cards):
    rank_board = rank_hand + rank_community_cards
    suit_board = suit_hand + suit_community_cards
    if any(suit_board.count(card) >= 5 for card in suit_board):  # Checking for any straight flushes
        if len(rank_board) >= 5:
            sort = sorted(rank_board)
            if any(
                    sort[i + 1] == sort[i] + 1 and
                    sort[i + 2] == sort[i] + 2 and
                    sort[i + 3] == sort[i] + 3 and
                    sort[i + 4] == sort[i] + 4
                    for i in range(len(rank_board) - 4)
            ):
                return '0% - Better Hand Available'
    if any(rank_board.count(rank) >= 4 for rank in set(rank_board)):  # Checking for quads
        return '0% - Better Hand Available'
    suit_mapping = {}
    for i in range(len(suit_hand)):     # labeling cards as user/cc cards & put them in suit_mapping w/ an index
        suit = suit_hand[i]
        #print(suit)
        rank = rank_hand[i]
        #print(rank)
        if suit not in suit_mapping:
            suit_mapping[suit] = []
        suit_mapping[suit].append((rank, 'user'))
    for i in range(len(suit_community_cards)):
        suit = suit_community_cards[i]
        #print(suit)
        rank = rank_community_cards[i]
        #print(rank)
        if suit not in suit_mapping:
            suit_mapping[suit] = []
        suit_mapping[suit].append((rank, 'community'))
    suit_flush = None
    for suit, cards in suit_mapping.items():
        if len(cards) >= 5:
            suit_flush = suit
        #print(suit, cards)
    if suit_flush:
        flush_cards = suit_mapping[suit_flush]
        #print(flush_cards)
        user_ranks = [rank for rank, source in flush_cards if source == 'user']
        #print(user_ranks)
        community_ranks = [rank for rank, source in flush_cards if source == 'community']
        #print(community_ranks)
        highest_hand_rank = max(user_ranks) if user_ranks else None
        #print(highest_hand_rank)
        highest_community_rank = max(community_ranks) if community_ranks else None
        #print(highest_community_rank)
        if highest_hand_rank == 13 or highest_community_rank == 13:
            return 1
        elif highest_hand_rank < highest_community_rank:
            highernumcards = 13 - highest_community_rank
            flush_prob = ((1 - (highernumcards / math.comb(len(deck), 2))) ** (int(num_players) - 1))
            return flush_prob
        elif highest_hand_rank >= highest_community_rank:
            highernumcards = 13 - highest_hand_rank
            flush_prob = ((1 - (highernumcards / math.comb(len(deck), 2))) ** (int(num_players) - 1))
            return flush_prob


def full_house(suit_hand, rank_hand, suit_community_cards, rank_community_cards):  # Needs testing
    rank_board = rank_hand + rank_community_cards
    suit_board = suit_hand + suit_community_cards
    if any(suit_board.count(card) >= 5 for card in suit_board):  # Checking for any straight flushes
        if len(rank_board) >= 5:
            sort = sorted(rank_board)
            if any(
                    sort[i + 1] == sort[i] + 1 and
                    sort[i + 2] == sort[i] + 2 and
                    sort[i + 3] == sort[i] + 3 and
                    sort[i + 4] == sort[i] + 4
                    for i in range(len(rank_board) - 4)
            ):
                return '0% - Better Hand Available'
    if any(rank_board.count(rank) >= 4 for rank in set(rank_board)):  # Checking for quads
        return '0% - Better Hand Available'
    # community_card_ranks = {}  # To know where each card is coming from
    # for rank in rank_community_cards:
    #     community_card_ranks[rank] = "community"
    # print(community_card_ranks)
    # user_ranks = {}
    # for rank in rank_hand:
    #     user_ranks[rank] = "user"
    # print(user_ranks)
    # rank_board = list(community_card_ranks.keys()) + list(user_ranks.keys())
    rank_count = {}
    for rank in rank_board:     # Finding the occurence of each card
        if rank in rank_count:
            rank_count[rank] += 1
        else:
            rank_count[rank] = 1
        print(rank_count)
        findtrip_house = [rank for rank,count in rank_count.items() if count >= 3]
        findpair_house = [rank for rank,count in rank_count.items() if count >= 2]
        findtrip_house.sort(reverse=True)
        findpair_house.sort(reverse=True)
        if not findtrip_house or len(findpair_house) < 2:
            return "No Full House"
        three_of_a_kind = findtrip_house[0] if findtrip_house else None
        print(three_of_a_kind)
        two_of_a_kind = None
        for rank in findpair_house:
            if rank != three_of_a_kind:
                two_of_a_kind = rank
                break
        if not two_of_a_kind:
            return "No Full House"
        community_card_ranks = {rank: "community" for rank in rank_community_cards}
        print(community_card_ranks)
        three_of_a_kind_contributors = []
        two_of_a_kind_contributors = []
        if three_of_a_kind:
            three_of_a_kind_contributors = [card for card in rank_hand if card == three_of_a_kind]
        if two_of_a_kind:
            two_of_a_kind_contributors = [card for card in rank_hand if card == two_of_a_kind]
        higher_than_three_of_a_kind = [rank for rank in rank_community_cards if rank > three_of_a_kind_contributors]
        higher_than_pair = [rank for rank in rank_community_cards if rank > two_of_a_kind_contributors]
        print(higher_than_three_of_a_kind)
        print(higher_than_pair)
        highernum3 = math.comb(3, 2) * len(higher_than_three_of_a_kind)
        highernum2 = math.comb(3, 1) * len(higher_than_pair)
        print(highernum3)
        print(highernum2)
        highernumcards = highernum3 * highernum2
        print(highernumcards)
        full_house_prob = ((1 - (highernumcards / math.comb(len(deck), 2))) ** (int(num_players) - 1))
        return full_house_prob

def quads(rank_hand, suit_community_cards, rank_community_cards):
    rank_board = rank_hand + rank_community_cards
    suit_board = suit_hand + suit_community_cards
    if any(suit_board.count(card) >= 5 for card in suit_board):  # Checking for any straight flushes
        if len(rank_board) >= 5:
            sort = sorted(rank_board)
            if any(
                    sort[i + 1] == sort[i] + 1 and
                    sort[i + 2] == sort[i] + 2 and
                    sort[i + 3] == sort[i] + 3 and
                    sort[i + 4] == sort[i] + 4
                    for i in range(len(rank_board) - 4)
            ):
                return '0% - Better Hand Available'
    quad_rank = None
    for rank in set(rank_board):
        if rank_board.count(rank) == 4:
            quad_rank = rank
            break
    if quad_rank is not None:
        num_higherCC = sum(1 for rank in rank_community_cards if rank > quad_rank)
        num_lowerCC = sum(1 for rank in rank_community_cards if rank < quad_rank)
        higherquads = num_higherCC * math.comb(4,4)
        print(higherquads)
        quads_prob = ((1 - (higherquads / math.comb(len(deck), 2))) ** (int(num_players) - 1))  # there is a 3 because the difference between C(4,2) and C(3,2) is 3
        return quads_prob   # It is not working right now so I need to fix this


# def str_flush(suit_hand, rank_hand, suit_community_cards, rank_community_cards):
#     return str_flush_prob


def roy_flush(suit_hand, rank_hand, suit_community_cards, rank_community_cards):
    return 1


def evaluate_hand(suit_hand, rank_hand, suit_community_cards, rank_community_cards):
    return {
            "High_card": high_card(rank_hand,suit_community_cards, rank_community_cards),
            "Pairs": pair(rank_hand, suit_community_cards, rank_community_cards),
            "Two_pairs": two_pair(rank_hand, suit_community_cards, rank_community_cards),
            "Three_of_a_kind": trips(rank_hand, suit_community_cards, rank_community_cards),
            "Straight": straight(rank_hand, suit_community_cards, rank_community_cards),
            "Flush": flush(suit_hand, rank_hand, suit_community_cards, rank_community_cards),
            "Full_house": full_house(suit_hand, rank_hand, suit_community_cards, rank_community_cards),
            "Four_of_a_kind": quads(rank_hand, suit_community_cards, rank_community_cards),
            # "Straight_flush": str_flush(suit_hand, rank_hand, suit_community_cards, rank_community_cards):,
            "Royal_flush": roy_flush(suit_hand, rank_hand, suit_community_cards, rank_community_cards)
         }


preflop = evaluate_hand(suit_hand, rank_hand, suit_community_cards, rank_community_cards)
print(preflop)


def update_community_cards(input_cards, community_cards, deck):     # Normalizes cards and put the in the CC
    new_cards = input_cards.replace(" ", "").split(",")
    community_cards += new_cards
    for card in new_cards:      # this is to change the length of the board and remove the known cars
        if card in deck:
            deck.remove(card)
    return community_cards, deck

input_community_cards = input("Enter the first 3 community cards (e.g., 9H, 8C, 7D): " + "\n").upper()
community_cards, deck = update_community_cards(input_community_cards, community_cards, deck)
print(len(deck))
suit_community_cards = [card2suit(card) for card in community_cards]
rank_community_cards = [card2rank(card) for card in community_cards]

postflop_high_card = evaluate_hand(suit_hand, rank_hand, suit_community_cards, rank_community_cards)
print(postflop_high_card)

for round_num in range(4, 6):           # 4th and 5th cards of the community cards
    input_card = input(f"Enter the {round_num}th community card: " + "\n").upper()
    community_cards, deck = update_community_cards(input_card, community_cards, deck)

    suit_community_cards = [card2suit(card) for card in community_cards]
    rank_community_cards = [card2rank(card) for card in community_cards]
    print(f"Current Community Cards:{community_cards}")
    probability = evaluate_hand(suit_hand, rank_hand, suit_community_cards, rank_community_cards)
    print(probability)
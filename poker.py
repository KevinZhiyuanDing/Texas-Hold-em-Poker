# Texas Hold'em Poker
# Name: Kevin Ding
# Date: March 29, 2021
# Purpose: Play simplified Texas Hold'Em poker with computer.

import random

class Card:
    cardrank = {
        "A": 14, "K": 13, "Q": 12, "J": 11, "10": 10, "9": 9,
        "8": 8, "7": 7, "6": 6, "5": 5, "4": 4, "3": 3, "2": 2,
    }

    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit

    def __eq__(self, other):
        if isinstance(other, Card):
            return self.rank == other.rank and self.suit == other.suit
        return False

    def __hash__(self):
        return hash((self.rank, self.suit))

    def value(self):
        return self.cardrank[self.rank]

    def __repr__(self):
        return f"{self.rank} of {self.suit}"

class Hand:
    def __init__(self, cards):
        self.cards = cards

    def add_sum(self):
        return sum(card.value() for card in self.cards)

    def sort_by_number(self):
        self.cards.sort(key=lambda card: card.value())
        return self.cards

    def __repr__(self):
        return f"Hand({self.cards})"

class Player:
    def __init__(self, id):
        self.id = id
        self.hand = Hand([])
        self.money = 0

    def set_hand(self, cards):
        self.hand = Hand(cards)

    def __repr__(self):
        return f"Player {self.id} with {self.hand}"

class PokerGame:
    def __init__(self):
        self.players = []

    def add_player(self, player):
        self.players.append(player)

    def __repr__(self):
        return f"PokerGame with players: {self.players}"

    @staticmethod
    def check_high_card(hand):
        return len(hand) == 1

    @staticmethod
    def check_pair(hand):
        values = [card.value() for card in hand]
        return len(set(values)) < len(values)

    @staticmethod
    def check_two_pairs(hand):
        values = [card.value() for card in hand]
        return len(set(values)) == 3

    @staticmethod
    def check_three_of_a_kind(hand):
        values = [card.value() for card in hand]
        return any(values.count(value) == 3 for value in values)

    @staticmethod
    def check_straight(hand):
        values = sorted(card.value() for card in hand)
        return all(values[i] == values[i - 1] + 1 for i in range(1, len(values)))

    @staticmethod
    def check_flush(hand):
        suits = [card.suit for card in hand]
        return len(set(suits)) == 1

    @staticmethod
    def check_full_house(hand):
        values = [card.value() for card in hand]
        return len(set(values)) == 2 and any(values.count(value) == 3 for value in values)

    @staticmethod
    def check_four_of_a_kind(hand):
        values = [card.value() for card in hand]
        return any(values.count(value) == 4 for value in values)

    @staticmethod
    def check_straight_flush(hand):
        return PokerGame.check_straight(hand) and PokerGame.check_flush(hand)

    @staticmethod
    def check_royal_flush(hand):
        values = sorted(card.value() for card in hand)
        return PokerGame.check_straight_flush(hand) and values == [10, 11, 12, 13, 14]

def add_card(deck, hand):
    hand.append(deck.pop(0))

def delete_card(hand, index):
    hand.pop(index)

def validity_of_bets(tally, highbet):
    return all(bet == 0 or bet == highbet for _, bet in tally)

def check_cards(card, hand):
    return card in hand

def betting_round(activeplayer, hands, tally, highbet):
    for i in activeplayer:
        while input(f"Others look away, Player {i+1} enter 'go' to continue:\n") != "go":
            print("Sorry, invalid.")
        print("Here is your hand:", hands[i])
        while True:
            bet = input(f"Please 'check' {highbet} tokens, 'bet' {highbet*2} tokens, or 'fold' this round:\n")
            if bet == "check":
                tally[i][1] = highbet
                break
            elif bet == "bet":
                highbet *= 2
                tally[i][1] = highbet
                break
            elif bet == "fold":
                tally[i][1] = 0
                break
            else:
                print("Sorry, invalid.")
                continue
        print("\n" * 40)  # Add blank lines to prevent the next player from seeing previous bets

    while not validity_of_bets(tally, highbet):
        for i in activeplayer:
            if tally[i][1] != 0 and tally[i][1] != highbet:
                while input(f"Others look away, Player {i+1} enter 'go' to continue:\n") != "go":
                    print("Sorry, invalid.")
                print("Here is your hand:", hands[i])
                while True:
                    bet = input(f"Please 'check' {highbet} tokens, 'bet' {highbet*2} tokens, or 'fold' this round:\n")
                    if bet == "check":
                        tally[i][1] = highbet
                        break
                    elif bet == "bet":
                        highbet *= 2
                        tally[i][1] = highbet
                        break
                    elif bet == "fold":
                        tally[i][1] = 0
                        break
                    else:
                        print("Sorry, invalid.")
                        continue
            print("\n" * 40)  # Add blank lines to prevent the next player from seeing previous bets

def main():
    suits = ["clubs", "diamonds", "hearts", "spades"]
    labels = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]
    cards = [Card(label, suit) for suit in suits for label in labels]
    random.shuffle(cards)

    while True:
        p = input("How many players? (max 10 players)\n")
        if p.isdigit() and 0 < int(p) < 11:
            p = int(p)
            break
        else:
            print("Sorry, invalid.")
            continue

    hands = [[f"Player {i+1}"] + [cards.pop(0) for _ in range(2)] for i in range(p)]
    for hand in hands:
        hand[1:3] = sorted(hand[1:3], key=lambda card: card.value())

    highbet = 1
    pot = p
    tally = [[f"Player {i+1}", 1] for i in range(p)]

    print("Each player looks at their cards and determines to 'check', 'bet', or 'fold'. The starting bet for everyone is 1 chip")
    betting_round(range(p), hands, tally, highbet)

    pot += sum(bet for _, bet in tally)
    print("\nHere is the amount of chips in the pot at stake:", pot)

    activeplayer = [i for i in range(p) if tally[i][1] == highbet]
    if len(activeplayer) == 1:
        print(f"Player {activeplayer[0]+1} is the only one who didn't fold. He wins the pot of {pot} chips.")
        return

    # The flop
    print("Only people who have not folded will continue to the next round. Including:")
    for i in activeplayer:
        print(f"Player {i+1}")

    flop = [cards.pop(0) for _ in range(3)]
    print("The flop is", flop)

    print("We will begin a new round of betting with the remaining players.\n")
    betting_round(activeplayer, hands, tally, highbet)

    pot += sum(bet for _, bet in tally)
    print("\nHere is the amount of chips in the pot at stake:", pot)

    activeplayer = [i for i in range(p) if tally[i][1] == highbet]
    if len(activeplayer) == 1:
        print(f"Player {activeplayer[0]+1} is the only one who didn't fold. He wins the pot of {pot} chips.")
        return

    # The turn
    print("These people who have not folded will continue to the next round. Including:")
    for i in activeplayer:
        print(f"Player {i+1}")

    turn = flop + [cards.pop(0)]
    print("The turn is", turn)

    print("We will begin the next round of betting with the remaining players.\n")
    betting_round(activeplayer, hands, tally, highbet)

    pot += sum(bet for _, bet in tally)
    print("\nHere is the amount of chips in the pot at stake:", pot)

    activeplayer = [i for i in range(p) if tally[i][1] == highbet]
    if len(activeplayer) == 1:
        print(f"Player {activeplayer[0]+1} is the only one who didn't fold. He wins the pot of {pot} chips.")
        return
    
    # The river
    print("These people who have not folded will continue to the final round. Including:")
    for i in activeplayer:
        print(f"Player {i+1}")

    river = turn + [cards.pop(0)]
    print("The river is", river)

    print("We will begin the final round of betting with the remaining players.\n")
    betting_round(activeplayer, hands, tally, highbet)

    pot += sum(bet for _, bet in tally)
    print("\nHere is the amount of chips in the pot at stake:", pot)

    activeplayer = [i for i in range(p) if tally[i][1] == highbet]
    if len(activeplayer) == 1:
        print(f"Player {activeplayer[0]+1} is the only one who didn't fold. He wins the pot of {pot} chips.")
        return

    highestplayer = 0
    highestscore = 0
    highesthand = []

    def get_hand_score(hand_type, createhand):
        hand_scores = {
            "Royal flush": 10,
            "Straight flush": 9,
            "Four of a kind": 8,
            "Full house": 7,
            "Flush": 6,
            "Straight": 5,
            "Three of a kind": 4,
            "Two pairs of cards": 3,
            "Pair of cards": 2,
            "High card": 1,
        }
        return hand_scores.get(hand_type, 0) + sum(card.value() for card in createhand)

    def check_hand(hand_type, createhand):
        check_functions = {
            "Royal flush": PokerGame.check_royal_flush,
            "Straight flush": PokerGame.check_straight_flush,
            "Four of a kind": PokerGame.check_four_of_a_kind,
            "Full house": PokerGame.check_full_house,
            "Flush": PokerGame.check_flush,
            "Straight": PokerGame.check_straight,
            "Three of a kind": PokerGame.check_three_of_a_kind,
            "Two pairs of cards": PokerGame.check_two_pairs,
            "Pair of cards": PokerGame.check_pair,
            "High card": PokerGame.check_high_card,
        }
        return check_functions.get(hand_type, lambda x: False)(createhand)

    valid_hand_types = [
        "High card", "Pair of cards", "Two pairs of cards", "Three of a kind",
        "Straight", "Flush", "Full house", "Four of a kind", "Straight flush", "Royal flush"
    ]

    hand_type_card_count = {
        "High card": 1,
        "Pair of cards": 2,
        "Two pairs of cards": 4,
        "Three of a kind": 3,
        "Straight": 5,
        "Flush": 5,
        "Full house": 5,
        "Four of a kind": 4,
        "Straight flush": 5,
        "Royal flush": 5
    }

    for j in activeplayer:
        totalcard = hands[j][1:] + river
        print(f"Player {j+1}, here are your total cards in your hands and the river: {totalcard}")
        print("Please select your card combination. (i.e. 'High card', 'Flush')")
        while True:
            while True:
                cardtype = input("Enter the type of hand you want to create: ")
                if cardtype not in valid_hand_types:
                    print("Invalid hand type. Please enter a valid hand type.")
                    continue
                else:
                    break
            createhand = []
            required_cards = hand_type_card_count.get(cardtype)
            for i in range(required_cards):
                acard = input(f"Enter card no.{i}: (e.g \"A of diamonds\" and \"7 of clubs\")\n")
                acard = acard.split(" of ")
                card = Card(acard[0], acard[1])

                print(f"Card: {card}, Type: {type(card)}")
                print(f"Totalcard: {totalcard}, Type: {type(totalcard)}")
                print(f"Totalcard: {totalcard[0]}, Type: {type(totalcard[0])}")

                if check_cards(card, totalcard):
                    createhand.append(card)
                else:
                    print("The card is not in your deck")
                    break
            if check_hand(cardtype, createhand):
                index = get_hand_score(cardtype, createhand)
                if index > highestscore:
                    print('Valid')
                    highestscore = index
                    highestplayer = j + 1
                    highesthand = createhand
                break
            else:
                print(f"There is no {cardtype.lower()}")
                continue

    print(f"The winner is player {highestplayer} with a hand of {highesthand} and a high score of {highestscore}")

if __name__ == "__main__":
    main()

# Texas Hold'em Poker
# Name: Kevin Ding
# Date: March 29, 2021
# Purpose: Play simplified Texas Hold'Em poker with computer.

#import functions here
import random

# hello world

#assign cards to value
cardrank = {
    "A" : 14,
    "K" : 13, 
    "Q" :  12,
    "J" : 11, 
    "10" : 10, 
    "9" : 9,
    "8" : 8,
    "7": 7, 
    "6": 6, 
    "5" : 5, 
    "4" : 4, 
    "3" : 3, 
    "2" : 2,
}

#add up the value of the cards in a hand according to the cardrank
def addsum (hand):
    sum = 0
    for i in hand:
        sum = sum + cardrank[i[0]]
    return sum

#sort number ascending order
def sortbynumber (hand):
    def takeFirst(elem):
        return elem[0]
    hand.sort(key=takeFirst)
    return hand

# print list
print('Sorted list:', random)

#check for high card
def checkHighcard (hand):
    if len(hand) == 1:
        return True
    else:
        return False

#check for pair
def checkPair (hand):
    if len(hand) == 2:
        if hand [0][0] == hand [1][0]:
            return True
        else:
            return False
    else:
        return False

#check for two pair
def checkTwopairs (hand):
    if len(hand) == 4:
        sortedhand = sortbynumber(hand)
        if sortedhand [0][0] == sortedhand [1][0] and sortedhand [2][0] == sortedhand [3][0]:
            return True
        else: 
            return False
    else:
        return False

#check for three of a kind
def checkThreeofakind (hand):
    if len(hand) == 3:
        sortedlist = sortbynumber(hand)
        if sortedlist [0][0] == sortedlist [1][0] == sortedlist [2][0]:
            return True
        else: 
            return False
    else:
        return False

#check for straight
def checkStraight (hand):
    if len(hand) == 5:
        sortedhand = sortbynumber(hand)
        sortedlist = []
        for i in range (len(sortedhand)):
            rank = cardrank[sortedhand[i][0]]
            sortedlist.append(rank)
        for i in range (5):
            if sortedlist == list(range(min(sortedlist), max(sortedlist)+1)):
                return True
            else: 
                return False
    else:
        return False

#check for flush
def checkFlush(hand):
    suit = hand[1][1]
    for i in range (1, len(hand)):
        if hand[i][1]==suit:
            continue
        else:
            return False
    return True

#check for full house
def checkFullhouse (hand):
    if len(hand) == 5:
        sortedhand = sortbynumber(hand)
        if sortedhand[0][0] == sortedhand[1][0] and sortedhand[2][0] == sortedhand[3][0] == sortedhand[4][0]:
            return True
        elif sortedhand[3][0] == sortedhand[4][0] and sortedhand[0][0] == sortedhand[1][0] == sortedhand[2][0]:
            return True
        else: 
            return False
    else:
        return False

#check for four of a kind
def checkFourofakind (hand):
    if len(hand) == 4:
        sortedhand = sortbynumber(hand)
        if sortedhand[0][0] == sortedhand[1][0] == sortedhand[2][0] == sortedhand[3][0]:
            return True
        else: 
            return False
    else:
        return False

#check for straight flush
def checkStraightflush (hand):
    if checkFlush (hand) == True and checkStraight (hand) == True:
        return True
    else:
        return False

#check for royal flush
def checkRoyalFlush (hand):
    sortedhand = sortbynumber(hand)
    if checkStraightflush (sortedhand) == True:
        return True
    else:
        return False

# Add a card to a hand given the current deck
def addCard(deck, hand):
    #Get a card off the top of the deck
    card = deck.pop(0)

    #append it to the given hand
    hand.append(card)

# Dispose of a card from a hand
def deleteCard(hand, index):
    hand.pop(index)

#if someone made a bet to double the stakes, after going to the last player, go back to the players before who didn't fold to ask if they want to check to new bet 
def validityofbets (tally):
    for i in range (p):
        if tally [i][1] != 0 and tally [i][1] != highbet:
            return False
        else:
            return True

#takes cards, check if it belongs in a hand   
def checkcards (card, hand):
    for i in hand:
        if card == i:
            return True
    return False

#format the input of use
def rewrite (x):
    y = x.replace("'", "")
    z = y.replace("[", "")
    a = z.replace("]", "")
    acard = a.split(", ")
    return acard

#Give rules
print("""
This is a game of Texas Hold'em Poker. Here is how to play:
If two people have the same hand, the person with the higher cards wins.
Here's howto​ play Texas Hold’Em:
• You’ll first need to bet your “ante,” which is your “buy in bet” to play the round. The ante is usually a small bet, like $1 or $5, and it’s decided by the table. 
• Once everyone has bet their ante, the dealer will deal two cards to each player. Keep these cards secret from everyone else. 
• Now, every player will take a look at their cards and choose whether or not to bet. Whenever there’s a betting round, you can choose to “fold,” which means not playing this round, “check,” which means matching their bet, or “raise,” which means adding more money to the betting pool. 
• Players that are unwilling to “check” a bet have to fold; and if everyone but one player “folds,” that player wins! 
• Once everyone has bet, the dealer will reveal three cards. These cards are known as the “flop.” When you see the flop, start planning what hand you want to make, keeping in mind that there are still two more cards to be revealed. For example, are your cards both diamonds, and did the flop include two diamond cards? In that case, you might want to aim for a flush, which is when you have five cards of the same suit. 
• After the flop, everyone has the chance to bet again, before the dealer reveals the next card, which is the “turn.” 
• Bet again if you want to, then the dealer will reveal the “river,” which is the last card. 
• At this point, you’ll see a total of 7 cards: two in your hands, and five on the table. Now, players will bet once last time, then everyone will reveal their hand. Your goal is to create the highest hand possible out of those seven cards, even if it means only using one card from your hand and four cards from the table. 
• The player with the best hand wins!
""")

#initialize the suits and labels
suits = ["clubs", "diamonds", "hearts", "spades"]
labels = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]

#populate the cards
cards = []
for suit in suits:
    for label in labels:
        cards.append([label, suit])

#shuffle the deck
random.shuffle(cards)

#get the number of players (p) and check error
while True:
    p = input("How many players? (max 10 players)\n")
    if p.isdigit() == True and 0 < int(p) < 11:
        p = int(p)
        break
    else:
        print("Sorry, invalid.")
        continue
n = 2

#set up p players, each with a hand of n cards - value 0 for now
hands = []
for i in range(1,p+1):
    hand = []
    #put in player name
    hand.append("Player "+str(i))
    for j in range(1, n+1):
        hand.append(0)
    hands.append(hand)

#deal out the p hands with n cards each, handing one card at a time to each player
for i in range (0, n):
    for j in range (0, p):
        #take card off top of deck, deal to each player
        card = cards.pop(0)
        hands[j][i+1]=card

#sort each players cards by ascending numerical order.
for i in range (0, p):
    if hands[i][1] > hands[i][2]:
        hands[i][1], hands[i][2] = hands[i][2], hands[i][1]

#main global variables
highbet = 1
highplayer = 0
pot = p
m = 0
activeplayer = []

#main program

#create tally for each player to record their bet
tally = []
for i in range (1, p+1):
    tallyunit = []
    tallyunit.append("Player "+str(i))
    tallyunit.append(1)
    tally.append (tallyunit)

#Ask players to check, bet or fold
print("Each player looks at their cards and determines to 'check', 'bet', or 'fold'. The starting bet for everyone is 1 chip")
for i in range (p):
    #press go for player x to look at his card and make a bet
    while True:
        x = input("Others look away, Player " + str(i+1) + " enter 'go' to continue:\n")
        if x == "go":
            break
        else:
            print("Sorry, invalid.")
            continue
    print("Here is your hand:", hands[i])
    #check bet
    while True:
        bet = input("Please 'check' " + str(highbet) + " tokens, 'bet' " + str(highbet*2) + " tokens, or 'fold' this round:\n")
        if bet == "check":
            tally[i][1] = highbet
            break
        elif bet == "bet":
            highbet = highbet * 2
            tally[i][1] = highbet
            highplayer = i
            break
        elif bet == "fold":
            tally[i][1] = 0
            break
        else:
            print("Sorry, invalid.")
            continue
    print("""
        LOOK AWAY
        LOOK AWAY
        LOOK AWAY
        LOOK AWAY
        LOOK AWAY
        LOOK AWAY
        LOOK AWAY
        LOOK AWAY
        LOOK AWAY
        LOOK AWAY
        LOOK AWAY
        LOOK AWAY
        LOOK AWAY
        LOOK AWAY
        LOOK AWAY
        LOOK AWAY
        LOOK AWAY
        LOOK AWAY
        LOOK AWAY
        LOOK AWAY
        LOOK AWAY
        LOOK AWAY
        LOOK AWAY
        LOOK AWAY
        LOOK AWAY
        LOOK AWAY
        LOOK AWAY
        LOOK AWAY
        LOOK AWAY
        """)

#go around the table a second time to ask those still in the game to check the new bet or not     
while validityofbets (tally) == False:
    for i in range(p):
        if tally[i][1] != 0 and tally [i][1] != highbet:
            while True:
                x = input("Others look away, Player " + str(i+1) + " enter 'go' to continue:\n")
                if x == "go":
                    break
                else:
                    print("Sorry, invalid.")
                    continue
            print("Here is your hand:", hands[i])
            #check bet
            while True:
                bet = input("Please 'check' " + str(highbet) + " tokens, 'bet' " + str(highbet*2) + " tokens, or 'fold' this round:\n")
                if bet == "check":
                    tally[i][1] = highbet
                    break
                elif bet == "bet":
                    highbet = highbet * 2
                    tally[i][1] = highbet
                    highplayer = i
                    break
                elif bet == "fold":
                    tally[i][1] = 0
                    break
                else:
                    print("Sorry, invalid.")
                    continue
       
#tell total chips in pot
for i in range (p):
    pot = pot + tally [i][1]
print("\nHere is the amount of chips in the pot at stake:", pot)

#List remaining players in game
for i in range (p):
    if tally [i][1] == highbet:
        activeplayer.append(i)
if len(activeplayer) == 1:
    print("Player "+ str(activeplayer[0]) + " is the only one who didn't fold. He wins the pot of " + str(pot) + " chips.")
else:
    print("Only people who have not folded will continue to the next round. Including:")
    for i in range(len(activeplayer)):
        print("Player " + str(activeplayer[i]+1))

#create the flop
flop = []
for i in range (3):
    flop.append(cards[i])
    cards.pop(i)
print("The flop is " + str(flop))

print("We will begin a new round of betting with the remaining players.\n")

#begin a new round of betting after everyone seen the flop, same logic as above
for i in (activeplayer):
    #press go for player x to look at his card and make a bet
    while True:
        x = input("Others look away, Player " + str(i+1) + " enter 'go' to continue:\n")
        if x == "go":
            break
        else:
            print("Sorry, invalid.")
            continue
    print("Here is your hand:", hands[i])
    #check bet
    while True:
        bet = input("Please 'check' " + str(highbet) + " tokens, 'bet' " + str(highbet*2) + " tokens, or 'fold' this round:\n")
        if bet == "check":
            tally[i][1] = highbet
            break
        elif bet == "bet":
            highbet = highbet * 2
            tally[i][1] = highbet
            highplayer = i
            break
        elif bet == "fold":
            tally[i][1] = 0
            break
        else:
            print("Sorry, invalid.")
            continue
    print("""
        LOOK AWAY
        LOOK AWAY
        LOOK AWAY
        LOOK AWAY
        LOOK AWAY
        LOOK AWAY
        LOOK AWAY
        LOOK AWAY
        LOOK AWAY
        LOOK AWAY
        LOOK AWAY
        LOOK AWAY
        LOOK AWAY
        LOOK AWAY
        LOOK AWAY
        LOOK AWAY
        LOOK AWAY
        LOOK AWAY
        LOOK AWAY
        LOOK AWAY
        LOOK AWAY
        LOOK AWAY
        LOOK AWAY
        LOOK AWAY
        LOOK AWAY
        LOOK AWAY
        LOOK AWAY
        LOOK AWAY
        LOOK AWAY
        """)
activeplayer = [] 

while validityofbets (tally) == False:
    for i in (activeplayer):
        if tally[i][1] != 0 and tally [i][1] != highbet:
            while True:
                x = input("Others look away, Player " + str(i+1) + " enter 'go' to continue:\n")
                if x == "go":
                    break
                else:
                    print("Sorry, invalid.")
                    continue
            print("Here is your hand:", hands[i])
            #check bet
            while True:
                bet = input("Please 'check' " + str(highbet) + " tokens, 'bet' " + str(highbet*2) + " tokens, or 'fold' this round:\n")
                if bet == "check":
                    tally[i][1] = highbet
                    break
                elif bet == "bet":
                    highbet = highbet * 2
                    tally[i][1] = highbet
                    highplayer = i
                    break
                elif bet == "fold":
                    tally[i][1] = 0
                    break
                else:
                    print("Sorry, invalid.")
                    continue

#tell total chips in pot
for i in range (p):
    pot = pot + tally [i][1]
print("\nHere is the amount of chips in the pot at stake:", pot)

#List remaining players in game
for i in range (p):
    if tally [i][1] == highbet:
        activeplayer.append(i)
#if all players but one folds, he/she wins
if len(activeplayer) == 1:
    print("Player "+ str(activeplayer[0]) + " is the only one who didn't fold. He wins the pot of " + str(pot) + " chips.")
else:
    print("These people who have not folded will continue to the final round. Including:")
    for i in range(len(activeplayer)):
        print("Player " + str(activeplayer[i]+1))

#create the river
river = flop
for i in range (2):
    river.append(cards[i])
    cards.pop(i)

print("The river is ", river)

print("""
Now players will make their deck with cards from their hand and the river. Here are the combinations:
1. 'High card'.
2. 'Pair of cards', like two 2s.
3. 'Two pairs of cards', like two 5s and two 9s.
4. 'Three of a kind', like three 4s.
5. 'Straight', which is five cards in sequential order. For example, a player might have a 3, 4, 5, 6, and 7 of any suit.
6. 'Flush', which is when a player has five cards of the same suit in any order. For example, a player might have a 2, 7, 10, Jack, and Queen of spades.
7. 'Full house', which is when a player has a pair and a three of a kind.
8. 'Four of a kind', like all four Aces.
9. 'Straight flush', which is when you have five cards in sequential order of the same suit. For example, a player might have a 5, 6, 7, 8, and 9 of clubs.
10. 'Royal flush', which is a straight flush containing a 10, Jack, Queen, King, and Ace.
If two people have the same hand, the person with the higher cards wins. It is calculated as the no. of the combination * 1000 + the individual values of the hand. 
""")


#ask the player for his card combination
highestplayer = 0
highestscore = 0
highesthand = []
for j in activeplayer:
    totalcard = []
    #combine cards in river and in hand to create overall deck
    totalcard.append(hands[j][1])
    totalcard.append(hands[j][2])
    for k in river:
        totalcard.append(k)
    print("Player " + str(j+1) + ", here is your the total cards in your hands and the river: " + str(totalcard))
    print("Please select your card combination. (i.e. 'High card', 'Flush')")
    #check player for his hand and verify
    while True:
        createhand = []
        cardtype = input("Enter here: ")
        if cardtype == "Royal flush":
            for i in range (5):
                x = input("Enter card no." + str(i+1) + ": (enter cards like ['A', 'diamonds'] and ['7', 'clubs']\n")
                acard = rewrite (x)
                if checkcards (acard, totalcard) == True:
                    createhand.append(acard)
                else:
                    print("The card is not in your deck")
                    break
            if checkRoyalFlush(createhand) == True:
                index = 10000 + addsum(createhand)
                if index > highestscore:
                    print('Valid')
                    highestscore = index
                    highestplayer = j + 1
                    highesthand = createhand
                    break
            else: 
                print("There is no royal flush")
                continue
            break
        elif cardtype == "Straight flush":
            for i in range (5):
                x = input("Enter card no." + str(i+1) + ": (enter cards like ['A', 'diamonds'] and ['7', 'clubs']\n")
                acard = rewrite (x)
                if checkcards (acard, totalcard) == True:
                    createhand.append(acard)
                else:
                    print("The card is not in your deck")
                    break
            if checkStraightflush(createhand) == True:
                index = 9000 + addsum(createhand)
                if index > highestscore:
                    print("'Valid")
                    highestscore = index
                    highestplayer = j + 1
                    highesthand = createhand
                    break
            else: 
                print("There is no straight flush")
                continue
            break
        elif cardtype == "Four of a kind":
            for i in range (4):
                x = input("Enter card no." + str(i+1) + ": (enter cards like ['A', 'diamonds'] and ['7', 'clubs']\n")
                acard = rewrite (x)
                if checkcards (acard, totalcard) == True:
                    createhand.append(acard)
                else:
                    print("The card is not in your deck")
                    break
            if checkFourofakind(createhand) == True:
                index = 8000 + addsum(createhand)
                if index > highestscore:
                    print('Valid')
                    highestscore = index
                    highestplayer = j + 1
                    highesthand = createhand
                    break
            else: 
                print("There is no four of a kind")
                continue
            break
        elif cardtype == "Full house":
            for i in range (5):
                x = input("Enter card no." + str(i+1) + ": (enter cards like ['A', 'diamonds'] and ['7', 'clubs']\n")
                acard = rewrite (x)
                if checkcards (acard, totalcard) == True:
                    createhand.append(acard)
                else:
                    print("The card is not in your deck")
                    break
            if checkFullhouse(createhand) == True:
                index = 7000 + addsum(createhand)
                if index > highestscore:
                    print('Valid')
                    highestscore = index
                    highestplayer = j + 1
                    highesthand = createhand
                    break
            else: 
                print("There is no full house")
                continue
            break
        elif cardtype == "Flush":
            for i in range (5):
                x = input("Enter card no." + str(i+1) + ": (enter cards like ['A', 'diamonds'] and ['7', 'clubs']\n")
                acard = rewrite (x)
                if checkcards (acard, totalcard) == True:
                    createhand.append(acard)
                else:
                    print("The card is not in your deck")
                    break
            if checkFlush(createhand) == True:
                index = 6000 + addsum(createhand)
                if index > highestscore:
                    print('Valid')
                    highestscore = index
                    highestplayer = j + 1
                    highesthand = createhand
                    break
            else: 
                print("There is no flush")
                continue
            break
        elif cardtype == "Straight":
            for i in range (5):
                x = input("Enter card no." + str(i+1) + ": (enter cards like ['A', 'diamonds'] and ['7', 'clubs']\n")
                acard = rewrite (x)
                if checkcards (acard, totalcard) == True:
                    createhand.append(acard)
                else:
                    print("The card is not in your deck")
                    break
            if checkStraight(createhand) == True:
                index = 5000 + addsum(createhand)
                if index > highestscore:
                    print('Valid')
                    highestscore = index
                    highestplayer = j + 1
                    highesthand = createhand
                    break
            else: 
                print("There is no straight")
                continue
            break
        elif cardtype == "Three of a kind":
            for i in range (3):
                x = input("Enter card no." + str(i+1) + ": (enter cards like ['A', 'diamonds'] and ['7', 'clubs']\n")
                acard = rewrite (x)
                if checkcards (acard, totalcard) == True:
                    createhand.append(acard)
                else:
                    print("The card is not in your deck")
                    break
            if checkThreeofakind(createhand) == True:
                index = 4000 + addsum(createhand)
                if index > highestscore:
                    print('Valid')
                    highestscore = index
                    highestplayer = j + 1
                    highesthand = createhand
                    break
            else: 
                print("There is no three of a kind")
                continue
            break
        elif cardtype == "Two pairs of cards":
            for i in range (4):
                x = input("Enter card no." + str(i+1) + ": (enter cards like ['A', 'diamonds'] and ['7', 'clubs']\n")
                acard = rewrite (x)
                if checkcards (acard, totalcard) == True:
                    createhand.append(acard)
                else:
                    print("The card is not in your deck")
                    break
            if checkTwopairs(createhand) == True:
                index = 3000 + addsum(createhand)
                if index > highestscore:
                    print('Valid')
                    highestscore = index
                    highestplayer = j + 1
                    highesthand = createhand
                    break
            else: 
                print("There is no two pairs")
                continue
            break
        elif cardtype == "Pair of cards":
            for i in range (2):
                x = input("Enter card no." + str(i+1) + ": (enter cards like ['A', 'diamonds'] and ['7', 'clubs']\n")
                acard = rewrite (x)
                if checkcards (acard, totalcard) == True:
                    createhand.append(acard)
                else:
                    print("The card is not in your deck")
                    break
            if checkPair(createhand) == True:
                index = 2000 + addsum(createhand)
                if index > highestscore:
                    print('Valid')
                    highestscore = index
                    highestplayer = j + 1
                    highesthand = createhand
                    break
            else: 
                print("There is no pair")
                continue
            break
        elif cardtype == "High card":
            for i in range (1):
                x = input("Enter card no." + str(i+1) + ": (enter cards like ['A', 'diamonds'] and ['7', 'clubs']\n")
                acard = rewrite (x)
                if checkcards (acard, totalcard) == True:
                    createhand.append(acard)
                else:
                    print("The card is not in your deck")
                    break
            if checkHighcard(createhand) == True:
                index = 1000 + addsum(createhand)
                if index > highestscore:
                    print('Valid')
                    highestscore = index
                    highestplayer = j + 1
                    highesthand = createhand
                    break   
            else: 
                print("There is no high card")
                continue
            break
        else:
            print("Sorry, invalid, Try to capitalize first letter and using []")
            continue
        break
    continue

print("The winner is player " + str(highestplayer) + " with a hand of " + str(highesthand) + " and a high score of " + str(highestscore))

#!/usr/bin/env python
# coding: utf-8

# In[17]:


import random
from IPython.display import clear_output


def deal(deck):
    hand = []
    while len(hand)!=2:
        random.shuffle(deck)
        card = deck.pop()
        if card == 11:
            card = "J"
        if card == 12:
            card = "Q"
        if card == 13:
            card = "K"
        if card == 1:
            card = "A"
        hand.append(card)
    return hand

def score(hand):
    total = 0
    flag = 0
    for card in hand:
        if card == "J" or card == "Q" or card == "K":
            total+= 10
        elif card == "A":
            flag += 1  
        else:
            total += card
    while flag !=0 :
        if total >= 11: 
            total+= 1
        else:
            total+= 11
        flag -= 1
    return total

def hit(hand):
    card = deck.pop()
    if card == 11 :
        card = "J"
    if card == 12 :
        card = "Q"
    if card == 13 :
        card = "K"
    if card == 1 :
        card = "A"
    hand.append(card)
    return hand

def comp(dealer_hand, player_hand):
    if score(dealer_hand) > 21:  
        print "Dealer busted. You win 1 time your original bet!\n"
    elif score(player_hand) < score(dealer_hand):
        print "Sorry, dealer has a better score. You lose your original amount!\n"
    elif score(player_hand) > score(dealer_hand):
        print "Congratulations. You have a better score than the dealer. You win 1 time your original bet!\n"
    elif score(player_hand) == score(dealer_hand) :
        print "You two have the same score. That's a push!"
        print "You do not win anyhting."

def replay():
    
    return raw_input('Do you want to play again? Enter Yes or No: ').lower().startswith('y')


clear_output()
while True:
    clear_output()
    print "Welcome to Blackjack!"
    bet = raw_input('How much do you want to bet?')
    deck = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]*4
    choice = ''
    game_on = True
    dealer_hand = []
    player_hand = []
    dealer_hand = deal(deck)
    player_hand = deal(deck)
    print "Dealer has X & " +str(dealer_hand[1])
    print "You have " +str(player_hand)
    while game_on:
        if score(player_hand) == 21 :
            print "Congratulations! You got a Blackjack!\n"
            if score(dealer_hand) == 21 :
                print "The dealer has also got a Blackjack!\n"
                print "That's a push"
                print "You do not win anything"
                game_on = False
                break
            else :
                bet += bet*1.5
                print "You win 1.5 times your original bet"
                game_on = False
                break
        while choice != "q" or choice != "quit" or game_on :
            choice = raw_input("Do you want to hit, stand, or quit: ").lower()
            if choice == "h" or choice == "hit":
                hit(player_hand)
                print "Now you have " +str(player_hand)
                if score(player_hand) > 21:
                    print "Sorry, you busted. You lose your original amount!"
                    game_on = False
                    break
            elif choice == "s" or choice == "stand":
                print "Dealer has " +str(dealer_hand)
                while score(dealer_hand) < 17:
                    hit(dealer_hand)
                    print "Since the dealer's score is below 17, dealer will get another card from the deck."
                    print "Now dealer has " +str(dealer_hand)
                    if score(dealer_hand) > 21:
                        game_on = False
                        break
                comp(dealer_hand, player_hand)
                game_on = False
                break
            elif choice == "q" or choice == "quit":
                print "Bye!"
                game_on = False
                break
    if not replay():
        break


# In[ ]:





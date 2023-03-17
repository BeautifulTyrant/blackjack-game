import random
import time
from logic import *
from test_values import *

suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace') * 4
values = {'Two': 2, 'Three': 3, 'Four': 4, 'Five': 5, 'Six': 6, 'Seven': 7, 'Eight': 8, 'Nine': 9, 'Ten': 10,
          'Jack': 10,
          'Queen': 10, 'King': 10, 'Ace': 11}


playing = True  # While loop controller

chip_total = 1000  # Starting chip total
pnl = 0


class Card:

    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank

    def __str__(self):
        return self.rank + ' of ' + self.suit


class Deck:

    def __init__(self):
        self.deck = []  # start with an empty list
        for suit in suits:
            for rank in ranks:
                self.deck.append(Card(suit, rank))

    def __str__(self):
        deck_comp = ''  # start with an empty string
        for card in self.deck:
            deck_comp += '\n ' + card.__str__()  # add each Card object's print string
        return 'The deck has:' + deck_comp

    def shuffle(self):
        random.shuffle(self.deck)

    def deal(self):
        single_card = self.deck.pop()
        return single_card


class Hand:
    def __init__(self):
        self.cards = []  # start with an empty list as we did in the Deck class
        self.value = 0  # start with zero value
        self.aces = 0  # add an attribute to keep track of aces

    def add_card(self, card):
        # adds card to hand and adjusts for an aces
        self.value += values[card.rank]
        self.cards.append(card)
        if card.rank == 'Ace':
            self.aces += 1  # add to self.aces
        while self.value > 21 and self.aces:
            self.value -= 10
            self.aces -= 1

    def get_value(self):
        pass

    def __len__(self):
        return len(self.cards)


class Chips:

    def __init__(self):
        self.bet = 0

    def win_bet(self):
        return self.bet

    def win_blackjack(self):
        return self.bet * 1.5

    def dd_bet(self):
        self.bet *= 2

    def lose_bet(self):
        return -self.bet


def player_action(game_deck, p_hand, d_hand):
    global playing  # to control an upcoming while loop

    while True:

        if p_hand.value == 21:
            print("21!")
            time.sleep(2.5)
            playing = False
            break

        else:
            x = input("Would you like to Hit, Stand or Double Down? Enter 'h', 's' or 'd': ")

            if x[0].lower() == 'h':
                hit(game_deck, p_hand)
                time.sleep(1)
                break

            elif x[0].lower() == 's':
                print("Player stands. Dealer is playing.")
                time.sleep(1)
                playing = False
                break

            elif x[0].lower() == 'd':
                if len(player_hand) == 2:
                    print("Player doubles down. Drawing last card. Bet 2x.")
                    time.sleep(1)
                    hit(game_deck, p_hand)
                    show_some(p_hand, d_hand)
                    time.sleep(1)
                    player_chips.dd_bet()
                    playing = False
                    break
                else:
                    print("Cannot double down. More than 2 cards in hand.")
                    time.sleep(2)
                    break

            else:
                print("Try again.")
                continue


def split(player, dealer, chips):
    global playing
    global chip_total
    global pnl

    player_hand_1 = Hand()
    player_hand_1.add_card(player.cards[0])
    player_hand_1.add_card(deck.deal())

    player_hand_2 = Hand()
    player_hand_2.add_card(player.cards[1])
    player_hand_2.add_card(deck.deal())

    while player_hand_1.value < 21:
        print("\nPlayer's Hand 1:", *player_hand_1.cards, sep='\n ')
        print("Player's Hand 1 =", player_hand_1.value)
        x = input("Hand 1: Would you like to Hit, Stand or Double Down? Enter 'h', 's' or 'd': ")

        if x[0].lower() == 'h':
            hit(deck, player_hand_1)  # hit() function defined above
            print("\nPlayer's Hand 1:", *player_hand_1.cards, sep='\n ')
            print("Player's Hand 1 =", player_hand_1.value)
            continue

        elif x[0].lower() == 's':
            print("\033[1mHand 1 stands.\033[0m")
            playing = False
            break

        elif x[0].lower() == 'd':
            if len(player_hand) == 2:
                print("Player doubles down. Drawing last card. Bet 2x.")
                time.sleep(1)
                hit(deck, player_hand_1)
                show_some(player_hand_1, dealer_hand)
                time.sleep(2)
                player_chips.dd_bet()
                playing = False
                break
            else:
                print("Cannot double down. More than 2 cards in hand.")
                time.sleep(2)
                break

        else:
            print("Try again.")
            continue

    while True:
        if player_hand_1.value > 21:
            print("\n\033[1mPlayer 1 Busts!\033[0m")
            break
        elif player_hand_1.value <= 21:
            print("\nContinuing to hand 2")
            time.sleep(0.5)
            break

    while player_hand_2.value < 21:
        print("\nPlayer's Hand 2:", *player_hand_2.cards, sep='\n ')
        print("Player's Hand 2 =", player_hand_2.value)
        x = input("Hand 2: Would you like to Hit, Stand or Double Down? Enter 'h', 's' or 'd': ")

        if x[0].lower() == 'h':
            hit(deck, player_hand_2)  # hit() function defined above
            print("\nPlayer's Hand 2:", *player_hand_2.cards, sep='\n ')
            print("Player's Hand 2 =", player_hand_2.value)
            continue

        elif x[0].lower() == 's':
            print("Hand 2 stands. \nDealer is playing.")
            playing = False
            time.sleep(2)
            break

        elif x[0].lower() == 'd':
            if len(player_hand) == 2:
                print("Player doubles down. Drawing last card. Bet 2x.")
                time.sleep(1)
                hit(deck, player_hand_2)
                show_some(player_hand_2, dealer_hand)
                time.sleep(2)
                player_chips.dd_bet()
                playing = False
                break
            else:
                print("Cannot double down. More than 2 cards in hand.")
                time.sleep(2)
                break

        else:
            print("Try again.")
            continue

    if player_hand_2.value > 21:
        print("\n\033[1mPlayer 2 Busts!\033[0m")

    elif player_hand_2.value <= 21:
        print("\nContinuing to results")
        time.sleep(0.5)

    # Different cases where dealer needs to play
    if player_hand_1.value <= 21 and player_hand_2.value <= 21:
        while dealer_hand.value < 17:
            hit(deck, dealer_hand)
        show_all(player_hand_1, dealer_hand)
        show_all(player_hand_2, dealer_hand)

    if player_hand_1.value >= 21 >= player_hand_2.value:
        while dealer_hand.value < 17:
            hit(deck, dealer_hand)
        show_all(player_hand_1, dealer_hand)
        show_all(player_hand_2, dealer_hand)

    if player_hand_1.value <= 21 <= player_hand_2.value:
        while dealer_hand.value < 17:
            hit(deck, dealer_hand)
        show_all(player_hand_1, dealer_hand)
        show_all(player_hand_2, dealer_hand)

    # Player bust cases
    if player_hand_1.value > 21:
        print("\nHand 1 Results: ")
        player_busts(player_hand_1, dealer, chips)
        pnl += player_chips.lose_bet()
        chip_total += player_chips.lose_bet()

    if player_hand_2.value > 21:
        print("\nHand 2 Results: ")
        player_busts(player_hand_2, dealer, chips)
        pnl += player_chips.lose_bet()
        chip_total += player_chips.lose_bet()

    # Different winning scenarios
    if player_hand_1.value <= 21:
        if dealer_hand.value > 21:
            print("\nHand 1 Results: ")
            dealer_busts(player_hand_1, dealer_hand, player_chips)
            # dealer_busts(player_hand_2, dealer_hand, player_chips)
            pnl += player_chips.win_bet()
            chip_total += player_chips.win_bet()

        elif dealer_hand.value > player_hand_1.value:
            print("\nHand 1 Results: ")
            dealer_wins(player_hand_1, dealer_hand, player_chips)
            pnl += player_chips.lose_bet()
            chip_total += player_chips.lose_bet()

        elif dealer_hand.value < player_hand_1.value:
            print("\nHand 1 Results: ")
            player_wins(player_hand_1, dealer_hand, player_chips)
            pnl += player_chips.win_bet()
            chip_total += player_chips.win_bet()

        else:
            print("\nHand 1 Results: ")
            push(player_hand_1, dealer_hand)
    else:
        print("\n-----------")

    if player_hand_2.value <= 21:
        if dealer_hand.value > 21:
            pnl += player_chips.win_bet()
            chip_total += player_chips.win_bet()
            print("\nHand 2 Results: ")
            print("\033[1mDealer busts!\033[0m")

        elif dealer_hand.value > player_hand_2.value:
            print("\nHand 2 Results: ")
            dealer_wins(player_hand_2, dealer_hand, player_chips)
            pnl += player_chips.lose_bet()
            chip_total += player_chips.lose_bet()

        elif dealer_hand.value < player_hand_2.value:
            print("\nHand 2 Results: ")
            player_wins(player_hand_2, dealer_hand, player_chips)
            pnl += player_chips.win_bet()
            chip_total += player_chips.win_bet()

        else:
            print("\nHand 2 Results: ")
            push(player_hand_2, dealer_hand)


print('Welcome to BlackJack! Get as close to 21 as you can without going over!\nDealer hits until it reaches 17. '
      'Aces count as 1 or 11.')
print(f"Player starts with {chip_total} chips")

is_blackjack = False

while True:

    # Create & shuffle the deck, deal two cards to each player
    deck = Deck()
    deck.shuffle()

    player_hand = Hand()
    player_hand.add_card(deck.deal())
    player_hand.add_card(deck.deal())

    dealer_hand = Hand()
    dealer_hand.add_card(deck.deal())
    dealer_hand.add_card(deck.deal())

    # Set up the Player's chips
    player_chips = Chips()

    # Prompt the Player for their bet
    take_bet(player_chips, chip_total)

    # Show cards (but keep one dealer card hidden)
    show_some(player_hand, dealer_hand)

    if blackjack_check(player_hand):  # if both player and dealer have blackjack
        if blackjack_check(dealer_hand):
            show_all(player_hand, dealer_hand)
            print("\nBoth have Blackjack. Push")

            print("\nPlayer's chip count is at", chip_total)
            print("Player's PnL is at", pnl)

            # Ask to play again
            new_game = input("\nWould you like to play another hand? Enter 'y' or 'n' ")

            if new_game[0].lower() == 'y':
                if chip_total > 1:
                    playing = True
                    continue
                else:
                    print("Out of chips. Thanks for playing!")
                    break
            else:
                print("Thanks for playing!")
                break
        else:  # if only player has blackjack
            show_all(player_hand, dealer_hand)
            pnl += player_chips.win_blackjack()
            chip_total += player_chips.win_blackjack()
            print("\033[1mBLACKJACK!\033[0m")

            print("\nPlayer's chip count is at", chip_total)
            print("Player's PnL is at", pnl)

            # Ask to play again
            new_game = input("\nWould you like to play another hand? Enter 'y' or 'n' ")

            if new_game[0].lower() == 'y':
                if chip_total > 1:
                    playing = True
                    continue
                else:
                    print("Out of chips. Thanks for playing!")
                    break
            else:
                print("Thanks for playing!")
                break

    elif not blackjack_check(player_hand):  # if player doesn't have blackjack
        if player_hand.cards[0].rank == player_hand.cards[1].rank:
            split_ask = input("\nSplit hands? (y/n): ")  # asking user if they want to split hands
            if split_ask.lower() == 'y':
                split(player_hand, dealer_hand, player_chips)
                print("\nPlayer's chip count is at", chip_total)
                print("Player's PnL is at", pnl)

                # Ask to play again
                new_game_if_split = input("\nWould you like to play another hand? Enter 'y' or 'n' ")

                if new_game_if_split[0].lower() == 'y':
                    if chip_total > 1:
                        playing = True
                        continue
                    else:
                        print("Out of chips. Thanks for playing!")
                        quit()
                else:
                    print("Thanks for playing!")
                    quit()
            else:
                while playing:  # recall this variable from our hit_or_stand function

                    # Prompt for Player to Hit or Stand
                    player_action(deck, player_hand, dealer_hand)

                    # Show cards (but keep one dealer card hidden)
                    show_some(player_hand, dealer_hand)

                    # If player's hand exceeds 21, run player_busts() and break out of loop
                    if player_hand.value > 21:
                        player_busts(player_hand, dealer_hand, player_chips)
                        pnl += player_chips.lose_bet()
                        chip_total += player_chips.lose_bet()
                        break

                        # If Player hasn't busted, play Dealer's hand until Dealer reaches 17
                if player_hand.value <= 21:

                    while dealer_hand.value < 17:
                        hit(deck, dealer_hand)

                        # Show all cards
                    show_all(player_hand, dealer_hand)

                    # Run different winning scenarios
                    if dealer_hand.value > 21:
                        dealer_busts(player_hand, dealer_hand, player_chips)
                        pnl += player_chips.win_bet()
                        chip_total += player_chips.win_bet()

                    elif dealer_hand.value > player_hand.value:
                        dealer_wins(player_hand, dealer_hand, player_chips)
                        pnl += player_chips.lose_bet()
                        chip_total += player_chips.lose_bet()

                    elif dealer_hand.value < player_hand.value:
                        player_wins(player_hand, dealer_hand, player_chips)
                        pnl += player_chips.win_bet()
                        chip_total += player_chips.win_bet()

                    else:
                        push(player_hand, dealer_hand)

                print("\nPlayer's chip count is at", chip_total)
                print("Player's PnL is at", pnl)

                # Ask to play again
                new_game = input("\nWould you like to play another hand? Enter 'y' or 'n' ")

                if new_game[0].lower() == 'y':
                    if chip_total > 1:
                        playing = True
                        continue
                    else:
                        print("Out of chips. Thanks for playing!")
                        break
                else:
                    print("Thanks for playing!")
                    break

        else:
            while playing:

                player_action(deck, player_hand, dealer_hand)

                # keep dealer's card hidden
                show_some(player_hand, dealer_hand)

                # If player's hand exceeds 21, player busts
                if player_hand.value > 21:
                    player_busts(player_hand, dealer_hand, player_chips)
                    pnl += player_chips.lose_bet()
                    chip_total += player_chips.lose_bet()
                    break

                    # If Player hasn't busted, play Dealer's hand until Dealer reaches 17
            if player_hand.value <= 21:

                while dealer_hand.value < 17:
                    hit(deck, dealer_hand)

                    # Show all cards
                show_all(player_hand, dealer_hand)

                # Run different winning scenarios
                if dealer_hand.value > 21:
                    print("\n")
                    dealer_busts(player_hand, dealer_hand, player_chips)
                    pnl += player_chips.win_bet()
                    chip_total += player_chips.win_bet()

                elif dealer_hand.value > player_hand.value:
                    print("\n")
                    dealer_wins(player_hand, dealer_hand, player_chips)
                    pnl += player_chips.lose_bet()
                    chip_total += player_chips.lose_bet()

                elif dealer_hand.value < player_hand.value:
                    print("\n")
                    player_wins(player_hand, dealer_hand, player_chips)
                    pnl += player_chips.win_bet()
                    chip_total += player_chips.win_bet()

                else:
                    print("\n")
                    push(player_hand, dealer_hand)

            print("\nPlayer's chip count is at", chip_total)
            print("Player's PnL is at", pnl)

            # Ask to play again
            new_game = input("\nWould you like to play another hand? Enter 'y' or 'n' ")

            if new_game[0].lower() == 'y':
                if chip_total > 1:
                    playing = True
                    continue
                else:
                    print("Out of chips. Thanks for playing!")
                    break
            else:
                print("Thanks for playing!")
                break

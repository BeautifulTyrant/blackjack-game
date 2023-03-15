def show_some(player, dealer):
    print("\nDealer's Hand:")
    print(" <card hidden>")
    print('', dealer.cards[1])
    print("\nPlayer's Hand:", *player.cards, sep='\n ')
    print(f"Player's Hand = {player.value}")


def show_all(player, dealer):
    print("\nDealer's Hand:", *dealer.cards, sep='\n ')
    print("Dealer's Hand =", dealer.value)
    print("\nPlayer's Hand:", *player.cards, sep='\n ')
    print("", player.value)


def player_busts(player, dealer, chips):
    print("\033[1mPlayer busts!\033[0m")
    chips.lose_bet()


def player_wins(player, dealer, chips):
    print("\033[1mPlayer wins!\033[0m")
    chips.win_bet()


def player_wins_bj(player, dealer, chips):
    chips.win_blackjack()


def dealer_busts(player, dealer, chips):
    print("\033[1mDealer busts!\033[0m")
    chips.win_bet()


def dealer_wins(player, dealer, chips):
    print("\033[1mDealer wins!\033[0m")
    chips.lose_bet()


def push(player, dealer):
    print("\033[1mDealer and Player tie! It's a push.\033[0m")


def hit(deck, hand):
    hand.add_card(deck.deal())


def take_bet(chips, chip_total):
    while True:
        try:
            chips.bet = int(input('\nHow many chips would you like to bet? '))
        except ValueError:
            print('Sorry, a bet must be an integer!')
        else:
            if chips.bet > chip_total:
                print("Sorry, your bet can't exceed", chip_total)
            else:
                break


def blackjack_check(hand):
    if len(hand) == 2 and hand.value == 21:
        return True


import os
import random
from art import logo    # ASCII art due to patorjk.com
from player import Player


# Clear the terminal, and print the logo again.
def refresh():
    os.system('cls' if os.name == 'nt' else 'clear')
    print(logo)


def Game(deck):
    # Create the 'Player' objects for the user and the computer (the dealer).
    user = Player(visible=True)
    computer = Player(visible=False)

    # Both the user and computer start with 2 cards.
    # Initially, the computer makes only one card visible, the other is face down -> 'visible=False'

    # Initially, both players are dealt 2 cards.
    for i in range(4):
        new_card = random.choice(deck)
        print("Drew", new_card)
        deck.remove(new_card)
        
        # The computer gets a card first, then the user/
        if i % 2 == 0:
            computer.deal(card=new_card)
        else:
            user.deal(card=new_card)

    refresh()
    print('Your cards: ', user.cards, ', current score: ', user.total, sep='')
    print("Computer's first card:", computer.cards[0])

    # User's turn. If the first two cards already add up to 21, the user automatically wins.
    if user.total == 21:
        user.finished = True
        print("Blackjack! You won!")
        return
    else:
        while not user.finished:
            user_choice = input("Type 'hit' or 'stand': ")
            if user_choice == 'stand':
                user.finished = True
            else:
                new_card = random.choice(deck)
                deck.remove(new_card)
                user.deal(card=new_card)
                if user.total >= 21:
                    user.finished = True
                refresh()
                print('Your cards: ', user.cards, ', current score: ', user.total, sep='')
                print("Computer's first card:", computer.cards[0])

    # User's turn is over. The computer receives cards unless its total becomes greater or equal to 17.
        computer.visible = True
        computer.correct_for_aces()

        if computer.total == 21:
            computer.finished = True
        else:
            while not computer.finished:
                if computer.total >= 17:
                    computer.finished = True
                else:
                    new_card = random.choice(deck)
                    deck.remove(new_card)
                    computer.deal(card=new_card)
                    if computer.total >= 21:
                        computer.finished = True

    # Computer's turn is over.
    # The winner is the player closest to 21, that has not gone over 21.
        refresh()
        print("Player's cards: ", user.cards, ", final score: ", user.total, sep='')
        if user.total > 21:
            print("That's a bust. The computer wins.")
        else:
            print("Computer's cards: ", computer.cards, ", final score: ", computer.total, sep='')
            if user.total == computer.total:
                print("It's a draw.")
            elif (user.total > computer.total) and (user.total <= 21):
                print("You win!")
            elif (user.total < computer.total) and (computer.total <= 21):
                print("The computer wins.")
            elif computer.total > 21:
                print("Dealer bust. You win!")


def play():
    # Clear the terminal, and prompt the user for the amount of decks to be included in the game.
    refresh()
    s1 = "How many decks would you like to shuffle together?\n"
    s2 = "You can choose any number from 2 to 8.\n"
    N = int(input(s1 + s2))

    if (N >= 2) and (N <= 8):        
        # Shuffle the specified amount of decks.
        Standard_Deck = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
        Shuffled_Deck = Standard_Deck * N

        new_game = True
        while new_game:
            Game(Shuffled_Deck[:])
            
            # After the game is over, ask if the user would like to play again.
            play_again = input(
                "Do you want to play a game of Blackjack. Type 'y' or 'n': ")
            if play_again == 'n':
                new_game = False
    
    else:
        print("Come back when you're serious.")


play()


class Player:
    def __init__(self, visible):
        self.cards = []     # The cards the player has been dealt
        self.amount_of_cards = 0    # The amount of cards the player has been dealt
        self.aces = 0       # The amount of Aces the player has been dealt
        self.total = 0      # The sum of the cards the player has been dealt
        self.visible = visible      # True if all the cards the player has been dealth are lying face up; False otherwise
        self.finished = False       # Whether the player has finished receiving cards

    # When the player's entire hand is visible and the total is over 21, we correct for any Aces the player has been dealt.
    def correct_for_aces(self):
        while (self.total > 21) and (self.aces > 0):
            self.total = self.total - 10
            self.aces = self.aces - 1
            for j in range(self.amount_of_cards):
                if self.cards[j] == 11:
                    self.cards[j] = self.cards[j] - 10
                    break

    # Dealing a card from the deck to the player.
    def deal(self, card):
        if card == 11:
            self.aces = self.aces + 1
        self.cards.append(card)
        self.amount_of_cards = self.amount_of_cards + 1
        self.total = self.total + card
        if self.visible:
            self.correct_for_aces()

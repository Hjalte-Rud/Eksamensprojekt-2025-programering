import random

class Deck:
    def __init__(self, deck_antal=1):
        # skab kortdeck(s)
        SUITS =('♡', '♠', '♣', '♢')
        VALUES = ['A']
        # Tilføj nummerkort
        for i in range(2, 10):
            VALUES.append(str(i))
        # Tilføj 10 - konge
        VALUES.extend(['10']*4)

        # Byg deck
        cards = []
        for suit in SUITS:
            for value in VALUES:
                cards.append(suit + value)

        # Tilføj jokere
        cards.extend(['J10']*3)

        # Kopier deck til deck_antal
        self.deck = []
        for i in range(deck_antal):
            self.deck.extend(cards)

    def __str__(self):
        return str(self.deck)

    def shuffle(self):
        random.shuffle(self.deck)
    # bland kort

    def deal(self, num_of_cards=1):
        out = []
        for i in range(num_of_cards):
            out.append(self.deck.pop(0))
        return out

class Game:

    def __init__(self):
        self.deck = Deck()
        self.deck.shuffle()

        self.dealer_hand = []
        self.dealer_hand.extend(self.deck.deal(2))

        self.player_hand = []

    def play_dealer_hand(self):
        while self.check_hand(self.dealer_hand) <= 16:
            self.hit(self.dealer_hand)

    def deal_player_hand(self):
        (self.player_hand.extend(self.deck.deal(2)))

    def hit(self, hand):
        hand.extend(self.deck.deal())

    def stand(self):
        for stand in self(num_of_cards):
           self.wait.turn(self.deck)

        return str(self.deck)




    def bet(self, amount):
        pass

    def check_win(self):
        pass

    def check_hand(self, hand):
        total = 0
        aces = 0
        for card in hand:
            value = card[1:]
            if value.isdigit():
                total += int(value)
            else:
                aces += 1
                total += 11

        # Konverter esser hvis bust
        while total > 21 and aces > 0:
            total -= 10
            aces -= 1

        return total

    def print_hand(self, hand):
        print(hand, self.check_hand(hand))

if __name__ == '__main__':
    game = Game()
    game.play_dealer_hand()
    game.print_hand(game.dealer_hand)

    game.deal_player_hand()

    choice = None
    while not game.check_win():
        game.print_hand(game.player_hand)
        choice = input()
        if choice == '':
            game.hit(game.player_hand)
        else:
            print(game.check_win())

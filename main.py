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

        self.hand = []
        self.hand.extend(self.deck.deal(4))

    def hit(self):
        self.hand.extend(self.deck.deal())

    def stand(self):
        pass

    def bet(self, amount):
        pass

    def check_win(self):
        pass

    def check_hand(self):
        total = 0
        aces = 0
        for card in self.hand:
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

if __name__ == '__main__':
    game = Game()
    print(game.hand)
    print(game.check_hand())
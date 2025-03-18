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

def start():
    pass

def main():
    # Spillet bliver styret herfra

    deck = Deck(3)
    start()




    mylist = deck
    mylist.shuffle()

    print(mylist)



if __name__ == '__main__':
    main()

class Game:
    def hit()
        pass

    def stand ()
        pass

    def bet ():
        pass

    def check_win ()
        pass

    def check_hand ()
        pass
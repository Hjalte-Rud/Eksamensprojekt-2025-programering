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

    def shuffle(self):
        self.deck.shuffle()
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


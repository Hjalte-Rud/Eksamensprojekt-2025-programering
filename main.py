

def setup_cards(deck_antal=1):
    # skab kortdeck(s)
    SUITS =('H', 'S', 'C', 'D')
    VALUES = ['A']
    # Tilføj nummerkort
    for i in range(2, 10):
        VALUES.append(str(i))
    # Tilføj 10 - konge
    VALUES.extend(['10']*4)

    # Byg deck
    deck = []
    for suit in SUITS:
        for value in VALUES:
            deck.append(suit + value)

    # Tilføj jokere
    deck.extend(['J10']*3)

    # Kopier deck til deck_antal
    deck_out = []
    for i in range(deck_antal):
        deck_out.extend(deck)

    return deck_out


    # bland kort

def start():
    pass

def main():
    # Spillet bliver styret herfra

    deck = setup_cards(1)
    print(len(deck))
    start()


    import random

    mylist = deck
    random.shuffle(mylist)

    print(mylist)



if __name__ == '__main__':
    main()


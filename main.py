# Todo Project files ud af git!

def setup_cards(deck_antal=1):
    # skab kortdeck(s)
    SUITS =('♡', '♠', '♣', '♢')
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
    return deck


    # bland kort

def start():
    pass

def main():
    # Spillet bliver styret herfra

    deck = setup_cards()
    print(deck)
    start()


if __name__ == '__main__':
    main()


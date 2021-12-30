import random

suits = {'Hearts', 'Diamonds', 'Spades', 'Clubs'}
ranks = {'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine',
         'Ten', 'Jack', 'Queen', 'King', 'Ace'}
values = {'Two': 2, 'Three': 3, 'Four': 4, 'Five': 5, 'Six': 6, 'Seven': 7,
          'Eight': 8, 'Nine': 9, 'Ten': 10, 'Jack': 10, 'Queen': 10,
          'King': 10, 'Ace': 11}

playing = True  # sprawdzanie, czy pilka nadal w grze


class Player:
    def __init__(self, name, type):
        self.name = name
        self.type = type
        self.points = 0
        self.playing = True  # sprawdzenie czy gracz uczestniczy w rundzie
        self.cards_played = 0

    def start_round(self, deck):  # dobranie reki na start rundy
        self.hand = Hand()
        self.hand.add_card(deck.deal())
        self.hand.add_card(deck.deal())
        self.cards_played += 2
        self.playing = True


class Card:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank

    def __str__(self):
        return self.rank + ' of ' + self.suit


class Deck:  # talia kart ugulem
    def __init__(self):
        self.deck = []  # lista, ktora wypelnimy kartami i otrzymamy talie kart
        for suit in suits:
            for rank in ranks:
                self.deck.append(Card(suit, rank))

    def __str__(self):
        deck_comp = ''
        for card in self.deck:
            deck_comp += '\n' + card.__str__()
        return 'The deck has: ' + deck_comp

    def shuffle_cards(self):  # wiadomo co, wiadomo kogo
        random.shuffle(self.deck)

    def deal(self):  # wybieranie karty z talii
        single_card = self.deck.pop()
        return single_card


class Hand:  # odkrywanie kart
    def __init__(self):
        self.cards = []
        self.value = 0
        self.aces = 0  # specjalnie miejsce dla ich, no bo specjalne są (maja wartosc albo 1 albo 11)

    def add_card(self, card):  # dobieranie karty zawodnikom
        self.cards.append(card)
        self.value += values[card.rank]
        if card.rank == 'Ace':
            self.aces += 1

    def adjust_for_ace(self):  # 1 lub 11 dla asa
        while self.value > 21 and self.aces:
            self.value -= 10
            self.aces -= 1


class Chips:  # zetony/coinsy
    def __init__(self):
        self.total = 1000
        self.bet = 0

    def win_bet(self):
        self.total += self.bet

    def lose_bet(self):          # potem trzeba dodac 2 kolejne dla wygranej/przegranej
        self.total -= self.bet   # przez doubla


def take_bet(chips):  # wez coinsy od gracza
    while True:
        try:
            chips.bet = int(input("How many chips would you like to bet?: "))
        except ValueError:
            print("Please type in a number: ")
        else:
            if chips.bet > chips.total:
                print("Your bet can't exceed 1000!")
            else:
                break


def hit(deck, hand):
    hand.add_card(deck.deal())
    hand.adjust_for_ace()


def hit_or_stand(deck, player):  # zapytaj gracza, czy chce podbijac dalej
    global playing

    while True:
        if player.type == "player":
            ask = input("Would you like to hit or stand? Please enter 'h' or 's': ")

            if ask[0].lower() == 'h':
                hit(deck, player.hand)
                player.cards_played += 1
            elif ask[0].lower() == 's':
                print("Player stands.")
                player.playing = False
            else:
                print("Sorry, I didn't understand that, please try again!")
                continue
            break

        if player.type == "ceasy":  # easy (losowe decyzje)
            ask = bool(random.getrandbits(1))
            if ask is True:
                print(player.name + " hits.")
                hit(deck, player.hand)
                player.cards_played += 1

            else:
                print(player.name + " stands.")
                player.playing = False

            break

        if player.type == "cmedium":  # medium (bierze karte gdy value reki <= 17)
            if player.hand.value <= 17:
                print(player.name + " hits.")
                hit(deck, player.hand)
                player.cards_played += 1

            else:
                print(player.name + " stands.")
                player.playing = False

            break

        if player.type == "chard":  # hard (podglada jaka karta bedzie nastepna)
            if player.hand.value + values[deck.deck[len(deck.deck) - 1].rank] > 21:
                if deck.deck[len(deck.deck) - 1].rank == 'Ace':
                    if player.hand.value + 1 <= 21:
                        print(player.name + " hits.")
                        hit(deck, player.hand)
                        player.cards_played += 1

                    else:
                        print(player.name + " stands.")
                        player.playing = False

                else:
                    print(player.name + " stands.")
                    player.playing = False

            else:
                print(player.name + " hits.")
                hit(deck, player.hand)
                player.cards_played += 1

            break


# def show_some(player, dealer):
#     print("'\nDealer's Hand: ")
#     print(" <card hidden>")
#     print("", dealer.cards[1])
#     # print("'\nDealer's Hand: ", *dealer.cards, sep='\n ')
#     print("'\nPlayer's Hand: ", *player.cards, sep='\n ')


# def show_all(player, dealer):
#     print("'\nDealer's Hand: ", *dealer.cards, sep='\n ')
#     print("Dealer's Hand = ", dealer.value)
#     print("'\nPlayer's Hand: ", *player.cards, sep='\n ')
#     print("Player's Hand = ", player.value)


# def player_busts(player, dealer, chips):
#     print("PLAYER BUSTS!")
#     chips.lose_bet()


# def player_wins(player, dealer, chips):
#     print("PLAYER WINS!")
#     chips.win_bet()


# def dealer_busts(player, dealer, chips):
#     print("DEALER BUSTS!")
#     chips.win_bet()


# def dealer_wins(player, dealer, chips):
#     print("DEALER WINS!")
#     chips.lose_bet()


# def push(player, dealer):
#     print("It's a push! Dealer and Player tie!")


def check_if_round_over(players):  # sprawdzenie czy wszyscy gracze skonczyli runde
    playing_round = False

    for player in players:
        if player.playing is True:
            playing_round = True
            break

    return playing_round


def add_points(players):  # dodawanie punktow po rundzie
    players_max = []
    for player in players:
        if player.hand.value > 21:  # sprawdzenie czy gracz nie spalil reki
            pass

        elif len(players_max) == 0 or player.hand.value == players_max[0].hand.value:
            players_max.append(player)

        elif player.hand.value > players_max[0].hand.value:
            players_max.clear()
            players_max = [player]

    for player in players_max:
        print(player.name + " " + str(player.hand.value))
        player.points += 1


deck = Deck()  # stworzenie talii
deck.shuffle_cards()

number_of_players = 4

player1 = Player("siema1", "player")     # gracz
player2 = Player("siema2", "ceasy")      # komputer latwy
player3 = Player("siema3", "cmedium")    # komputer sredni
player4 = Player("siema4", "chard")      # komputer trudny

players = [player1, player2, player3, player4]

while len(deck.deck) > number_of_players * 2:
    if playing:
        print("Welcome to Blackjack!")
        playing_round = True

        player1.start_round(deck)
        player2.start_round(deck)
        player3.start_round(deck)
        player4.start_round(deck)

        while playing_round:  # round loop
            for player in players:
                print("Playing: " + player.name + " value: " + str(player.hand.value))
                if player.playing is True:
                    hit_or_stand(deck, player)
                    print("value: " + str(player.hand.value))
                    if len(deck.deck) == 0:
                        playing = False
                        playing_round = False
                        break

            playing_round = check_if_round_over(players)

        add_points(players)

    else:
        break

        # player_hand = Hand()
        # player_hand.add_card(deck.deal())
        # player_hand.add_card(deck.deal())

        # dealer_hand = Hand()
        # dealer_hand.add_card(deck.deal())
        # dealer_hand.add_card(deck.deal())

        # if player_hand.value <= 21:
        #     while dealer_hand.value < 17:
        #         hit(deck, dealer_hand)

        #     show_all(player_hand, dealer_hand)

        #     if dealer_hand.value > 21:
        #         dealer_busts(player_hand, dealer_hand, player_chips)

        #     elif dealer_hand.value > player_hand.value:
        #         dealer_wins(player_hand, dealer_hand, player_chips)

        #     elif dealer_hand.value < player_hand.value:
        #         player_wins(player_hand, dealer_hand, player_chips)

        #     elif player_hand.value > 21:
        #         player_busts(player_hand, dealer_hand, player_chips)

        # print("\nPlayer's winnings stand at: ", player_chips.total)

        # new_game = input("Would you like to play again? Enter 'y' or 'n': ")
        # if new_game[0].lower() == 'y':
        #     playing = True
        #     continue
        # else:
        #     print("Thanks for playing")
        #     break

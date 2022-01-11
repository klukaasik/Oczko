import random
from .player import Player
from .hand import Hand
# from card import Card
from .cards import Cards
# from deck import Deck
# from replay import Replay
from .convert_methods import Convert
import sqlite3 as sql

cards = Cards()
suits = cards.suits
ranks = cards.ranks
values = cards.values
playing = True  # sprawdzanie, czy pilka nadal w grze


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


def hit_on_replays(card, hand):
    hand.add_card(card)


def hit_or_stand(deck, player, decision):  # zapytaj gracza, czy chce podbijac dalej
    if player.type == "player":
        if decision == 'hit':
            hit(deck, player.hand)
            player.cards_played += 1
            update_cards(player.name)
            return True

        elif decision == 'stand':
            player.playing = False
            return False

    if player.type == "ceasy":  # easy (losowe decyzje)
        ask = bool(random.getrandbits(1))
        if ask is True and player.hand.value < 21:
            print(player.name + " hits.")
            hit(deck, player.hand)
            player.cards_played += 1
            return True

        else:
            print(player.name + " stands.")
            player.playing = False
            return False

    if player.type == "cmedium":  # medium (bierze karte gdy value reki <= 17)
        if player.hand.value <= 17:
            print(player.name + " hits.")
            hit(deck, player.hand)
            player.cards_played += 1
            return True

        else:
            print(player.name + " stands.")
            player.playing = False
            return False

    if player.type == "chard":  # hard (podglada jaka karta bedzie nastepna)
        if player.hand.value + values[deck.deck[len(deck.deck) - 1].rank] > 21:
            if deck.deck[len(deck.deck) - 1].rank == 'Ace':
                if player.hand.value + 1 <= 21:
                    print(player.name + " hits.")
                    hit(deck, player.hand)
                    player.cards_played += 1
                    return True

                else:
                    print(player.name + " stands.")
                    player.playing = False
                    return False

            else:
                print(player.name + " stands.")
                player.playing = False
                return False

        else:
            print(player.name + " hits.")
            hit(deck, player.hand)
            player.cards_played += 1
            return False


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
        if player.hand.value > 21 and player.check_if_pers() is False:  # sprawdzenie czy gracz nie spalil reki
            pass

        elif len(players_max) == 0 or player.hand.value == players_max[0].hand.value:
            players_max.append(player)

        elif player.hand.value > players_max[0].hand.value:
            players_max.clear()
            players_max = [player]

    return players_max

def update_cards(player):
    try:
        db = sql.connect('database.db')  # łączymy się do bazy
        c = db.cursor()  # dodajemy kursor

        # query = "SELECT user_id, username, password, games_played, win_rate, time_spent, cards_used, coins from users"
        # c.execute(query)
        # db.commit()

        query = "UPDATE users SET cards_used = cards_used + 1 where username = '{}'".format(player)
        c.execute(query)
        db.commit()

    except sql.Error as e:
        print("sth wrong with update")


# deck = Deck()  # stworzenie talii
# deck.shuffle_cards()

# number_of_players = 4

# player1 = Player("siema1", "player", 1)     # gracz
# player2 = Player("siema2", "ceasy", 2)      # komputer latwy
# player3 = Player("siema3", "cmedium", 3)    # komputer sredni
# player4 = Player("siema4", "chard", 4)      # komputer trudny

# players = [player1, player2, player3, player4]

# replay = Replay()
# replay.add_players(players)
# print("Welcome to Blackjack!")


# while len(deck.deck) > number_of_players * 2:
#     if playing:
#         playing_round = True

#         player1.start_round(deck)
#         player2.start_round(deck)
#         player3.start_round(deck)
#         player4.start_round(deck)

#         round_number = 1

#         replay.add_first_hands(players)

#         while playing_round:  # round loop
#             for player in players:
#                 print("Playing: " + player.name + " value: " + str(player.hand.value))
#                 if player.playing is True:
#                     decision = hit_or_stand(deck, player)
#                     replay.add_move(decision, player.player_number, player.hand.new_card)
#                     print("value: " + str(player.hand.value))
#                     if len(deck.deck) == 0:
#                         playing = False
#                         playing_round = False
#                         break

#             playing_round = check_if_round_over(players)

#         round_number += 1
#         replay.add_round_to_game_replay()
#         add_points(players)

#     else:
#         break

# odczytywanie zapisu z replaya

# replay = [['siema11', 'siema22', 'siema33', 'siema44'], ['DTC5C8CAHKD8S8C7', '1S', '2HC4', '3S', '4S', '2HHJ', '2HCJ', '2S'],
# ['S4CTSASKH6HTH4H9', '1S', '2S', '3HDK', '4S', '3S', '4S']]
# players = []
# number_of_players = len(replay[0])
# convert = Convert()

# for player in replay[0]:
#     player, player_number = player[:-1], player[-1]
#     player_number = int(player_number)

#     players.append(Player(player, "replay", player_number))

# i = 1
# while i < len(replay):
#     aux = number_of_players - 1
#     first_hands = replay[i][0]
#     while first_hands != "":
#         first_hands, card = first_hands[:-2], first_hands[-2:]
#         players[aux].hand = Hand()
#         hit_on_replays(convert.convert_string_to_card(card), players[aux].hand)
#         first_hands, card = first_hands[:-2], first_hands[-2:]
#         hit_on_replays(convert.convert_string_to_card(card), players[aux].hand)
#         aux = aux - 1

#     j = 1
#     while j < len(replay[i]):
#         player = players[int(replay[i][j][0]) - 1]
#         if replay[i][j][1] == "H":
#             card = replay[i][j][-2:]
#             hit_on_replays(convert.convert_string_to_card(card), players[int(replay[i][j][0]) - 1].hand)

#         if replay[i][j][1] == "S":
#             pass

#         j += 1

#     i += 1

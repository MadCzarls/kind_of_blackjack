# python3

# Copyright (C) 2016 Karol Kasiarz

# Kind of blackjack, according to the rules we used to have when we play in my 
# home ;]. Your score has to be higher than another player and as close to the 
# 21 points as possible. Having more then 21 points means autofail.

# Having 21 points with ten and ace means "natural twenty-one (pl: "oczko")" 
# and it beats another player"s 21 points if the latter consists of with more than two cards.

# The one exception when you can have more then 21 is having two aces 
# (22 points) and that means you have "blackjack (pl: "perskie oczko")" which beats
# "natural twenty-one". Having more than 21 points in the rest of cases means 
# "going bust/busting (pl: "fura")" which is game over and means defeat for this player, 
# even if the second one hasn"t made his/hers turn yet. That"s why you should 
# play two matches (or even number of them) each time.


import random
import sys
import os


class Deck:

    """class for decks; on the beginning of the game players choose which one 
    they will be using; every deck consisted of pairs card_name<>card_points_value"""
    
    small = {
        "dziewiątka kier": 0, "dziesiątka kier": 10, "walet kier": 3, 
        "dama kier": 4, "król kier": 5, "as kier": 11,
        "dziewiątka pik": 0, "dziesiątka pik": 10, "walet pik": 3, 
        "dama pik": 4, "król pik": 5, "as pik": 11,
        "dziewiątka karo": 0, "dziesiątka karo": 10, "walet karo": 3, 
        "dama karo": 4, "król karo": 5, "as karo": 11,
        "dziewiątka trefl": 0, "dziesiątka trefl": 10, "walet trefl": 3,
        "dama trefl": 4, "król trefl": 5, "as trefl": 11
        }
    
    full = {
        "dwójka kier": 2, "trójka kier": 3, "czwórka kier": 4, 
        "piątka kier": 5, "szóstka kier": 6, "siódemka kier": 7, 
        "ósemka kier": 8, "dziewiątka kier": 9, "dziesiątka kier": 10,
        "walet kier": 3, "dama kier": 4, "król kier": 5, "as kier": 11,
        "dwójka pik": 2, "trójka pik": 3, "czwórka pik": 4,
        "piątka pik": 5, "szóstka pik": 6, "siódemka pik": 7, 
        "ósemka pik": 8, "dziewiątka pik": 9, "dziesiątka pik": 10,
        "walet pik": 3, "dama pik": 4, "król pik": 5, "as pik": 11,
        "dwójka karo": 2, "trójka karo": 3, "czwórka karo": 4, 
        "piątka karo": 5, "szóstka karo": 6, "siódemka karo": 7, 
        "ósemka karo": 8, "dziewiątka karo": 9, "dziesiątka karo": 10, 
        "walet karo": 3, "dama karo": 4, "król karo": 5, "as karo": 11,
        "dwójka trefl": 2, "trójka trefl": 3, "czwórka trefl": 4, 
        "piątka trefl": 5, "szóstka trefl": 6, "siódemka trefl": 7, 
        "ósemka trefl": 8, "dziewiątka trefl": 9, "dziesiątka trefl": 10,
        "walet trefl": 3, "dama trefl": 4, "król trefl": 5, "as trefl": 11
        }


class Opening:

    """class for opening of the game"""

    def start(self):

        """starting function, here players type their names and choose deck"""

        print("\nROZPOCZNIJMY GRĘ!")
        print("\nBy gra była fair należy rozegrać mecz i rewanż")
        print("(lub parzystą liczbę gier).\n")

        print("Podaj imię pierwszego gracza: ")
        name_1 = input(">>> ")

        print("Podaj imię drugiego gracza: ")
        name_2 = input(">>> ")

        print("Teraz wybierzcie talię, którą chcecie grać:")
        print("1. Mała talia.")
        print("2. Pełna talia.")
        
        while True:
            choice = input("Numer talii? ")
            deck = Deck()
            
            player_1 = Player(name_1)
            player_2 = Player(name_2)
        
            if choice == "1":
                game = Game(player_1, player_2, deck.small)
            elif choice == "2":
                game = Game(player_1, player_2, deck.full)
            else:
                print("Podaj numer talii!")
            
            cls()
            game.first_deal()


class Game:

    """manages order of action during the game; has scores-checking mechanisms"""

    def __init__(self, player1, player2, chosen_deck):
        self.player1 = player1
        self.player2 = player2
        self.chosen_deck = chosen_deck
        self.turn = 1
        
    def first_deal(self):

        """first deal of the game, automatically dispense cards to the players 
        and go to the next turn"""
        
        print("*-" * 10)
        print("Tura %d" % self.turn) 
        print("*-" * 10)
        print(u"\nKażdy z graczy otrzymuje po jednej karcie.")
                        
        self.player1.pick_card(self.chosen_deck)
        self.player2.pick_card(self.chosen_deck)

        print("Liczba punktów:")
        print("%s: %d punktów." % (self.player1.name, self.player1.points))
        print("%s: %d punktów." % (self.player2.name, self.player2.points))
        print("Wciśnij ENTER, aby przejść dalej.")
        input(">>> ")
        cls()
        self.turn += 1
        self.next_deals()

    def next_deals(self):

        """every next deal of the game"""

        while True:
            print("*-" * 10)
            print("Tura %d" % self.turn)
            print("*-" * 10)

            if self.player1.stand == False and self.player2.stand == False:
                self.player1.play_turn(self.player2, self.chosen_deck)
                self.player2.play_turn(self.player1, self.chosen_deck)

            elif self.player1.stand == True and self.player2.stand == False:
                print("%s pasuje." % self.player1.name)
                self.player2.play_turn(self.player1, self.chosen_deck)

            elif player1.stand == False and player2.stand == True:
                print("%s pasuje." % self.player2.name)
                self.player1.play_turn(self.player2, self.chosen_deck)

            else:
                print("Obu graczy spasowało. Trwa sprawdzanie wyników...")
                self.last_checking()

            cls()
            print("-" * 20)
            print("KONIEC TURY nr %d." % self.turn)
            print("Liczba punktów:")
            print("%s: %d punktów." % (self.player1.name, self.player1.points))
            print("%s: %d punktów.\n" % (self.player2.name, self.player2.points))

            self.turn += 1
            
            self.checking()

    def checking(self):
    
        """scores checking"""

        if self.player1.points < 21 and self.player2.points < 21:
            self.next_deals()
        
        else:
            if self.player1.points == 22 and len(self.player1.cards_in_hand) == 2 \
                and self.player2.points == 22 and len(self.player2.cards_in_hand) == 2:
                print("Obu graczy ma PERSKIE OCZKO! WOW!")
                print("REMIS.")

            elif self.player1.points == 21 and len(self.player1.cards_in_hand) == 2 \
                and self.player2.points == 21 and len(self.player2.cards_in_hand) == 2:
                print("Obu graczy ma OCZKO!")
                print("REMIS.")
            
            elif self.player1.points == 21 and len(self.player1.cards_in_hand) == 2:
                print("%s ma OCZKO!" % self.player1.name)
                print("Zwycięża %s!!!" % self.player1.name)

            elif self.player2.points == 21 and len(self.player2.cards_in_hand) == 2:
                print("%s ma OCZKO!" % self.player2.name)
                print("Zwycięża %s!!!" % self.player2.name)

            elif self.player1.points == 22 and len(player1.cards_in_hand) == 2:
                print("%s ma PERSKIE OCZKO!" % self.player1.name)
                print("Zwycięża %s!!!" % self.player1.name)

            elif self.player2.points == 22 and len(self.player2.cards_in_hand) == 2:
                print("%s ma PERSKIE OCZKO!" % self.player2.name)
                print("Zwycięża %s!!!" % self.player2.name)
            
            elif self.player1.points == 21 and self.player2.points == 21:
                print("Obu graczy ma 21 punktów!")
                print("REMIS.")
            
            elif self.player1.points == 21:
                print("%s ma 21 punktów!" % self.player1.name)
                print("Zwycięża %s!!!" % self.player1.name)
            
            elif self.player2.points == 21:
                print("%s ma 21 punktów!" % self.player2.name)
                print("Zwycięża %s!!!" % self.player2.name)
                
        
            print("KONIEC.")
            sys.exit(0)
        
    def last_checking(self):

        """scores checking in case of both players passing their turns"""

        if self.player1.points > self.player2.points:
            print("%s ma więcej punktów niż %s." % (player1.name, player2.name))
            print("Zwycięża %s!" % player1.name)
            
        elif self.player2.points > self.player1.points:
            print("%s ma więcej punktów niż %s." % (player2.name, player1.name))
            print("Zwycięża %s!" % player2.name)

        elif self.player1.oints == self.player2.points:
            print("Obu graczy ma taką samą ilość punktów!")
            print("REMIS.")
        
        print("KONIEC.")
        sys.exit(0)


class Player:

    """class for player; has methods which handle his/hers actions during
    the game and manages cards in hand; also has "busting" mechanism"""

    def __init__(self, name):
        self.name = name
        self.points = 0
        self.cards_in_hand = []
        self.stand = False

    def pick_card(self, deck):

        """defines mechanism of picking card, removing picked one from deck, 
        adding points value to the specific player"s pool etc"""

        card_name = random.sample(list(deck), 1)[0]# index is needed since sample() returns list
        card_value = deck[card_name]
        print("%s otrzymuje: %s." % (self.name, card_name))
        
        del deck[card_name]
        
        self.points += card_value
        self.cards_in_hand.append(card_name)

    def play_turn(self, another_player, deck):

        """defines player"s turn, second argument is another player;
        here is also defined mechanism of autofailing when one of the player
        has more than 21 points, no matter if the latter player did his/her turn"""

        print("Akcja należy do: %s." % self.name)
        print("1) Dobranie karty.")
        print("2) Pass.")
        print("Wpisz numer akcji:")
        
        while True:
            action = input(">>> ")

            if action == "1":
                self.pick_card(deck)
                                
                if self.points > 21 and len(self.cards_in_hand) > 2:
                    if self.points == 22 or self.points == 23 or self.points == 24:
                        correct_noun = "punkty"
                    else:
                        correct_noun = "punktów"
                    
                    print("%s ma %d %s - 'fura'! PRZEGRYWA." % (self.name, self.points, correct_noun))
                    print("%s zwycięża, z liczbą punktów: %d!" % (another_player.name, another_player.points))
                    print("KONIEC.")
                    sys.exit(0)

                else:
                    break

            elif action == "2":
                print("%s pasuje." % self.name)
                self.stand = True
                break

            else:
                print("Podaj numer akcji!")

        print("%s - liczba punktów - %d." % (self.name, self.points))
        print("%s - koniec akcji." % self.name)
        print("Wciśnij ENTER, aby przejść dalej.")
        input(">>> ")


def cls():

    '''clears terminal window'''
    
    os.system('cls' if os.name=='nt' else 'clear')


def run():
    opening = Opening()
    opening.start()


run()
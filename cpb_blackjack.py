#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar 21 17:07:59 2020

@author: adunster
"""
'''
Simple 1 Player Blackjack
Created as a milestone project for Complete Python Bootcamp on Udemy.
Class objectives:
    - Text based Blackjack game
    - One player vs automated dealer
    - Player can stand or hit
    - Player can pick betting amount 
    - Track player's total money
    - Alert player of wins, losses, busts, etc.
    - IMPORTANT:  use classes and OOP, not just functions. Use classes to
      define deck, player hand.
    - Have fun
Personal additional objectives:
    - Create a visually appealing playing board using unicode text
    - Color cards if possible
    - Practice setting up some unittest tests for appropriate actions
'''

#from IPython.display import clear_output
import random
from cpb_blackjack_cardart import cardart
import pickle
#
#variable = input('Some input here: ')
#
#clear_output(wait=True)
#
#print(variable)

class Deck():
    '''
    Deck of cards with related methods
    '''
    def __init__(self):
        self.fresh = ['AD','2D','3D','4D','5D','6D','7D','8D','9D','10D','JD',
                      'QD','KD',
                      'AH','2H','3H','4H','5H','6H','7H','8H','9H','10H','JH',
                      'QH','KH',
                      'AC','2C','3C','4C','5C','6C','7C','8C','9C','10C','JC',
                      'QC','KC',
                      'AS','2S','3S','4S','5S','6S','7S','8S','9S','10S','JS',
                      'QS','KS'
                      ]

        
    def shuffle(self):
        self.shuffled = list(self.fresh)
        random.shuffle(self.shuffled)
        
    def remaining(self):
        return self.shuffled
        
    def deal(self):
        return self.shuffled.pop()
            
            

class Player():
    '''
    Player class
    '''
    def __init__(self,name='Player 1',balance=200,wins=0,losses=0):
        self.name = name
        self.balance = balance
        self.hand = []
        self.wins = wins
        self.losses = losses
    
    def rec_deal(self,card):
        self.hand.append(card)
    
    def discard(self):
        self.hand = []
    
    def bet(self,bet):
        self.balance -= bet
        
    def place_bet(self):
        ''' Requests bet, subtracts from balance and returns integer'''
        bet = ''
        while bet.isdigit() == False:
            bet = input('How much do you want to bet? Enter a number: ')
            if bet.isdigit():
                if int(bet) > self.balance:
                    print('Sorry, can\'t bet more than you have!')
                    bet = ''
                elif int(bet) < 0:
                    print('Can\'t place negative bet.')
                    bet = ''
            else:
                print('Please enter a number only.')
        self.bet(int(bet))
        return int(bet)
    
    def win(self,winnings):
        if self.balance + winnings >= 99999:
            self.balance = 99999
        else:
            self.balance += winnings
        self.wins += 1
        
    def __str__(self):
        return 'Player: {name}\nBalance: {bal} Wins: {wins} Losses: {loss}'.format(name=self.name,
                        bal=self.balance, wins=self.wins, loss=self.losses)
        


class Dealer(Player):
    '''
    Dealer class
    '''
    
    def __init__(self):
        self.visible_hand = []
        self.hand = []
        
    
    def rec_deal(self,card):
        '''Expects only one card at a time.'''
        if len(self.hand) == 0:
            self.hand.append(card)
            self.visible_hand.append('*')
        else: 
            self.hand.append(card)
            self.visible_hand.append(card)
            
    def discard(self):
        self.hand = []
        self.visible_hand = []




def player_select():
    '''
    Select player profile from file.
    Will create file if nonexistent, default to new player setup if empty, 
    saves new player profile as created, allows for deletion of unwanted 
    player profiles.
    '''
    global player
    global current

    '''Check for and create file'''
    try:
        with open('cpb_blackjack_players.data', 'rb') as players_file:
            player = pickle.load(players_file)
    except FileNotFoundError:
        with open('cpb_blackjack_players.data', 'wb') as players_file:
            player = []
            pickle.dump(player, players_file)
        
    '''Selection menu'''
    while len(player) > 0:
        choice = ''
        for i in range(len(player)):
            print('\nFILE {}: '.format(i),player[i],sep='')
        choice = input('Entire file number to select player, \'N\' for new player, or \'D\' followed by a file number to delete a profile: ')
        if choice.isdigit():
            if int(choice) in range(len(player)):
                current = int(choice)
                print('Welcome to Blackjack, {}!'.format(player[current].name))
                break
            else:
                print('Please enter a valid selection.')

        elif str.upper(choice) == 'N':
            player.append(Player(*new_player_setup()))
            with open('cpb_blackjack_players.data', 'wb') as players_file:
                pickle.dump(player, players_file)
            current = -1
            print('Welcome to Blackjack, {}!'.format(player[current].name))
            break
        elif str.upper(choice[0]) == 'D':
            lst = [str(char) for char in choice if char.isdigit()]
            if not lst:
                print('Invalid input, enter a file selection with D.')
                continue
            index = ''
            for i in lst:
                index = index + i
            confirm = ''
            while confirm == '':
                confirm = input('Delete {}? Type \'Y\' to confirm: '.format(player[int(index)].name))
                if str.upper(confirm[0]) == 'Y':
                    print('{} deleted!'.format(player[int(index)].name))
                    player.pop(int(index))
                    with open('cpb_blackjack_players.data', 'wb') as players_file:
                        pickle.dump(player, players_file)
                    break
                else:
                    break

        
    '''Default to new player creation if no players found'''
    if len(player) == 0:
        print('No players found! Create a new player.')
        player.append(Player(*new_player_setup()))
        with open('cpb_blackjack_players.data', 'wb') as players_file:
            pickle.dump(player, players_file)

def save():
    '''
    Saves current player info after discards hand data.
    '''
    player[current].discard()
    dealer.discard()
    with open('cpb_blackjack_players.data', 'wb') as players_file:
        pickle.dump(player, players_file)

def new_player_setup():
    name = ''
    balance = ''
    while name == '':
        name = input('Please enter a player name: ')
    while balance.isdigit() == False:
        balance = input('Please enter a starting balance (hit enter for $200 default): $')
        if balance.isdigit() and int(balance) >= 99999:
            print('Invalid starting balance.')
            balance = ''
        elif balance == '':
            return (name), (200)
    return (name), (int(balance))
    


def draw_card(line,hand):
    '''
    Draw given cards to the screen, one line at a time.
    Input: integer, list of strings
    Output: string
    '''
    
    output = ''

    for i in range(len(hand)):
        output += cardart[hand[i]][line]
    return output

def check_value(hand):
    '''
    Determine value of hand.
    Input: list of strings
    Output: integer
    '''
    ace = False
    count_ace = 0
    total = []
    for card in hand:
        if card[0] == 'A':
            ace = True
            count_ace += 1
            total.append(11)
        elif card[0] in ('J','Q','K') or card[0:2] == '10':
            total.append(10)
        elif str.isdigit(card[0]):
            total.append(int(card[0]))
            
    if not ace:
        return sum(total)
    
    while count_ace > 0:
        if sum(total) <= 21:
            return sum(total)
        else:
            total.append(-10)
        count_ace -= 1
        
    return sum(total)

def initial_deal(deck,player,dealer):
    '''
    Shuffle deck, deal initial two cards to player and dealer, one at a time.
    '''
    deck.shuffle()
    for _ in range(2):
        player.rec_deal(deck.deal())
        dealer.rec_deal(deck.deal())
    

def draw_board(dealer_hand,player_hand):
    '''
    Draws the current board with dealer hand on top, representation of
    remaining deck, and player's hand, bet and balance at bottom of window.
    '''
#    clear_output(wait=False)
    for i in range(6):
        if i == 2:
            print('  DEALER Hand:    ',draw_card(i,dealer_hand),sep='')
        else:
            print(' '*18,draw_card(i,dealer_hand),sep='')
            
    print()
    
    for i in range(6):
        if i == 0:
            print('   ',draw_card(i,'*'),sep='')
        elif i == 1:
            print('  .',draw_card(i,'*'),sep='')
        else:
            print('  |',draw_card(i,'*'),sep='')
    print('  |/_~_\|')
    print()
    
    for i in range(6):
        if i == 1:
            print('  {:^14.14}  '.format(player[current].name),draw_card(i,player_hand),sep='')
        elif i == 2:
            print('  PLAYER Hand:    ',draw_card(i,player_hand),sep='')
        elif i == 3:
            print('  Bet:  {:5d}     '.format(bet),draw_card(i,player_hand),sep='')
        elif i == 4:
            print('  Bal:  {:5d}     '.format(player[current].balance),draw_card(i,player_hand),sep='')
        elif i == 5:
            print('  Cards:   {:2d}     '.format(check_value(player[current].hand)),draw_card(i,player_hand),sep='')
        else: 
            print(' '*18,draw_card(i,player_hand),sep='')
    print()

def press_enter(string='Press enter to continue.'):
    _ = input(string)
            
def player_move():
    '''
    Player's move choices.
    '''
    global player_turn
    choice = ''
    while choice == '':
        choice = input('[H]it or [S]tand?: ')
        if choice == '':
            print('Invalid input.')
        elif choice[0].upper() == 'H':
            player[current].rec_deal(deck.deal())
        elif choice[0].upper() == 'S':
            print('Stand! Dealer\'s turn.')
            player_turn = False
            break
        else:
            choice = ''
            print('Invalid input.')
    
    
def dealer_move():
    '''
    Automated dealer turn with pauses for player to see what's happening.
    Returns False when turn is over.
    '''
    global natural
    draw_board(dealer.hand,player[current].hand)
    print('Dealer total: {}'.format(check_value(dealer.hand)))
    '''Check initial reveal win conditions.'''
    if check_value(player[current].hand) == check_value(dealer.hand) == 21:
        print('Draw! No win or loss. Bet returned.')
        player[current].balance += bet
        return False
    elif natural == True and check_value(dealer.hand) < 21:
        winnings = int(bet * 1.5)
        print('Player has a natural and dealer does not. You win!')
        print('Congratulations, {p}, your winnings: ${b} + ${w} = ${t}!'.format(p=player[current].name,b=bet,w=winnings,t=(bet + winnings)))
        player[current].win((winnings + bet))
        save()
        natural = False
        return False
    elif 21 > check_value(dealer.hand) > check_value(player[current].hand):
        print('Dealer wins with {}! Sorry, you lose.'.format(check_value(dealer.hand)))
        player[current].losses += 1
        save()
        return False
    press_enter('Dealer hits. Press enter to continue.')
    while check_value(player[current].hand) >= check_value(dealer.hand):
        dealer.rec_deal(deck.deal())
        draw_board(dealer.hand,player[current].hand)
        if check_value(player[current].hand) == check_value(dealer.hand) == 21:
            print('Draw! No win or loss. Bet returned.')
            player[current].balance += bet
            return False
        elif check_value(dealer.hand) == 21:
            print('Dealer Blackjack! Sorry, you lose.')
            player[current].losses += 1
            save()
            return False
        elif check_value(dealer.hand) > 21:
            winnings = int(bet)
            print('Dealer busts with {}! You win!'.format(check_value(dealer.hand)))
            print('Congratulations, {p}, your winnings: ${b} + ${w} = ${t}!'.format(p=player[current].name,b=bet,w=winnings,t=(bet + winnings)))
            player[current].win((winnings + bet))
            save()
            natural = False
            return False
        elif 21 > check_value(dealer.hand) > check_value(player[current].hand):
            print('Dealer wins with {}! Sorry, you lose.'.format(check_value(dealer.hand)))
            player[current].losses += 1
            save()
            return False
        elif check_value(player[current].hand) >= check_value(dealer.hand):
            print('Dealer total: {}'.format(check_value(dealer.hand)))
            press_enter('Dealer hits.')
        


def check_win(hand):
    if check_value(hand) == 21:
        return True
    else:
        return False


def check_reshuffle():
    if len(deck.shuffled) <= 13:
        return True
    else:
        return False

def draw_welcome():
    '''Draws the welcome screen with a random selection of 6 cards'''
    hand_welcome = random.sample(deck.fresh, k = 6)
    print(' '*3,draw_card(0,[hand_welcome[0]]),' '*22,draw_card(0,[hand_welcome[1]]),
          ' '*8,'_',' '*4,'_',sep='')
    print(' '*3,draw_card(1,[hand_welcome[0]]),' '*18,'_',' '*3,
          draw_card(1,[hand_welcome[1]]),' '*7,'/ \  / \\',' '*5,
          draw_card(0,[hand_welcome[2]]),sep='')
    print(' '*3,draw_card(2,[hand_welcome[0]]),' '*11,'______| |',' '*2,
          draw_card(2,[hand_welcome[1]]),' '*3,'___/__ \/ _ \\',' '*4,
          draw_card(1,[hand_welcome[2]]),sep='')
    print(' '*3,(draw_card(3,[hand_welcome[0]])[:2]),'__',
          (draw_card(3,[hand_welcome[0]])[4:7]),' '*9,'_|  ____| |',' '*2,
          (draw_card(3,[hand_welcome[1]])[:5]),'_|__/_____ \  / \ \\',' '*3,
          draw_card(2,[hand_welcome[2]]),sep='')
    print(' '*3,(draw_card(4,[hand_welcome[0]])[:2]),'\ \\',
          (draw_card(4,[hand_welcome[0]])[5:7]),' '*8,'/ / |____| |',' '*2,
          (draw_card(4,[hand_welcome[1]])[:4]),'/ ____ \| |\ \/  |_|___',
          draw_card(3,[hand_welcome[2]]),sep='')
    print(' '*3,(draw_card(5,[hand_welcome[0]])[:3]),'\ \\',
          (draw_card(4,[hand_welcome[0]])[6:7]),' '*2,'/\\',' '*3,
          '/ /|  ___|| |__',(draw_card(5,[hand_welcome[1]])[:3]),
          '/ / ( (\_)_| ) ) |  _____|',(draw_card(4,[hand_welcome[2]])[2:7]),sep='')
    print(' '*7,'\ \ /  \ / /_| |____|______( (   \ \____/ /  | |___ ',
          (draw_card(5,[hand_welcome[2]])),sep='')
    print(' '*8,'\   /\   /',(draw_card(1,[hand_welcome[3]])[1:3]),'|_______|',
          ' '*6,'\ \___\/ )___/   |  ___|',sep='')
    print(' '*9,'\_/  \_/',(draw_card(2,[hand_welcome[3]])),' '*12,'\______/',
          (draw_card(1,[hand_welcome[4]])[5:7]),' '*6,'| |_____',sep='')
    print(' '*17,(draw_card(3,[hand_welcome[3]])),' '*15,
          (draw_card(2,[hand_welcome[4]])),' '*6,'|_______| ',
          (draw_card(0,[hand_welcome[5]])),sep='')
    print(' '*6,'*TO*',' '*7,(draw_card(4,[hand_welcome[3]])),' '*15,
          (draw_card(3,[hand_welcome[4]])),' '*16,
          (draw_card(1,[hand_welcome[5]])),sep='')
    print(' '*17,(draw_card(5,[hand_welcome[3]])),' '*15,
          (draw_card(4,[hand_welcome[4]])),' '*16,
          (draw_card(2,[hand_welcome[5]])),sep='')
    print(' '*39,(draw_card(5,[hand_welcome[4]])),' '*16,
          (draw_card(3,[hand_welcome[5]])),sep='')
    print(' '*10,'BlackJack!!!',' '*40,(draw_card(4,[hand_welcome[5]])),sep='')
    print(' '*62,(draw_card(5,[hand_welcome[5]])),sep='')




deck = Deck()
dealer = Dealer()
bet = 0
current = 0
ready = False
natural = False


#hand = ['AH', 'JD']

#player_select()

#player_setup = new_player_setup()

#player.append(Player(*new_player_setup()))
#player.append(Player('George',345))

#print(player[0])

#print(random.choices(deck.fresh, k = 4))

#draw_welcome()

##
#player[current].discard()
#initial_deal(deck,player[current],dealer)
##print(player[current].hand)
##print(dealer.hand)
##print(dealer.visible_hand)
#draw_board(dealer.visible_hand,player[current].hand)
##player[current].rec_deal(deck.deal())
##draw_board(dealer.visible_hand,player[current].hand)
#player[current].hand = ['JH','7D']
#
#dealer_turn()


#print(player.balance)
#bet = player.place_bet()
#print(player.balance)
#print(bet)

#for i in range(6):
#    print(draw_card(i,hand),draw_card(i,hand))

#print(check_value(hand))
#
#for i in range(2,11):
#    hand.append(str(i) + 'H')

#player.rec_deal(deck.deal())
#player.rec_deal(deck.deal())
#player.rec_deal(deck.deal())

#
#print(dealer.hand)
#
#dealer.rec_deal('AS')
#
#print(dealer.hand, dealer.visible_hand)
#
#dealer.rec_deal('2S')
#
#print(dealer.hand, dealer.visible_hand)
#'''

if __name__ == '__main__':
    draw_welcome()
    print('Select a player profile:\n\n')
    player_select()
    draw_board(dealer.visible_hand,player[current].hand)
#    are_you_ready = input('Are you ready to play? ')
#    if are_you_ready[0].lower() == 'y' or are_you_ready.lower() == 'ready':
    ready = True
#    else:
#        print('Thanks for playing!')
    while ready:
        player_turn = True
        while player_turn:
            while bet == 0:
                bet = player[current].place_bet()
                draw_board(dealer.visible_hand,player[current].hand)
            if not player[current].hand:
                press_enter('Press enter to deal.')
                initial_deal(deck,player[current],dealer)
                draw_board(dealer.visible_hand,player[current].hand)
                if check_win(player[current].hand) == True:
                    natural = True
                    print('Total: {}'.format(check_value(player[current].hand)))
                    print('A natural! Dealer\'s turn.')
                    player_turn = False
                    break
            draw_board(dealer.visible_hand,player[current].hand)
            print('Total: {}'.format(check_value(player[current].hand)))
            if check_win(player[current].hand) == True:
                print('Blackjack! Dealer\'s turn.')
                player_turn = False
                break
            elif check_value(player[current].hand) > 21:
                print('Bust! Sorry, you lose!')
                player[current].losses += 1
                player_turn = False
                player_lost = True
                save()
                break
            player_move()
        
        dealer_turn = True
        while dealer_turn and not player_lost:
            dealer_turn = dealer_move()
        
        
        press_enter()
        
        
        
        
        
        
        bet = 0
        player[current].discard()
        dealer.discard()
        ready = False
        are_you_ready = input('Play another round? ')
        if are_you_ready[0].lower() == 'y' or are_you_ready.lower() == 'ready':
            ready = True
        else:
            print('Thanks for playing! Re-run program to play again or with a different profile.')
            break
    
#'''
'''
game

welcome screen
draw staggered cards? range 8, some i, some i+/-2 .. ? 
if i == 0-1, draw i
if i == 2-6, draw i, draw i-2
if i == 6-8, draw i-2
, options: new player, player select (IF players exist)

if new player, auto select generated player

if select player, display options

or:
    
welcome screen, press whatever to begin. 

retrieves players from file.

displays list of players, select index, or type new for new player, or del + index to delete player

check for strings 'new' and 'del x', check if digit, if digit check if in range len list

if player loses all money, ie  balance == 0 and dealer just won, player at that index should be deleted 
if player balance goes over 99,999, set bal to 99999

player places bet

initial deal

check for natural (check for ace?): both natural, draw (bet returned to player). if only player has a natural, 
he gets bet + 1.5x bet. if only dealer has natural, display dealer's hand, player loses bet.

player option: hit or stand:

if hit, player receives another card.
check value: over 21 = lose (bust), bet forfeit

if 21 or under, and player chooses stand, then dealer's turn

per assignment, if dealer is under 21 and under player, dealer will hit. 
(pause for input? how to get input of just pressing enter, etc?)
if dealer = player = 21, player receives original bet.
if player did not bust and dealer busts, player receives 2x original bet.
if dealer is > player <= 21, dealer wins, player loses bet.

save balance, win/loss to player list

Play again? (play again, player select, exit)

'''

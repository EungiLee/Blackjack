'''
This runs a blackjack game

Eungi Lee, 28/08/02
'''
import random

class Card:
    def __init__(self,value,colour):
        self.value=value
        self.colour=colour

def Blackjack(money,deck):
    ''' Eungi Lee
    This function runs a simulation of a blackjack game

    inputs:
    money : amount of money to bet (int)
    deck : deck of cards (list)

    output:
    final : final balance (int)

    notes:
    Each bet is assumed to be $50

    '''
    
    #Condition for total money
    while money >0 or len(deck)>0:

        print('New round!')

        #Dealer hand
        Dealer= []
        for i in range(2):
            Dealer.append(deck.pop(0).value)
        
        print('The dealers hand is: '+ str(Dealer[1]))
        
        #Players hand
        Player= []
        for i in range(2):
            Player.append(deck.pop(0).value)
        
        print('Your hand is: '+ str(Player) + ' giving a total of '+ str(sum(Player)))

        x= input('Do you wish to hit (Y/N):').lower()

        while x=='y':
            Player.append(deck.pop(0).value)
            print('Your hand is:'+ str(Player)+ 'giving a total of '+ str(sum(Player)))

            if sum(Player)>21:
                money-=50
                print ('Bust! Bet of $50 lost, remaining balance: '+ str(money))
                break
            
            elif sum(Player)==21:
                money+=50
                print ('You won!, remaining balance: '+ str(money))
                break
                
            else:
                x= input('Do you wish to hit again (Y/N):').lower()
        
        if x =='n'

        


if __name__ == '__main__':

    #Create deck of cards (Ace is assumed to be 1)
    Colours = ['Diamond','Spades','Clubs','Hearts']
    Deck = [Card(value,colour) for value in range (1,11) for colour in Colours]
    JQK= [Card(10,colour) for i in range (3) for colour in Colours]
    Deck.extend(JQK)
    random.shuffle(Deck)

    money = int(input('Amount of money to play with (e.g. 500):'))

    Blackjack(money,Deck)

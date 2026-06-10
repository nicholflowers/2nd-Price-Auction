import random
import numpy as np


class User:
    '''Class to represent a user with a secret probability of clicking an ad.'''

    def __init__(self):
        '''Generating a probability between 0 and 1 from a uniform distribution'''
        self.__probability = random.uniform(0,1)
       
       
    def __repr__(self):
        '''User object with secret probability'''
        return "User object with secret probability" + str(self.__probability)
        

    def __str__(self):
        '''User object with a secret likelihood of clicking on an ad'''
        return "User object with a secret likelihood of clicking an ad"+ str(self.__probability)
        

    def show_ad(self):
        '''Returns True to represent the user clicking on an ad or False otherwise'''
        return np.random.choice([True, False], p=[self.__probability, 1-self.__probability])
        

class Auction:
    '''Class to represent an online second-price ad auction'''
    
    def __init__(self, users, bidders):
        '''Initializing users, bidders, and dictionary to store balances for each bidder in the auction'''
        self.users = users
        self.bidders = bidders
        self.balances = {}
        self.current_round = 0 

        #gets bidder object and index of bidder -- dont forgetdict key has to be immutable
        for bidder_id, bidder in enumerate(bidders): 
            self.balances[bidder_id] = 0 
        
    def __repr__(self):
        '''Return auction object with users and qualified bidders'''
        return f"Auction(users={self.users}, bidders={self.bidders})"

    def __str__(self):
        '''Return auction object with users and qualified bidders'''
        return f"Auction(users={self.users}, bidders={self.bidders})"

    def execute_round(self):
        '''Executes a single round of an auction, completing the following steps:
            - random user selection
            - bids from every qualified bidder in the auction
            - selection of winning bidder based on maximum bid
            - selection of actual price (second-highest bid)
            - showing ad to user and finding out whether or not they click
            - notifying winning bidder of price and user outcome and updating balance
            - notifying losing bidders of price'''
       
        #Select random User with uniform probability
        selected_user_id = random.randint(0, len(self.users)-1)  
        
		#Collect bids from qualified bidders
        bids = {}
  
        for bidder_id, bidder in enumerate(self.bidders): # 

            if self.balances[bidder_id] >= -1000:               
                bid_amount = bidder.bid(selected_user_id)
                bids[bidder_id] = bid_amount
                
        
        #Determine winner based on highest bid
        winning_bid = max(bids.values())
        
        tied_bidders = [ self.bidders[bidder_id] for bidder_id, bid in bids.items() if bid == winning_bid ]

        #Randomly select one winner from tied winners (each with equal probability)
        selected_winner = random.choice(tied_bidders)

        #Select winning price which is the 2nd highest price 
        
        if len(tied_bidders) == len(self.bidders):
            winning_price = winning_bid
        else:
            winning_price = sorted(bids.values(), reverse=True)[len(tied_bidders)]

        #showing ad to user and finding out whether or not they click -- returns 
        clicked = self.users[selected_user_id].show_ad()

        #returns each bidder with their 0.
        for bidder_id, bidder in enumerate(self.bidders):
            if bidder == selected_winner:  # notifying winning bidder of price, user outcome and updating balance
                bid_winner_id = bidder_id 
                #bidder.notify(win=True, price=winning_price, outcome=None)
                bidder.notify(auction_winner=True, clicked=clicked, price=winning_price)   
                #update balance for winner only
                self.balances[bidder_id]  -=  winning_price

                #if user clicked add 1 to bidder balance
                if clicked:
                    self.balances[bidder_id] += 1
                    # balances is a dict and key is the index of it in the bidders list#
        		
            else: # notifying losing bidders of price
                bidder.notify(auction_winner=False, clicked=None, price=winning_price)
       
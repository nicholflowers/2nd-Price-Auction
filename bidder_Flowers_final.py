import random


class Bidder:#solver
    '''Class to represent a bidder in an online second-price ad auction'''
    def __init__(self, num_users, num_rounds):
        '''Setting initial balance to 0, number of users, number of rounds, and round counter'''
        self.num_users  = num_users
        self.num_rounds = num_rounds 
        self.counter = 0 
        self.balance = 0
       
        
        # users_clicks dictionary : user_id -> sum of clicks observed (after notify)
        self.user_clicks = {user_id: 0 for user_id in range(num_users)} 

        # users_bids dictionary : user_id -> how many times did we bid on user_id  
        self.user_bids = {user_id: 0 for user_id in range(num_users)} 

        # users_wins dictionary : user_id -> how many times did we win on user_id  
        self.user_for_wins = {user_id: 0 for user_id in range(num_users)} 
        
        #User for current round -- given user_id in bid to use it in notify 
        self.user_for_round = None

    def __repr__(self):
       '''Bidder object with balance'''
       return f"Bidder(balance={self.balance})"

    def __str__(self):
        '''Bidder object with balance'''
        return f"Bidder(balance={self.balance})"

    def bid(self, user_id): 
        '''Returns a non-negative bid amount'''
        self.counter += 1 #incrementing
        
        self.user_for_round = user_id

        bid_amount = 0
        if self.user_for_wins[user_id] > 0:
          bid_amount = self.user_clicks[user_id] / self.user_for_wins[user_id]
        if bid_amount == 0:
          bid_amount = random.random()

        return round(bid_amount, 3) 
    
    def notify(self, auction_winner, price, clicked):
        '''Updates bidder attributes based on results from an auction round'''
        #increment bid count for bidder after each round
        self.user_bids[self.user_for_round] += 1
        if auction_winner:
           self.balance -= price
           self.user_for_wins[self.user_for_round] += 1
           if clicked:
              self.balance += 1
              self.user_clicks[self.user_for_round] += 1


# 💰 Second-Price Ad Auction Strategy

**A bidding agent for a simulated online ad auction that learns which users are worth paying for, recognized as one of the top algorithms in the class.**

## 📌 Overview

In an online ad auction, advertisers bid for the chance to show an ad to a user, and the value of that chance depends on something no one can see directly: how likely that user is to click. This project simulates that setting as a second-price sealed-bid auction. Each user has a fixed but hidden probability of clicking. In every round, bidders compete for a randomly chosen user, the highest bid wins, and the winner pays the second-highest bid. The winner earns one dollar if the user clicks and nothing if not, less the price paid.

The difficulty is that a bidder has to figure out which users are worth paying for while competing against other bidding algorithms doing exactly the same thing. That is the classic explore-versus-exploit problem: spend to learn, or spend on what already looks promising.

## 🎯 The Goal

The goal was to design a bidding agent that finishes with the highest possible balance over many rounds, competing head to head against bidding algorithms written by others. Because each user's click probability is hidden and never revealed, the agent has to infer a user's value from the outcomes it observes, weighing the cost of exploring unfamiliar users against the payoff of bidding on those it has already found to click.

## 🧭 The Approach

My agent treats each user as a separate learning problem and bids based on what it has seen so far.

- **Exploring unknown users.** When the agent has no history of winning a given user, it places a small random bid. This is inexpensive exploration: a way to occasionally win unfamiliar users and begin gathering evidence about them.
- **Exploiting known users.** Once the agent has won a user at least once, it bids that user's observed click rate, the number of clicks divided by the number of times it has won that user. Because a click is worth exactly one dollar, the observed click rate is a direct estimate of the user's expected value, so the agent bids roughly what the opportunity is worth.
- **Why this suits a second-price auction.** In a second-price auction, bidding close to true value is a sound strategy, since the winner pays the runner-up's bid rather than its own. Bidding the estimated value keeps the agent competitive without systematically overpaying.

The agent tracks per-user clicks, bids, and wins, updating them after every round as results come back. The surrounding simulation, the users with their hidden click probabilities and the auction that runs each round, determines the winner, and charges the second price, was built to a specified object-oriented structure.

## 🏆 Results

The agent was recognized by the instructor as one of the top algorithms in the class, earning full marks in the head-to-head competition against other students' submissions.

## 🧠 Skills Demonstrated

- **Decision-making under uncertainty:** an explore-and-exploit strategy for learning hidden user values, the core of a multi-armed bandit problem
- **Object-oriented design:** User, Bidder, and Auction classes with clear responsibilities and clean interfaces
- **Probabilistic reasoning:** estimating expected value from observed outcomes and bidding accordingly
- **Simulation:** modeling a competitive auction environment round by round

## 🧰 Stack

Python, using the standard library and NumPy.
# 2nd-Price-Auction

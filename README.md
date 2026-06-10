# 💰 Second-Price Ad Auction Strategy

**A bidding agent for a simulated second-price ad auction that infers each user's value from observed behavior.**

## 📌 Overview

In an online ad auction, advertisers bid for the chance to show an ad to a user, and the value of that chance depends on something no one can see directly: how likely that user is to click. This project simulates that setting as a second-price sealed-bid auction. Each user has a fixed but hidden probability of clicking. In every round, bidders compete for a randomly chosen user, the highest bid wins, and the winner pays the second-highest bid. The winner earns one dollar if the user clicks and nothing if not, less the price paid.

The difficulty is that a bidder has to figure out which users are worth paying for while competing against other bidding algorithms doing exactly the same thing. That is the classic explore-versus-exploit problem: spend to learn, or spend on what already looks promising.

## 🎯 The Goal

The goal was to design a bidding agent that finishes with the highest possible balance over many rounds, competing head to head against bidding algorithms written by others. Because each user's click probability is hidden and never revealed, the agent has to infer a user's value from the outcomes it observes, weighing the cost of exploring unfamiliar users against the payoff of bidding on those it has already found to click.

## 🧭 The Approach

My agent treats each user as a separate learning problem and bids based on what it has seen so far.

- **Exploring with a random bid.** When a user has no positive click rate yet, whether the agent has never won them or has won them but never seen a click, it places a small random bid. This is inexpensive exploration: a way to occasionally win such users and keep gathering evidence about them.
- **Exploiting a known click rate.** Once a user has a click rate above zero, the agent bids that rate, the number of clicks divided by the number of times it has won that user. Because a click is worth exactly one dollar, the observed click rate is a direct estimate of the user's expected value, so the agent bids roughly what the opportunity is worth.
- **Why this suits a second-price auction.** In a second-price auction, bidding close to true value is a sound strategy, since the winner pays the runner-up's bid rather than its own. Bidding the estimated value keeps the agent competitive without systematically overpaying.

The agent tracks per-user clicks, bids, and wins, updating them after every round as results come back (`bidder_Flowers_final.py`). The surrounding simulation (`auction_Flowers_final.py`) is organized into clear, single-responsibility classes: the users, each carrying a hidden click probability, and the auction, which runs each round, determines the winner, and charges the second price.

## 🏆 Results

My bidding strategy outperformed most others in the competition, earning the full performance bonus reserved for the strongest strategies.

## 🧠 Skills Demonstrated

- **Decision-making under uncertainty:** an explore-and-exploit strategy for learning hidden user values, the core of a multi-armed bandit problem
- **Object-oriented design:** User, Bidder, and Auction classes with clear responsibilities and clean interfaces
- **Probabilistic reasoning:** estimating expected value from observed outcomes and bidding accordingly
- **Simulation:** modeling a competitive auction environment round by round

## 🧰 Stack

Python standard library and NumPy.

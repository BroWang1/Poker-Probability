# Poker-Probability-Python
To Clone
Open your terminal and navigate to the directory where you want to store the project.
Run the following command to clone the repository:

     git clone https://github.com/BroWang1/Poker-Probability-Python.git
     cd Poker-Probability-Python
     
Overview
This program is a rudimentary tool that estimates the probability of winning a poker game based on the combinations of cards lower than your hand. While it does not take into account all possible scenarios, it provides a rough estimation to help you gauge the strength of your hand during gameplay. Note these rules are made by my research online and intuition of the game.

Current Functionality
Focus on Lower Cards: The program calculates the chance of winning by only considering combinations that are (lower than your hand and unseen/total unseen cards).
Basic Estimator: This approach allows for a quick estimation of your hand's strength without simulating every possible hand.

Limitations
Partial Coverage: The program does not account for:
Cards held by opponents.
Combinations that could beat your hand (e.g., straights, flushes, full houses).
Rudimentary Design: This is an early-stage prototype aimed at providing a foundational estimator, not a comprehensive analysis.
Simplified Win Types: Currently, the program focuses on basic win types and does not consider the full range of poker hand rankings.

How to Use
1. Put the number of players including yourself
2. Input your hand into the program.
3. Input the Flop
4. Input the Turn
5. Input the River
6. Each turn will give you a probabilty of winning
The program will calculate the probability of winning based on lower card combinations.
Use the results as a rough guide to assess your hand’s potential.


Disclaimer
This tool is a work in progress and should not be relied upon for accurate decision-making in high-stakes poker games. Use it for educational purposes and as a stepping stone for understanding poker probabilities.












Note to self (What I learned)

-list comprehension

-tuple unpacking

-debugging w/ print

-any()

-Initialization (ex. var = None, var1 = 0, var2 = [], etc.)

-importing from different .py files

-branching 

-manipulating index to find order

-combining two dictionaries

-function calling another function

-.upper or .lower w/ .replace() & .split to clean answers

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Connor Mentel 
pig
CS 5001
HW3
"""

import random

player1_points = 0
player2_points = 0
bank_player1 = 0
bank_player2 = 0

print
('''Get ready to play PIG!
If a player rolls '1' they get no new points and it's the next player's turn.
If they roll a '2-6' they can hold or roll again via 'h' for hold or 'r' for roll.
If player holds, the sum of all their rolls is added to their points and turn is over.
The first to 20 points wins
Player one please roll.''')

#giant loop for game
while player1_points <=20 and player2_points <=20:
    #loop for player 1 
    while player1_points <= 20 and player2_points <= 20: #while both are under 20
        #Player 1 turn
        player1_turn = input("Player 1,Enter 'r' to roll or 'h' to hold: ")
        if player1_turn == 'r':
            roll = random.randint(1,6)
            #if roll is any number besides 1
            if roll != 1:
                bank_player1 += roll
                print("Player 1 rolled:", roll ,"\nplayer 1 score:", bank_player1)
                continue
            else:
                #if roll is 1
                print("Player 1 rolled:", roll ,"\n" "0 points earned""\n""Current score:", player1_points)
                break
        elif player1_turn == 'h':
            player1_points += bank_player1
            print("Player 1 holds \nplayer 1 score:", player1_points)
            if player1_points >= 20:
                print("Congrats player 1! You won!!")
            break #stop looping and continue downward
        else:
            print("Please choose either 'h' for Hold or 'r' for Roll.")
        
        
    while player1_points <= 20 and player2_points <= 20: #while both are under 20
    #Player 2 turn
        player2_turn = input("Player 2,Enter 'r' to roll or 'h' to hold: ")
        if player2_turn == 'r':
            roll = random.randint(1,6)
            #if roll is any number besides 1
            if roll != 1:
                bank_player2 += roll
                print("Player 2 rolled:", roll ,"\nplayer 2 score:", bank_player2)
                continue
            else:
                #if roll is 1
                print("Player 2 rolled:", roll ,"\n" "0 points earned""\n""Current score:", player2_points)
                break
        elif player2_turn == 'h':
            player2_points += bank_player2
            print("Player 2 holds \nplayer 2 score:", player2_points)
            if player2_points >= 20:
                print("Congrats player 2! You won!!")
            break #stop looping and continue downward
        else:
            print("Please choose either 'h' for Hold or 'r' for Roll.")

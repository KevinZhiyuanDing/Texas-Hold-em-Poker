# Texas Hold'em Poker Game

A console-based implementation of the popular Texas Hold'em Poker game where players can compete against each other.

## Overview

This project is a simplified version of Texas Hold'em Poker implemented in Python. Players take turns betting, checking, or folding based on their hand and the community cards.

## Features

- Supports up to 10 players
- Full betting rounds (pre-flop, flop, turn, river)
- Card evaluation system for determining the winning hand
- Hand ranking detection (Royal Flush, Straight Flush, Four of a Kind, etc.)
- Interactive console interface

## Game Logic

The game follows standard Texas Hold'em rules:
1. Each player receives 2 private cards
2. 5 community cards are dealt in stages (flop, turn, river)
3. Betting rounds occur after each stage
4. Players create their best 5-card hand using their private cards and community cards
5. The player with the best hand wins the pot

## How to Play

1. Run the program (`python poker.py`)
2. Enter the number of players (1-10)
3. Each player will take turns viewing their cards and deciding to:
   - Check (match the current bet)
   - Bet (raise the bet)
   - Fold (withdraw from the round)
4. After all betting rounds, remaining players select their best hand combination
5. The player with the highest-scoring hand wins the pot

## Technical Implementation

The game is structured with the following classes:
- `Card`: Represents a playing card with rank and suit
- `Hand`: Collection of cards with methods to analyze them
- `Player`: Represents a player with hand and money
- `PokerGame`: Contains game logic and hand evaluation methods

Hand evaluation includes checks for:
- Royal Flush
- Straight Flush
- Four of a Kind
- Full House
- Flush
- Straight
- Three of a Kind
- Two Pairs
- Pair
- High Card

## Requirements

- Python 3.6 or higher
- No external packages required

## Creator

Created by Kevin Ding, March 29, 2021
"""This code reads the full name of a playing card"""
card = input().upper()
ranks = {"A": "Ace", "J": "Jack", "Q": "Queen", "K": "King"}
suits = {
    "D": "Diamonds", "H": "Hearts", "S": "Spades", "C": "Clubs"
}
rank = ranks.get(card[:-1], card[:-1])
print(rank, "of", suits[card[-1]])

# Secret Auction

from art import logo
from os import system

bidders = {}
name = ""
bid = ""
endbid = False
highest_bidder = ""
max_bid = 0

print(logo)
print("Bienvenue dans l'encan silencieux!!!")
while not endbid:
    name = input("Quel est votre nom? ")
    bid = int(input("Quel est votre bid? "))
    bidders[name] = bid
    if input("Un autre participant (o/n)? ") == 'n':
        endbid = True
    system('cls')

for item in bidders:
    if bidders[item] > max_bid:
        max_bid = bidders[item]
        highest_bidder = item

print(f"Le gagnant de l'encan est {highest_bidder} avec {max_bid} $")

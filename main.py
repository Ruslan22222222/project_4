import os

from art import logo
print(logo)

bids = {}

bidding_finish = False

def find_highest_bidder(bidding_record):
    highest_bid = 0
    winner = ""
    for bidder in bidding_record:
        bid_amount = bidding_record[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder

    print(f"The winner is {WInner} with a bit of ${highest_bid}")


while not bidding_finish:
    name = input("What's your name?: ")
    price = int(input("What's your price?: $"))
    bids[name] = price
    should_countinue = input("Are there any bidders? Type 'yes' or 'not'.\n")
    if should_countinue == "no":
        bidding_finish = True
        find_highest_bidder(bids)

    else:
        os.system('clear')

        
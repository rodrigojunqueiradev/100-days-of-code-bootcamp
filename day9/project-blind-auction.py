# TODO-1: Ask the user for input
# TODO-2: Save data into dictionary {name: price}
# TODO-3: Whether if new bids need to be added
# TODO-4: Compare bids in dictionary

from art import logo
print(logo)
print("Welcome to the secret auction program!")

def find_highest_bidder(bidding_record):
    highest_bid = 0
    winner = ""
    for bidder in bidding_record:
        bid_amount = bidding_record[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder
    print(f"The winner is {winner} with a bid of ${highest_bid:.2f}")

bids = {}
keep_bidding = True

while keep_bidding: 
    name = input("What is your name? ")
    price = float(input("What is your bid? $"))
    bids[name] = price
    another_bid = input("Are there any other bidders? Type 'yes' or 'no': ")

    if another_bid == "no":
        print("Bye!")
        keep_bidding = False
        find_highest_bidder(bids)
    
    elif another_bid == "yes":
        print("\n")
    
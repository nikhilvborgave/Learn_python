# TODO-1: Ask the user for input
import art
bidding = {}
print(art.logo)
# TODO-2: Save data into dictionary {name: price}
Name = input("What is your name? \n")
Bid = int(input("What is your bid? \n$"))
bidding[Name] = Bid
print(bidding)

# TODO-3: Whether if new bids need to be added
new_bids = True


while new_bids:
    new_bid = input("Are there any new bidders? Type 'Yes' or 'No' \n").lower()
    print("\n" * 100)
    if new_bid == "no":
        new_bids = False
    else:
        Name = input("What is your name? \n")
        Bid = int(input("What is your bid? \n$"))
        bidding[Name] = Bid
        # print(bidding)


# TODO-4: Compare bids in dictionary

winning_bid = max(bidding.values())
# print(winning_bid)
for Name, Bid in bidding.items():
    if Bid == winning_bid:
        print(f"And the winner is {Name} with bid of ${winning_bid}")
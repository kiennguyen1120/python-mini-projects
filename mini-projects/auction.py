# todo 1: ask user for input
# todo 2: save data into dictionary {name: price}
# todo 3: whether if new bids need to be added


def find_highest_bidder(bidding_dictionary):
    winner = ""
    highest_bid = 0
    winner = max(bidding_dictionary, key = bidding_dictionary.get)
    # for bidder in bidding_dictionary:
    #     bid_amount = bidding_dictionary[bidder]
    #     if bid_amount > highest_bid:
    #         highest_bid = bid_amount
    #         winner = bidder

    print(f"the winner is {winner}")


bids = {}
continue_bidding = True
while continue_bidding:
    name = input("What is your name?: ")
    price = int(input("What is your bid?: $"))
    bids[name] = price 
    should_continue = input("Are there any other bidders? Type'yes' or 'no'. ").lower()
    if should_continue == "no":
        continue_bidding = False
        find_highest_bidder(bids)
    elif should_continue == "yes":
        print("________________________")
        






auction = []

def response_fun():
  response = input('Are there any other bidders? yes or no: ').lower()
  if response == 'yes':
    return True 
  else:
    return False

while response_fun(): 
  name = input('Enter name: ')
  bid = float(input('Enter bid: $'))

  entry = {
    'name': name,
    'bid': bid
  }

  auction.append(entry)

def higest_bid(auction):
    highest = auction[0]["bid"]
    bidder = auction[0]["name"]
    #print(auction)
    for i in range(1, len(auction)):
        if(auction[i]["bid"] > highest):
            highest = auction[i]["bid"]
            bidder = auction[i]["name"]
        else:
            continue

    print(f"The highest bidder is: {bidder} with bid: {highest}.")

higest_bid(auction)
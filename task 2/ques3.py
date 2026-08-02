# Problem 3: Write a program that will take user input of cost price and selling price and determines whether its a loss or a profit.

cost=int(input("Enter the cost price of the product: "))
selling=int(input("Enter the selling price of the product: "))

if selling>cost:
    print("profit!! total profit on the product: ", selling-cost)
elif selling==cost:
    print("NO PROFIT AND NO LOSS!! Product is Sell on Cost Price : ",cost)
else:
    print("Loss!! total Loss on the product: ", cost-selling)
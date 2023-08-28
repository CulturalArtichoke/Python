# Your code below:
print("Len's Slice")
#list with toppings
toppings = ["pepperoni", "pineapple", "cheese", "sausage", "olives", "anchovies", "mushrooms"]

#list of prices
prices = [2, 6, 1, 3, 2, 7, 2]

#count occurences of $2
num_two_dollar_slices = prices.count('2')

#number of pizzas
num_pizzas = len(toppings)

#int to string
print("We sell " + str(num_pizzas) + " different kinds of pizza!")

#two-dimensional list for prices and toppings of pizzas
pizza_and_prices = [[2, "pepperoni"], [6, "pineapple"], [1, "cheese"], [3,"sausage"], [2,"olives"], [7,"anchovies"], [2,"mushrooms"]]

#sort pizzas from cheapest to most expensive
pizza_and_prices.sort()

cheapest_pizza = pizza_and_prices[0]
priciest_pizza = pizza_and_prices[-1]

print(pizza_and_prices)
print(cheapest_pizza)
print(priciest_pizza)

pizza_and_prices.pop()
pizza_and_prices.insert(2, [2.5, 'peppers'])

#sort pizza list with peppers, without anchovies
pizza_and_prices.sort()
print(pizza_and_prices)

three_cheapest = pizza_and_prices[:3]

#print three cheapest pizzas
print(three_cheapest)




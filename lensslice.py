toppings = ['pepperoni', 'pineapple', 'cheese', 'sausage', 'olives', 'anchovies', 'mushrooms']
prices = [2, 6, 1, 3, 2, 7, 2]

num_two_dollar_slices = prices.count(2)
print(num_two_dollar_slices)

num_pizzas = len(toppings)

print('We sell', num_pizzas, 'different kinds of pizza!')

#2D List
pizza_and_prices = [[2, 'pepperoni'], [6, 'pineapple'], [1, 'cheese'], [3, 'sausage'], [2, 'olives'], [7, 'anchovies'], [2, 'mushrooms']]
pizza_and_prices.append([2.5, 'peppers'])
pizza_and_prices.append([3, 'banana peppers'])
pizza_and_prices.append([6, 'meat lovers'])
pizza_and_prices.append([2, 'white'])
pizza_and_prices.sort()
cheapest_pizza = pizza_and_prices[0]
priciest_pizza = pizza_and_prices[-1]
pizza_and_prices.pop(-1)
three_cheapest = slice(0, 3)

print(pizza_and_prices[three_cheapest])

print(pizza_and_prices)
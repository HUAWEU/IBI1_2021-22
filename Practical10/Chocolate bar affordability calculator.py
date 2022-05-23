import math


def chocolate_bar(i, j):
    """
    input: i, total money
           j, price
    return: the number of chocolate bar and the change left
    """
    money = i
    price = j
    number = math.floor(money/price)
    change = money - price*number
    print("The number of bars:" + str(number))
    print("The change left:" + str(change))


total_money = input('Please type the total money:')
the_bar_price = input('Please type the bar price:')
print(chocolate_bar(int(total_money), int(the_bar_price)))

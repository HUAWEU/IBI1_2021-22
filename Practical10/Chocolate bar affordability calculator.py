<<<<<<< HEAD
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


total_money = 100
the_bar_price = 7
print(chocolate_bar(total_money, the_bar_price))

=======
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


total_money = 100
the_bar_price = 7
print(chocolate_bar(total_money, the_bar_price))

>>>>>>> e22e09b592cc8a054107ad38ad83d7f407d9cd31

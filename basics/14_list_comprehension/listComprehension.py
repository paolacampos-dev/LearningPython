# 1.for:
squares = []

for i in range(10):
    squares.append(i * i)
print(squares)  # [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]


# 2. map():
txns = [1.09, 23.56, 57.84, 4.56, 6.78]
TAX_RATE = 0.08

def get_price_with_tax(txn):
    return txn * (1 + TAX_RATE)

final_prices = map(get_price_with_tax, txns)
print(list(final_prices))   # [1.1772000000000002, 25.4448, 62.467200000000005, 4.9248, 7.322400000000001]


#3. List Expressions:
squares = [i * i for i in range(10)]
print(squares)

txns = [1.09, 23.56, 57.84, 4.56, 6.78]
TAX_RATE = .08

def get_price_with_tax(txn):
    return txn * (1 + TAX_RATE)

final_prices = [get_price_with_tax(i) for i in txns]
print(final_prices)    # [1.1772000000000002, 25.4448, 62.467200000000005, 4.9248, 7.322400000000001]

#===================
sentence = 'the rocket came back from mars'
vowels = [i for i in sentence if i in 'aeiou']


sentence = 'The rocket, who was named Ted, came back \
from Mars because he missed his friends.'
def is_consonant(letter):
    vowels = 'aeiou'
    return letter.isalpha() and letter.lower() not in vowels
consonants = [i for i in sentence if is_consonant(i)]


original_prices = [1.25, -9.45, 10.22, 3.78, -5.92, 1.16]
prices = [i if i > 0 else 0 for i in original_prices]
# def get_price(price):
    # return price if price >0 else 0
# prices = [get_price(i) for i in  original_prices]
print(prices)


# walrus operator:
import random

def get_weather_data():
    return random.randrange(90, 110)

hot_temps = [temp for _ in range(20) if (temp := get_weather_data()) >= 100]


# Nested comprehensions:
cities = ['Austin', 'Tacoma', 'Topeka', 'Sacramento', 'Charlotte']
temps = {city: [0 for _ in range(7)] for city in cities}
print(temps)


matrix = [[i for i in range(5)] for _ in range(6)]
print(matrix)

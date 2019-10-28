# EX 1

shopping_cart = ['water', 'carrots', 'milk', 'honey', 'detergent']
# a
print('The 4th item of the list is ' + shopping_cart[3] + '.')
# b
detergent_index = str(shopping_cart.index('detergent'))
print('Detergent is the ' + detergent_index + 'th item in the list.')
# c
number_of_items = str(len(shopping_cart))
print ('There are ' + number_of_items + ' items in the shopping list.')
# d
shopping_cart.append('banana')
print (shopping_cart)

# EX 2

number_test = input('Enter a number to compare :')
if float(number_test) < 500:
    print('This number is smaller to 500.')
elif float(number_test) > 500:
    print('This number is greater than 500.')
elif float(number_test) == 500:
    print('This number is equal to 500.')

# EX 3

n = 4
for i in range(n):
    print((n * ' ') + (n - i) * '*')

# EX 4

n = 4
for i in range(n):
    print(((n - i) * ' ') + (((2 * i) + 1) * '*') )

# EX 5

n1 = float(input('Enter a 1st number : '))
n2 = float(input('Enter a 2nd number : '))

operator = input("Choose the operation you\'d like to perform (+, -, *, /) : ")

if operator == '+':
    result1 = n1 + n2
    print(str(result1))
elif operator == '-':
    result1 = n1 - n2
    print(str(result1))
elif operator == '*':
    result3 = n1 * n2
    print(str(result3))
elif operator == '/':
    result4 = n1 / n2
    print(str(result4))
else:
    print('Use an operator from the list.')

# EX 6

names = ['Calvin', 'Theodore', 'Maelis', 'Martin', 'Gabrielle']
# a
# if names.index(str(name_test)) =
n = 3
i = 0
while i < n :
    name_test = input('Enter a name to test if it is on the list: ')
    i = i + 1
    try:
        test = names.index(name_test)
    except ValueError:
        print('Sorry, we cannot find that user name.')
        print(str(n-i) + ' tries left')
    else:
        i = 5
        print('Welcome, ' + str(name_test) + ' ! ')
else:
    if i == 3:
        print('Login is locked')
    else:
        print(' ')

# EX 7

shopping_cart = []
t = 'Y'
while t == 'Y':
    a = input('Add an item to buy :')
    n = input('Quantity ?')
    for i in range(int(n)):
        shopping_cart.append(a)
    
    # print(shopping_cart)

    t = input('Continue ? (Y / N)')
else:
    print('Cart :  ' + str(shopping_cart))
    print('There are ' + str(len(shopping_cart)) + ' items in the cart.')

# EX 8

text_file = open('addressbook.txt', 'a')
t = 'Y'
while t == 'Y':
    address = input('Enter an address to add to the address book : ')
    text_file.write('\n' + address)
    t = input('Continue ? (Y / N)')
else: 
    show = text_file.read
    print(show)
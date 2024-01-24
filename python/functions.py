# function :
# also, it can have globals varibles

def hello():
    print('hello tefo')
hello()

def print_my_name(name):
    print(f"hello {name}")
print_my_name("vale")


def color():
    color = "blue"
    print(color)
color()


def numbers(highest_number, lowest_number):
    print(highest_number)
    print(lowest_number)
# numbers(15,2)
numbers(lowest_number=3, highest_number=10)


def multiply(a,b):
    return a * b

solution = multiply(2,2)
print(solution)


def list_with_for(numbers):
    for x in numbers:
        print(x)
list_number = [1,2,3]
print(list_number)



def buy_item(cost_of_item):
    return cost_of_item + add_tax_to_item(cost_of_item)

def add_tax_to_item(cost_of_item):
    current_tax_rate = .03
    return cost_of_item * current_tax_rate

final_cost = buy_item(50)
print(final_cost)




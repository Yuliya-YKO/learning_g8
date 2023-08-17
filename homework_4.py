# task_1
def conv_str_to_num():
    return int(input("enter your number for task_1: "))

try:
    print(f'you entered number: {conv_str_to_num()}')

except ValueError:
    print("Entered not valid data")
finally:
    print('The End of task_1')

# task_2

def operations_with_strings(a, b):
    try:
        num1 = int(a)
        num2 = int(b)
        result = num1 + num2
    except ValueError:
        result = a + b

    print("Result:", result)


str1 = input("Enter the first string or number for task_2: ")
str2 = input("Enter the second string or number for task_2: ")

operations_with_strings(str1, str2)

# task_3

def getting_a_number():
    while True:
        try:
            inp_val = int(input("Enter a number for task_3: "))
            print("THX!")
            return inp_val
        except ValueError:
            print("It isn't a number. Try again.")
N = getting_a_number()
print("You've entered number:", N)

#task_4

class OnlyEvenError(Exception):
    def __init__(self, value):
        self.value = value
        self.message = f"OnlyEvenError: {value} isn't an even number"

def check_digit(number):
    if number % 2 != 0:
        raise OnlyEvenError(number)
    else:
        return number

try:
    user_input = int(input("Enter same even number for task_4: "))
    result = check_digit(user_input)
    print("Your even number:", result)
except OnlyEvenError as e:
    print(e.message)
except ValueError:
    print("Entered value in task_4 isn't a number")

#task_5
def func_numb(number):
    try:
        result = check_digit(number)
    except OnlyEvenError:
        number += 1
        print(f"You've entered odd number {user_input}, so now you get {user_input}+1: ", number)
    else:
        result *= 2
        print(f"You've entered even number {user_input}, so now you get {user_input}*2: ", result)

try:
    user_input = int(input("Enter same number for task_5: "))
    func_numb(user_input)
except ValueError:
    print("Entered value in task_5 isn't a number")
finally:
    print("I'm always typing something in task_5")
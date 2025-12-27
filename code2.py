# Conditional statements

salary = float(input("Enter your salary: "))

if salary < 30000:
    tax_rate = 5
elif 30000 <= salary <= 70000:
    tax_rate = 15
else:
    tax_rate = 25

print(f"The final tax rate is {tax_rate}%.")

#functions

def print_even_numbers(a, b):
    start = min(a, b)
    end = max(a, b)
    print(f"Even numbers between {start} and {end}:")
    for num in range(start, end + 1):
        if num % 2 == 0:
            print(num)

print_even_numbers(10, 20)

# Print Digits
def print_digits(n):
    n = abs(n) # Handle negative numbers
    if n == 0: print(0)
    while n > 0:
        print(n % 10)
        n //= 10

#Count Digits
def count_digits(n):
    n = abs(n)
    if n == 0: return 1
    count = 0
    while n > 0:
        count += 1
        n //= 10
    return count

print(count_digits(798098))

#Sum of Digits
def sum_of_digits(n):
    n = abs(n)
    total = 0
    while n > 0:
        total += n % 10
        n //= 10
    return total

print(sum_of_digits(687))

#Divisible by both 3 and 5 (1 to 100)
def div_by_3_and_5():
    for i in range(1, 101):
        if i % 3 == 0 and i % 5 == 0:
            print(i)
div_by_3_and_5()

#Simple Calculator using match case
def calculator(a, b, operation):
    match operation:
        case '+':
            return a + b
        case '-':
            return a - b
        case '*':
            return a * b
        case '/':
            return a / b if b != 0 else "Error: Division by zero"
        case _: #default case
            return "Invalid Operation"
    
print(calculator(2,3,'/'))

#is prime
def is_prime(n):
    for i in range(2,n-1):
        if(n%i==0):
            return False
    return True

print(is_prime(7))

#guess the number (87)
secret_number=87 
while True:
    guess = int(input("Enter your guess: "))
    if guess > secret_number:
        print("Too high")
    elif guess < secret_number:
        print("Too low")
    else:
        print("Correct!")
        break # Exit the loop once correct






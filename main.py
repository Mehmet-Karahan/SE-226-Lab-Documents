n = int(input("Enter a number greater than 9: "))
current_value = n
steps = 0
print(n, end="-> ")

while current_value > 9:
    sum_of_digits = 0
    temp = current_value
    while temp > 0:
        sum_of_digits += temp % 10
        temp //= 10
        current_value = sum_of_digits
        steps +=1
print(current_value, end="-> ")

print(f"\nFinal Value: {current_value}")
print(f"\nTotal steps: {steps}")


while True:
    n = int(input("Enter a number between 10 and 100: "))
    if 10 <= n <= 100:
        break
    print("Invalid input.")

fizz_c, buzz_c, fb_c = 0, 0, 0

for i in range(1, n + 1):
    if i % 7 == 0:
        print(i, "is skipped")
        continue
    elif i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")
        fb_c += 1
    elif i % 3 == 0:
        print("Fizz")
        fizz_c += 1
    elif i % 5 == 0:
        print("Buzz")
        buzz_c += 1
    else:
        print(i)

print(f"Summary\nFizz count: {fizz_c}\nBuzz count: {buzz_c}\nFizzBuzz count: {fb_c}")

n = int(input("Enter a number between 3 and 9: "))
for i in range(1, 2 * n):
    k = n - abs(n - i)


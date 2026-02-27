user = int(input("Enter your number:- "))

fact = 1

for i in range(1, user + 1):
    fact = fact * i

find_zero = str(fact)

print("Total zeros:", find_zero.count("0"))
print("Factorial:", fact)
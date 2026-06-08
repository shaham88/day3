# Star Pattern
for i in range(1, 5):
    print("*" * i)

print()

# Number Pattern
for i in range(1, 6):
    for j in range(1, i + 1):
        print(j, end="")
    print()

print()

# Alphabet Pattern
for i in range(1, 6):
    for j in range(i):
        print(chr(65 + j), end="")
    print()

print()

# 5 Pattern
for i in range(1, 6):
    print("5" * i)

print()

# Reverse Star Pattern
for i in range(5, 0, -1):
    print("*" * i)

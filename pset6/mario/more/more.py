from cs50 import get_int
# Loop for taking input from user
while True:
    h = get_int("Height: ")
    if h < 9 and h > 0:
        break

# for loop of printing pattern 
for i in range(1, h + 1):
    print(" " * (h - i) + "#" * i + "  " + ("#" * i))
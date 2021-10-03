from cs50 import get_float

# Take input from user
while True:
    change = get_float("Change owed: ")*100
    if change > 0:
        break

coin = 0
# Calculate the change 
# Calculate the change 
# Calculate the change 
# Calculate the change 
while(change >= 25):
    change = change-25
    coin += 1

while(change >= 10):
    change = change-10
    coin += 1

while(change >= 5):
    change = change-5
    coin += 1

while(change >= 1):
    change = change-1
    coin += 1

print(coin)
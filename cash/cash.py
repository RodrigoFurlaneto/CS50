change_owed = float(input("Change owed: "))

coins = 0

while change_owed > 0:
    if change_owed > 0.25:
        change_owed -= 0.25
        coins += 1
    elif change_owed > 0.1:
        change_owed = change_owed - 0.1
        coins += 1
    elif change_owed > 0.05:
        change_owed -= 0.05
        coins += 1
    else:
        change_owed -= 0.01
        coins += 1

print(coins)
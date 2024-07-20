def calc_min_coins(total):
    total_coins = 0   
    for coin_value in [5,3,1]:
        no_of_coins = int(total / coin_value)
        total= total - no_of_coins * coin_value
        total_coins += no_of_coins
    print(total_coins)

while True:
    line = int(input("Enter input:\n"))
    if line:
        calc_min_coins(line)
    else:
        break
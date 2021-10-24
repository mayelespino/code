#
#
#

def coins_amount(coin_list, amount):
    combinations_list = [0] * (amount + 1)
    combinations_list[0] = 1

    for coin in coin_list:
        for combination in range(1,len(combinations_list)):
            if combination >= coin:
                combinations_list[combination] += combinations_list[combination - coin]
    return(combinations_list[amount])

def main():
    print(coins_amount([1,2,5], 5))

if __name__ == "__main__": main()

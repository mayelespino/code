#
# This is my solution to the coin change problem. I liked this apprach because:
# - it provides the list of coins used
# - I can modify the code easily to give me the number of coins of just True or False.
# - I started with a greedy approach and then combined it with a bit of Dynamic programming.
#

def makeChangeFor(target, coins, memo):

    minRemainder = target
    maxCoin = 0
    for coin in coins:
        remainder = target - coin
        if remainder < 0: continue
        if remainder < minRemainder:
            minRemainder = remainder
            maxCoin = coin

    if minRemainder == target:
        return
    elif minRemainder == 0:
        memo.append(maxCoin)
        return
    else:
        memo.append(maxCoin)
        prevResult = makeChangeFor(minRemainder, coins, memo)
        if prevResult is not None:
            memo.append(prevResult)
    return

def bestMakeChange(target, coins):
    memos = [0] * len(coins)
    for index, coin in enumerate(coins):
        memos[index] = []
        memos[index].append(coin)
        remainder = target - coin
        makeChangeFor(remainder, coins, memos[index])
    minNumberOfCoins = memos[0]
    for memo in memos:
        #print(memo)
        if len(memo) < len(minNumberOfCoins): minNumberOfCoins = memo
    return(minNumberOfCoins)

memo = []
makeChangeFor(32,[1,10,25],memo)
print(memo)

memo = []
makeChangeFor(7,[1,2,3,4],memo)
print(memo)

print(bestMakeChange(32,[1,10,25]))
print(bestMakeChange(7,[1,2,3,4]))
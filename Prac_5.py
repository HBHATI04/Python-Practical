from flask import Flask, render_template, request
import time
from collections import Counter

app = Flask(__name__)

def min_coins(coins, amount):
    dp = [float('inf')] * (amount + 1)
    coin_used = [-1] * (amount + 1)
    dp[0] = 0 
    
    for i in range(1, amount + 1):
        for coin in coins:
            if coin <= i:
                if dp[i - coin] + 1 < dp[i]:
                    dp[i] = dp[i - coin] + 1
                    coin_used[i] = coin

    if dp[amount] == float('inf'):
        return -1, {}
    
    result_coins = []
    while amount > 0:
        result_coins.append(coin_used[amount])
        amount -= coin_used[amount]
    
    coin_count = dict(Counter(result_coins))
    
    return dp[amount + sum(result_coins)], coin_count

@app.route('/', methods=['GET', 'POST'])
def coin_change():
    result = None
    coins_used = {}
    execution_time = None
    
    if request.method == 'POST':
        coins = [int(x) for x in request.form.get('coins').split(',')]
        amount = int(request.form.get('amount'))
        
        start_time = time.time()
        result, coins_used = min_coins(coins, amount)
        execution_time = time.time() - start_time
    
    return render_template('Prac_5.html', result=result, coins_used=coins_used, execution_time=execution_time)

app.run(debug=True)

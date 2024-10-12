from flask import Flask, render_template

app = Flask(__name__)

def knapsack(W, wt, val, n):
    K = [[0 for x in range(W + 1)] for x in range(n + 1)]
     
    for i in range(n + 1):
        for w in range(W + 1):
            if i == 0 or w == 0:
                K[i][w] = 0
            elif wt[i-1] <= w:
                K[i][w] = max(val[i-1] + K[i-1][w-wt[i-1]], K[i-1][w])
            else:
                K[i][w] = K[i-1][w]

    res = K[n][W] 
    w = W
    selected_items = []

    for i in range(n, 0, -1):
        if res <= 0:
            break
        if res == K[i-1][w]:
            continue
        else:
            selected_items.append(i)
            res -= val[i-1]
            w -= wt[i-1]

    return K, K[n][W], selected_items

@app.route('/')
def knapsack_solution():
    val = [3, 4, 5, 6]
    wt = [2, 3, 4, 5]
    W = 5
    n = len(val)
    
    K, max_value, selected_items = knapsack(W, wt, val, n)
    
    return render_template('Prac_7.html', K=K, W=W, n=n, max_value=max_value, selected_items=selected_items)

if __name__ == '__main__':
    app.run(debug=True)

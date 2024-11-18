from flask import Flask, render_template, request

app = Flask(__name__)

# Function to perform fractional knapsack with sorted profits
def fractional_knapsack(p, w, W):
    n = len(p)
    # List to store (profit per weight, profit, weight)
    items = [(p[i] / w[i], p[i], w[i]) for i in range(n)]
   
    # Sort based on profit per weight in descending order
    items.sort(reverse=True, key=lambda x: x[0])
   
    total_profit = 0
    selected_items = [0] * n  # Array to store the fraction of each item taken

    for i in range(n):
        profit_per_weight, profit, weight = items[i]
        if weight <= W:
            W -= weight
            total_profit += profit
            selected_items[i] = 1  # Take the entire item
        else:
            selected_items[i] = W / weight  # Take a fraction of the item
            total_profit += profit * (W / weight)
            break

    return selected_items, total_profit, items

@app.route('/', methods=['POST', 'GET'])
def index():
    if request.method == 'POST':
        if 'profits' in request.form and 'weights' in request.form and 'capacity' in request.form:
            # Retrieve input values from the form
            profits = request.form['profits']  # Example input: "280,100,120,120"
            weights = request.form['weights']  # Example input: "40,10,20,24"
            W = int(request.form['capacity'])  # Max capacity as an integer

            # Split the input strings by commas and convert each value to int
            p = [int(x) for x in profits.split(',')]
            w = [int(x) for x in weights.split(',')]

            # Call the knapsack function
            selected_items, total_profit, items = fractional_knapsack(p, w, W)

            # Return the result to the front end
            return render_template('Prac_9.html', selected_items=selected_items, total_profit=total_profit, items=items)
        else:
            return "Please provide all the required inputs."

    return render_template('Prac_9.html')

if __name__ == '__main__':
    app.run(debug=True)

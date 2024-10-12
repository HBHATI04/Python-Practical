from flask import Flask, render_template
import matplotlib.pyplot as plt
import io
import base64
import sys

app = Flask(__name__)

sys.setrecursionlimit(5000)

# Iterative Fibonacci
def fib_iterative(n):
    a, b = 0, 1
    steps = 0
    for _ in range(n):
        a, b = b, a + b
        steps += 1
    return a, steps

# Recursive Fibonacci
def fib_recursive(n, steps=0):
    steps += 1
    if n <= 1:
        return n, steps
    else:
        a, steps = fib_recursive(n - 1, steps)
        b, steps = fib_recursive(n - 2, steps)
        return a + b, steps

@app.route('/')
def index():
    months = range(1, 18)
    iterative_counts = []
    recursive_counts = []
    rabbit_pairs = []

    for month in months:
        rabbits_iter, steps_iter = fib_iterative(month)
        rabbits_rec, steps_rec = fib_recursive(month)
        
        rabbit_pairs.append(rabbits_iter)
        iterative_counts.append(steps_iter)
        recursive_counts.append(steps_rec)

    # Plotting the comparison
    plt.figure()
    plt.plot(months, iterative_counts, color='r', linestyle='-', label='Iteration')
    plt.plot(months, recursive_counts, color='g', linestyle='-', label='Recursion')
    plt.xlabel('Month')
    plt.ylabel('Steps Count')
    plt.legend()
    
    img = io.BytesIO()
    plt.savefig(img, format='png')
    img.seek(0)
    plot_url = base64.b64encode(img.getvalue()).decode()

    return render_template('Prac_2_2.html', plot_url=plot_url,
                           months=list(months),
                           rabbit_pairs=rabbit_pairs,
                           iterative_steps=iterative_counts,
                           recursive_steps=recursive_counts)

if __name__ == '__main__':
    app.run(debug=True)

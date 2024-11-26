from flask import Flask, render_template
import matplotlib.pyplot as plt
import io
import base64
import sys

app = Flask(__name__)

sys.setrecursionlimit(1000)

@app.route('/')
def index():
    lst = [10, 50, 100, 250, 400, 450]
    sum1 = 0
    sum2 = 0
    sum3 = 0
    count_for_loop = []
    count_for_equation = []
    count_for_recursion = []

    for i in lst:
        loop = 0
        for j in range(1, i + 1):
            sum1 += 1
            loop += 1
        count_for_loop.append(loop)
        
        equation = 1  
        sum2 = (i * (i + 1)) / 2
        count_for_equation.append(equation)
        
        recursion = [0] 
        sum3 = sumUsingRecursion(i, recursion)
        count_for_recursion.append(recursion[0])

    # Plotting
    plt.figure()
    plt.plot(lst, count_for_loop, color='r', linestyle='-', label='Iteration')
    plt.plot(lst, count_for_equation, color='b', linestyle='-', label='Equation')
    plt.plot(lst, count_for_recursion, color='g', linestyle='-', label='Recursion')
    plt.xlabel('Number')
    plt.ylabel('Count')
    plt.legend()

    img = io.BytesIO()
    plt.savefig(img, format='png')
    img.seek(0)
    plot_url = base64.b64encode(img.getvalue()).decode()

    return render_template('Prac_2_1.html', plot_url=plot_url,
                           numbers=lst,
                           count_loops=count_for_loop,
                           count_equations=count_for_equation,
                           count_recursions=count_for_recursion)

def sumUsingRecursion(n, counter):
    counter[0] += 1
    if n == 0:
        counter[0] += 1
        return 0
    else:
        counter[0] += 1
        return n + sumUsingRecursion(n - 1, counter)

if __name__ == '__main__':
    app.run(debug=True, port=5001)

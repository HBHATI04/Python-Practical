from flask import Flask, request, render_template
import numpy as np

app = Flask(__name__)

# Matrix chain multiplication algorithm to calculate minimum multiplications
def practical_6(p):
    n = len(p) - 1
    m = [[0] * n for _ in range(n)]
    s = [[0] * n for _ in range(n)]
    
    # L is the chain length
    for L in range(2, n + 1):
        for i in range(n - L + 1):
            j = i + L - 1
            m[i][j] = float('inf')
            for k in range(i, j):
                q = m[i][k] + m[k + 1][j] + p[i] * p[k + 1] * p[j + 1]
                if q < m[i][j]:
                    m[i][j] = q
                    s[i][j] = k
    return m, s

# Function to generate the optimal parenthesization
def optimal(s, i, j):
    if i == j:
        return f"A{i + 1}"
    return f"({optimal(s, i, s[i][j])}{optimal(s, s[i][j] + 1, j)})"

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        dimensions = list(map(int, request.form['dimensions'].split(',')))
        m, s = practical_6(dimensions)
        op = optimal(s, 0, len(dimensions) - 2)
        
        # Prepare the matrix for display
        matrix = []
        n = len(m)
        for i in range(n):
            row = ["0" if j < i else str(m[i][j]) if m[i][j] != float('inf') else '∞' for j in range(n)]
            matrix.append(row)

        return render_template('Prac_6.html', op=op, matrix=matrix)

    return render_template('Prac_6.html')

if __name__ == '__main__':
    app.run(debug=True, port=8000)

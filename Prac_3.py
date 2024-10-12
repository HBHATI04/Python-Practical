import random
import time
import matplotlib.pyplot as plt
from flask import Flask, render_template, Response
import io
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas

app = Flask(__name__)

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

def insertion_sort(arr):
    n = len(arr)
    for i in range(1, n):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        left_half = arr[:mid]
        right_half = arr[mid:]

        merge_sort(left_half)
        merge_sort(right_half)

        i = j = k = 0
        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k += 1

        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1

        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1

def measure_sorting_time(sort_function, data):
    start_time = time.time()
    sort_function(data)
    end_time = time.time()
    return end_time - start_time

def generate_food_quantities(n):
    return [random.randint(1, 1000) for _ in range(n)]

@app.route('/')
def index():
    input_sizes = [10, 50, 100, 500, 1000]
    bubble_sort_times = []
    insertion_sort_times = []
    merge_sort_times = []

    for n in input_sizes:
        data = generate_food_quantities(n)
        bubble_sort_time = measure_sorting_time(bubble_sort, data.copy())
        bubble_sort_times.append(bubble_sort_time)
        insertion_sort_time = measure_sorting_time(insertion_sort, data.copy())
        insertion_sort_times.append(insertion_sort_time)
        merge_sort_time = measure_sorting_time(merge_sort, data.copy())
        merge_sort_times.append(merge_sort_time)

    plt.figure()
    plt.plot(input_sizes, bubble_sort_times, label='Bubble Sort')
    plt.plot(input_sizes, insertion_sort_times, label='Insertion Sort')
    plt.plot(input_sizes, merge_sort_times, label='Merge Sort')
    plt.xlabel('Input Size (n)')
    plt.ylabel('Time (seconds)')
    plt.legend()
    plt.title('Comparison of Sorting Methods')
    plt.grid(True)

    # Render the plot to a PNG image and send it as a response
    canvas = FigureCanvas(plt.gcf())
    output = io.BytesIO()
    canvas.print_png(output)
    plt.close()  # Close the figure after rendering

    return Response(output.getvalue(), mimetype='image/png')

if __name__ == '__main__':
    app.run(debug=True)

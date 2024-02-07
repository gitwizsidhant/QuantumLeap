import tkinter as tk
from tkinter import ttk
import time
import random

root = tk.Tk()
root.title("Sorting Algorithms Visualizer")
root.maxsize(1400, 900)
root.config(bg="white")

algo_name = tk.StringVar()
algo_list = ['Merge Sort', 'Selection Sort', 'Bubble Sort', 'Insertion Sort', 'Quick Sort']

speed_name = tk.StringVar()
speed_list = ['Fast', 'Medium', 'Slow']

arr = []


def displayArr(arr, colorArray):
    canvas.delete("all")
    canvas_width = 800
    canvas_height = 400
    width_x = canvas_width / (len(arr) + 1)
    ini = 4
    space = 2
    tempArr = [i / max(arr) for i in arr]

    for i in range(len(tempArr)):
        x1 = i * width_x + ini + space
        y1 = canvas_height - tempArr[i] * 390
        x2 = (i + 1) * width_x + ini
        y2 = canvas_height
        canvas.create_rectangle(x1, y1, x2, y2, fill=colorArray[i])

    root.update_idletasks()


def createArr():
    global arr

    array_size = 20
    range_begin = 20
    range_end = 150

    arr = [122, 41, 134, 112, 41, 233, 32, 52, 123, 86, 212, 261]
    for i in range(0, array_size):
        random_integer = random.randint(range_begin, range_end)
        arr.append(random_integer)

    displayArr(arr, ["blue" for _ in range(len(arr))])


def set_speed():
    slow = 0.5
    medium = 0.05
    fast = 0.0000001

    if speed_comboBox.get() == 'Slow':
        return slow
    elif speed_comboBox.get() == 'Medium':
        return medium
    elif speed_comboBox.get() == "Fast":
        return fast


def merge(arr, begin, mid, end, displayArr):
    p = begin
    q = mid + 1
    tempArray = []

    for _ in range(begin, end + 1):
        if p > mid:
            tempArray.append(arr[q])
            q += 1
        elif q > end:
            tempArray.append(arr[p])
            p += 1
        elif arr[p] < arr[q]:
            tempArray.append(arr[p])
            p += 1
        else:
            tempArray.append(arr[q])
            q += 1

    for p in range(len(tempArray)):
        arr[begin] = tempArray[p]
        begin += 1


def merge_sort(arr, begin, end, displayArr, tym):
    if begin < end:
        mid = int((begin + end) / 2)
        merge_sort(arr, begin, mid, displayArr, tym)
        merge_sort(arr, mid + 1, end, displayArr, tym)

        merge(arr, begin, mid, end, displayArr)

        displayArr(arr, ["#71189E" if begin <= x < mid else "#A225AD" if x == mid
                          else "#F381FC" if mid < x <= end else "blue" for x in range(len(arr))])
        time.sleep(tym)

    displayArr(arr, ["blue" for _ in range(len(arr))])


def selection_sort():
    global arr
    n = len(arr)

    for i in range(0, n - 1):
        for j in range(i + 1, n):
            if arr[i] > arr[j]:
                arr[i], arr[j] = arr[j], arr[i]
                displayArr(arr, ["yellow" if x == i else "red" if x == j + 1 else "blue" for x in range(len(arr))])
                time.sleep(tym)

    displayArr(arr, ["blue" for _ in range(len(arr))])


def bubble_sort():
    global arr
    n = len(arr)

    for i in range(n - 1):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                displayArr(arr, ["yellow" if x == j else "red" if x == j + 1 else "blue" for x in range(len(arr))])
                time.sleep(tym)

    displayArr(arr, ["blue" for _ in range(len(arr))])


def insertion_sort():
    global arr

    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1

            displayArr(arr, ["yellow" if x == j else "red" if x == j + 1 else "blue" for x in range(len(arr))])
            time.sleep(tym)
        arr[j + 1] = key

    displayArr(arr, ["blue" for _ in range(len(arr))])


def partition(arr, low, high, displayArr):
    i = low - 1
    pivot = arr[high]

    for j in range(low, high):
        if arr[j] <= pivot:
            i = i + 1
            arr[i], arr[j] = arr[j], arr[i]
            displayArr(arr, ["yellow" if x == i else "red" if x == j + 1 else "blue" for x in range(len(arr))])
            time.sleep(tym)

    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    displayArr(arr, ["yellow" if x == i + 1 else "blue" for x in range(len(arr))])
    time.sleep(tym)
    return i + 1


def quick_sort(arr, low, high, displayArr, tym):
    if low < high:
        pi = partition(arr, low, high, displayArr)

        quick_sort(arr, low, pi - 1, displayArr, tym)
        quick_sort(arr, pi + 1, high, displayArr, tym)


def sort():
    global tym
    tym = set_speed()

    if algo_comboBox.get() == 'Merge Sort':
        merge_sort(arr, 0, len(arr) - 1, displayArr, tym)

    elif algo_comboBox.get() == 'Selection Sort':
        selection_sort()

    elif algo_comboBox.get() == 'Bubble Sort':
        bubble_sort()

    elif algo_comboBox.get() == 'Insertion Sort':
        insertion_sort()

    elif algo_comboBox.get() == 'Quick Sort':
        quick_sort(arr, 0, len(arr) - 1, displayArr, tym)


display_window = tk.Frame(root, width=900, height=300, bg="white")
display_window.grid(row=0, column=0, padx=10, pady=5)

lbl1 = tk.Label(display_window, text="Algorithm: ", bg="white")
lbl1.grid(row=0, column=0, padx=10, pady=5, sticky=tk.W)
algo_comboBox = ttk.Combobox(display_window, textvariable=algo_name, values=algo_list)
algo_comboBox.grid(row=0, column=1, padx=5, pady=5)
algo_comboBox.current(0)

lbl2 = tk.Label(display_window, text="Sorting Speed: ", bg="white")
lbl2.grid(row=1, column=0, padx=10, pady=5, sticky=tk.W)
speed_comboBox = ttk.Combobox(display_window, textvariable=speed_name, values=speed_list)
speed_comboBox.grid(row=1, column=1, padx=5, pady=5)
speed_comboBox.current(0)

btn1 = tk.Button(display_window, text="Sort", command=sort, bg="#C4C5BF")
btn1.grid(row=4, column=1, padx=5, pady=5)

btn2 = tk.Button(display_window, text="Create Array", command=createArr, bg="#C4C5BF")
btn2.grid(row=4, column=0, padx=5, pady=5)

canvas = tk.Canvas(root, width=800, height=400, bg="white")
canvas.grid(row=1, column=0, padx=10, pady=5)

root.mainloop()

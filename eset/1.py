from random import randrange as rr
from typing import List

def find_most_profitable_trade(arr: List[int | float]) -> Tuple[int | float, Tuple[int]]:
    curr_most_profit = (arr[-1] - arr[0], (0,len(arr)-1))
    for j in range(len(arr)-1, -1, -1):
        if curr_most_profit[0] < arr[j] - arr[0]:
            curr_most_profit = (arr[j] - arr[0], (0,j))
            print("init, ", curr_most_profit)
    for i in range(1,len(arr)):
        if arr[curr_most_profit[1][0]] > arr[i]:
            new_most_profit = (arr[-1] - arr[i], (i,len(arr)-1))
            for j in range(len(arr)-1, i-2, -1):
                if new_most_profit[0] < arr[j] - arr[i]:
                    new_most_profit = (arr[j] - arr[i], (i,j))
                    print("new, ", new_most_profit)
            if new_most_profit[0] > curr_most_profit[0]:
                curr_most_profit = new_most_profit
                print("new replaces current: ", curr_most_profit)
    return curr_most_profit


#arr = [35, 34, 1, 38, 25, 29, 36, 38, 6, 36, 18, 39, 32, 40, 47, 18, 21, 36, 30, 24, 43, 36, 32, 44, 10, 44, 17, 46, 30, 17]
arr = [rr(1,50) for i in range(30)]
print("Array we are finding most profitable trade in:\n", arr)
print("Result: ", find_most_profitable_trade(arr))

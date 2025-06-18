def play_with_arrays(arr):
    result = [x + 2 for x in arr if x > 5]
    print(result)
    original_array = [2, 8, 9, 48, 8, 22, -12, 2]
    play_with_arrays(original_array)
# Implement a function to make pairs of even-odd numbers


def get_pairs(array):
    odd_queue = []
    even_queue = []
    result = []
    for num in array:
        if num % 2 == 0:
            even_queue.append(num)
        else:
            odd_queue.append(num)

    for i in range(min(len(odd_queue), len(even_queue))):
        pair = (even_queue[i], odd_queue[i])
        result.append(pair)

    return result


print(
    get_pairs(
        [74, 21, 18, 22, 71, 77, 82, 16, 77, 32, 90, 37, 98, 31, 59, 37, 99, 46, 28, 65]
    )
)

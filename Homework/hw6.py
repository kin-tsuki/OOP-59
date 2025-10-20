
def two_sum(array: list, target: int):
    for ind1 in range(0, len(array)):
        for ind2 in range(ind1 + 1, len(array)):
            if array[ind1] + array[ind2] == target:
                return [ind1, ind2]
    return []

print(two_sum([1, 3, 5, 8, 9], 13))


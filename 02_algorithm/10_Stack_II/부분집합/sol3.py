from itertools import permutations

a = range(1, 11)
b = list(permutations(a, 3))
c = [subset for subset in permutations(a, 3) if sum(subset) == 10]
print(c)
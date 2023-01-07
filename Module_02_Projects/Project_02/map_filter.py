numbers = [15, 30, 47, 82, 95]
def lesser(numbers):
   return numbers < 50

small = list(filter(lesser, numbers))
print(small)

small_2 = list(map(lesser, numbers))
print(small_2)
import numpy

# 1. N and M read panrom
n, m = map(int, input().split())

# 2. Input-ah list-ah eduthu numpy array-ah mathurom
storage = []
for _ in range(n):
    storage.append(list(map(float, input().split())))

my_array = numpy.array(storage)

# 3. Task 1: Mean along axis 1
print(numpy.mean(my_array, axis=1))

# 4. Task 2: Var along axis 0
print(numpy.var(my_array, axis=0))

# 5. Task 3: Std along axis None
# Sample output format match panna round use pannalam
print(round(numpy.std(my_array, axis=None), 11))


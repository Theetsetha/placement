import numpy

# 1. N and M read panrom
n, m = map(int, input().split())

# 2. Array create panrom
my_array = numpy.array([input().split() for _ in range(n)], int)

# 3. Axis 1-la min kandupudichu, athoda max-ah print panrom
min_values = numpy.min(my_array, axis=1)
print(numpy.max(min_values))

# native-python-array-math
Array math for super lightweight applications where importing numpy is too cumbersome or otherwise not possible. This is not optimized at all, but it's lightweight.

## Implementation
I like to use the "nm" alias since it's similar to "np"
~~~
In [1]: from native_array_math import array_math as nm

# compute the average with even weights
In [2]: nm.dot_product([2,4,6,8], [0.25, 0.25, 0.25, 0.25])
Out[2]: 5.0
~~~

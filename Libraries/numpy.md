# Numpy
Date: 07/01/19

Name: Matthew Gleich

ID Teach Camp - Introduction to Coding for Machine Learning

## What is Numpy?
**Numpy** and **Matplotlib** can be used to handle data for the machine learning.
There are two types of data that we are sorting though when doing machine learning:
1. Training data
2. Testing data

### Adding numpy to you file
Add the following line to the top of your program:

```python
import numpy as np
# the as np is not needed
```

### Making a array using numpy
Do the following to make an array using numpy:

```python
import numpy as np

array = np.array([1, 2, 3, 4])
print(array)  # prints [1, 2, 3, 4]
```

### Shape in Numpy
Shape in numpy is similar to doing len([]) to a normal array

```python
import numpy as np

array = np.array([1, 2, 3, 4])
print(array.shape)  # prints (4,) due to that fact that their are 4 items in the list
```

### Multidimensional Arrays in Numpy
Multidimensional arrays is really just a fancy way of saying "arrays in arrays". Below is an example of a multidimensional array.
```python
import numpy as np

array = np.array([1, 2], [3, 4])

print(array.shape)  # prints(2,2) because there are two array values each with two values

array2 = np.array( [ [1, 2, 3], [2, 3, 4], [5, 4, 3] ])

print(array2.shape) # prints(3,3) because there are three array values each with three values
```

### Array Arithmetic in Numpy
Similar to the zip() function in general python, you can join two lists together doing the following operation:
```python
num1 = [1 ,1 ,1 ,1 ,1]
num2 = [1 ,1 ,1 ,1 ,1]

both_lists = num1 + num2  # Is [1 ,1 ,1 ,1 ,1, 1 ,1 ,1 ,1 ,1]
```

### Arithmetic with NumPy Arrays
Can can do arithmetic operations on arrays using Numpy by doing the following:

```python

```

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

# Shape in Numpy
Shape in numpy is similar to doing len([]) to a normal array

```python
import numpy as numpy

array = np.array([1, 2, 3, 4])
print(array.shape)  # prints (4,) due to that fact that their are 4 items in the list
```
import numpy as np
from numpy import random
import matplotlib.pyplot as plt

class Neuron:
    """
    The Neuron class
    """

    def __init__(self, weight_count):
        """
        The init function
        :param weight_count: the amount of random weights
        :return: none
        """
        random.seed(1)
        self.weights = initial_weights = 2 * random.random((1,1)) - 1

    def tanh_derivative(self, x):
        return 1 - np.tanh(x) ** 2

    def step(self, x):
        dot_product = np.dot(x, self.weights)
        return np.tanh(dot_product)

    def train(self, iterations, train_inputs, train_outputs):
        for i in range(iterations):
            output = self.step(train_inputs)
            error = train_outputs - output
            adjustment = np.dot(train_inputs.T, (error * self.tanh_derivative(output)))
            self.weights += adjustment


def function(x):
    return 2 * x


x = [i/100 for i in range(300)]
y = [function(i/100) for i in range(300)]
data = []
for i in range(300):
    data.append(function(i/100)+random.randint(1, 100)/50)
# plt.plot(data, "b.")
# plt.show()
x = np.asarray([x])/100
y = np.asarray([y])/100

neuron = Neuron(300)
x = x.reshape(300, 1)
y = y.T
neuron.train(10000, x, y)
constnat = neuron.weights[0][0]

test_data = []
for i in x:
    test_data.append(i *100* constnat)
plt.plot(data, "bo")
plt.plot(test_data, "r-")
plt.show()


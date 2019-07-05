import matplotlib.pyplot as plt
import numpy as np
from numpy import random as random

'''
--------------------------------------------------
Author: Tyler Hanf
06/20/2019
Filename: ML_Visual.py

This code graphs basic machine learning aspects
with linear regression.

It demonstrate how each step approaches the target
function with a decreasing error rate and smaller
adjustments as the learning function approaches
the desired function.

*Note: This code is for basic teaching purposes,
so do not run a large number of training steps,
the code is not designed for it. The max number
of training steps should be about 75-100 depending
on the machine.
--------------------------------------------------
'''

'''
--------------------------------------------------
The Graph class is used for easily graphing very
basic plots. It is designed for making one figure
with a variable number of subplots and a variable
pause time both based on user input.
--------------------------------------------------
'''
class Graph:
    #Standard font to be changed if desired
    STANDARD_FONT = "Helvetica"
    '''
    Init function
    numSubPlots -> user defined number of subplots
                   for figure
    pauseTime -> Amount of pause time to be used
                 between plotting (assuming iterative
                 plotting)
    '''
    def __init__(self, numSubPlots, pauseTime):
        self.figure = plt.figure()
        self.numPlots = numSubPlots
        self.pauseTime = pauseTime

    '''
    Plots a graph
    plotNum -> the subplot number
    data -> the data for y-axis
    title -> the title of the plot
    color -> color of the plot line
    *args -> an optional variable for x-axis if needed
    '''
    def plot(self, plotNum: int, data, title: str, color: str, *args):
        self.figure.add_subplot(self.numPlots, 1, plotNum)
        if args:
            plt.plot(args, data, color)
        else:
            plt.plot(data, color)
        plt.title(title)
        #allows space between subplots
        plt.tight_layout()

    '''
    Used to pause plotting
    '''
    def pause(self):
        plt.pause(self.pauseTime)

    '''
    Adds text to the figure with medium font size
    x -> the x-axis positioning
    y -> the y-axis positioning
    text -> the string to be displayed
    return -> the figure text to be assigned
              so it can removed if needed
    '''
    def addFigText(self, x, y, text: str):
        return plt.figtext(x, y, text, fontname=Graph.STANDARD_FONT, fontsize="medium")

'''
------------------------------------------------
Class Neuron represents a single neuron designed
for training a linear regression model.
It includes a plotting function for displaying
aspects of the learning process
------------------------------------------------
'''
class Neuron:

    '''
    Initializes neuron with random seed
    and random weights. For linear regression
    only one weight is needed.

    weight_count -> number of weights in the neuron
    function -> the desired function (to display for graph)
    graph -> the graph to be used for displaying learning data
    '''
    def __init__(self, weight_count, function, graph):
        random.seed(1)
        self.weights = initial_weights = 2 * random.random((1, weight_count)) - 1
        self.graph = graph
        self.function = function

    '''
    Calculates the derivative of the tanh
    function with respect to some output
    value of the step: x

    x -> respected value in tanh derivative
    '''
    def tanh_derivative(self, x):
        return 1 - np.tanh(x) ** 2

    '''
    Calculates the dot_product of
    train_input vectors and weights,
    then feeds it into the tanh function
    to give activation value

    x -> train_inputs
    '''
    def step(self, x):
        dot_product = np.dot(x, self.weights)
        tan = np.tanh(dot_product)
        return tan

    '''
    The heart of the learning algorithm, train
    teaches the data by making adjustments to the
    weights based on a found error between the
    train_inputs and train_outputs.
    This process is repeated based on the number of
    iterations defined by the user.

    iterations -> number of times train() will repeat
    train_inputs -> the dataPoints that will be trained
    train_outputs -> the correct data to be compared with the train_inputs
    '''
    def train(self, iterations, train_inputs, train_outputs):
        for i in range(iterations):
            output = self.step(train_inputs)
            error = train_outputs - output
            adjustment = np.dot(train_inputs.T, (error * self.tanh_derivative(output)))
            self.weights += adjustment
            self.plotTrainGraphs(i, output, train_outputs, error, adjustment)

    '''
    Plots the following data:
        1. output data--shows how the data learns to approach the desired function
        2. error--shows how the error decreases as data learns
        3. adjustment--shows how the adjustment size decreases as desired function
                       is approached. Perfect example of gradient descent

    Displays the following data:
        1. The step number
        2. The desired function
        3. The current function

    stepNum -> the current step number
    output -> the current output data
    train_outputs -> the desired output data
    error -> the current error
    adjustment -> the adjustment to change the weights
    '''
    def plotTrainGraphs(self, stepNum, output, train_outputs, error, adjustment):
            step = self.graph.addFigText(0.5, 0, "Training Step #: " + str(stepNum))
            tFunction = self.graph.addFigText(0.7, 0, "Target Function: " + self.function)
            cFunction = self.graph.addFigText(0.1, 0, "Current Function: " + str(self.weights[0][0]) + "*x")

            self.graph.plot(1, output, "Output", "b")
            self.graph.plot(1, train_outputs, "Output", "y")
            self.graph.plot(3, adjustment, "Adjustment", "g.", [i for i in range(stepNum+1)])
            self.graph.plot(2, error, "Error", "r")
            self.graph.pause()

            #necessary to remove in order to update
            tFunction.remove()
            cFunction.remove()
            step.remove()

'''
Calculates a value based on
defined coefficient and value
x

coefficient -> function coefficient
x -> value to be multiplied by coefficient
'''
def func(coefficient, x):
    return coefficient*x

'''
------------------------------------------
Gets coefficient number, number of training steps,
and pause time between plots by user then
creates and prepares data to be trained.
Creates a neuron and trains the data.
------------------------------------------
'''
def main():
    #number of subplots for graph
    NUM_SUB_PLOTS = 3
    #number of data points for function
    NUM_OF_DATA_POINTS = 200

    coefficient = int(input("Enter a coefficient: "))
    numTrainSteps = int(input("Enter the number of training steps: "))
    pauseTime = float(input("Enter the pause time between each train step: "))

    #initializes the graph
    graph = Graph(NUM_SUB_PLOTS, pauseTime)

    #Sets training input data
    x = [i/100 for i in range(NUM_OF_DATA_POINTS)]

    #Sets training output data
    y = [func(coefficient, i/100) for i in range(NUM_OF_DATA_POINTS)]

    #Creates a neuron
    neuron = Neuron(1, str(coefficient) + "*x", graph)

    #divide each entry by 100
    #for ease of plotting and training
    x = np.asarray([x])/100
    y = np.asarray([y])/100

    #reshape the arrays
    x = x.T
    y = y.T

    #train the input data x, with output data y
    neuron.train(numTrainSteps, x, y)


if __name__ == '__main__':
    main()

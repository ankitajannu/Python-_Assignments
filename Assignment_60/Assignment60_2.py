# ---------------------------------------------------------
# Program : Artificial Neuron with Sigmoid, ReLU, Tanh Activation
# Author  : Ankita Ramesh Jannu
# ---------------------------------------------------------

import math
import matplotlib.pyplot as plt
import numpy as np

# ---------------------------------------------------------
# Function Name : Marvellous_ReLU
# Description   : Applies ReLU activation function
# Formula       : ReLU(x) = max(0, x)
# Use           : Commonly used in hidden layers
# ---------------------------------------------------------
def Marvellous_ReLU(value):
    return max(0, value)


# ---------------------------------------------------------
# Function Name : Marvellous_Sigmoid
# Description   : Applies Sigmoid activation function
# Formula       : 1 / (1 + e^(-x))
# Use           : Commonly used in output layer for
#                 binary classification
# Output Range  : 0 to 1
# ---------------------------------------------------------
def Marvellous_Sigmoid(value):
    return 1 / (1 + math.exp(-value))


# ---------------------------------------------------------
# Function Name : Marvellous_Tanh
# Description   : Applies Tanh activation function
# Formula       :  (e^x - e^-x) / (e^x + e^-x)
# Use           : Used in hidden layers
# Output Range  : -1 to 1
# ---------------------------------------------------------
def Marvellous_Tanh(value):
    return (math.exp(value) - math.exp(-value)) / (math.exp(value) + math.exp(-value))


# ---------------------------------------------------------
# Function Name : Marvellous_Plot_Activation_Functions
# Description   : Plot Sigmoid, ReLU, Tanh functions
# ---------------------------------------------------------
def Marvellous_Plot_Activation_Functions():
    print("\n================ ACTIVATION FUNCTIONS ================\n")

    # Generate input values from -10 to 10
    x_values = np.linspace(-10,10,200)

    # Calculate outputs for all activation functions
    sigmoid_values = [Marvellous_Sigmoid(x) for x in x_values]
    relu_values = [Marvellous_ReLU(x) for x in x_values]
    tanh_values = [Marvellous_Tanh(x) for x in x_values]

    # ---------------------------------------------------------
    # Plot Sigmoid functions
    # ---------------------------------------------------------  

    plt.figure(figsize=(8,5))
    plt.plot(x_values, sigmoid_values)
    plt.title("Sigmoid Activation Function")
    plt.xlabel("Input values")
    plt.ylabel("Output values")
    plt.grid(True)
    plt.show()  

    # ---------------------------------------------------------
    # Plot ReLU functions
    # ---------------------------------------------------------  

    plt.figure(figsize=(8,5))
    plt.plot(x_values, relu_values)
    plt.title("ReLU Activation Function")
    plt.xlabel("Input values")
    plt.ylabel("Output values")
    plt.grid(True)
    plt.show()  

    # ---------------------------------------------------------
    # Plot Tanh functions
    # ---------------------------------------------------------  

    plt.figure(figsize=(8,5))
    plt.plot(x_values, tanh_values)
    plt.title("Tanh Activation Function")
    plt.xlabel("Input values")
    plt.ylabel("Output values")
    plt.grid(True)
    plt.show()  


# ---------------------------------------------------------
# Function Name : Marvellous_Display_Uses
# Description   : Display uses of activation functions
# ---------------------------------------------------------
def Marvellous_Display_Uses():
    print("\n========== USE OF ACTIVATION FUNCTIONS ==========\n")

    print("1. Sigmoid Function : ")
    print("     - Output range : 0 to 1")
    print("     - Used in output layer")
    print("     - Used for binary classification problems\n")

    print("2. ReLU Function : ")
    print("     - Output range : 0 to infinity")
    print("     - Mostly used in hidden layer")
    print("     - Fast and efficient activation function\n")

    print("1. Sigmoid Function : ")
    print("     - Output range : -1 to 1")
    print("     - Centers values around zero")
    print("     - Used in hidden layers of neural networks\n")


# ---------------------------------------------------------
# Main Function
# ---------------------------------------------------------
def main():
    # Plot all activation Functions
    Marvellous_Plot_Activation_Functions()

    # Display uses of Activation functions
    Marvellous_Display_Uses()


# ---------------------------------------------------------
# Starter
# ---------------------------------------------------------
if __name__ == "__main__":
    main()
# ---------------------------------------------------------
# Program : Artificial Neuron with Sigmoid Activation
# Author  : Ankita Ramesh Jannu
# ---------------------------------------------------------

import math
import matplotlib.pyplot as plt
import numpy as np

# ---------------------------------------------------------
# STEP 1 : Sigmoid Activation Function
# ---------------------------------------------------------
# Sigmoid converts input into range (0, 1)
# Used for probability-based outputs

def sigmoid(z):
    return 1/(1 + math.exp(-z))

# ---------------------------------------------------------
# STEP 2 : Neuron Forward Pass
# ---------------------------------------------------------
# Performs:
# 1. Weighted sum
# 2. Add bias
# 3. Apply sigmoid activation

def Neuron_forward(inputs, weights, bias):
    print("\n----- NEURON CALCULATION START -----\n")

    # Display inputs
    print("Inputs (x)   :", inputs)
    print("Weights (w)  :", weights)
    print("Bias (b)     :", bias)

    # -----------------------------------------------------
    # Weighted Sum Calculation
    # z = w·x + b
    # -----------------------------------------------------

    z = sum(w * x for w, x in zip(weights, inputs)) + bias

    print("\nStep 1 : Weighted sum : ")
    print("z = ",z)

    # -----------------------------------------------------
    # Apply Sigmoid function
    # -----------------------------------------------------

    y_hat = sigmoid(z)

    print("\nStep 2 : Activation Function")
    print("Activation Function : Sigmoid")
    print("Output (ŷ) = ",y_hat)

    print("\n----- NEURON CALCULATION END -----\n")

    return z, y_hat

# ---------------------------------------------------------
# STEP 3 : Main Function
# ---------------------------------------------------------

def main():
    print("\n===== Sigmoid Function =====\n")

    # Inputs
    inputs = [2,3]

    # Weights
    weights = [0.4,0.6]

    # Bias
    bias = 0.5

    # Forward pass
    z, y_hat = Neuron_forward(inputs, weights, bias)

    print("Final z = ",z)
    print("Final y_hat = ",y_hat)

    if y_hat > 0.5:
        print("\nInterpretation : Output is close to 1")
        print("Neuron is strongly activated")   
    else:
        print("\nInterpretation : Output is close to 0")
        print("Neuron is weekly activated")
    

if __name__ == "__main__":
    main()
# ------------------------------------------------------------
# Program : Flatten layer demonstration in CNN
# Author  : Ankita Ramesh Jannu
# ------------------------------------------------------------

import numpy as np

# ------------------------------------------------------------
# Function Name : Flatten
# Description   : Convert 2D matrix into 1D vector
# ------------------------------------------------------------
def Flatten(matrix):
    flatten_output = matrix.flatten()
    return flatten_output

#-------------------------------------------------------------
# Function    : Fully_Connected_Layer
# Description : Passes flatten output to fully 
#               connected layer and calculates output
#-------------------------------------------------------------
def Fully_Connected_Layer(flatten_output):
    weights = np.array([0.5, 0.2, 0.3, 0.4])
    bias = 1.0

    print("Flatten Input :", flatten_output)
    print("Weights       :", weights)
    print("Bias          :", bias)

    multiplication = flatten_output * weights

    print("\nInput × Weight:")

    for i in range(len(flatten_output)):
        print(f"{flatten_output[i]:.0f} × {weights[i]} = {multiplication[i]:.2f}")

    total = np.sum(multiplication)

    print("\nSum =", total)

    final_output = total + bias

    print("Final Output = Sum + Bias")
    print(f"{total:.2f} + {bias} = {final_output:.2f}")

    return final_output


# ------------------------------------------------------------
# Function Name : Demonstrate_Flattening
# Description   : Demonstrates Flatten Layer in CNN
# ------------------------------------------------------------
def Demonstrate_Flattening():
    # Input matrix
    matrix = np.array([
        [6, 4],
        [8, 6]
    ])

    print("\n================ INPUT MATRIX ================\n")
    print(matrix)

    # Flatten Layer
    flatten_output = Flatten(matrix)
    print("\n================ FLATTEN OUTPUT ================\n")
    print(flatten_output)

    # Fully Connected layer 
    final_output = Fully_Connected_Layer(flatten_output)

    # Explanation
    print("\n================ EXPLANATION ================\n")

    print("Flatten Layer converts 2D feature maps")
    print("into a 1D vector")

    print("\nThis 1D vector is passed to the")
    print("Fully Connected Layer")

    print("\nFlattening helps CNN connect")
    print("convolution layers with dense layers")


def main():
    Demonstrate_Flattening()

if __name__ == "__main__":
    main()
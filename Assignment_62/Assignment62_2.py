# ------------------------------------------------------------
# Program : ReLU and Max Pooling Demonstration
# Author  : Ankita Ramesh Jannu
# ------------------------------------------------------------

import numpy as np

# ------------------------------------------------------------
# Function Name : ReLU
# Description   : Applies ReLU activation function
# Rule          :
#   If value < 0  -> convert to 0
#   If value >= 0 -> keep same
# ------------------------------------------------------------
def ReLU(feature_map):
    relu_output = np.maximum(0,feature_map)
    return relu_output


# ------------------------------------------------------------
# Function Name : MaxPooling
# Description   : Applies 2x2 Max Pooling
# ------------------------------------------------------------
def MaxPooling(feature_map):
    rows, cols = feature_map.shape

    pooled_output = np.zeros((rows // 2, cols // 2))

    for i in range(0, rows-1, 2):
        for j in range(0, cols-1, 2):
            
            # Extract 2x2 region 
            region = feature_map[i:i+2, j:j+2]

            print("\n2x2 Region : ")
            print(region)

            # Find maximum value
            max_value = np.max(region)

            print("Maximum value : ",max_value)

            pooled_output[i // 2, j // 2] = max_value
    return pooled_output

# ------------------------------------------------------------
# Function Name : Demonstrate_ReLU_And_Pooling
# Description   : Demonstrates ReLU and Max Pooling
# ------------------------------------------------------------
def Demonstrate_ReLU_And_Pooling():
    # Feature map
    feature_map = np.array([
        [ 3, 3, 3],
        [ 0, 0, 0],
        [-3,-3,-3]
    ])

    print("\n================ INPUT FEATURE MAP ================\n")
    print(feature_map)

    # Apply ReLU
    relu_output = ReLU(feature_map)
    print("\n================ ReLU OUTPUT ================\n")
    print(relu_output)

    # Apply Max pooling
    pooled_output = MaxPooling(relu_output)
    print("\n================ MAX POOLED OUTPUT ================\n")
    print(pooled_output)

    # Explanation
    print("\n================ EXPLANATION ================\n")

    print("ReLU converts all negative values into 0")
    print("Positive values remain unchanged\n")

    print("Max Pooling selects the maximum value")
    print("from each 2x2 region")

    print("\nPooling reduces feature map size because")
    print("multiple values are compressed into one value")
    print("This reduces computation and helps")
    print("in extracting important features")


def main():
    Demonstrate_ReLU_And_Pooling()

if __name__ == "__main__":
    main()
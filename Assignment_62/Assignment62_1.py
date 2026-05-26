# ------------------------------------------------------------
# Program : Manual Convolution Operation
# Author  : Ankita Ramesh Jannu
# ------------------------------------------------------------

import numpy as np

# ------------------------------------------------------------
# Function Name : ManualConvolution
# Description   : Performs manual convolution using
#                 3x3 edge detection kernel
# ------------------------------------------------------------
def ManualConvolution():
    
    # ------------------------------------------------------------
    # Step 1 : Create 5x5 Image
    # ------------------------------------------------------------
    image = np.array([
        [0,   0,   0,   0,   0,   0],
        [0,   0,   0,   0,   0,   0],
        [1,   1,   1,   1,   1,   1],
        [0,   0,   0,   0,   0,   0],
        [0,   0,   0,   0,   0,   0],
    ])

    print("\n================ INPUT IMAGE ================\n")
    print(image)

    # ------------------------------------------------------------
    # Step 2 : 3x3 Kernel for Edge Detection
    # ------------------------------------------------------------
    kernel = np.array([
        [-1, -1, -1],
        [ 0,  0,  0],
        [ 1,  1,  1]
    ])

    print("\n================ KERNEL ================\n")
    print(kernel)

    # ------------------------------------------------------------
    # Step 3 : Convolution Operation
    # Output Size = (5-3+1) x (5-3+1) = 3x3
    # ------------------------------------------------------------
    feature_map = np.zeros((3,3))

    for i in range(3):
        for j in range(3):

            # Extract 3x3 region
            region = image[i:i+3, j:j+3]

            print(f"\nRegion({i},{j}) : ")
            print(region)

            # Perform Multiplication and Addition
            result = np.sum(region * kernel)

            # Display calculation
            print("\nCalculation : ")

            calculation = ""

            for row in range(3):
                for col in range(3):

                    calculation = calculation + (
                        f"{region[row][col]}*{kernel[row][col]}"
                    )

                    if not (row == 2 and col ==2):
                        calculation = calculation + "+"

            print(calculation)

            print("\nOutput = ",result)

            # Store result in feature map
            feature_map[i][j] = result

    # ------------------------------------------------------------
    # Step 4 : Show Feature Map
    # ------------------------------------------------------------
    print("\nFeature Map (Detected Edge)")
    print(feature_map)

def main():
    ManualConvolution()

if __name__ == "__main__":
    main()
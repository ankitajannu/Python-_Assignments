# ---------------------------------------------------------
# Program : Loss Calculation
# Author  : Ankita Ramesh Jannu
# ---------------------------------------------------------

import math

# ---------------------------------------------------------
# Function Name : Marvellous_MSE
# Description   : Calculates Mean Squared Error Loss
# Formula       : MSE = Σ(y_true - y_pred)^2 / n
# Use           : Used in Regression problems
# ---------------------------------------------------------
def Marvellous_MSE(y_true, y_pred):
    n = len(y_true)
    total_error = 0

    print("\n================ MEAN SQUARED ERROR ================\n")

    for index in range(n):
        error = y_true[index] - y_pred[index]
        squared_error = error ** 2   # Squared error

        print(f"Actual value : {y_true}[index]")
        print(f"Predicted value : {y_pred}[index]")
        print(f"Error : {error}")
        print(f"Squared error : {squared_error}[index]\n")

        total_error = total_error + squared_error

    mse = total_error / n
    return mse

# ---------------------------------------------------------
# Function Name : Marvellous_Binary_CrossEntropy
# Description   : Calculates Binary Cross Entropy Loss
# Formula       :
# BCE = -(y log(p) + (1-y) log(1-p))
# Use           : Used in Binary Classification problems
# ---------------------------------------------------------
def Marvellous_Binary_CrossEntropy(y_true, y_pred):
    total_loss = 0
    n = len(y_true)

    print("\n================ BINARY CROSS ENTROPY ================\n")


    for index in range(n):
        y = y_true[index]
        p = y_pred[index]

        # Avoid log(0)
        p = max(min(p, 0.999), 0.001)

        loss = -(y * math.log(p) + (1 - y) * math.log(1 - p))

        print(f"Actual Value    : {y}")
        print(f"Predicted Value : {p}")
        print(f"Loss             = {loss:.4f}\n")

        total_loss += loss

    bce =  total_loss / n
    return bce

# ---------------------------------------------------------
# Function Name : Marvellous_Display_Uses
# Description   : Displays use of loss functions
# ---------------------------------------------------------
def Marvellous_Display_Uses():
    print("\n================ USE OF LOSS FUNCTIONS ================\n")

    print("1. Mean Squared Error(MSE) : ")
    print("     - Used in regression problems")
    print("     - Measures difference between")
    print("     actual and predicted values")
    print("   - Lower MSE means better model\n")

    print("2. Binary Cross Entropy(BCE) : ")
    print("     - Used in Binary classification")
    print("     - Measures prediction probability error")
    print("   - Lower BCE means better classification\n")


# ---------------------------------------------------------
# Main Function
# ---------------------------------------------------------
def main():
    # Sample data for MSE
    y_true_regression = [10,20,30]
    y_pred_regression = [12,18,33]

    mse_loss = Marvellous_MSE(y_true_regression, y_pred_regression)

    print(f"Final MSE Loss : {mse_loss:.4f}")

    # Sample data for BCE
    y_true_classification = [1,0,1]
    y_pred_classification = [0.9,0.2,0.8]

    bce_loss = Marvellous_Binary_CrossEntropy(y_true_classification, y_pred_classification)

    print(f"Final Binary Cross Entropy Loss : {bce_loss:.4f}")

    # Display uses
    Marvellous_Display_Uses()


# ---------------------------------------------------------
# Starter
# ---------------------------------------------------------
if __name__ == "__main__":
    main()
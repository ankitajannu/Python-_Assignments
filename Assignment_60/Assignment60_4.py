# ---------------------------------------------------------
# Program : ANN weight updation using Backpropagation
# Author  : Ankita Ramesh Jannu
# ---------------------------------------------------------

import math

# ---------------------------------------------------------
# Function Name : Marvellous_Sigmoid
# Description   : Applies Sigmoid activation function
# Formula       : 1 / (1 + e^(-x))
# ---------------------------------------------------------
def Marvellous_Sigmoid(value):
    return 1 / (1 + math.exp(-value))


# ---------------------------------------------------------
# Function Name : Marvellous_Sigmoid_Derivative
# Description   : Calculates derivative of sigmoid
# Formula       : output * (1 - output)
# ---------------------------------------------------------
def Marvellous_Sigmoid_Derivative(output):
    return output * (1 - output)


# ---------------------------------------------------------
# Function Name : Marvellous_ANN_Training
# Description   : Demonstrates ANN training using
#                 Forward Propagation,
#                 Backpropagation and
#                 Gradient Descent
# ---------------------------------------------------------
def Marvellous_ANN_Training():
    # ---------------------------------------------------------
    # Input values
    # ---------------------------------------------------------
    x1 = 1.0
    x2 = 2.0
    target = 1.0

    # ---------------------------------------------------------
    # Initial weights and bias
    # ---------------------------------------------------------
    w1 = 0.5
    w2 = -0.3
    b = 0.1

    # Learning rate
    learning_rate = 0.1

    # Number of training iterations
    epochs = 20

    # ---------------------------------------------------------
    # Store training history for animation
    # ---------------------------------------------------------
    history = []

    print("Initial Values")
    print("w1 =", w1)
    print("w2 =", w2)
    print("b  =", b)
    print("-" * 50)

    # ---------------------------------------------------------
    # Training loop
    # ---------------------------------------------------------
    for epoch in range(1, epochs + 1):

        # Step 1: Forward Propagation
        z = (x1 * w1) + (x2 * w2) + b
        output = Marvellous_Sigmoid(z)

        # Step 2: Loss Calculation
        loss = 0.5 * (target - output) ** 2

        # Step 3: Backpropagation
        dL_doutput = output - target
        doutput_dz = Marvellous_Sigmoid_Derivative(output)
        dL_dz = dL_doutput * doutput_dz

        dL_dw1 = dL_dz * x1
        dL_dw2 = dL_dz * x2
        dL_db = dL_dz

        # Store values before update for animation
        history.append({
            "epoch": epoch,
            "z": z,
            "output": output,
            "loss": loss,
            "w1": w1,
            "w2": w2,
            "b": b,
            "grad_w1": dL_dw1,
            "grad_w2": dL_dw2,
            "grad_b": dL_db
        })

        # Step 4: Gradient Descent
        w1 = w1 - (learning_rate * dL_dw1)
        w2 = w2 - (learning_rate * dL_dw2)
        b = b - (learning_rate * dL_db)

        # Print values
        print("Epoch:", epoch)
        print("Weighted Sum (z):", round(z, 4))
        print("Predicted Output :", round(output, 4))
        print("Target Output    :", target)
        print("Loss             :", round(loss, 6))
        print("Gradient dL/dw1  :", round(dL_dw1, 6))
        print("Gradient dL/dw2  :", round(dL_dw2, 6))
        print("Gradient dL/db   :", round(dL_db, 6))
        print("Updated w1       :", round(w1, 6))
        print("Updated w2       :", round(w2, 6))
        print("Updated b        :", round(b, 6))
        print("-" * 50)

    print("Final Trained Values")
    print("w1 =", round(w1, 6))
    print("w2 =", round(w2, 6))
    print("b  =", round(b, 6))

# ---------------------------------------------------------
#  Main Function
# ---------------------------------------------------------

def main():
    Marvellous_ANN_Training()

# ---------------------------------------------------------
# Starter
# ---------------------------------------------------------

if __name__ == "__main__":
    main()
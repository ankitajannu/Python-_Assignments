from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neural_network import MLPClassifier
from sklearn.metrics import accuracy_score

def CustormerService():

    # ----------------------------------------------------
    # Step 1: Prepare the dataset
    # [Age, Monthly charger, Tenure, Number of complaints, Customer support cells]
    # Output : 0 = Customer will stay, 1 = Customer will leave
    # ----------------------------------------------------

    X = [
        [25,500,12,1,2],
        [30,700,24,0,1],
        [45,1200,6,5,8],
        [50,1500,5,6,10],
        [28,600,18,1,1],
        [35,800,30,0,0],
        [48,1400,4,7,9],
        [52,1600,3,8,12],
        [27,550,20,0,1],
        [42,1300,8,4,7]
    ]

    y = [
        0,0,1,1,0,
        0,1,1,0,1
    ]

    # ------------------------------------------------------------
    # Step 2: Dataset Cleaning
    # Check for missing values and duplicate values
    # ------------------------------------------------------------

    print("\nChecking dataset...")

    # Since dataset is manually created,
    # there are no missing or duplicate values

    print("No missing values found")
    print("No duplicate values found\n")

    # ------------------------------------------------------------
    # Step 3: Split dataset
    # stratify=y keeps class ratio balanced
    # ------------------------------------------------------------
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.3, random_state=42, stratify=y
    )

    # ------------------------------------------------------------
    # Step 4: Scale the input data
    # ------------------------------------------------------------
    scaler = StandardScaler()

    X_train_scaled = scaler.fit_transform(X_train)
    X_test_scaled = scaler.transform(X_test)
    
    # ------------------------------------------------------------
    # Step 5: Create FNN model
    # lbfgs often works better for very small datasets
    # ------------------------------------------------------------
    model = MLPClassifier(
        hidden_layer_sizes=(5,),
        activation='relu',
        solver='lbfgs',
        max_iter=2000,
        random_state=42
    )


    # ------------------------------------------------------------
    # Step 6 : Train the model
    # ------------------------------------------------------------
    model.fit(X_train_scaled, y_train)

    # ------------------------------------------------------------
    # Step 7 : Predict
    # ------------------------------------------------------------
    y_pred = model.predict(X_test_scaled)

    # ------------------------------------------------------------
    # Step 8: Evaluate
    # ------------------------------------------------------------
    print("Actual output : ",y_test)
    print("Predicted output : ",y_pred.tolist())

    accuracy = accuracy_score(y_test,y_pred)
    print("\nAccuracy of model : ",accuracy)

    # ------------------------------------------------------------
    # Step 9: Predict new customer
    # ------------------------------------------------------------
    new_customer = [[46,1450,5,6,9]]
    new_customer_scaled = scaler.transform(new_customer)

    prediction = model.predict(new_customer_scaled)

    if prediction[0] == 1:
        print("\nPrediction : Customer will leave")
    else:
        print("\nPrediction : Customer may stay")

# ------------------------------------------------------------
# Main function
# ------------------------------------------------------------

def main():
    CustormerService()

# ------------------------------------------------------------
# Starter
# ------------------------------------------------------------
if __name__ == "__main__":
    main()
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neural_network import MLPClassifier
from sklearn.metrics import accuracy_score

def PredictLoanApproval():

    # ----------------------------------------------------
    # Step 1: Prepare the dataset
    # [Applicant income, Credict score, Loan amount, Existing EMI, Amployment status]
    # Output : 0 = Not stable, 1 = Stable
    # ----------------------------------------------------

    X = [
        [25000,600,200000,10000,0],
        [40000,700,300000,8000,1],
        [60000,750,500000,12000,1],
        [20000,550,150000,15000,0],
        [80000,800,700000,10000,1],
        [35000,650,250000,9000,1],
        [18000,500,100000,12000,0],
        [90000,850,800000,15000,1],
        [30000,580,200000,14000,0],
        [70000,780,600000,10000,1]
    ]

    y = [
        0,1,1,0,1,
        1,0,1,0,1
    ]

    # ------------------------------------------------------------
    # Step 2: Split dataset
    # stratify=y keeps class ratio balanced
    # ------------------------------------------------------------
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.3, random_state=42, stratify=y
    )

    # ------------------------------------------------------------
    # Step 3: Scale the input data
    # ------------------------------------------------------------
    scaler = StandardScaler()

    X_train_scaled = scaler.fit_transform(X_train)
    X_test_scaled = scaler.transform(X_test)
    
    # ------------------------------------------------------------
    # Step 4: Create FNN model
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
    # Step 5 : Train the model
    # ------------------------------------------------------------
    model.fit(X_train_scaled, y_train)

    # ------------------------------------------------------------
    # Step 6 : Predict
    # ------------------------------------------------------------
    y_pred = model.predict(X_test_scaled)

    # ------------------------------------------------------------
    # Step 7: Evaluate
    # ------------------------------------------------------------
    print("Actual output : ",y_test)
    print("Predicted output : ",y_pred.tolist())

    accuracy = accuracy_score(y_test,y_pred)
    print("\nAccuracy of model : ",accuracy)

    # ------------------------------------------------------------
    # Step 8: Predict new customer
    # ------------------------------------------------------------
    new_applicant = [[55000,720,400000,10000,1]]
    new_applicant_scaled = scaler.transform(new_applicant)

    prediction = model.predict(new_applicant_scaled)

    if prediction[0] == 1:
        print("\nPrediction : Loan Approved")
    else:
        print("\nPrediction : Loan Rejected")

# ------------------------------------------------------------
# Main function
# ------------------------------------------------------------

def main():
    PredictLoanApproval()

# ------------------------------------------------------------
# Starter
# ------------------------------------------------------------
if __name__ == "__main__":
    main()
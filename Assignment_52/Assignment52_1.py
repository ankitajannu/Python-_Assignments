import pandas as pd
import matplotlib.pyplot as plt

from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans

def StudentPerformanceClustering():
    border = "="*70

    #-------------------------------------------------------------------
    # Step 1 : Load the dataset
    #-------------------------------------------------------------------

    print(border)
    print("Step 1 : Load the dataset")
    print(border)
    df = pd.read_csv("student-mat.csv", sep=';')

    print("First few records : ")
    print(df.head())

    print("Shape of dataset : ")
    print(df.shape)

    print("Missing values : ")
    print(df.isnull().sum())

    #-------------------------------------------------------------------
    # Step 2 : Select Features
    #-------------------------------------------------------------------

    print(border)
    print("Step 2 : Select Features")
    print(border)

    X = df[["G1",
            "G2",
            "G3",
            "studytime",
            "failures",
            "absences"]]

    print("Selected Features : ")
    print(X.head())

    print("Shape of selected features : ")
    print(X.shape)

    #----------------------------------------------------------------
    # Step 3 : Data Scaling 
    #---------------------------------------------------------------

    print(border)
    print("Step 3 : Data Scaling")
    print(border)

    scalar = StandardScaler()

    X_scaled = scalar.fit_transform(X)

    print("Data after scaling : ")
    print(X_scaled[:5])

    #----------------------------------------------------------------
    # Step 4 : Use Elbow Method
    #---------------------------------------------------------------

    print(border)
    print("Step 4 : Use Elbow method")
    print(border)

    WCSS = []

    for i in range(1,11):
        model = KMeans(n_clusters=i,random_state=42,n_init=10)
        model.fit(X_scaled)
        WCSS.append(model.inertia_)

    plt.figure(figsize=(8,5))
    plt.plot(range(1,11), WCSS, marker = 'o')
    plt.xlabel("Number of clusters")
    plt.ylabel("WCSS")
    plt.title("Elbow method")
    plt.grid(True)
    plt.show()

    #----------------------------------------------------------------
    # Step 5 : Train the model
    #---------------------------------------------------------------

    print(border)
    print("Step 5 : Train the model")
    print(border)

    kmeans = KMeans(
        n_clusters=3,
        random_state=42,
        n_init=10
    )

    clusters = model.fit_predict(X_scaled)

    df["clusters"] = clusters

    print("Dataset with cluster")
    print(df.head(30))

############################################################################
# Main Function
############################################################################

def main():
    StudentPerformanceClustering()

############################################################################
# Starter
############################################################################

if __name__ == "__main__":
    main()
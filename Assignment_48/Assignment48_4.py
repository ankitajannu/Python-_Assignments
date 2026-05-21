import numpy as np
from sklearn.preprocessing import StandardScaler
from scipy.spatial.distance import euclidean

def FeatureScaling():
    data = np.array([
        [25,20000],
        [30,40000],
        [35,80000]
    ])

    distance_before = euclidean(data[0], data[1])

    print("Euclidean distance before scaling : ")
    print(distance_before)

    scalar = StandardScaler()

    scaled_data = scalar.fit_transform(data)

    print("\nScaled dataset : ")
    print(scaled_data)

    distance_after = euclidean(scaled_data[0], scaled_data[1])

    print("\nEuclidean distance after scaling : ")
    print(distance_after)

    print("\nExplanation :")
    print("1.Before scaling, some features may have very large values compared to other features.")
    print("2.Because of this, features with larger values dominate the Euclidean distance calculation.")
    print("3.After applying feature scaling, all features are transformed to a similar range.")
    print("4.This makes the distance calculation balanced and more meaningful.")

def main():
    FeatureScaling()

if __name__ == "__main__":
    main()
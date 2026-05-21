import numpy as np
from sklearn.preprocessing import StandardScaler

def FeatureScaling():
    X = [
        [25,20000],
        [30,40000],
        [35,80000]
    ]

    scaler = StandardScaler()

    scaled_data = scaler.fit_transform(X)

    print("Scaled Dataset : ")
    print(scaled_data)

def main():
    FeatureScaling()

if __name__ == "__main__":
    main()
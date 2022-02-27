import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score


def runModel(data, mod=DecisionTreeClassifier, testProportion=0.2, weight=np.array([])):
    xn = int(len(data)*(1-testProportion))
    x = data[:, 1:]
    y = data[:, 0]

    x_train = x[:xn]
    x_test = x[xn:]
    y_train = y[:xn]
    y_test = y[xn:]

    model = mod()
    if len(weight) == 0:
        model.fit(x_train, y_train)
    else:
        model.fit(x_train, y_train, sample_weight=weight[:xn])
    predictions = model.predict(x_test)

    score = model.score(x_test, y_test)

    plt.figure(0)
    plt.plot(predictions, label="predictions")
    plt.plot(y_test, label="y_test")
    plt.legend()
    plt.show()

    plt.figure(1)
    plt.plot(abs(y_test - predictions))
    plt.title(r"|y_test-predictions|")
    # plt.legend()
    plt.show()
    averageError = np.average(abs(y_test - predictions))

    closeHits = 0
    bigError = 0
    mediumError = 0
    for ind, val in enumerate(y_test):
        if abs(val - predictions[ind]) <= 1:
            closeHits += 1
        elif abs(val - predictions[ind]) >= 3 and val:
            bigError += 1
        elif abs(val-predictions[ind]) >= 2:
            mediumError += 1


    print(f"Score : {score}\nAverage error : {averageError}\nSize of test-data : {len(y_test)}")
    print(f"Close hits (error<=1): {closeHits}\nBig misses (error>=3): {bigError}\nMedium errors (2<=error<=3): {mediumError}")

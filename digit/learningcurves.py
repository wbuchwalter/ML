
import matplotlib.pyplot as plt
from sklearn.learning_curve import learning_curve
import numpy as np

def graphLearningCurves(forest, X, y):
    train_sizes, train_scores, test_scores = learning_curve(forest, X, y)

    train_scores_mean = np.mean(train_scores, axis=1)
    test_scores_mean = np.mean(test_scores, axis=1)

    plt.figure()
    plt.ylim(0.6, 1.01)
    plt.gca().invert_yaxis()
    plt.grid()

    plt.plot(train_sizes, train_scores_mean, 'o-', color='b', label='Train')
    plt.plot(train_sizes, test_scores_mean, 'o-', color= 'r', label='Test')

    plt.draw()
    plt.show()
    plt.gca().invert_yaxis()

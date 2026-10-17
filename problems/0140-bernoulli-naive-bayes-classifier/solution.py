import numpy as np

class NaiveBayes():
    def __init__(self, smoothing=1.0):
        self.smoothing = smoothing

    def forward(self, X, y):
        # Probability of each class
        pr_1 = np.sum(y == 1)/len(y)
        pr_0 = np.sum(y == 0)/len(y)

        x_0 = X[y == 0]
        x_1 = X[y == 1]

        ## in each feature probabilty of x_i = 1 in x_1 i.e we are seeing now along the columns for prob of 1 for which prediction is 1
        pr_1_x_1 = (np.sum(x_1,axis=0)+self.smoothing)/(len(x_1)+2*self.smoothing)
        pr_0_x_1 = 1-pr_1_x_1

        ## in each feature probabilty of x_i = 1 in x_0 i.e we are seeing now along the columns for prob of 1 for which prediction is 1
        pr_1_x_0 = (np.sum(x_0,axis=0)+self.smoothing) / (len(x_0) + 2*self.smoothing)
        pr_0_x_0 = 1-pr_1_x_0

        # Store log probabilities
        self.log_pr_1 = np.log(pr_1) if pr_1>0 else -np.inf
        self.log_pr_0 = np.log(pr_0) if pr_0>0 else -np.inf

        self.log_pr_1_x_1 = np.log(pr_1_x_1)
        self.log_pr_0_x_1 = np.log(pr_0_x_1)
        self.log_pr_1_x_0 = np.log(pr_1_x_0)
        self.log_pr_0_x_0 = np.log(pr_0_x_0)

    def predict(self, X):
        predictions = []
        # Predict class labels for test set X
        for x in X:
            # Calculating score assuming class 0
            score_0 = self.log_pr_0+np.sum(x*self.log_pr_1_x_0+(1-x)*self.log_pr_0_x_0)

            # Calculating score assuming class 1
            score_1 = self.log_pr_1+np.sum(x*self.log_pr_1_x_1+(1 - x)*self.log_pr_0_x_1)

            predictions.append(1 if score_1>score_0 else 0)

        return np.array(predictions)
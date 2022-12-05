import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
class LR:
    def __init__(self):
        self.m = None
        self.b = None
    def fit(self,X_Train,Y_Train):
        num = 0
        den = 0
        for i in range(X_Train.shape[0]):
            num+= (X_Train[i]-X_Train.mean())*(Y_Train[i]-Y_Train.mean())
            den+= (X_Train[i]-X_Train.mean())**2
        self.m = num/den
        self.b = Y_Train.mean() - (self.m*X_Train.mean())
    def predict(self,X_Test):
        return self.m*X_Test + self.b

data = pd.read_csv("placement.csv")
X = data.iloc[:,0].values
Y = data.iloc[:,1].values
X_Train,X_Test,Y_Train,Y_Test = train_test_split(X,Y,test_size=0.2,random_state=2)
Linear = LR()
Linear.fit(X_Train,Y_Train)
userInput = int(input("Enter Your CGPA :"))
if userInput <=10:
    print(Linear.predict(userInput))
else:
    print("Please! No SGPA Above 10")
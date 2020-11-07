import pandas
import os
import time
from sklearn.linear_model import LinearRegression
    
def prediction():
    print("Predict Salary vs Number of Years \n \n")
    dataset=pandas.read_csv('machine_learning/Salary_Data.csv')
    y=dataset['Salary']
    x=dataset['YearsExperience']
    x=x.values
    x=x.reshape(-1,1)
    print("Fitting the Model")
    time.sleep(1)
    model=LinearRegression()
    model.fit(x,y)
    print("Model fitting is done.... \n \n")
    time.sleep(1)
    exp=input('Enter the Number of Years :-   ')
    print('Predicted Salary is :-  ', end='')
    print(model.predict([[float(exp)]]))
    input("\n \n Task Completed, press Enter To Continue")



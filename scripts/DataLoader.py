import pandas as pd
import sklearn.model_selection as sk


class DataLoader:
    def __init__(self, path):
        self.path=path


    def load(self):
        return pd.read_csv(self.path)


    def split_data_x_y(self):
        df=self.load()
        df['gender'] = df['gender'].replace({'Male': 1, 'Female': 0})
        df['partner']=df['partner'].replace({'Yes': 1, 'No': 0})
        df['OnlineSecurity'] = df['OnlineSecurity'].replace({'Yes': 1, 'No': 0, 'No internet service': 0})
        
        df[]
        X=df.drop(columns=['customerID', 'Churn']) #
        Y=df['Churn']
        return X,Y


    def set_train_test_split(self,X,Y): #testowe i treningowe zbiory
        pass









import pandas as pd
import sklearn.model_selection as sk
from config.config import PATH


class DataLoader:
    def __init__(self):
        self.path=PATH

    def load(self):
        df_tmp = pd.read_csv(self.path)
        df_tmp['TotalCharges'] = pd.to_numeric(df_tmp['TotalCharges'], errors='coerce')
        df_tmp = df_tmp.dropna()
        df = df_tmp.drop(columns=['customerID'])
        return df

    def split_data_x_y(self): #split data and change for 0 and 1
        df=self.load()
        x=df.drop(columns=['Churn'])
        y=df['Churn']
        return x,y

    def set_train_test_split(self): #test and train sets
        x,y=self.split_data_x_y()
        x_train,x_test,y_train,y_test=sk.train_test_split(x,y,test_size=0.2)
        return x_train,x_test,y_train,y_test

    def get_columns(self, x_train):
        return list(x_train.columns)












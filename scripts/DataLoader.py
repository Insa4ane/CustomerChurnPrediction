import pandas as pd
import sklearn.model_selection as sk


class DataLoader:
    def __init__(self, path):
        self.path=path

    def load(self):
        df_tmp = pd.read_csv(self.path)
        df_tmp['TotalCharges'] = pd.to_numeric(df_tmp['TotalCharges'], errors='coerce')
        df_tmp = df_tmp.dropna()
        df_tmp = df_tmp.drop(columns=['customerID'])
        df = pd.get_dummies(df_tmp, drop_first=True, dtype=int)
        return df

    def split_data_x_y(self): #split data and change for 0 and 1
        df=self.load()
        x=df.drop(columns=['Churn_Yes'])
        y=df['Churn_Yes']
        return x,y


    def set_train_test_split(self): #testowe i treningowe zbiory
        x,y=self.split_data_x_y()
        x_train,x_test,y_train,y_test=sk.train_test_split(x,y,test_size=0.2)
        return x_train,x_test,y_train,y_test









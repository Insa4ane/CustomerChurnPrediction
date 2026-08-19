import joblib
import pandas as pd
import sklearn.model_selection as sk
import os


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

    def set_train_test_split(self): #test and train sets
        x,y=self.split_data_x_y()
        x_train,x_test,y_train,y_test=sk.train_test_split(x,y,test_size=0.2)
        return x_train,x_test,y_train,y_test

    def get_columns(self, x_train):
        return list(x_train.columns)

    def save_columns(self, x_train):
        columns=self.get_columns(x_train)
        try:
            os.makedirs("models", exist_ok=True) #os.mkdir -> we get an error when folder exist
            joblib.dump(columns,"columns/columns.joblib")
            return "Success Saved Columns"

        except Exception as e:
            return f"Error: saving columns: {e}"











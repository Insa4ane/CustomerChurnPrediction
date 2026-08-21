import joblib
import os
from sklearn.ensemble import  RandomForestClassifier
from sklearn.metrics import accuracy_score
from pathlib import Path
import pandas as pd


class ModelAgent:
    def __init__(self):
        self.model=RandomForestClassifier(n_estimators=100,random_state=42, class_weight='balanced', max_depth=10)


    def predict(self, x_test):
        predictions=self.model.predict(x_test)
        return predictions

    def train(self, x_train, y_train):
        self.model.fit(x_train, y_train)

    def evaluate(self, y_test, predictions): #
        score=accuracy_score(y_test,predictions)
        return score

    def save_model(self, agent):
        try:
            os.makedirs("models", exist_ok=True)
            joblib.dump(agent, "models/model.joblib")
            return "Model Saved"
        except Exception as e:
            return f"Error: saving model: {e}"


    def run(self, loader, agent):
        x_train, x_test, y_train, y_test = loader.set_train_test_split()
        agent.train(x_train, y_train)
        predictions = agent.predict(x_test)
        score = agent.evaluate(y_test, predictions)
        try:
            os.makedirs("model", exist_ok=True)
            joblib.dump(agent, "model/model.joblib")
            os.makedirs("columns", exist_ok=True)
            joblib.dump(list(x_train.columns), "columns/columns.joblib")
            return score
        except Exception as e:
            return f"Error: saving model: {e}"















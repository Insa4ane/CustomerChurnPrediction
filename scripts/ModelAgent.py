import joblib
import os
from sklearn.metrics import accuracy_score
from config.config import CHURN_MODEL_PIPELINE
from config.config import MODEL
from config.config import COLUMNS_TYPES


class ModelAgent:
    def __init__(self):
        self.model = CHURN_MODEL_PIPELINE

    def predict(self, x_test):
        return self.model.predict(x_test)

    def train(self, x_train, y_train):
        self.model.fit(x_train, y_train)

    def evaluate(self, y_test, predictions):
        return accuracy_score(y_test, predictions)

    def run(self, loader):
        x_train, x_test, y_train, y_test = loader.set_train_test_split()
        self.train(x_train, y_train)
        predictions = self.predict(x_test)
        score = self.evaluate(y_test, predictions)
        try:
            os.makedirs("model", exist_ok=True)
            joblib.dump(self.model, MODEL)

            os.makedirs("columns", exist_ok=True)
            joblib.dump(x_train.dtypes.to_dict(), COLUMNS_TYPES)
            return score
        except Exception as e:
            return f"Error: saving model: {e}"
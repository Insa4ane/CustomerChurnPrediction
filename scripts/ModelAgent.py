import joblib
from sklearn.ensemble import  RandomForestClassifier
from sklearn.metrics import accuracy_score


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
            joblib.dump(agent, "models/model.joblib")
            return "Model Saved"
        except Exception as e:
            return "we have a probelem with saving the model"
















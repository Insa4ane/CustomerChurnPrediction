import pandas as pd
from scripts.DataLoader import DataLoader
from scripts.ModelAgent import ModelAgent
import joblib



def testing_function(df):
    data=df.load()
    with open("data/file.csv","w") as f:
        pd.DataFrame(data).to_csv(f,index=False)

    print(data.head())
    print("The END of all data")

    x_train, y_train, x_test,y_test=df.set_train_test_split()
    with open("testing/train_x.csv","w") as f:
        pd.DataFrame(x_train).to_csv(f,index=False)
        print(f"here is x=> {x_train.info()}")
        print("END X")

    with open("testing/train_y.csv","w") as f:
        pd.DataFrame(y_train).to_csv(f,index=False)
        print(f"here is y=> {y_train.info()}")
        print("END Y")

def main():
    loader = DataLoader("data/WA_Fn-UseC_-Telco-Customer-Churn.csv")
    x_train, x_test, y_train, y_test = loader.set_train_test_split()
    agent = ModelAgent()
    print("Train Ranodm forestr...")
    agent.train(x_train, y_train)
    print("Exam")
    predictions = agent.predict(x_test)

    score = agent.evaluate(y_test, predictions)
    print(f"\n(Accuracy)=={score * 100:.2f}%")
    joblib.dump(agent, "models/model.joblib")
    joblib.dump(list(x_train.columns), "columns/columns.joblib")

if __name__ == "__main__":
    main()
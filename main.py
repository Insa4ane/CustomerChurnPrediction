import pandas as pd

from scripts.DataLoader import DataLoader
from scripts.ModelAgent import ModelAgent
from pathlib import Path
from frontend.frontend import Frontend
from config.config import PATH

def main():
    loader = DataLoader()
    agent = ModelAgent()
    path=Path("model/model.joblib")
    if not path.is_file():
        agent.run(loader)
    columns=pd.read_csv(PATH)
    columns=columns.drop(columns=['customerID'])
    columns=columns.drop(columns=['Churn'])
    frontend=Frontend(columns) #tworzymy obiekt frontend
    frontend.run()


if __name__ == "__main__":
    main()
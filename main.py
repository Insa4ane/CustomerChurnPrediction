import joblib
from scripts.DataLoader import DataLoader
from scripts.ModelAgent import ModelAgent
from pathlib import Path
from frontend.frontend import Frontend

def main():
    loader = DataLoader()
    agent = ModelAgent()
    path=Path("model/model.joblib")
    if not path.is_file():
        agent.run(loader, agent)
    #jesli tutaj doszlismy to znaczy ze mamy folder model oraz columns
    columns=joblib.load("columns/columns.joblib")
    column_list=list(columns) #dla upewnienia ze mamy liste
    # frontend=Frontend(column_list)


if __name__ == "__main__":
    main()
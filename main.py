import pandas as pd
from scripts.DataLoader import DataLoader



def main():
    df=DataLoader("data/WA_Fn-UseC_-Telco-Customer-Churn.csv") #tworzymy sobie obiekt
    data=df.load()

    with open("data/file.csv","w") as f:
        pd.DataFrame(data).to_csv(f,index=False)

    print(data.head())


if __name__ == "__main__":
    main()
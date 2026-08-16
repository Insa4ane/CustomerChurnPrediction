from scripts.DataLoader import DataLoader



def main():
    df=DataLoader("data/WA_Fn-UseC_-Telco-Customer-Churn.csv") #tworzymy sobie obiekt
    data=df.load()
    print(data.head())
    print(data.info())


if __name__ == "__main__":
    main()
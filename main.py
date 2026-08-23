import joblib
from scripts.DataLoader import DataLoader
from scripts.ModelAgent import ModelAgent
from pathlib import Path
from frontend.frontend import Frontend
from config.config import MODEL, COLUMNS_TYPES


def main():
    loader = DataLoader()
    agent = ModelAgent()
    path=Path(MODEL)
    if not path.is_file():
        agent.run(loader)
    columns_with_types=joblib.load(COLUMNS_TYPES)
    frontend=Frontend(columns_with_types)
    frontend.run()


if __name__ == "__main__":
    main()
import logging
from scripts.DataLoader import DataLoader
from scripts.ModelAgent import ModelAgent
from pathlib import Path
from config.config import MODEL


def train_model():
    try:
        loader = DataLoader()
        agent = ModelAgent()
        path=Path(MODEL)
        if not path.is_file():
            agent.run(loader)
    except Exception as e:
        logging.error(e)
        raise

if __name__ == "__main__":
    train_model()
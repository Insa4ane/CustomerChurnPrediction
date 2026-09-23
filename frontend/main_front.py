import logging
from pathlib import Path
from scripts.DataLoader import DataLoader
from scripts.ModelAgent import ModelAgent
from config.config import MODEL

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def train_model():
    try:
        path = Path(MODEL)
        if not path.is_file():
            logging.info("Training")
            loader = DataLoader()
            agent = ModelAgent()
            agent.run(loader)
            logging.info("Training has been finished.")
        else:
            logging.info(f"Model is existed")

    except Exception as e:
        logging.exception(f"Error! We cannot load/train model{e}")

if __name__ == "__main__":
    train_model()
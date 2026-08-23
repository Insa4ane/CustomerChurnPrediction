# Customer Churn Prediction App

An end-to-end machine learning application designed to predict customer churn. 

This project features a machine learning model served by a fast, asynchronous API and an interactive graphical user interface. The entire system is fully containerized using Docker for seamless deployment.

## Tech Stack

* **Machine Learning:** Python, Scikit-Learn (RandomForestClassifier, custom Pipelines, and ColumnTransformer), Pandas.
* **Backend API:** FastAPI, Uvicorn - an asynchronous server handling data and returning predictions.
* **Frontend UI:** Streamlit - an interactive web-based form for end users.
* **DevOps:** Docker, Docker Compose - environment isolation and effortless deployment.

## How to Run the Project

Thanks to containerization, launching this application requires only one command. You only need to have **Docker Desktop** installed on your machine.

1. Clone this repository and navigate to the project's root directory.
2. Open your terminal and run the following command:
   ```bash
   docker-compose up --build
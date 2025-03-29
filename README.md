# MNIST Digit Recognition Web App

**Web App**: [http://37.27.211.254:8501/](http://37.27.211.254:8501/)

## Project Overview

This project builds an end-to-end MNIST digit recognition app using PyTorch, PostgreSQL, Docker, and Streamlit. The app is deployed on a self-managed server.

### Features:
- **ML Model**: Trains a CNN using the MNIST dataset.
- **Frontend**: Built with Streamlit for interactive user input.
- **Logging**: Uses PostgreSQL for storing predictions.
- **Containerization**: Docker is used to containerize the app and PostgreSQL.
- **Deployment**: The app is deployed on a server for production.

---

## Setup Instructions

1. **Create a Virtual Environment**:
    ```bash
    python3 -m venv venv
    source venv/bin/activate
    ```

2. **Install Dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

3. **Download MNIST Dataset**:
    Set up Kaggle API token to download the dataset automatically.

4. **Train Model**:
    Train a LeNet-5 CNN model on MNIST using PyTorch and save it as `model.pth`.

5. **Frontend with Streamlit**:
    Run the Streamlit app:
    ```bash
    streamlit run app.py
    ```

6. **PostgreSQL Logging**:
    Install PostgreSQL: Optionally containerize with Docker.

    Create Database:
    ```sql
    CREATE DATABASE prediction_log;
    \c prediction_log
    CREATE TABLE predictions (
        id SERIAL PRIMARY KEY,
        timestamp TIMESTAMP NOT NULL,
        predicted_digit INT NOT NULL,
        true_label INT
    );
    ```

7. **Dockerize the App**:
    Build the Docker image:
    ```bash
    docker build -t my_ml_app .
    ```
    Run the container:
    ```bash
    docker run -d -p 8501:8501 my_ml_app
    ```

---

## Deployment

Access the app on: [http://37.27.211.254:8501/](http://37.27.211.254:8501/)

---

## Conclusion

This project demonstrates the integration of machine learning with web deployment, logging, and containerization. The app serves as a real-world example for training and deploying models in production environments.

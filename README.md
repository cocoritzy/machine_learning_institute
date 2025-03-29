# MNIST Digit Recognition Web App

**Web App**: [http://37.27.211.254:8501/](http://37.27.211.254:8501/)

## Project Overview

This project builds an end-to-end MNIST digit recognition app using PyTorch, PostgreSQL, Docker, and Streamlit. The app is deployed on a self-managed server.

### Features:
- **ML Model**: Trains a CNN using the MNIST dataset.
- **Frontend**: Built with Streamlit for interactive user input.
- **Logging**: Uses PostgreSQL for storing predictions.
- **Containerization**: Docker is used to containerize the app, the ML model and PostgreSQL.
- **Deployment**: The app is deployed on a server for production .

---

## Architecture
    
1. **Train Model**:
    Train a LeNet-5 CNN model on MNIST using PyTorch and save it as `model.pth`.

2. **Frontend with Streamlit**:

3. **PostgreSQL Logging**:
    Install PostgreSQL: Optionally containerize with Docker.

4. **Dockerize the App**:
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

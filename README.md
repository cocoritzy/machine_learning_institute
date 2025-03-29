this project aims at building a small, end-to-end application on a self-managed server is one of the best ways to prepare for our programme.
- create a virtual environemnt 
i have dowloaded the data on my computer - # downloading the MNIST dataset from Kaggle  with an API keys 
- create the ML model - using a CNN - LeNet-5
1- Train a Pytorch Model
- retreive the data set from kaggle ( set API new token)
2- design a front end with streamlit 
3- Logging with PostgreSQL
4- Containerization with Docker
5- Deployment


tensorflow 
Define your model: Using Sequential() and adding layers like Conv2D, MaxPooling2D, etc.

Compile the model: Set the optimizer, loss function, and metrics.

Train the model: Use .fit() with the training data and labels.

Evaluate the model: Use .evaluate() to test the model on unseen data (test set).

Save the model: Save the trained model for later use.



pytorch - 
Install PyTorch and Dependencies
- One of the great things about PyTorch (and TorchVision specifically) is that it has built-in functionality to download and load datasets like MNIST automatically. You don't need to download the data manually from Kaggle or any other source.
Training: You teach the robot by showing it examples of numbers and telling it when it’s wrong.

Testing: You check how well the robot can guess new numbers it hasn’t seen before.

Loss: This is how we measure how wrong the robot is. The goal is to make the loss smaller by learning from mistakes.

Accuracy: This tells us how well the robot is doing at recognizing numbers.


Define a model (SimpleModel).

Train it on the MNIST dataset.

Save the trained model’s parameters to a file called 'model.pth'



Install PostgreSQL on your local computer (if you haven’t already).

Update the database connection details in the code to point to your local PostgreSQL instance.

Create a PostgreSQL database on your local system and update the connection parameters accordingly.


docker 
- install docker  - brew install --cask docker
Why Use Docker for PostgreSQL?
If you want to run PostgreSQL locally but without the hassle of installing it on your machine, Docker is a great solution because:

It isolates PostgreSQL in its own container, so you don’t have to worry about conflicts with other applications on your system.

It is easy to manage: Starting, stopping, or removing the PostgreSQL instance is simple with Docker commands.

Portability: Once your PostgreSQL is containerized, you can easily move it between environments or deploy it to production, ensuring consistency.

- i need to install Docker daemon
Containers are an isolated environment to run any code. Select the container, and go to the Files tab to see what's in it.
docker pull postgres - pull the official PostgreSQL image

start a PostgreSQL container - docker run --name my_postgres -e POSTGRES_PASSWORD=mysecretpassword -d postgres

start an sql query - docker exec -it my_postgres psql -U postgres


create the database - -- Step 1: Create the database
CREATE DATABASE prediction_log;

-- Step 2: Switch to the newly created database
\c prediction_log

-- Step 3: Create the predictions table
CREATE TABLE predictions (
    id SERIAL PRIMARY KEY,
    timestamp TIMESTAMP NOT NULL,
    predicted_digit INT NOT NULL,
    true_label INT
);

\dt - to list all the table 



connecting the app with the data base - Ensure PostgreSQL Server is Running, Confirm that the container is running and accessible at localhost:5432
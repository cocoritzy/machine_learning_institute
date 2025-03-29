# downloading the MNIST dataset from Kaggle 
import os
import kaggle #Kaggle’s API for downloading datasets.

# Dataset details
dataset = 'hojjatk/mnist-dataset'

# Define where to store the dataset
dataset_dir = './mnist'  # This is the folder where your dataset will be stored

# Download the dataset
os.makedirs(dataset_dir, exist_ok=True)
kaggle.api.dataset_download_files(dataset, path=dataset_dir, unzip=True)



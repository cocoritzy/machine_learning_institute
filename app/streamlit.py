import streamlit as st
import torch
import torch.nn as nn
import numpy as np
import psycopg2  # PostgreSQL adapter
import pandas as pd
from PIL import Image
from torchvision import transforms
from datetime import datetime
from streamlit_drawable_canvas import st_canvas
import os

def create_connection():
    conn = psycopg2.connect(
        host=os.getenv("DATABASE_HOST", "localhost"),
        port=os.getenv("DATABASE_PORT", "5432"),
        user=os.getenv("DATABASE_USER", "postgres"),
        password=os.getenv("DATABASE_PASSWORD", "mysecretpassword"),
        dbname=os.getenv("DATABASE_NAME", "prediction_log")
    )
    return conn

# Insert a new prediction log only when the user provides a true label
def log_prediction(predicted_digit, true_label):
    timestamp = datetime.now()  # Get current timestamp when user enters the correct label
    conn = create_connection()
    cur = conn.cursor()
    cur.execute(
        "INSERT INTO predictions (timestamp, predicted_digit, true_label) VALUES (%s, %s, %s);",
        (timestamp, predicted_digit, true_label)
    )
    conn.commit()
    cur.close()
    conn.close()

# Fetch logged predictions (only 3 columns)
def get_predictions():
    conn = create_connection()
    cur = conn.cursor()
    cur.execute("SELECT timestamp, predicted_digit, true_label FROM predictions ORDER BY timestamp DESC LIMIT 10;")
    data = cur.fetchall()
    cur.close()
    conn.close()
    return data


# Define the model structure
class SimpleModel(nn.Module):
    def __init__(self):
        super(SimpleModel, self).__init__()
        self.conv_layers = nn.Sequential(
            nn.Conv2d(1, 32, kernel_size=3),
            nn.ReLU(),
            nn.Conv2d(32, 64, kernel_size=3),
            nn.ReLU(),
            nn.Conv2d(64, 64, kernel_size=3),
            nn.ReLU()
        )
        self.fc_layers = nn.Sequential(
            nn.Flatten(),
            nn.Linear(64 * 22 * 22, 10)
        )

    def forward(self, x):
        x = self.conv_layers(x)
        x = self.fc_layers(x)
        return x

# Load the model
model = SimpleModel()
model.load_state_dict(torch.load('model.pth'))
model.eval()

# Streamlit app UI
st.title("🖌️ Draw a Digit and Let the Model Predict!")

# Canvas for drawing
canvas_result = st_canvas(
    fill_color="black",
    stroke_width=10,
    stroke_color="white",
    background_color="black",
    width=280,
    height=280,
    drawing_mode="freedraw",
    key="canvas",
)

# Preprocessing function
def preprocess_image(img):
    pil_img = Image.fromarray(img).convert("L").resize((28, 28))
    img_tensor = transforms.ToTensor()(pil_img).unsqueeze(0)
    return img_tensor

# Prediction logic
if canvas_result.image_data is not None:
    img_data = canvas_result.image_data
    img = np.array(img_data, dtype=np.uint8)
    
    if np.sum(img) > 0:  # If something is drawn
        img = preprocess_image(img)
        with torch.no_grad():
            output = model(img)
            probabilities = torch.nn.functional.softmax(output, dim=1)
            confidence = torch.max(probabilities).item()
            _, predicted_label = torch.max(output, 1)

        # Display prediction
        st.write(f"**Predicted Digit: {predicted_label.item()}**")
        st.write(f"**Confidence: {confidence * 100:.2f}%**")

        # User feedback
        true_label = st.text_input("Enter the correct digit (if the model's prediction is wrong):", "")

        if st.button("Log Correct Label"):
            if true_label.isdigit():
                true_label = int(true_label)
                st.write("✅ Thank you for your feedback! Logging the data now.")
                log_prediction(predicted_label.item(), true_label)  # Log prediction only when user confirms
            else:
                st.write("⚠️ Please enter a valid digit.")

# Display logged predictions
st.subheader("📜 Prediction History")

# Fetch and display predictions from the database
data = get_predictions()

if data:
    # Convert data into a DataFrame for a cleaner table
    df = pd.DataFrame(data, columns=["Timestamp", "Predicted Digit", "True Label"])
    st.table(df)
else:
    st.write("No predictions logged yet.")



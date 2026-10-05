# 🌱 AgriSense

<p align="center">
  <img src="assets/agrisense-agriculture.gif" alt="AgriSense animated agriculture banner" width="100%">
</p>

<p align="center">
  <b>Smart crop recommendations powered by machine learning.</b><br>
  Turn soil and environmental conditions into a practical crop recommendation.
</p>

<p align="center">
  <a href="https://github.com/anuroy15052005/AgriSense">
    <img src="https://img.shields.io/badge/GitHub-AgriSense-181717?style=for-the-badge&logo=github" alt="GitHub">
  </a>
  <img src="https://img.shields.io/badge/Python-3.12-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python">
  <img src="https://img.shields.io/badge/Flask-3.1-000000?style=for-the-badge&logo=flask&logoColor=white" alt="Flask">
  <img src="https://img.shields.io/badge/Docker-Ready-2496ED?style=for-the-badge&logo=docker&logoColor=white" alt="Docker">
  <img src="https://img.shields.io/badge/Scikit--Learn-1.6.1-F7931E?style=for-the-badge&logo=scikit-learn&logoColor=white" alt="Scikit-learn">
</p>

---

## 🌾 What is AgriSense?

**AgriSense** is an end-to-end machine learning application that recommends a suitable crop from soil and environmental conditions.

Instead of stopping at a notebook, the project takes the model all the way to a usable web application:

**data analysis → model training → validation → Flask API → web interface → Docker → cloud deployment**

The application uses seven inputs:

- **Nitrogen (N)**
- **Phosphorus (P)**
- **Potassium (K)**
- **Temperature**
- **Humidity**
- **Soil pH**
- **Rainfall**

The trained Random Forest model then predicts the most suitable crop from **22 crop classes**.

> **Note:** The model's reported accuracy is based on the dataset used for this project. It should not be treated as a substitute for professional agricultural advice or field-specific agronomic testing.

---

## 🚀 Live Demo

**AgriSense is deployed on Render.**

👉 **[Open the live application](YOUR_RENDER_URL_HERE)**

> Replace `YOUR_RENDER_URL_HERE` with your actual Render URL.

---

## ✨ Highlights

| | What AgriSense does |
|---|---|
| 🌱 | Recommends crops from 22 classes |
| 🤖 | Uses a tuned Random Forest classifier |
| 📊 | Includes EDA, correlation and outlier analysis |
| 🔄 | Evaluates models using 5-Fold Cross-Validation |
| 🎯 | Performs hyperparameter tuning |
| 🧪 | Includes feature ablation experiments |
| 🌐 | Provides a Flask prediction API |
| 💻 | Includes a browser-based frontend |
| 🐳 | Runs inside Docker |
| ☁️ | Deployed as a live web service |

---

## 🧠 Machine Learning Pipeline

```text
                    Crop Recommendation Dataset
                                │
                                ▼
                     ┌─────────────────────┐
                     │   Data Exploration  │
                     │  Cleaning & Analysis│
                     └──────────┬──────────┘
                                │
                                ▼
                     ┌─────────────────────┐
                     │ Feature Analysis    │
                     │ Correlation/Outlier │
                     └──────────┬──────────┘
                                │
                                ▼
                     ┌─────────────────────┐
                     │ Model Comparison    │
                     │ 5-Fold CV           │
                     └──────────┬──────────┘
                                │
                                ▼
                     ┌─────────────────────┐
                     │ Random Forest       │
                     │ Hyperparameter Tune │
                     └──────────┬──────────┘
                                │
                                ▼
                     ┌─────────────────────┐
                     │ Saved ML Model      │
                     │ .pkl                │
                     └──────────┬──────────┘
                                │
                                ▼
                 ┌────────────────────────────┐
                 │       Flask REST API       │
                 └─────────────┬──────────────┘
                               │
                               ▼
                    🌾 Recommended Crop
```

---

## 📊 Model Performance

The final Random Forest model was evaluated using cross-validation and a separate test set.

| Metric | Result |
|---|---:|
| Best 5-Fold CV Accuracy | **99.60%** |
| Final Test Accuracy | **99.55%** |

### Best Hyperparameters

```text
n_estimators      = 200
max_depth         = None
min_samples_leaf  = 1
min_samples_split = 5
```

### Cross-Validation

The model was evaluated across five folds rather than relying on a single split. This helped check whether the model was consistently performing well across different subsets of the training data.

---

## 🔬 Feature Analysis

Feature importance and ablation experiments were used to understand how the model was making use of the available inputs.

### Feature Importance

The model identified the following features as particularly influential:

```text
Rainfall       0.220753
Humidity       0.220182
K              0.178327
P              0.148808
N              0.106676
Temperature    0.074563
pH             0.050691
```

### Feature Ablation

| Feature Set | CV Accuracy |
|---|---:|
| All features | **99.60%** |
| Without pH | 99.32% |
| Core features | 99.03% |

The experiments showed that keeping all seven features produced the strongest validation result on this dataset.

---

## 🌾 Supported Crops

AgriSense currently supports recommendations for:

`Apple` · `Banana` · `Blackgram` · `Chickpea` · `Coconut` · `Coffee`

`Cotton` · `Grapes` · `Jute` · `Kidney Beans` · `Lentil` · `Maize`

`Mango` · `Moth Beans` · `Mung Bean` · `Muskmelon` · `Orange` · `Papaya`

`Pigeon Peas` · `Pomegranate` · `Rice` · `Watermelon`

---

## 🏗️ Application Architecture

```text
┌─────────────────────┐
│       Browser       │
│   HTML/CSS/JS UI    │
└──────────┬──────────┘
           │
           │ POST /predict
           ▼
┌─────────────────────┐
│      Flask API      │
│     backend/main.py │
└──────────┬──────────┘
           │
           ▼
┌─────────────────────┐
│   Input Validation  │
│     schemas.py      │
└──────────┬──────────┘
           │
           ▼
┌─────────────────────┐
│  Prediction Layer   │
│   prediction.py     │
└──────────┬──────────┘
           │
           ▼
┌─────────────────────┐
│  Random Forest      │
│  crop_model.pkl     │
└──────────┬──────────┘
           │
           ▼
      🌱 Crop Result
```

---

## 🛠️ Tech Stack

### Machine Learning
- Python
- Pandas
- Scikit-learn
- Joblib
- Jupyter Notebook

### Backend
- Flask
- REST API
- Gunicorn

### Frontend
- HTML
- CSS
- JavaScript

### Deployment
- Docker
- Render
- GitHub

---

## 📁 Project Structure

```text
AgriSense/
│
├── backend/
│   ├── __init__.py
│   ├── main.py
│   ├── prediction.py
│   └── schemas.py
│
├── data/
│   └── Crop_recommendation.csv
│
├── frontend/
│   ├── index.html
│   ├── script.js
│   └── style.css
│
├── models/
│   └── crop_recommendation_model.pkl
│
├── notebooks/
│   └── crop_eda.ipynb
│
├── assets/
│   └── agrisense-agriculture.gif
│
├── app.py
├── train_model.py
├── requirements.txt
├── Dockerfile
├── .dockerignore
├── .gitignore
├── LICENSE
└── README.md
```

---

## ⚙️ Run Locally

### 1. Clone the repository

```bash
git clone https://github.com/anuroy15052005/AgriSense.git
cd AgriSense
```

### 2. Create a virtual environment

#### Windows

```bash
python -m venv venv
venv\Scripts\activate
```

#### macOS / Linux

```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the application

```bash
python app.py
```

Open:

```text
http://127.0.0.1:5000
```

---

## 🐳 Run with Docker

Make sure Docker Desktop is running.

### Build the image

```bash
docker build -t agrisense .
```

### Start the container

```bash
docker run -p 5000:5000 agrisense
```

Then open:

```text
http://localhost:5000
```

The production container uses **Gunicorn** and binds to the port provided through the `PORT` environment variable.

---

## 🔌 API

AgriSense exposes a prediction endpoint:

```http
POST /predict
```

### Request

```json
{
  "N": 90,
  "P": 42,
  "K": 43,
  "temperature": 20,
  "humidity": 80,
  "ph": 6.5,
  "rainfall": 200
}
```

### Response

```json
{
  "crop": "rice"
}
```

The API also validates incoming values and returns an appropriate error response when the request is missing or invalid.

---

## 🧪 Example

### Input

```text
N            = 90
P            = 42
K            = 43
Temperature  = 20°C
Humidity     = 80%
pH           = 6.5
Rainfall     = 200 mm
```

### Prediction

```text
🌾 Recommended Crop: Rice
```

---

## 🔮 What I Want to Improve Next

AgriSense is a working end-to-end system, but there is plenty of room to make it more useful in real agricultural settings.

Possible next steps include:

- 🌦️ Real-time weather integration
- 📍 Location-aware recommendations
- 🧪 Fertilizer recommendations
- 📈 Prediction confidence scores
- 🌱 Crop-specific cultivation guidance
- 🌐 Multilingual support
- 📱 Better mobile experience
- 📊 Larger and more diverse agricultural datasets
- 🧑‍🌾 Field-level recommendations using real-world soil data

---

## 💡 Why I Built This

I wanted this project to be more than a model with a high accuracy score.

The goal was to understand what it takes to turn a machine learning experiment into a complete application — from exploring the data and evaluating the model to building an API, connecting a frontend, containerizing the application, and deploying it online.

AgriSense is my practical implementation of that complete workflow.

---

## 👨‍💻 Author

### Anu Kumar

**B.Tech Computer Science — Data Science**

[GitHub](https://github.com/anuroy15052005) ·
[LinkedIn](https://www.linkedin.com/in/anu-kumar-b837a5401/)

---

<p align="center">
  <b>🌱 Data → Intelligence → Better Crop Decisions</b>
</p>

<p align="center">
  Built with Python, Machine Learning, Flask and Docker.
</p>

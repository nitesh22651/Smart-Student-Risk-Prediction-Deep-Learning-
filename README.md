<h1 align="center">
    Student Dropout Predictor
</h1>

<p>
    A machine learning application designed to predict the likelihood that a student may drop a course, based on academic performance, engagement metrics, and behavioral indicators. The system provides a dropout confidence score that can help institutions or educators identify at-risk students early.
</p>

## Overview

This project implements a complete machine learning pipeline for student dropout prediction. It includes:

* Data preprocessing using an sklearn ColumnTransformer with imputation and MinMax scaling
* Model training using both classical machine learning algorithms and a residual neural network
* A FastAPI backend that exposes a prediction endpoint
* Dockerized deployment for production use
* A scalable, modular codebase suitable for integration into larger systems

## Machine Learning Algorithms Used

The project experiments with and compares multiple algorithms:

1. **Random Forest Regressor**
   Applied during early prototyping as part of a GridSearchCV hyperparameter tuning stage.

2. **Support Vector Regressor (SVR)**
   Evaluated using GridSearchCV for baseline modeling comparisons.

3. **Residual Neural Network (ResNet-style MLP)**
   Final production model implemented in TensorFlow/Keras.
   This model includes:

   * Dense layers with batch normalization
   * Residual skip connections
   * Dropout and L2 regularization
   * MinMax-scaled numerical inputs

The final deployed model is the ResNet-style neural network saved as a `.keras` file.

## Dataset Used

The training data is sourced from the publicly available Kaggle dataset:

Dataset link:
[Dataset](https://www.kaggle.com/datasets/mahmoudelhemaly/students-grading-dataset)

This dataset includes student academic performance metrics such as attendance percentage, assignment completion rate, quiz scores, study time, stress level, and extracurricular involvement.
A target feature named `dropout_confidense` was engineered to represent the estimated probability of dropout.

## Tech Stack

| Component       | Technology Used                |
| --------------- | ------------------------------ |
| Language        | Python                         |
| ML Models       | Scikit-learn, TensorFlow/Keras |
| Web Framework   | FastAPI                        |
| Deployment      | Docker                         |
| Data Processing | Pandas, NumPy, Scikit-learn    |

## How to Run the Project

### Clone the Repository
```bash
git clone git@github.com:PradyumnaCharate/student-risk-prediction.git
```

### Navigate to Project Directory

```bash
cd student-risk-prediction
```

### Create a Python Virtual Environment

> **Required Python version:** `3.12.3`

#### For Windows:

```bash
python -m venv venv
venv\Scripts\activate
```

#### For macOS:

```bash
python3 -m venv venv
source venv/bin/activate
```

#### For Linux:

```bash
python3 -m venv venv
source venv/bin/activate
```

### Install Required Dependencies

```bash
pip install -r requirements.txt
```

### Start the Application

```bash
python server.py
```

Your Detector app should now be up and running 🎉

## Run with Docker

### Build the docker image of Project
```bash
docker build -t universe/student-risk-prediction .
```

### Run the docker container with env file
```
docker run -d \
    -p 8000:8000 \
    --name student-risk-prediction \
    universe/student-risk-prediction
``` 

<br/>
<br/>
<br/>
<p align="center">
    Made with ❤️
</p>

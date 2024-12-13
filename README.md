# Trajectory-Based-Anomaly-Detection-in-Marine-Vessels

This repository contains the implementation of an integrated machine learning framework designed for detecting and classifying maritime anomalies using Automatic Identification System (AIS) data. The framework aims to enhance maritime surveillance capabilities by identifying unauthorized activities, such as illegal fishing, smuggling, and navigational deviations, which pose threats to maritime security and the marine ecosystem.

## Table of Contents

1. [Introduction](#introduction)
2. [Features](#features)
3. [Technologies Used](#technologies-used)
4. [Data Preprocessing](#data-preprocessing)
5. [Models and Methodology](#models-and-methodology)
6. [Results](#results)
7. [Usage](#usage)
8. [Contributing](#contributing)
9. [License](#license)

---

## Introduction

The exponential growth of maritime traffic has increased the risk of anomalous activities, such as unauthorized zone entry, illegal fishing, and smuggling. This project leverages machine learning techniques for real-time detection and classification of such anomalies using AIS data. By integrating clustering (DBSCAN), regression (SVR), and classification (Logistic Regression) models, this framework provides actionable insights to enhance maritime operations.

---

## Features

- **Real-Time Anomaly Detection**: Identifies vessels displaying unusual trajectories or behaviors.
- **Categorical Classification**: Classifies anomalies into actionable categories like unauthorized zone entry or suspicious idling.
- **Improved Surveillance**: Enhances regulatory compliance and environmental protection.

---

## Technologies Used

- **Programming Language**: Python
- **Libraries**:
  - Pandas
  - NumPy
  - scikit-learn
  - Matplotlib
  - Seaborn
- **Machine Learning Models**:
  - DBSCAN (Density-Based Spatial Clustering of Applications with Noise)
  - Support Vector Regression (SVR)
  - Logistic Regression

---

## Data Preprocessing

AIS data includes critical attributes such as latitude, longitude, speed over ground (SOG), and course over ground (COG). The preprocessing pipeline involves:

1. **Data Cleaning**: Handling missing and inconsistent values.
2. **Normalization**: Scaling data to improve model performance.
3. **Feature Engineering**: Generating additional features to enhance prediction accuracy.

---

## Models and Methodology

1. **DBSCAN**:

   - Clusters typical maritime routes.
   - Identifies outliers that may indicate anomalous behavior.
   - Achieved a silhouette score of **0.78**.

2. **Support Vector Regression (SVR)**:

   - Predicts expected vessel trajectories.
   - Identifies deviations indicative of anomalies.

3. **Logistic Regression**:

   - Classifies anomalies into actionable categories, such as unauthorized zone entries and suspicious idling.
   - Achieved a classification accuracy of **91%**.

---

## Results


### Run the Project

   ```bash
   python app.py
   ```

For any questions or suggestions, feel free to reach out via [vspatil0001@gmail.com].

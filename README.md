# Trajectory-Based-Anomaly-Detection-in-Marine-Vessels

This repository contains the implementation of an integrated machine learning framework designed for detecting and classifying maritime anomalies using Automatic Identification System (AIS) data. The framework aims to enhance maritime surveillance capabilities by identifying unauthorized activities, such as illegal fishing, smuggling, and navigational deviations, which pose threats to maritime security and the marine ecosystem.

## Table of Contents

1. [Introduction](#introduction)
2. [Features](#features)
3. [Technologies Used](#technologies-used)
4. [Data Preprocessing](#data-preprocessing)
5. [Models and Methodology](#models-and-methodology)
6. [Results](#results)
---

## Introduction

The exponential growth of maritime traffic has increased the risk of anomalous activities, such as unauthorized zone entry, illegal fishing, and smuggling. This project leverages machine learning techniques for real-time detection and classification of such anomalies using AIS data. By integrating clustering (DBSCAN), regression (SVR), and classification (Logistic Regression) models, this framework provides actionable insights to enhance maritime operations.

### Networking Knowledge, DSA Concepts, and SQLite/Flask Usage in Project:

#### **Networking-Related Knowledge**
1. **Automatic Identification System (AIS):**
   - AIS data represents a real-world application of maritime networking. It tracks vessel positions, speeds, and movements, forming the basis of your anomaly detection.
   - The project involves understanding geospatial data (latitude, longitude), which is crucial in networking contexts like routing, GPS systems, and IoT networks.

2. **Client-Server Communication:**
   - Flask's role as a web framework enables client-server interactions, where user requests (via forms or APIs) are processed on the server-side to generate predictions or handle user data.

3. **Web Routing:**
   - Routes like `/register`, `/login`, and `/predict` implement HTTP communication patterns (GET and POST methods) common in web development.

---

#### **Data Structures and Algorithms (DSA) Concepts**
1. **Feature Engineering:**
   - Utilizes arrays (via NumPy) to process and organize AIS data, incorporating derived attributes such as speed and course deltas.
   - PCA (Principal Component Analysis) is an optimization algorithm that reduces data dimensionality, enhancing efficiency for large datasets.

2. **Clustering Algorithms:**
   - DBSCAN (Density-Based Spatial Clustering of Applications with Noise) groups data points based on density, employing graph traversal concepts to identify connected regions.

3. **Classification Algorithms:**
   - Logistic Regression and SVR (Support Vector Regression) apply mathematical optimization and linear algebra to predict and classify anomalies.

4. **Hashing for Security:**
   - Passwords are hashed using bcrypt, a secure cryptographic algorithm, before being stored in the database.

---

#### **SQLite Database with Flask**
1. **Database Integration:**
   - SQLite is a lightweight relational database used for managing user and contact information, as defined in the `User` and `Contact` models in your code.

2. **SQLAlchemy ORM:**
   - SQLAlchemy handles object-relational mapping (ORM), allowing Python classes (`User`, `Contact`) to interact seamlessly with the SQLite database without writing raw SQL queries.

3. **Session Management:**
   - Flask session management enables secure, temporary storage of user credentials (e.g., email) during active logins, ensuring restricted access to user-specific data like the dashboard.

4. **CRUD Operations:**
   - `db.session.add` and `db.session.commit` represent Create operations.
   - Queries such as `User.query.filter_by(email=email).first()` implement Read operations.
   - These are fundamental database operations, integral to web development.
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
   - Identifies deviations indicative of anomalies and gives accuracy of **98%**.

3. **Logistic Regression**:

   - Classifies anomalies into actionable categories, such as unauthorized zone entries and suspicious idling.
   - Achieved a classification accuracy of **90%**.
---

## Results

![Screenshot (884)](https://github.com/user-attachments/assets/7a83d758-4cf0-429b-aaa3-98162face7d8)
![Screenshot (885)](https://github.com/user-attachments/assets/ea762461-8b5a-4c8e-ba9c-f472b0e8fa9f)
![Screenshot (886)](https://github.com/user-attachments/assets/3e5d8e02-4e53-4596-b63d-3a168a94dbe0)
![Screenshot (888)](https://github.com/user-attachments/assets/1c293c0b-ca5b-476c-a753-79b9a1c51aa7)
![image](https://github.com/user-attachments/assets/df1910c8-2b83-4c34-8a0c-3f36fd370838)
![Screenshot (890)](https://github.com/user-attachments/assets/28dea210-50ea-4349-acf1-a77ca34774a0)
![Screenshot (891)](https://github.com/user-attachments/assets/d8e33432-0a8a-4b41-9a8a-5570fe7cc52f)
![Screenshot (893)](https://github.com/user-attachments/assets/8c6be3fc-2f48-4cc3-8f44-93c1acca8ed4)
![image](https://github.com/user-attachments/assets/4b208c9c-4114-415c-9b7c-2241e4619484)
![image](https://github.com/user-attachments/assets/cc4b00fb-f890-4c8c-bb31-6686ef6443e4)
![image](https://github.com/user-attachments/assets/53c4293f-e46d-466e-ad30-54dfceb4729d)
![image](https://github.com/user-attachments/assets/d25b3090-2337-4970-bdba-e1972b32b8e1)
![image](https://github.com/user-attachments/assets/d79e0d00-d746-46d5-b5d2-14a7823e73d0)
![image](https://github.com/user-attachments/assets/e3c6a832-ff39-49a3-9583-a958439393dc)
![Screenshot (894)](https://github.com/user-attachments/assets/9c225e5c-2ba8-4be3-81b3-a9f1f45bdcac)



### Run the Project

   ```bash
   python app.py
   ```

For any questions or suggestions, feel free to reach out via [vspatil0001@gmail.com].

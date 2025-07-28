
# Predictive Analytics for Road Safety using Modern Web & AI Tools

This project is a complete data-driven solution to predict the **severity of road accidents** based on real-world traffic conditions. Using **machine learning (Random Forest)**, **Flask** for the web interface, and **Power BI** for visual analytics, the system helps understand and forecast accident patterns.

---

## Objectives

- Predict accident severity (Low, Moderate, High) using ML.
- Use a dynamic web interface for real-time prediction.
- Provide a data visualization dashboard for analysis and trends.

---

## Tech Stack

| Component        | Tools/Technologies         |
|------------------|----------------------------|
| Machine Learning | Python, scikit-learn, Pandas |
| Backend API      | Flask, Pickle              |
| Frontend         | HTML, CSS, Bootstrap       |
| Dashboard        | Power BI                   |

---

## Dataset Overview

- **Size**: 1000+ records (CSV format)
- **Features**: Weather, Road Type, Lighting, Time of Day, etc.
- **Target**: Accident Severity (Low, Moderate, High)

---

## Model Training

- Categorical and target columns encoded with `LabelEncoder`
- Trained using `RandomForestClassifier`
- Serialized using `pickle` for web integration

---

## Web Application

**Features:**
- Pages: Home | Predict | About
- Input: 12 dynamic traffic-related features
- Output:
  - Severity Level (Low/Moderate/High)
  - Chance of Accident (%)
  - Flag (Yes/No)

---

## Power BI Dashboard

- **Visuals Include**:
  - Monthly accident distribution
  - Road condition vs severity
  - Traffic density vs accident type
  - Used for identifying trends and improving traffic safety insights.

---

## Disclaimer
This is an academic project intended for learning and experimentation only. The predictions should not be used for real-life traffic decisions without validation by traffic safety experts.

---

## Limitations & Future Scope
   -- Works on a small dataset; can be improved with live or larger datasets.
   -- Future enhancements may include:
       * Live GPS + weather feed integration
       * Real-time severity alerts
       * Deployment on cloud platforms (AWS/GCP)

 ---

#  This project is the result of a collaborative academic effort aimed at applying real-world machine learning techniques to improve road safety through predictive analytics. It brings together data science principles, web development skills, and visualization tools into a single, deployable application.

The team has collectively worked on:
     * Data Analysis – exploring and preprocessing traffic accident data.
     * Model Building – training and evaluating a machine learning model.
     * Web Development – designing and integrating a user-friendly Flask interface.
     * Visualization – creating dashboards for insights using Power BI.
     

We hope this solution inspires others to use technology for public safety initiatives. We welcome contributions from the community! If you have ideas to improve the model, enhance the web interface, or extend dashboard capabilities, feel free to Fork this repository or open a Pull Request. 

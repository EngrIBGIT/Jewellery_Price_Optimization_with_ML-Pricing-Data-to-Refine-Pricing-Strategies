# **Jewellery_Price_Optimization_with_ML-Pricing-Data-to-Refine-Pricing-Strategies**


## **Jewelry Price Prediction - Machine Learning App**


## **Project Overview**
This project aims to predict jewelry prices using machine learning models. It leverages historical sales data, competitor pricing, and customer demographics to build an AI-driven pricing strategy. The model helps jewelry businesses optimize pricing for maximum profitability while remaining competitive.

### **Core Features**
**Single Prediction**: Enter jewelry attributes and get an estimated price.

**Bulk Predictions**: Upload CSV/Excel files for multiple predictions.

**Data Visualization**: Interactive dashboard for insights.

**Export Predictions**: Save results in CSV, Excel, PDF, and Word formats.

**User-Friendly UI**: Beautiful Streamlit interface designed for a jewelry store.

## **Problem Statement**
Gemineye Emporium, a growing jewelry business, faces pricing challenges due to rapid expansion. 

## The Key issues include:

- **Market Dynamics**: Consumer preferences and trends change frequently.

- **Competitive Pricing**: Setting prices to attract customers while maintaining profitability.

- **Cost Management**: Balancing material costs, craftsmanship, and logistics.

The goal is to develop a `machine learning` model that predicts optimal jewelry prices based on various attributes.

## **Dataset Information**

The dataset contains details about jewelry orders, including:

The following are the feature	description
- `Category`:	Type of jewelry (Necklace, Ring, etc.)
- `Brand_ID`:	Unique identifier for brands
- `Target_Gender`:	Intended gender for the jewelry
- `Main_Color`:	Primary color of the jewelry piece
- `Main_Metal`:	Main metal used (Gold, Silver, etc.)
- `Main_Gem`:	Gemstone type (Diamond, Ruby, etc.)
- `Order Month`:	Month in which the order was placed
- `Order Day`:	Day of the month when the order was placed
- `Price (Target)`:	The jewelry price in USD

## **Tech Stack**
The project is built using:

- **`Python`** 🐍

- **`Machine Learning Models`**: Catboost Regressor, Linear Regression, Extra-Trees, Decision Trees, Adaboost Regressor
  
- **`Data Preprocessing`**: Pandas, NumPy, Scikit-Learn

= **`Visualization`**: Matplotlib, Seaborn, Plotly

## **Experiment Tracking**: `MLflow`

## **Deployment**: `Streamlit, Render, GitHub`

- Machine Learning Workflow (CRISP-DM Approach)

1. Business Understanding
- Define pricing challenges for the jewelry market.

- Collaborate with stakeholders to align business goals with AI-driven pricing.

2. Data Collection & Preprocessing
- Collect historical sales data, competitor pricing, and customer demographics.

- Handle missing values, remove outliers, and encode categorical features.

3. Exploratory Data Analysis (EDA)
- Analyze seasonality, pricing trends, and consumer preferences.

- Identify key features affecting jewelry prices.

4. Feature Engineering
- Create new features to improve model accuracy.

- Scale numeric features and encode categorical variables.

5. Model Training & Evaluation
Implemented Models include :

- Linear Regression

- Decision Tree

 -Extra Trees

- AdaBoost

- CatBoost

**Evaluation Metrics**:

- Mean Absolute Error (MAE)

- Root Mean Squared Error (RMSE)

- R² Score

## **Hyperparameter Tuning using GridSearchCV for performance improvement**.

6. Experiment Tracking with MLflow
Track different models and hyperparameter tuning results.

Compare model performance and log metrics.

7. Model Deployment
Deploying the best model using Streamlit & Render.

Created an interactive UI for users to enter jewelry details and get predictions.

## **How to Run the Project Locally**
 1. Clone the Repository

- git clone [Jewelry Price Prediction](https://github.com/EngrIBGIT/Jewellery_Price_Optimization_with_ML-Pricing-Data-to-Refine-Pricing-Strategies)
- cd jewelry-price-prediction

2. Install Dependencies

- pip install -r requirements.txt

3. Run the Streamlit App

- streamlit run app.py

## Deployment on Streamlit and Render
The project is hosted on Streamlit and Render, follow these steps to deploy:

- Push the project to GitHub.

- Create a new Web Service on Render.

- Connect to GitHub repository.

- Set the following configurations:

**`Python Version: 3.9`**

Start Command: gunicorn -w 4 -k uvicorn.workers.UvicornWorker app:app

Deploy and get live URL!

**Live Demo**: Jewelry Price Prediction App

### Dashboard Features
- Upload CSV/Excel files for bulk predictions.

- Interactive Price Distribution visualization.

- Download predictions in CSV, Excel, PDF, and Word formats.

## **File Structure**

## jewelry-price-prediction/

│── app.py                # Streamlit app for UI & predictions  
│── best_model.pkl        # Saved ML model  
│── requirements.txt      # Project dependencies  
│── runtime.txt           # Python runtime version  
│── setup.sh              # Setup script for deployment  
│── Procfile              # Render deployment configuration  
│── README.md             # Project documentation


### **Explanation of Files**
1. **`app.py`**:  
   - The main Streamlit application file that handles the user interface (UI) and predictions.

2. **`best_model.pkl`**:  
   - A serialized file containing the trained machine learning model for jewelry price prediction.

3. **`requirements.txt`**:  
   - Lists all the Python dependencies required to run the project.

4. **`runtime.txt`**:  
   - Specifies the Python runtime version for deployment.

5. **`setup.sh`**:  
   - A shell script for setting up the environment during deployment.

6. **`Procfile`**:  
   - Configuration file for deploying the app on platforms like Render.

7. **`README.md`**:  
   - Documentation file that provides an overview of the project, setup instructions, and usage guidelines.

## **Insights & Recommendations**
- Leverage AI for Competitive Pricing:

- AI-based pricing helps adjust prices dynamically to market trends.

- Feature Importance Analysis:

- Jewelry category, brand, and gemstones significantly influence prices.

- Implement Customer Segmentation:

- Different pricing strategies for luxury vs. budget jewelry can optimize sales.

## Additional Resources
Notebook: [Open in Google Colab](https://colab.research.google.com/drive/15efNUBC215IPPNNHwgYZc_CNXCnlBch7?usp=sharing)

GitHub Repo: [Jewelry Price Prediction](https://github.com/EngrIBGIT/Jewellery_Price_Optimization_with_ML-Pricing-Data-to-Refine-Pricing-Strategies)

Live Demo: [Jewel Price Prediction App](https://jewelpriceprediction.streamlit.app/)

### Final Thoughts
This project demonstrates how machine learning can optimize jewelry pricing by leveraging data-driven insights.

If you found this useful, don't forget to ⭐️ Star this repository on GitHub!






















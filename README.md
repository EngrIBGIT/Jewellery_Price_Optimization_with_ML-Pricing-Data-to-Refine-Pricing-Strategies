# Jewellery_Price_Optimization_with_ML-Pricing-Data-to-Refine-Pricing-Strategies

💎 Jewelry Price Prediction - Machine Learning App
🚀 Deployed on Render | 📊 Interactive Dashboard | 📦 Bulk Predictions

📌 Project Overview
This project aims to predict jewelry prices using machine learning models. It leverages historical sales data, competitor pricing, and customer demographics to build an AI-driven pricing strategy. The model helps jewelry businesses optimize pricing for maximum profitability while remaining competitive.

✅ Core Features:

Single Prediction: Enter jewelry attributes and get an estimated price.
Bulk Predictions: Upload CSV/Excel files for multiple predictions.
Data Visualization: Interactive dashboard for insights.
Export Predictions: Save results in CSV, Excel, PDF, and Word formats.
User-Friendly UI: Beautiful Streamlit interface designed for a jewelry store.
📊 Problem Statement
Gemineye Emporium, a growing jewelry business, faces pricing challenges due to rapid expansion. Key issues include:

1️⃣ Market Dynamics: Consumer preferences and trends change frequently.
2️⃣ Competitive Pricing: Setting prices to attract customers while maintaining profitability.
3️⃣ Cost Management: Balancing material costs, craftsmanship, and logistics.

The goal is to develop a machine learning model that predicts optimal jewelry prices based on various attributes.

📂 Dataset Information
The dataset contains details about jewelry orders, including:

Feature	Description
Category	Type of jewelry (Necklace, Ring, etc.)
Brand_ID	Unique identifier for brands
Target_Gender	Intended gender for the jewelry
Main_Color	Primary color of the jewelry piece
Main_Metal	Main metal used (Gold, Silver, etc.)
Main_Gem	Gemstone type (Diamond, Ruby, etc.)
Order Month	Month in which the order was placed
Order Day	Day of the month when the order was placed
Price (Target)	The jewelry price in USD
🛠️ Tech Stack
The project is built using:

Python 🐍
Machine Learning Models: Linear Regression, Random Forest, XGBoost, CatBoost, Neural Networks
Data Preprocessing: Pandas, NumPy, Scikit-Learn
Visualization: Matplotlib, Seaborn, Plotly
Experiment Tracking: MLflow
Deployment: Streamlit, Render, GitHub
📈 Machine Learning Workflow (CRISP-DM Approach)
1️⃣ Business Understanding
Define pricing challenges for the jewelry market.
Collaborate with stakeholders to align business goals with AI-driven pricing.
2️⃣ Data Collection & Preprocessing
Collect historical sales data, competitor pricing, and customer demographics.
Handle missing values, remove outliers, and encode categorical features.
3️⃣ Exploratory Data Analysis (EDA)
Analyze seasonality, pricing trends, and consumer preferences.
Identify key features affecting jewelry prices.
4️⃣ Feature Engineering
Create new features to improve model accuracy.
Scale numeric features and encode categorical variables.
5️⃣ Model Training & Evaluation
Implemented Models:

Linear Regression
Support Vector Machine
Polynomial Regression
Gradient Boosting
XGBoost
Decision Tree
Random Forest
Extra Trees
AdaBoost
CatBoost
Neural Networks
Evaluation Metrics:

Mean Absolute Error (MAE)
Mean Squared Error (MSE)
Root Mean Squared Error (RMSE)
R² Score
Hyperparameter Tuning using GridSearchCV for performance improvement.

6️⃣ Experiment Tracking with MLflow
Track different models and hyperparameter tuning results.
Compare model performance and log metrics.
7️⃣ Model Deployment
Deploy the best model using Streamlit & Render.
Create an interactive UI for users to enter jewelry details and get predictions.
📌 How to Run the Project Locally
🔹 1. Clone the Repository
bash
Copy
Edit
git clone https://github.com/YourUsername/jewelry-price-prediction.git
cd jewelry-price-prediction
🔹 2. Install Dependencies
bash
Copy
Edit
pip install -r requirements.txt
🔹 3. Run the Streamlit App
bash
Copy
Edit
streamlit run app.py
🚀 Deployment on Render
The project is hosted on Render, follow these steps to deploy:

1️⃣ Push the project to GitHub.
2️⃣ Create a new Web Service on Render.
3️⃣ Connect to your GitHub repository.
4️⃣ Set the following configurations:

Python Version: 3.9
Start Command: gunicorn -w 4 -k uvicorn.workers.UvicornWorker app:app
5️⃣ Deploy and get your live URL! 🎉
🔗 Live Demo: Jewelry Price Prediction App

📊 Dashboard Features
📤 Upload CSV/Excel files for bulk predictions.
📈 Interactive Price Distribution visualization.
📥 Download predictions in CSV, Excel, PDF, and Word formats.
📌 File Structure
bash
Copy
Edit
jewelry-price-prediction/
│── app.py                # Streamlit app for UI & predictions  
│── best_model.pkl        # Saved ML model  
│── requirements.txt      # Project dependencies  
│── runtime.txt           # Python runtime version  
│── setup.sh              # Setup script for deployment  
│── Procfile              # Render deployment configuration  
│── README.md             # Project documentation  
📢 Insights & Recommendations
Leverage AI for Competitive Pricing:
AI-based pricing helps adjust prices dynamically to market trends.
Feature Importance Analysis:
Jewelry category, brand, and gemstones significantly influence prices.
Implement Customer Segmentation:
Different pricing strategies for luxury vs. budget jewelry can optimize sales.
🔗 Additional Resources
📌 GitHub Repo: Jewelry Price Prediction
📌 Live Demo: Render Deployment

🎯 Final Thoughts
This project demonstrates how machine learning can optimize jewelry pricing by leveraging data-driven insights. 🚀

If you found this useful, don't forget to ⭐️ Star this repository on GitHub!

Happy Coding! 🎉💎
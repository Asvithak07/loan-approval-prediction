# Loan Approval Prediction

This project predicts whether a loan application will be approved or not using a **Random Forest Classifier**.  
I also built a simple **Streamlit web app** to make predictions interactively.

---

## 📂 Project Structure


Loan-Approval-Project/
│── data/ # Training and testing datasets
│── model/ # Saved model and encoders
│── notebooks/ # Jupyter/Colab notebook (EDA + training)
│── app.py # Streamlit app for predictions
│── requirements.txt # Dependencies
│── .gitignore
│── README.md


---

## 📊 Dataset
The dataset contains the following columns:

- Loan_ID  
- Gender  
- Married  
- Dependents  
- Education  
- Self_Employed  
- ApplicantIncome  
- CoapplicantIncome  
- LoanAmount  
- Loan_Amount_Term  
- Credit_History  
- Property_Area  
- Loan_Status (Target)

---

## 🚀 Model
- Algorithm used: **Random Forest Classifier**  
- Accuracy achieved: **95%**  
- Features were preprocessed using **Label Encoding** for categorical variables.

---

## 🖥️ Streamlit App
To run the web app locally:

```bash
pip install -r requirements.txt
streamlit run app.py

Then open the link shown in the terminal (usually http://localhost:8501). 


📌 Results

Accuracy: 95%

Precision/Recall balanced well.

The app allows users to enter loan details and instantly see approval prediction.

🛠️ Future Improvements

Add more advanced models (XGBoost, Neural Nets).

Hyperparameter tuning.

Deploy app on Streamlit Cloud or Heroku. 


Author 
Asvithaa k
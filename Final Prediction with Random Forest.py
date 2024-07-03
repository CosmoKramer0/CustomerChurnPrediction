import pandas as pd
from sklearn.ensemble import RandomForestClassifier

# Load dataset
data = pd.read_csv("Churn_Modelling.csv")

# Feature selection
X = data[['CreditScore', 'Geography', 'Gender', 'Age', 'Tenure', 'Balance', 'NumOfProducts', 'HasCrCard', 'IsActiveMember', 'EstimatedSalary']]
y = data['Exited']

# Encode categorical variables
X = pd.get_dummies(X, columns=['Geography', 'Gender'], drop_first=True)

# Model Building
rf_model = RandomForestClassifier(n_estimators=100, random_state=42)
rf_model.fit(X, y)

# Take user input
credit_score = float(input("Enter Credit Score: "))
geography = input("Enter Geography (France, Germany, Spain): ")
gender = input("Enter Gender (Male or Female): ")
age = int(input("Enter Age: "))
tenure = int(input("Enter Tenure: "))
balance = float(input("Enter Balance: "))
num_of_products = int(input("Enter Number of Products: "))
has_cr_card = int(input("Enter 1 if has Credit Card, 0 otherwise: "))
is_active_member = int(input("Enter 1 if active member, 0 otherwise: "))
estimated_salary = float(input("Enter Estimated Salary: "))

# Convert user input into DataFrame
user_input = pd.DataFrame({
    'CreditScore': [credit_score],
    'Age': [age],
    'Tenure': [tenure],
    'Balance': [balance],
    'NumOfProducts': [num_of_products],
    'HasCrCard': [has_cr_card],
    'IsActiveMember': [is_active_member],
    'EstimatedSalary': [estimated_salary],
    'Geography_Germany': [1 if geography.lower() == 'germany' else 0],
    'Geography_Spain': [1 if geography.lower() == 'spain' else 0],
    'Gender_Male': [1 if gender.lower() == 'male' else 0]
})

# Predict the outcome for user input
prediction = rf_model.predict(user_input)
print("Prediction (Exited):", prediction[0])

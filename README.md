# Customer Churn Prediction

Customer churn, the loss of customers, poses a significant challenge across industries. Businesses aim to mitigate churn by implementing targeted retention strategies. The objective of this project is to develop an effective predictive model leveraging advanced data mining techniques to accurately identify customers at risk of churn based on historical data and behavior patterns.

## Introduction
In today's hyper-competitive business landscape, maintaining customer loyalty and retention has become a paramount concern for organizations spanning various industries. The objective of my project is to develop an effective customer churn prediction system leveraging advanced analytics techniques. Customer churn, or customer attrition, is a critical challenge for businesses across various industries, including telecommunications, banking, and subscription-based services. By understanding and predicting customer churn, companies can implement proactive strategies to retain valuable customers and mitigate revenue loss.
My dataset encompasses a wide range of customer-related factors, including demographics, usage patterns, transaction history, customer service interactions, and satisfaction metrics. Through comprehensive analysis and predictive modelling, we aim to uncover underlying patterns and key indicators that contribute to customer churn.
Utilizing sophisticated analytical methods and machine learning algorithms, we seek to identify actionable insights and build a robust predictive model. This model will enable businesses to forecast which customers are at risk of churning, allowing for targeted retention efforts and personalized interventions.
Ultimately, by leveraging predictive analytics for customer churn prediction, we aspire to empower businesses to enhance customer retention strategies, optimize resource allocation, and ultimately foster long-term customer loyalty and profitability.

## Motivation
- Business Sustainability: Recognizing the pivotal role of customer retention in sustaining long-term business growth and profitability.
- Revenue Protection: Understanding that each lost customer represents not just a decline in immediate revenue but also potential future revenue streams.
- Competitive Advantage: Acknowledging the importance of differentiation through superior customer experience in increasingly saturated markets.
- Data Utilization Opportunity: Leveraging the abundance of historical customer data available to gain deep insights into customer behaviour and preferences.
- Efficiency and Optimization: Enabling businesses to allocate resources more efficiently, optimize marketing efforts, and enhance overall customer satisfaction through proactive churn prediction and targeted retention strategies.


## Overview

This project is divided into three phases:
1. **Data Preprocessing**: Handling missing values, encoding categorical variables, converting data types, detecting and handling outliers, and exploring data relationships. The Preprocessing has been done in R.
2. **Modelling**: Using various models (Random Forest, Decision Tree, KNN, SVM) to predict customer churn and selecting the best model based on accuracy.
3. **User Interface**: Creating a user interface to input customer data and predict churn using the selected model.

## Dataset

The dataset contains customer information with the following columns:
- RowNumber
- CustomerId
- Surname
- CreditScore
- Geography
- Gender
- Age
- Tenure
- Balance
- NumOfProducts
- HasCrCard
- IsActiveMember
- EstimatedSalary
- Exited

Sample data:
![image](https://github.com/CosmoKramer0/CustomerChurnPrediction/assets/122899893/c027b262-645d-4bfa-8304-2d66c669953c)


## Preprocessing

- **Identified Missing Values**: Detected and handled missing values.

![image](https://github.com/CosmoKramer0/CustomerChurnPrediction/assets/122899893/305f395d-145f-4646-9a9b-283989869441)

- **Encoded Categorical Variables**: Converted categorical variables to numerical values.

![image](https://github.com/CosmoKramer0/CustomerChurnPrediction/assets/122899893/431ef275-efab-44ab-9490-1fe6e9cac9e6)

- **Data Types**: Converted data types to appropriate formats.
- **Outliers**: Detected and handled outliers.
- **Explored Data Relationships**: Visualized and analyzed relationships between features.

![image](https://github.com/CosmoKramer0/CustomerChurnPrediction/assets/122899893/c4166156-8b7a-4317-ae3b-2eabae1614ff)



## Modelling

Used the following models to predict customer churn:
- Random Forest
- Decision Tree
- K-Nearest Neighbors (KNN)
- Support Vector Machine (SVM)

Random Forest gave the highest accuracy (0.8585) and was selected as the final model.

## User Interface

Created a user interface to input customer data and predict churn. The interface asks for:
- Credit Score
- Geography (France, Germany, Spain)
- Gender (Male or Female)
- Age
- Tenure
- Balance
- Number of Products
- Whether customer uses Credit Card or not
- Whether customer is active member or not
- Estimated Salary

After taking the above parameters as input, the model predicts whether the customer has exited or not.

## Results

![image](https://github.com/CosmoKramer0/CustomerChurnPrediction/assets/122899893/54f89fa7-f855-4139-bb1d-42ca66e047c3)
![image](https://github.com/CosmoKramer0/CustomerChurnPrediction/assets/122899893/46470d5d-ad87-442a-b69e-b2d495452ae4)

## Challenges Faced 
- Data Quality: Ensuring data quality and consistency across different sources posed challenges, including dealing with missing values and outliers.
- Feature Selection: Selecting relevant features and engineering them for predictive modelling required careful analysis and domain expertise.
- Model Interpretability: Balancing model complexity with interpretability was challenging, particularly in explaining predictions to stakeholders.
- Class Imbalance: Addressing class imbalance in the dataset, where churned customers were fewer than non-churned, presented modelling challenges.
- Deployment: Integrating the predictive model into operational systems while ensuring data security and privacy was complex.

## Conclusion
In conclusion, the project underscores the critical role of predictive modelling in addressing the challenges of customer churn in today's business landscape. By leveraging advanced data mining techniques and machine learning algorithms, businesses can gain valuable insights into customer behaviour, anticipate churn risks, and implement proactive retention strategies.
Throughout the project, we encountered various challenges, including data quality issues, feature selection complexities, and deployment considerations. However, these challenges provided valuable learning opportunities, emphasizing the importance of thorough data preprocessing, effective feature engineering, and balanced model interpretability.
Despite the challenges, the project yielded significant insights and lessons learned. By adopting an iterative approach and continuously refining the predictive model, we have developed a robust framework for churn prediction that can be integrated into operational systems for real-time decision-making.
Looking ahead, the project sets the stage for continued innovation and improvement in customer relationship management. By embracing data-driven strategies and predictive analytics, businesses can enhance customer satisfaction, foster brand loyalty, and drive long-term growth and success in today's competitive marketplace.

## Contact
For any questions or feedback, please contact fahadbaig247@gmail.com.

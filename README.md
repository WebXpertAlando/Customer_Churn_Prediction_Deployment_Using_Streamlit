
# Telco Customer Churn Prediction Model and Retention Strategy

![customer_churn retention](https://github.com/user-attachments/assets/af22c4fc-5fff-4993-9c84-14912beedd6e)

### Introduction
Customer churn is the percentage of customers that stopped using your company's product or service during a certain time frame. It’s easier to keep an existing customer than to gain a new one, and it’s much simpler to save a departing customer than to tempt them back later. Customer churn is measured using customer churn rate. That’s the number of people who stopped being customers during a set period of time, such as a year, a month, or a financial quarter.
### About Dataset
Telco customer churn contains information about a fictitious telecom company providing home phone and Internet services to 7043 customers in California in the third quarter. It includes which customers left, stayed or signed up for service.

##  1. Data Collection:
Access the Telco customer churn dataset from Kaggle, which includes information on demographics, transaction history, customer service interactions, subscription details, and whether the customer churned.


##  2. Data Preprocessing.
Data preprocessing is the processes of cleaning, transforming, and integrating of data in order to make it ready for analysis. The goal of data preprocessing is to improve the quality of the data and to make it more suitable for the specific data mining task.

### Data Preprocessing Steps.

#### Handling Missing Values
From our Dataset of Churn it contained no missing values there by making our models fit correctly. There was also no issues of underfitting or overfittig since our standardization and feature engineering was well taken care of.

#### Encoding categorical variables
categorical data represents discrete values or categories, such as gender, country, or product type. Machine learning algorithms, however, require numerical input, making it essential to convert categorical data into a numerical format. This process is known as encoding for example in our dataset, Gender, Churn Column were encoded using OneHot Encoding.

## 3. Exploratory Data Analysis ( EDA )
#### Analysis on Categorical Variables
- In the above findings, It can be seen that Males were the most involved in Churn than females.
- Then on SeniorCitizen, most customers were not Senior Citizens.
- Most clients Did not have partners. (Yes, No) ? Married or not. Living together, being roommates
- Most of the clients had no dependents e.g (Child, mother, father, grandmothe).
- Most Clients had phone services. This enables the Telco
- Most customers had no Multiples line meaning that most customers could be reached when only a single phone line is in use.
- 

## 4.  Model Development
     The model has been deployed using streamlit. 


(https://churnappprediction.streamlit.app/)



## 5.  Interpretability and Feature Importance:


## 6. . Retention Strategy Development.
A customer retention strategy helps you keep your customers around longer, which helps you avoid having to go out and find new ones.
 - Get to the root of the Churn.
 - Customer Segmentation.
 - Monitor User Engagement.
 - Create an intuitive user onboarding process.
 - Offer personalized and proactive customer communication.
 - Reward customer loyalty .
 - Follow up with customers.
 - Develop a data roadmap and stick to it.







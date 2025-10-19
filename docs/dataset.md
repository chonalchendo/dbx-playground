# Dataset
## Kaggle Fraud Transactions 
SOURCE: https://www.kaggle.com/datasets/kartik2112/fraud-detection

This is a simulated credit card transaction dataset containing legitimate and fraud transactions from the duration 1st Jan 2019 - 31st Dec 2020. It covers credit cards of 1000 customers doing transactions with a pool of 800 merchants.

## Features
- trans_date_trans_time
- cc_num
- merchant
- category
- amt
- first
- last
- gender
- street
- city
- state
- zip
- lat
- long
- city_pop
- job
- dob
- trans_num
- unix_time
- merch_lat
- merch_long
- is_fraud

## Data Modelling
Using the STAR schema, we can split the data into fact and dimensions data. This does mean splitting out the dataset, but it will provide good practice for data modelling and introducing best practices and visibility over the dataset.
- Fact: transactions
- Dimensions:
    - users
    - merchants
    - locations
    - account
    - time

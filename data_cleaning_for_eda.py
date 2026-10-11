import pandas as pd
import numpy as np
import math

df=pd.read_csv('Sales_transactions_2022_2025.csv')

df.columns=df.columns.str.strip()
col_text=df.select_dtypes('string').columns
df[col_text]=df[col_text].apply(lambda x:x.str.strip())
df[col_text]=df[col_text].replace('', np.nan)

df['Customer_Age']=df['Customer_Age'].astype('float').astype('Int64')
df['Order_Date']=pd.to_datetime(df['Order_Date'], errors='coerce')
df['Order_Time']=pd.to_datetime(df['Order_Time'], format='%H:%M:%S', errors='coerce').dt.time
df['Delivery_Days']=df["Delivery_Days"].astype('float').astype('Int64')
df['Customer_Rating']=df["Customer_Rating"].astype('float').astype('Int64')
df['Inventory_Level']=df["Inventory_Level"].astype('float').astype('Int64')

average_age=math.ceil(df['Customer_Age'].mean())
df['Customer_Age']=df['Customer_Age'].fillna(average_age)
df['Customer_Name']=df['Customer_Name'].fillna('Anonymous')
customer_gender_mode=df['Customer_Gender'].mode()[0]
df['Customer_Gender']=df['Customer_Gender'].fillna(customer_gender_mode)
df['Product_Name']=df['Product_Name'].fillna('Unknown')
payment_method_mode=df['Payment_Method'].mode()[0]
df['Payment_Method']=df['Payment_Method'].fillna(payment_method_mode)
delivery_days_median=df['Delivery_Days'].median()
df['Delivery_Days']=df['Delivery_Days'].fillna(delivery_days_median)
df['Return_Reason']=df['Return_Reason'].fillna('Not specified')
df['Promotion_Code']=df['Promotion_Code'].fillna('No code')
customer_rating_median=df['Customer_Rating'].median()
df['Customer_Rating']=df['Customer_Rating'].fillna(customer_rating_median)
inventory_level_median=df['Inventory_Level'].median()
df['Inventory_Level']=df['Inventory_Level'].fillna(inventory_level_median)

df['Customer_Age']=df['Customer_Age'].astype('int')
df['Delivery_Days']=df['Delivery_Days'].astype('int')
df['Customer_Rating']=df['Customer_Rating'].astype('int')
df['Inventory_Level']=df['Inventory_Level'].astype('int')

df['Customer_Gender']=df['Customer_Gender'].apply(lambda x:x.title())
df['Customer_Gender']=df['Customer_Gender'].str.replace('-', ' ')

df['Product_Category']=df['Product_Category'].apply(lambda x:x.title())

df['Payment_Method']=df['Payment_Method'].apply(lambda x:x.title())

print(df.duplicated().sum())
df=df.drop_duplicates()

print(df.info())
print(df.isnull().sum())

df.to_csv('Sales_Transactions_Cleaned.csv', index=False)
import pandas as pd

df=pd.read_csv('Sales_Transactions_Cleaned.csv')

df.columns=df.columns.str.strip()
col_text=df.select_dtypes('string').columns
df[col_text]=df[col_text].apply(lambda x:x.str.strip())

df['Order_Date']=pd.to_datetime(df['Order_Date'], errors='coerce')
df['Order_Time']=pd.to_datetime(df['Order_Time'], format='%H:%M:%S', errors='coerce').dt.time

df=pd.get_dummies(df, columns=['Customer_Gender', 'Customer_Segment', 'Sales_Channel','Product_Category', 'Country', 'Region']
                  , drop_first=True, dtype=int)

df['Order_Month']=df['Order_Date'].dt.month
df['Order_Day']=df['Order_Date'].dt.day
df['Order_Year']=df['Order_Date'].dt.year
df['Order_Hour']=df['Order_Time'].apply(lambda x:x.hour)
df['Order_Minute']=df['Order_Time'].apply(lambda x:x.minute)

df=df.drop(['Order_Date', 'Order_Time'], axis=1)
print(df.columns)
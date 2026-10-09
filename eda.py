import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt 

df=pd.read_csv('Sales_Transactions_Cleaned.csv')

df.columns=df.columns.str.strip()
col_text=df.select_dtypes('string').columns
df[col_text]=df[col_text].apply(lambda x:x.str.strip())

df['Order_Date']=pd.to_datetime(df['Order_Date'], errors='coerce')
df['Order_Time']=pd.to_datetime(df['Order_Time'], format='%H:%M:%S', errors='coerce').dt.time

def boxplots():
    sns.boxplot(y=df['Customer_Age'])
    plt.show()
    df = df[(df['Customer_Age']>14) & (df['Customer_Age']<85)]
    sns.boxplot(y=df['Customer_Age'])
    plt.show()

    df=df[df['Quantity']>=1]
    sns.boxplot(y=df['Quantity'])
    plt.show()

#print(df[['Quantity', 'Unit_Price', 'Sales_Amount']].describe())

def corr_matrix():
    numeric_col=df.select_dtypes(include=('int', 'float'))
    corrs=numeric_col.corr(method='spearman')
    plt.figure(figsize=(9,6))
    sns.heatmap(corrs, annot=True, cmap='coolwarm', fmt='.2f')
    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()
    plt.show()

def bar_charts():
    df['Customer_Gender'].value_counts().plot(kind='bar')
    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()
    plt.show()

    df['Customer_Segment'].value_counts().plot(kind='bar')
    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()
    plt.show()

    df['Sales_Channel'].value_counts().plot(kind='bar')
    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()
    plt.show()

    df['Country'].value_counts().plot(kind='bar')
    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()
    plt.show()

    df['Product_Category'].value_counts().plot(kind='bar')
    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()
    plt.show()

    df['Payment_Method'].value_counts().plot(kind='bar')
    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()
    plt.show()

#sns.pairplot(df[['Sales_Amount', 'Profit', 'Discount_Percentage', 'Sales_Channel']], hue='Sales_Channel')
#plt.show()

top_categories=df.groupby('Product_Category')[['Profit', 'Sales_Amount', 'Quantity']].sum().sort_values(by='Profit', ascending=False).head(3)
#print(top_categories)
top_products=df.groupby('Product_Name')[['Profit', 'Sales_Amount', 'Quantity']].sum().sort_values(by='Profit', ascending=False).head(3)
#print(top_products)

#print(top_categories.iloc[1, 0] - top_categories.iloc[2, 0])

top_channels=df.groupby('Sales_Channel')[['Profit']].sum().sort_values(by='Profit', ascending=False)
top_channels['Count']=df.groupby('Sales_Channel')['Sales_Channel'].agg(func='count')
#print(top_channels)

bottom_perform_categ=df.groupby('Product_Category')[['Profit', 'Quantity']].sum().sort_values(by='Profit', ascending=True)
bottom_perform_prod=df.groupby('Product_Name')[['Profit', 'Quantity']].sum().sort_values(by='Profit', ascending=True).head(5)
#print(bottom_perform_categ)
#print(bottom_perform_prod)

regions_best_revenue=df.groupby(['Country', 'Region'])['Sales_Amount'].sum().sort_values(ascending=False)
#print(regions_best_revenue)

no_discount_profit=df[df['Discount_Percentage']==0]['Profit'].sum()
high_discount_profit=df[df['Discount_Percentage']>=20]['Profit'].sum()
#print(no_discount_profit - high_discount_profit)

df['Order_Month']=df['Order_Date'].dt.month
monthly_sales=df.groupby('Order_Month')['Sales_Amount'].sum().reset_index()
#sns.lineplot(x='Order_Month', y='Sales_Amount', data=monthly_sales, marker='o')
#plt.show()

df['Order_Year']=df['Order_Date'].dt.year
annual_sales=df.groupby('Order_Year')['Sales_Amount'].sum().reset_index()
#sns.lineplot(x='Order_Year', y='Sales_Amount', data=annual_sales, marker='o')
#plt.show()
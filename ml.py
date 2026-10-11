import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor

df=pd.read_csv('Cleaned_Data_FE.csv')

df.columns=df.columns.str.strip()

x=df.drop(['Profit', 'Sales_Amount', 'Cost_Amount', 'Profit_Margin'], axis=1)
y=df['Sales_Amount']

x_train, x_test, y_train, y_test=train_test_split(x,y,test_size=0.2,random_state=42)

model=LinearRegression()
model.fit(x_train, y_train)

predictions=model.predict(x_test)

#print('Real prices: ', y_test[:5].values)
#print('Predicted prices: ', predictions[:5])

rfr_model=RandomForestRegressor()
rfr_model.fit(x_train,y_train)

rfr_predictions=rfr_model.predict(x_test)

print('Real prices: ', y_test[:5].values)
print('Predicted prices: ', rfr_predictions[:5])
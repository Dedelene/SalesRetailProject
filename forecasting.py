import pandas as pd
from prophet import Prophet
import matplotlib.pyplot as plt

df=pd.read_csv('Sales_Cleaned_FE.csv')

df['Order_Date']=pd.to_datetime(
    df[['Order_Year', 'Order_Month', 'Order_Day']].rename(
        columns={'Order_Year': 'year', 'Order_Month': 'month', 'Order_Day': 'day'}
        )
    )
df_forecast=df.groupby('Order_Date')['Sales_Amount'].sum().reset_index()
df_forecast=df_forecast.rename(columns={'Order_Date': 'ds', 'Sales_Amount': 'y'})

model=Prophet(yearly_seasonality=True, daily_seasonality=False)
model.fit(df_forecast)

future=model.make_future_dataframe(periods=365)
prediction=model.predict(future)

fig1 = model.plot(prediction)
plt.title('Sales Forecast for the Next Year')
plt.show()

fig2 = model.plot_components(prediction)
plt.show()

prediction.to_csv('Sales_Forecast.csv', index=False)
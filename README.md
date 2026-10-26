# Retail Sales Project

## Description

I developed this project as a hands-on exercise in data analytics and to familiarize myself with handling and interpreting realistic business data.
The dataset, sourced from Kaggle, contains synthetic retail sales records and covers areas like customers, products, pricing, discounts, profit, location, sales and revenue. It contains 18,045 records and 36 features and has some missing or inconsistent values.

#### Project Workflow:

1. Data cleaning 
2. Exploratory Data Analysis
3. Feature Engineering
4. Time Series Forecasting

## First Step - Cleaning the Data (data_cleaning_for_eda.py)

The initial step, after reading the data set and aligning the csv file, was to use the strip method to erase the white spaces and replace the missing values (‘’) with nan.
Most column types were strings, such as customer age or order date, so I converted them to float then to Int64 (to not get an error for the missing ones) and to datetime for date and time columns.
To handle the null values, I used the central tendency - mean and median - for age, delivery days, customer rating and inventory level; for categorical columns like gender and payment method I used mode and for the nominal data as customer name, product name or return reason I replaced the empty data with ‘Anonymous’, ‘Unknown’ or ‘Not specified’.
While searching for outliers, I have found illogical extremes such as 4 and 112 in the customer age column and negative values in the quantity column, so I filtered out the records (remaining 17,989 records). The high values from the financial metrics that I decided to keep represent premium transactions, essential for accurate revenue analysis.
To complete the cleaning, I checked for duplicate records and dropped them.
With the dataset cleaned, I saved the data into a new csv file, ready to be analyzed. (Sales_Transactions_Cleaned.csv)

## 2nd. Exploratory Data Analysis (eda.py)

In the next phase I plotted a correlation heatmap for the numerical columns. The method used is Spearman rank correlation, because, observing the boxplots, I understood that the data is not normally distributed and for non-linear data, Spearman method fits perfectly. Analyzing the matrix, strong positive correlations are among the financial columns: unit price, cost, sales and profit. The discount percentage shows a negative score (-0.33) with the profit; an insight that addresses one of the project’s goals.

#### The following charts are generated with Power BI

### Which countries and regions generate the most profit?

<img src='/Charts/ProfitByRegion.png' width='700'>

The US and the UK are the most profitable countries overall, with England standing out as the single highest-performing region. Based on these margins, the company should consider focusing its expansion plans and open new shops in this area.

### Which is the most popular sales channel?

<img src='/Charts/QuantityByChannel.png' width='700'>

The highest volume of items is sold through online platforms, reaching 14.5K units. To capitalize on this trend, the company should continue investing in the maintenance and user experience of its web and mobile apps. Although the retail store has a higher sales volume than the B2B portal, the latter generates almost the same amount of profit. This indicates that B2B portal transactions are highly valuable and bring a significantly higher return per order.

### How do discounts impact profitability?

<img src='/Charts/ProfitByDiscount.png' width='700'>

When the discount percentage increases, the total profit drops significantly. This inverse relationship indicates that high discounts affect profit margins to a point where the company would need to sell massive quantities just to maintain a normal profit level. Therefore, deep discounts should be limited primarily to the B2B portal, where bulk purchasing volumes are high enough to compensate for the heavily reduced margins.

### How is the sale amount changing over time?

<img src='/Charts/TrendForSaleAmount.png' width='700'>

The trend reveals strong seasonality, with sales consistently peaking during the winter months, followed by a secondary spike in the fall. Knowing that the top-selling product categories are electronics, furniture and appliances, the massive winter jump is highly likely driven by holiday shopping and Christmas gifts. Similarly, the increased sales volume in the fall can be attributed to the back to school season, as consumers are likely buying office supplices and study furniture during this period.

## 3rd. Feature Engineering (fe.py)

First, I transformed the categorical data, such as customer gender and customer segment, into 0 and 1 values using the One-Hot Encoding method using get_dummies. For the datetime data, I split the order date into day, month and year and the order time into hour and minute. There was a column named Return Flag with yes and no values, so I replaced them with 1 and 0. I dropped the nominal data that is not important for time series forecasting, such as the ids, names, return reason etc. Finally, I added a new column – profit margin – dividing the profit by the sales amount.

(Sales_Cleaned_FE.csv)

## 4th. Time Series Forecasting (forecasting.py)

To predict future sales and analyze long-term trends, I applied Time Series Forecasting using Meta's Prophet library. First, I reassembled the separated year, month and day columns back into a standard datetime format and aggregated the total sales on a daily basis. I then trained the prophet model to recognize historical patterns, specifically enabling yearly seasonality. The model generated a 365-day future forecast, calculating not only the predicted sales, but also the upper and lower confidence intervals.

<img src='/Charts/SalesForecast.png' width='700'>

The forecast chart shows that overall sales will keep growing in the future. The model successully caught the huge spikes that the company get every year during winter holidays.

<img src='/Charts/Components.png' width='700'>

Looking at the daily data, there's a strong weekly habit: sales are higher on monday and tuesday and drop during the weekend.

The company needs to stock up on inventory early before winter to handle the high sales. Furthermore, to fix the weekend drop, the marketing team should run special weekend sales to get people to buy more on those slow days.

## Conclusion

This project demonstrates a complete data analytics workflow, transforming raw, messy data into actionable business strategies. By combining Python's processing power with Power BI's visual storytelling and Prophet's temporal forecasting, I identified key growth areas useful for the company.

## How to Run the Project

1. Clone this repository to your local machine using git clone.

2. Open the project folder in Visual Studio Code.

3. Open a new PowerShell terminal and create a virtual environment by running python -m venv .venv.

4. Activate the virtual environment using the command .\.venv\Scripts\activate.

5. Install all the necessary dependencies by running pip install -r requirements.txt.
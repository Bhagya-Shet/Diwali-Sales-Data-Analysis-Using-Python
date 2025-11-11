Diwali Sales Analysis
Project Overview

The Diwali Sales Analysis project explores customer purchasing behavior and overall sales performance during the festive Diwali season. Using retail transaction data, the project identifies key trends, customer segments, and regional sales patterns to support strategic business decisions and data-driven marketing efforts.

Dataset Summary

Dataset Name: Diwali Sales Data.csv
Size: 11,250 rows × 13 columns

Key Features:

Customer Demographics: Customer_ID, Gender, Age Group, Marital Status, State, Zone

Purchase Details: Product Category, Orders, Amount, Date of Purchase

Customer Behavior: Segment, Purchase Preferences

This dataset provides detailed insights into customer shopping patterns during Diwali sales.

Tools and Technologies

Programming Language: Python

Libraries: pandas, numpy, matplotlib, seaborn

Visualization Tool: Power BI

Exploratory Data Analysis (EDA)

Exploratory Data Analysis (EDA) was performed using Python to clean, transform, and visualize the data. The main steps included:

Handling missing values

Converting data types and transforming fields

Grouping and aggregating sales data

Creating visualizations to identify spending trends

Example Code Snippet:

import pandas as pd

df = pd.read_csv('Diwali Sales Data.csv')
df.dropna(inplace=True)
df['Amount'] = df['Amount'].astype('int')
sales_summary = df.groupby('Product_Category')['Amount'].sum().sort_values(ascending=False)
print(sales_summary)

Key Insights

Female customers contributed approximately 70 percent of total sales.

The 26–35 age group recorded the highest number of purchases, representing young professionals.

The top-performing states were Maharashtra, Uttar Pradesh, and Karnataka.

The Western and Central zones showed the highest revenue contributions.

Clothing, Food, and Electronics were the most purchased product categories.

Business Recommendations

Increase promotional campaigns focused on female customers, the primary spending group.

Target marketing efforts towards the 26–35 age group.

Introduce bundled offers and festive discounts for popular categories.

Improve sales in low-performing zones through targeted regional campaigns.

Launch loyalty programs to retain high-value customers.

Visualization Dashboard

A Power BI dashboard was created to visually represent the sales insights derived from the analysis. The dashboard provides an overview of total sales, order counts, demographic contributions, and regional performance.
It highlights that female customers dominate purchases, especially in categories such as clothing and food. The 26–35 age group remains the most active, and states such as Maharashtra, Uttar Pradesh, and Karnataka lead in total sales.

Conclusion

The Diwali Sales Analysis project demonstrates the importance of data analytics in understanding customer behavior and improving business outcomes. Through Python-based analysis and Power BI visualization, this project successfully translates raw sales data into actionable insights. The findings can help businesses optimize marketing strategies, focus on high-value segments, and enhance overall festive sales performance.

References

Diwali Sales Dataset (Kaggle)

Python Libraries: pandas, numpy, matplotlib, seaborn

Power BI for Data Visualization

Retail Company Sales Records

YouTube Tutorial: "Python Project for Data Analysis - Exploratory Data Analysis" by Rishabh Mishra, 2024

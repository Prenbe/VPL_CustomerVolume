import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Example: 'mysql://username:password@localhost:3306/database_name'
mysql_connection_string = 'mysql://root:PeachBiscuit202$@127.0.0.1:3306/vpl'

# Function to execute MySQL query and return DataFrame
def execute_mysql_query(query):
    return pd.read_sql_query(query, mysql_connection_string)

# 1. Monthly Trends in FedEx Inbound Shipments
monthly_trends_query = f"""
    SELECT YEAR(Invoice_Date) AS Year,
           MONTH(Invoice_Date) AS Month,
           COUNT(*) AS ShipmentCount
    FROM tblinvoice
    WHERE Carrier_Name = 'FEDEX'
        AND Package_Direction = 'Inbound'
    GROUP BY Year, Month
"""

df_monthly_trends = execute_mysql_query(monthly_trends_query)

plt.figure(figsize=(12, 6))
sns.lineplot(x='Month', y='ShipmentCount', hue='Year', data=df_monthly_trends)
plt.title('Monthly Trends in FedEx Inbound Shipments')
plt.xlabel('Month')
plt.ylabel('Shipment Count')
plt.show()

# 2. Comparison of Volumes between Old and New FedEx Accounts Over Time
comparison_query = f"""
    SELECT YEAR(Invoice_Date) AS Year,
           MONTH(Invoice_Date) AS Month,
           COUNT(*) AS ShipmentCount,
           SUM(CASE WHEN Account = '2002' THEN 1 ELSE 0 END) AS OldAccountCount,
           SUM(CASE WHEN Account = '1562' THEN 1 ELSE 0 END) AS NewAccountCount
    FROM tblinvoice
    WHERE Carrier_Name = 'FEDEX'
        AND Package_Direction = 'Inbound'
    GROUP BY Year, Month
"""

df_comparison = execute_mysql_query(comparison_query)

plt.figure(figsize=(12, 6))
plt.plot(df_comparison['Year'].astype(str) + '-' + df_comparison['Month'].astype(str), df_comparison['OldAccountCount'], label='Old Account')
plt.plot(df_comparison['Year'].astype(str) + '-' + df_comparison['Month'].astype(str), df_comparison['NewAccountCount'], label='New Account')
plt.title('Comparison of Volumes between Old and New FedEx Accounts')
plt.xlabel('Year-Month')
plt.ylabel('Shipment Count')
plt.legend()
plt.show()

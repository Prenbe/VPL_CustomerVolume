# Import necessary libraries
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import mysql.connector

# Set up a MySQL connection
db_config = {
    "host": "127.0.0.1",
    "user": "root",
    "password": "PeachBiscuit202$",  # Replace with your actual password
    "database": "vpl"
}

# Connect to MySQL
connection = mysql.connector.connect(**db_config)

# Define the SQL query
query = """
    SELECT
        YEAR(Invoice_Date) AS Year,
        MONTH(Invoice_Date) AS Month,
        SUM(CASE WHEN Carrier_Name = 'FEDEX' AND Account = '2002' THEN 1 ELSE 0 END) AS BeforeChangeVolume,
        SUM(CASE WHEN Carrier_Name = 'FEDEX' AND Account = '1562' THEN 1 ELSE 0 END) AS AfterChangeVolume
    FROM tblinvoice
    WHERE Package_Direction = 'Inbound'
    AND Customer_Name LIKE '%ACME%'
    GROUP BY YEAR(Invoice_Date), MONTH(Invoice_Date)
    ORDER BY YEAR(Invoice_Date), MONTH(Invoice_Date)
"""

# Execute the query and load the results into a DataFrame
df = pd.read_sql(query, connection)

# Close the MySQL connection
connection.close()

# Set the aesthetic style of the plots
sns.set_style("whitegrid")

# Convert the 'Year' and 'Month' columns to a datetime format
df['Date'] = pd.to_datetime(df[['Year', 'Month']].assign(day=1))

# Create a figure and axis
plt.figure(figsize=(12, 6))
plt.plot(df['Date'], df['BeforeChangeVolume'], label='Before Change Volume', marker='o', linestyle='-')
plt.plot(df['Date'], df['AfterChangeVolume'], label='After Change Volume', marker='o', linestyle='-')

# Set labels and title
plt.xlabel('Date')
plt.ylabel('Shipment Volume')
plt.title('Inbound Shipment Volume for FedEx (Before and After Account Change)')
plt.legend()

# Show the plot
plt.tight_layout()
plt.grid(True)
plt.xticks(rotation=45)
plt.show()
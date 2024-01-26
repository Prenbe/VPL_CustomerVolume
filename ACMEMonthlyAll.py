import mysql.connector
import matplotlib.pyplot as plt

# MySQL database connection configuration
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
    GROUP BY YEAR(Invoice_Date), MONTH(Invoice_Date)
    ORDER BY YEAR(Invoice_Date), MONTH(Invoice_Date);
"""

# Execute the query and fetch the data
cursor = connection.cursor()
cursor.execute(query)
results = cursor.fetchall()

# Close the MySQL connection
connection.close()

# Extract data from the results
years = [result[0] for result in results]
months = [result[1] for result in results]
before_change_volume = [result[2] for result in results]
after_change_volume = [result[3] for result in results]

# Create a figure and axis
plt.figure(figsize=(12, 6))
plt.plot(range(len(results)), before_change_volume, label='Before Change Volume', marker='o', linestyle='-')
plt.plot(range(len(results)), after_change_volume, label='After Change Volume', marker='o', linestyle='-')

# Set labels and title
plt.xlabel('Year-Month')
plt.ylabel('Shipment Volume')
plt.title('Inbound Shipment Volume for FedEx (Before and After Account Change)')
plt.xticks(range(len(results)), [f'{year}-{month:02}' for year, month in zip(years, months)], rotation=45)

# Add legend
plt.legend()

# Show the plot
plt.tight_layout()
plt.grid(True)
plt.show()

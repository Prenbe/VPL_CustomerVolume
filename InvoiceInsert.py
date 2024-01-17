import mysql.connector
import pandas as pd

# Establish a connection to MySQL database
conn = mysql.connector.connect(
    host='your_mysql_host',
    user='your_mysql_user',
    password='your_mysql_password',
    database='your_mysql_database'
)

# Create a cursor
cursor = conn.cursor()

# Read data from CSV file
csv_file_path = 'path/file.csv'  # Replace CSV file path
data = pd.read_csv(csv_file_path)

# Define the INSERT INTO query
insert_query = """
    INSERT INTO ShippingData
    (Customer_Name, Import_Date, Invoice_Date, Ship_Date, Package_Direction, 
    Shipment_Type, Bill_Status, Carrier_Name, Account, Invoice_Number, Tracking_Number, 
    Supplier_ID, Shipper_Name, Shipper_Company, Recipient_Name, Recipient_Company, 
    Service_Base_Name, Charge_Amt)
    VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
"""

# Convert DataFrame to list of tuples
data_tuples = [tuple(row) for row in data.itertuples(index=False)]

# Insert data into tblInvoice using executemany
cursor.executemany(insert_query, data_tuples)

# Commit the changes
conn.commit()

# Close the cursor and connection
cursor.close()
conn.close()

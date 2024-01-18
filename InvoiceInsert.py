import mysql.connector
import pandas as pd
from tqdm import tqdm

# Establish a connection to MySQL database
conn = mysql.connector.connect(
    host='127.0.0.1',
    user='root',
    password='',
    database='vpl'
)

# Create a cursor
cursor = conn.cursor()

# Read data from CSV file
excel_file_path = "C:\\VPL\\ACME Health Data Challenge.xlsx"

# Specify the sheet name if your Excel file has multiple sheets
sheet_name = "Data"  # Change to the actual sheet name

# Specify the encoding when reading the Excel file (optional)
# encoding = 'utf-8' or other encoding if needed

# Read data from the Excel file
data = pd.read_excel(excel_file_path, sheet_name=sheet_name)

# Handle 'nan' values by replacing them with None
data = data.where(pd.notna(data), None)

# Define the INSERT INTO query
insert_query = """
    INSERT INTO tblInvoice
    (Customer_Name, Import_Date, Invoice_Date, Ship_Date, Package_Direction, 
    Shipment_Type, Bill_Status, Carrier_Name, Account, Invoice_Number, Tracking_Number, 
    Supplier_ID, Shipper_Name, Shipper_Company, Recipient_Name, Recipient_Company, 
    Service_Base_Name, Charge_Amt)
    VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
"""

# Convert DataFrame to list of tuples
data_tuples = [tuple(row) for row in data.itertuples(index=False)]

# Batch size for optimization
batch_size = 1000

# Insert data into ShippingData using executemany with progress bar for each batch
tqdm_iterator = tqdm(range(0, len(data_tuples), batch_size), desc="Inserting data into tblInvoice", unit="batches")
for i in tqdm_iterator:
    batch = data_tuples[i:i+batch_size]
    
    # Insert batch
    cursor.executemany(insert_query, batch)
    
    # Commit the changes for each batch
    conn.commit()
    
    # Update the progress bar description
    tqdm_iterator.set_postfix({"Batches Inserted": i // batch_size + 1})

# Close the cursor and connection
cursor.close()
conn.close()
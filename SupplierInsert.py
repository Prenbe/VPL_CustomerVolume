import mysql.connector
import pandas as pd

# Establish a connection to your MySQL database
conn = mysql.connector.connect(
    host='127.0.0.1',
    user='root',
    password='',
    database='vpl'
)

# Create a cursor
cursor = conn.cursor()

# Read data from Excel file
excel_file_path = r"C:\VPL\ACME Health Data Challenge.xlsx"

# Specify the sheet name if your Excel file has multiple sheets
sheet_name = "Supplier Table"  # Change to the actual sheet name

# Read data from the Excel file
data = pd.read_excel(excel_file_path, sheet_name=sheet_name)

# Convert DataFrame to list of tuples
data_tuples = [tuple(row) for row in data.itertuples(index=False)]

# Insert data into the Supplier table
for row in data_tuples:
    cursor.execute("INSERT INTO tblSupplier (Supplier_ID, Supplier) VALUES (%s, %s)", row)

# Commit the changes for the tblInvoice table
conn.commit()

# Close the cursor and connection
cursor.close()
conn.close()
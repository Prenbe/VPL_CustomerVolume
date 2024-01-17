CREATE TABLE tblInvoice (
    Customer_Name VARCHAR(255),
    Import_Date DATE,
    Invoice_Date DATE,
    Ship_Date DATE,
    Package_Direction VARCHAR(50),
    Shipment_Type VARCHAR(50),
    Bill_Status VARCHAR(50),
    Carrier_Name VARCHAR(255),
    Account INT,
    Invoice_Number VARCHAR(255),
    Tracking_Number VARCHAR(255),
    Supplier_ID INT,
    Shipper_Name VARCHAR(255),
    Shipper_Company VARCHAR(255),
    Recipient_Name VARCHAR(255),
    Recipient_Company VARCHAR(255),
    Service_Base_Name VARCHAR(255),
    Charge_Amt DECIMAL(10, 2)
);

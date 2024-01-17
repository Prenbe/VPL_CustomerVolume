# VPL Operations Data Analysis

## Mission
The mission of VPL is to deliver excellent products and services that help hospitals and healthcare systems obtain increased visibility and savings in their healthcare supply chain. The VPL operations team has conducted a review of customer shipping volume, specifically focusing on ACME HEALTH. The goal is to understand the changes in ACME HEALTH's shipping volume from Q1 2021 to Q2 2022 and identify opportunities to return the customer to their previous volume.

## Background
ACME HEALTH experienced a change in their FedEx account (from 2002 to 1562) in Q1 2021, which was expected to have no impact on their inbound shipping volume. However, the data suggests a material change in volume, prompting further investigation.

## Data Provided
### Invoice Master
- Detailed invoice information from carriers (FedEx and UPS).
- Includes recipient locations, entities, shipper locations, entities, etc.

### Supplier Table
- Contains IDs for VPL's suppliers.

### Additional Data Dictionary
- **Customer Name:** Customer name who records correspond to
- **Import_Date:** The date VPL ingested the record into our system
- **Invoice_Date:** The date the carrier bills VPL
- **Ship_Date:** The date the package shipped
- **Package_Direction:** Inbound/Outbound flag. Inbound are packages going to the customer, Outbound as shipments sent from the customer
- **Shipment_Type:** Small package/LTL flag; Small package is the default shipment, LTL is larger/more expensive shipment(s)
- **Bill_Status:** Billed/Unbilled Flag; indicates if VPL billed the customer
- **Carrier_Name:** Carrier responsible for delivery of shipment
- **Account:** Carrier Account number a shipment is charged to
- **Invoice_Number:** Number assigned by a carrier to VPL which groups multiple shipments together
- **Tracking_Number:** Individual shipment ID string. There can be multiple records with the same tracking number, often indicating an additional charge or adjustment assigned by the carrier after the initial billing
- **Supplier_ID:** Id that links a shipment to the supplier table. Customer buy from suppliers who ship to the customer. Not all suppliers are mapped
- **Shipper Name:** Name of the shipper on the label (free form text means this can be messy or blank) For Inbound Packages, this is usually associated with the supplier
- **Shipper Company:** Name of the shipper company on the label (free form text means this can be messy or blank). For inbound packages, this is usually associated with the supplier
- **Recipient Name:** Name of the shipper on the label (free form text means this can be messy or blank) For outbound packages, this is usually associated with the supplier or is an internal shipment between customer locations
- **Recipient Company:** Name of the shipper company on the label (free form text means this can be messy or blank) For outbound packages, this is usually associated with the supplier or is an internal shipment between customer locations
- **Service_Base_Name:** The mode chosen to ship a package. Corresponds to how quickly a shipment is intended to arrive at its destination
- **Charge_Amt:** Amount billed to the customer by VPL for the shipment


## Questions to Address
1. What patterns does the data evidence with ACME HEALTH's shipping volume?
2. What may have caused the change in carrier volume from Q1 2021 to Q2 2022?
3. Have any suppliers/shippers experienced material volume changes, and if so, how?
4. Has inbound volume to ACME HEALTH's receiving locations changed materially? If so, which locations?
5. Are there any insights into what may be driving these changes?
6. What other meaningful insights and recommendations can be obtained from this data?

## Usage Instructions
1. Review the provided Invoice Master and Supplier Table data.
2. Extract relevant information such as recipient locations, entities, shipper locations, and supplier details.
3. Analyze the data to address the questions outlined above.
4. Formulate insights and recommendations based on the analysis.

## Further Steps
Identify any additional questions arising from the data that require further probing and investigation.

## Contributing
Feel free to contribute to the analysis by providing additional context or insights.


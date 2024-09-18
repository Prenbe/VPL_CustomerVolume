# VPL Internal Notes

## Customer and Purchase Order (PO) Data Insights
When a customer isn’t meeting their goals:
- **PO and AP Data**: Every time a customer places an order, it generates a Purchase Order (PO). When orders decrease, the number of POs may decrease as well. If PO activity does not change, examining **Managed and AP data** could indicate that shipment volume is going through **Pre Pay & Add (PPA)**, meaning it's not captured in Accounts Payable (AP) data.

### Mayo Clinic Insights:
- **Hidden Tier**: The Mayo Clinic uses a **hidden tier with Vizient**, which is more aggressive than other programs. It leverages **gain shares**, where benchmark pricing is higher than institutions like Duke.

## Rate Table Upload Process
Each year, VPL receives updated rate tables from carriers that need to be processed and uploaded. The process involves:
1. **Receiving rate tables** from Accounting/Billing.
2. **Data Analysts** transforming the data into an appropriate format.
3. **Retroactively terminating** old rates and uploading new ones via Engineering.
4. **Validation** of the upload before moving to production.

### Key Rate Groups (FedEx/UPS):
- **FedEx**: Different rate groups include:
  - FedEx List Rates
  - HealthTrust Rates
  - Ascension Pricing
  - UNC FedEx Pricing
- **UPS**: Includes Daily Rates, Healthcare Rates, and NASPO Multi-Base Agreements, among others.

## Competitor Comparison: Optifreight/Cardinal Health vs. Triose vs. VPL
- **Optifreight (Cardinal Health)**: Exclusively uses FedEx for its shipments.
- **Triose**: Works exclusively with UPS.
- **VPL**: Stands out because it integrates both FedEx and UPS, allowing VPL to leverage more suppliers and drive higher volume through multiple carriers. This results in more flexibility and a higher volume uplift (around 15%). This gives VPL a competitive advantage by offering better pricing and volume.

### Uplift:
This refers to the additional volume VPL can capture compared to competitors, driving about 15-20% more volume than other programs.

## Percept & Data Latency
- **Percept**: VPL's analytics platform for reporting and data visualization. **Percept won’t show any shipments with a ship date within the last month** because only 95% of shipments are processed in 2-3 weeks, with the rest taking up to 4 weeks. This means shipments may not be up-to-date in the database.

## Sales Analysis Process
Sales analyses are now managed through **Jira** (previously Trello) and typically involve:
- The **sales team** gathering data from prospects and creating a Jira ticket for the **data team** to analyze.
- The **data team** compiles the necessary data, such as shipment volumes and managed/unmanaged costs.
- Key team members like **Vince, Paige, Nikos, and Isaiah** review the analysis before presenting it to the customer.

### Example Sales Analysis:
- **St. Luke’s Savings Analysis**: The file includes several tabs:
  - The **top sheet** summarizes savings.
  - The second tab focuses on **inbound shipments**.
  - The third tab analyzes **outbound shipments**.
  - It details freight and fuel data from a previous RFP and compares historical rates to VPL’s program.

## Freight Management Terminology
- **Actual Weight vs. Billed Weight**: The actual weight is calculated in 0.1 increments, while the billed weight is rounded to the nearest whole number.
- **Service Base**: Refers to the type of shipping service (e.g., Ground, Overnight).
- **Cross Charge**: Allocating shipment costs across multiple cost centers, which adds extra charges.
- **PPA (Pre-Pay & Add)**: When the supplier uses their own shipping method and charges the customer.
- **Dimensional Weight Pricing**: A billing method based on the size (volume) of the package rather than its actual weight.
- **Zone**: The geographical distance between the shipment origin and destination. Rates typically increase with the distance between zones.
- **Accessorial Fees**: Extra charges for additional services like fuel surcharges, residential delivery, or liftgate usage.
- **LTL (Less Than Truckload)**: A shipping method where multiple customers' shipments share space on a truck, splitting the cost.
- **FOB (Free on Board)**: Defines when the ownership of a shipment transfers from the seller to the buyer and who pays for shipping.
- **Bill of Lading (BOL)**: A legal document between the shipper and carrier detailing the goods being transported.
- **Freight Class**: A classification system based on factors like density, value, and handling needs, used for pricing LTL shipments.
- **Drayage**: Short-distance transport, typically between ports, warehouses, or rail terminals.

## Historical Data and DAR (Detail Activity Report)
**Historical DAR Data** shows suppliers' participation in past programs. This data:
- Assists with **sales guarantees**.
- Helps with **pricing negotiations** and auditing.

This allows VPL to establish benchmarks for **supplier compliance** and customer savings.

## Rate Table Upload Process Automation
VPL uses an R script to automate the preparation of rate tables:
1. Ensuring tab names match a pre-approved list.
2. Correcting the format for zones, weights, and dates.
3. Preparing a CSV file for Engineering to upload.

## Implementation Process
The process starts with a **kick-off**, followed by **setup**, **testing/training**, and finally **go-live**. After go-live, QA ensures the correct data flow, especially the AP and PO files provided by the **data team**. Customers are gradually integrated into **Percept**, though **Percept data takes about 30 days to seed** fully.

## Reporting and Analysis
VPL provides regular reports, such as:
- **QBR (Quarterly Business Reviews)**.
- **Aging and Unbilled Reports** for **Advance** and **Surpass** programs.
- **Sales Analyses** comparing savings between current and legacy shipping methods.

### Managed vs. Unmanaged Spend:
- **Managed Spend**: Shipments processed through VPL’s platform.
- **Unmanaged Spend**: Shipments outside VPL’s program, often reflected in **Accounts Payable** data.

## Pharmacy Solutions: Traject RX
**Traject RX** is VPL's platform for **pharmacy outbound shipments** and is one of its fastest-growing services. It includes:
- **Shipping insurance** for high-value drugs.
- Integration with **pharmacy management systems**, streamlining reporting and processes.

## Freight Management Overview
- **Inbound Freight**: Involves auditing and managing suppliers' shipments to reduce costs and improve compliance.
- **Outbound Freight**: Managed through the **Traject** platform, focused on pharmacy deliveries and high-value goods.

### Advanced Freight Auditing:
- **Dimensional Weight Pricing**: Billed weight is adjusted based on the package dimensions.
- **Zone Jump**: Carriers batch shipments together and adjust pricing based on the total weight of the batch.

## Key Tools:
- **Percept**: VPL's data analytics and reporting platform.
- **Power BI**: Used for detailed compliance trend reports and supplier audits.
- **Traject RX**: Portal for managing pharmacy-related shipments.
- **VPL View**: Provides visibility into inbound shipments, allowing customers to track products more effectively.

## Miscellaneous Notes:
- **Advance**: VPL’s primary inbound program.
- **Surpass**: A more standardized, scalable program that simplifies customer billing compared to Advance.
- **RFP (Request for Proposal)**: Documents that VPL uses to bid for new business, often comparing current and potential shipping rates.
- **LTL (Less Than Truckload)**: Freight shipped in smaller quantities that don't fill a full truck, shared by multiple customers.
- **Pre-Pay & Add (PPA)**: Freight costs where suppliers use their own shipping methods and charge customers accordingly.


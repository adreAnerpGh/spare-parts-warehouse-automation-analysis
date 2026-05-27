# Dataset & Field Dictionary

This document describes the main operational fields used across the spare-parts warehouse analysis project.

The datasets reproduce a realistic ERP/WMS-inspired spare-parts warehouse environment used for inventory-control, replenishment, warehouse operations, and warehouse automation analyses.

---

# part_master.csv

Core spare-parts master dataset containing:
- inventory classifications
- movement indicators
- physical dimensions
- warehouse references
- supplier references
- warehouse automation inputs

| Field                | Description                                          |
| -------------------- | ---------------------------------------------------- |
| Part_ID              | Anonymised spare-part identifier                     |
| Part_Name            | Spare-part description                               |
| Equipment_Family     | Equipment category associated with the spare part    |
| Equipment_Model      | Equipment model associated with the spare part       |
| Part_Category        | Functional spare-part category                       |
| Demand_Profile       | Demand-behaviour profile used for inventory analysis |
| Criticality          | Operational criticality level of the spare part      |
| Supplier_ID          | Primary supplier identifier                          |
| Supplier_Region      | Supplier geographical region                         |
| Unit_Cost_EUR        | Unit inventory cost in EUR                           |
| Storage_Type         | Storage handling category                            |
| Lifecycle_Status     | Inventory lifecycle classification                   |
| Target_Service_Level | Target inventory service level                       |
| ABC_Class            | Inventory-value classification                       |
| Movement_Class       | Warehouse movement-frequency classification          |
| Movement_Lines_36M   | Total warehouse movement lines over 36 months        |
| Avg_Monthly_Lines    | Average monthly warehouse movements                  |
| Manual_Location      | Original manual warehouse location                   |
| UDC_Type             | Handling/container type                              |
| Dim_X_mm             | Part dimension X in millimetres                      |
| Dim_Y_mm             | Part dimension Y in millimetres                      |
| Dim_Z_mm             | Part dimension Z in millimetres                      |
| Unit_Volume_cm3      | Unit volume in cubic centimetres                     |
| Max_Dimension_mm     | Largest physical dimension                           |
| Min_Dimension_mm     | Smallest physical dimension                          |
| Stock_Managed        | Indicator for stock-managed parts                    |
| Lead_Time_Weeks      | Average replenishment lead time                      |
| Safety_Stock_Qty     | Safety-stock quantity                                |
| Reorder_Point_Qty    | Reorder threshold quantity                           |
| Max_Stock_Qty        | Maximum stock target                                 |
| Stock_Qty            | Current stock quantity                               |

---

# supplier_master.csv

Supplier-level operational dataset.

| Field              | Description                     |
| ------------------ | ------------------------------- |
| Supplier_ID        | Supplier identifier             |
| Supplier_Name      | Anonymised supplier name        |
| Supplier_Region    | Supplier geographical region    |
| Avg_Lead_Time_Days | Average replenishment lead time |
| Lead_Time_SD_Days  | Lead-time variability           |
| Reliability_Score  | Supplier reliability indicator  |
| Default_Incoterm   | Default purchasing incoterm     |

---

# demand_history_weekly.csv

Weekly spare-parts demand history.

| Field         | Description                     |
| ------------- | ------------------------------- |
| Week_Start    | Weekly demand reference date    |
| Part_ID       | Spare-part identifier           |
| Demand_Qty    | Weekly demand quantity          |
| Order_Lines   | Warehouse order lines/movements |
| Demand_Source | Demand source category          |

---

# inventory_status.csv

Current inventory and replenishment-status dataset.

| Field                       | Description                          |
| --------------------------- | ------------------------------------ |
| Part_ID                     | Spare-part identifier                |
| On_Hand_Qty                 | Physical stock quantity              |
| On_Order_Qty                | Quantity already ordered             |
| Allocated_Qty               | Quantity allocated to operations     |
| Available_Qty               | Available usable stock               |
| Avg_Weekly_Demand           | Average weekly demand                |
| Demand_SD                   | Demand standard deviation            |
| Demand_CV                   | Demand coefficient of variation      |
| XYZ_Class                   | Demand-variability classification    |
| Safety_Stock_Qty            | Safety-stock quantity                |
| Reorder_Point_Qty           | Reorder threshold                    |
| Suggested_Replenishment_Qty | ERP/WMS replenishment recommendation |
| Planner_Exception_Flag      | ERP/WMS replenishment exception flag |

---

# purchase_requisitions.csv

ERP-style replenishment workflow dataset.

| Field                   | Description                          |
| ----------------------- | ------------------------------------ |
| Purchase_Requisition_ID | Purchase requisition identifier      |
| Part_ID                 | Spare-part identifier                |
| Supplier_ID             | Supplier identifier                  |
| Requested_Qty           | Requested replenishment quantity     |
| Estimated_Value_EUR     | Estimated requisition value          |
| Priority                | Replenishment priority               |
| Reason_Code             | Replenishment trigger reason         |
| Status                  | Purchase requisition workflow status |
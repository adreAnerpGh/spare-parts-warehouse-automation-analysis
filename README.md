# Spare-Parts Warehouse Analysis & Automated Warehouse Transition

This repository contains an end-to-end supply-chain, inventory-planning and warehouse-engineering analysis of a spare-parts warehouse environment using simulated ERP/WMS-derived operational datasets.

The project evaluates inventory performance, replenishment workflows, warehouse operations and selective warehouse automation opportunities within a realistic spare-parts environment.

The project evaluates how selective warehouse automation can improve:
- warehouse accessibility
- storage density
- picking efficiency
- inventory visibility
- operational workload distribution

The analyses include:

- inventory classification and demand segmentation
- warehouse structure and occupied-volume analysis
- inventory-control and replenishment planning
- ERP-style inventory planner workflows
- supplier and replenishment exposure analysis
- operational control-tower dashboard development
- Power BI reporting dataset preparation
- automated warehouse feasibility evaluation
- tray configuration and storage allocation logic
- warehouse transition evaluation

The project combines:
- inventory analytics
- warehouse-engineering logic
- replenishment planning
- ERP-style decision support
- operational KPI monitoring
- business-intelligence reporting
- warehouse automation analysis

The datasets included in this repository were anonymised, partially reconstructed and reduced in scale to preserve the operational logic of the original analyses while avoiding disclosure of proprietary operational information.

# Dashboard Outputs

The repository includes operational control-tower dashboards [operational control-tower dashboards](outputs/reports/supply_chain_operational_dashboard.html) generated from ERP-style inventory-planning and warehouse-operation datasets.

Dashboard components include:

- Supply Chain Control Tower
- Planner Exception Queue
- Supplier Review Queue
- Inventory Service-Level Monitoring
- Warehouse Transition Dashboard

The dashboards are designed to simulate the type of operational decision-support views commonly used by inventory planners, supply-chain analysts and ERP users.

Power BI datasets and standalone HTML dashboard outputs are generated throughout the project for reporting and visualisation purposes.


# Repository Structure

spare-parts-warehouse-automation-analysis/
│
├── data/
│
├── notebooks/
│
│   ├── 01_business_context.ipynb
│   ├── 02_operational_data_validation.ipynb
│
│   ├── 03_inventory_classification_analysis.ipynb
│   ├── 04_inventory_structure_analysis.ipynb
│   ├── 05_inventory_control_analysis.ipynb
│   ├── 06_replenishment_workflow_analysis.ipynb
│   ├── 07_powerbi_reporting_dataset_preparation.ipynb
│
│   ├── 08_automated_warehouse_feasibility_analysis.ipynb
│   ├── 09_tray_configuration_optimisation.ipynb
│   ├── 10_warehouse_transition_evaluation.ipynb
│
│   ├── 11_erp_inventory_planning_workspace.ipynb
│   ├── 12_operational_control_tower_dashboard.ipynb
│
├── docs/
│
├── outputs/
│
├── powerbi/
│
├── README.md
├── LICENSE
└── .gitignore


# Technologies Used

- Python
- pandas
- NumPy
- matplotlib
- Jupyter Notebook
- Power BI
- CSV-based reporting datasets


# Key Topics

- Spare-parts warehouse operations
- Inventory analytics
- ABC / XYZ inventory segmentation
- Warehouse movement analysis
- Inventory-control workflows
- Replenishment planning
- Warehouse automation feasibility
- Tray allocation optimisation
- Warehouse transition engineering
- Power BI operational reporting
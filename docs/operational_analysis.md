
# Operational & Inventory Analysis

This section of the repository focuses on operational inventory behaviour, replenishment logic, inventory segmentation, and operational monitoring.

Related notebooks:
- `03_inventory_classification_analysis.ipynb`
- `04_inventory_structure_analysis.ipynb`
- `05_inventory_control_analysis.ipynb`
- `06_replenishment_workflow_analysis.ipynb`
- `07_powerbi_reporting_dataset_preparation.ipynb`

---

# Inventory Classification Logic

The project uses multiple inventory classifications to support operational analyses.

## ABC Classification

ABC analysis evaluates inventory importance primarily from an inventory-value perspective.

Typical interpretation:
- A → high-impact inventory
- B → medium-impact inventory
- C → lower-impact inventory

---

## XYZ Classification

XYZ analysis evaluates demand variability and predictability.

Typical interpretation:
- X → stable demand
- Y → moderate variability
- Z → intermittent or unpredictable demand

XYZ analysis supports:
- replenishment evaluation
- inventory-risk analysis
- safety-stock logic
- operational monitoring

---

## Movement Classification

Movement classes evaluate warehouse operational activity and picking frequency.

Movement analysis is particularly important because operational warehouse activity is often concentrated within a limited subset of inventory items.

Typical movement interpretation:
- A+ → extremely high movement
- A → high movement
- B → medium movement
- C → lower movement
- D → very low movement
- NC → inactive or almost inactive

---

# Operational Analyses

The operational analyses focus on:
- inventory concentration patterns
- warehouse movement concentration
- slow-moving inventory
- replenishment priorities
- inventory-control indicators
- supplier lead-time impact
- operational KPIs
- inventory-risk exposure

The analyses reproduce operational inventory and warehouse-monitoring workflows commonly used in industrial spare-parts environments.
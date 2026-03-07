# Innovation Diffusion Modeling Report
## Electric Shaver Market Case Study
### Course: Marketing Analytics (DS 223)

---

# 1. Introduction

Technological innovations rarely spread instantly through a market. Instead, adoption typically follows a **diffusion process**, where a small group of early adopters is followed by a much larger group influenced by social interaction, visibility, and market penetration.

One of the most widely used models to analyze this process is the **Bass Diffusion Model**, developed by Frank Bass in 1969. The model explains how new products are adopted over time by considering two primary forces:

- **Innovation** – adoption driven by external influences such as advertising or technological novelty.
- **Imitation** – adoption driven by social influence and word-of-mouth.

This report applies the Bass diffusion model to analyze the **adoption dynamics of electric shavers in the global market**.

---

# 2. Data Source

Market data used in this project was derived from an industry report:

**Data Bridge Market Research – Global Electric Shaver Market Report**

The report provides:

- Market valuation
- Forecast growth rate
- Compound Annual Growth Rate (CAGR)

However, the report does not provide a complete historical dataset with yearly values.

---

# 3. Data Reconstruction Using CAGR

Because the report only provides a limited number of numerical observations, historical market values were reconstructed using the **Compound Annual Growth Rate (CAGR)**.

The CAGR formula is defined as:

``Future Value = Present Value × (1 + CAGR)^n``

Where:

- **CAGR** is the compound annual growth rate
- **n** represents the number of years

Using the known current market value and the CAGR provided in the report, earlier market values were estimated.

Historical market values were reconstructed using the CAGR provided in the Data Bridge Market Research report. This estimation approach follows **Fermi-style reasoning recommended in the assignment when full time-series datasets are unavailable**.

This method allows approximate historical values to be generated when only summary statistics are available.

---

# 4. Adoption Dataset Preparation

After reconstructing the market revenue dataset, the data was transformed to approximate **technology adoption levels**.

Revenue values were converted into an **adoption index**, which serves as a proxy for the number of adopters of electric shaver technology.

Additional variables were computed:

- **Yearly growth rate**
- **Adoption index**

This processed dataset provides a simplified representation of the adoption process required for Bass model estimation.

---

# 5. Bass Diffusion Model

The **Bass Diffusion Model** describes how new technologies spread through a population.

The model is expressed by the following equation:

``f(t) = (p + qF(t))(1 − F(t))``

Where:

- **p** = coefficient of innovation  
- **q** = coefficient of imitation  
- **F(t)** = cumulative adoption proportion  

The Bass model predicts an **S-shaped diffusion curve**.

The adoption process typically follows three phases:

1. **Early adoption phase** driven by innovators.
2. **Growth phase** where imitation accelerates adoption.
3. **Saturation phase** where adoption slows as the market approaches its maximum potential.

---

# 6. Parameter Estimation

The parameters of the Bass model were estimated using **nonlinear curve fitting** implemented with the SciPy optimization library.

The estimation process identifies three parameters:

- **p (innovation coefficient)** – representing adoption driven by external factors.
- **q (imitation coefficient)** – representing adoption driven by social influence.
- **M (market potential)** – representing the maximum possible adoption level.

These parameters determine the shape and speed of the diffusion curve.

---

# 7. Diffusion Visualization

The predicted adoption pattern was visualized using Python and Matplotlib.

```python
plt.figure(figsize=(10,6))
plt.plot(predicted,label="Predicted Adoption")
plt.scatter(t,sales,label="Historical")
plt.legend()
plt.title("Bass Diffusion Curve")
plt.xlabel("Time")
plt.ylabel("Adoption")
plt.savefig("img/diffusion_curve.png")
plt.show()
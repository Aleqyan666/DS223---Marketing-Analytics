 # Innovation Diffusion Analysis – AI Electric Shaver

## Overview

This project analyzes the diffusion of a modern consumer innovation using the Bass diffusion model. The innovation selected is the Philips Norelco i9000 Prestige Ultra, which was featured in the TIME Best Inventions of 2025 list.

The goal of the project is to estimate how this innovation may diffuse in the market over time using historical data from a similar product category.

The analysis follows a typical marketing analytics workflow:

1. Select an innovation.
2. Identify a similar historical innovation.
3. Obtain or reconstruct historical market data.
4. Estimate Bass diffusion model parameters.
5. Predict future adoption patterns.

The Bass model is widely used in marketing science to describe how new products spread through a population.

---

## Selected Innovation

The selected innovation is the **Philips Norelco i9000 Prestige Ultra**, an AI-powered electric shaver that integrates sensors, machine learning, and adaptive shaving guidance.

Source:

TIME Best Inventions 2025
https://time.com/collections/best-inventions-2025/7318257/philips-norelco-i9000-prestige-ultra/

The device represents a new generation of grooming technology that combines traditional hardware with intelligent software systems.

---

## Analog Innovation

Electric shavers were selected as the analogous historical innovation.

Both innovations:

* perform the same core grooming function
* target the same consumer market
* follow similar product upgrade cycles
* are distributed globally by major consumer electronics companies

While traditional electric shavers introduced automated shaving through motorized blades, the AI-powered shaver improves the experience through intelligent sensors and personalized feedback.

Therefore, the diffusion pattern of electric shavers provides a reasonable basis for estimating the adoption trajectory of the newer AI-powered device.

---

## Data Source

Market information was derived from the following industry report:

Data Bridge Market Research
Global Electric Shavers Market
https://www.databridgemarketresearch.com/reports/global-electric-shavers-market

The report provides the current market size and expected growth rates for the global electric shaver industry.

---

## Data Reconstruction

The report provides the most recent market value and compound annual growth rate (CAGR) but does not provide a complete historical time series dataset.

Therefore, historical values were reconstructed using the compound annual growth rate.

Historical market values were reconstructed using the CAGR provided in the Data Bridge Market Research report. This estimation approach follows Fermi-style reasoning recommended in the assignment when full time-series datasets are unavailable.

The CAGR reconstruction formula used was:

``Value_previous = Value_current / (1 + CAGR)``

Using this approach, a time series dataset from 2010–2024 was generated.

---

## Methodology

The analysis was conducted in the following steps:

1. Generate the reconstructed dataset using CAGR.
2. Prepare an adoption proxy variable based on market size.
3. Estimate Bass model parameters using nonlinear regression.
4. Predict future adoption using the fitted model.
5. Visualize diffusion curves.

---

## Bass Diffusion Model

The Bass model describes how innovations spread through two mechanisms:

* Innovation effect (p): adoption driven by advertising or early adopters.
* Imitation effect (q): adoption driven by word-of-mouth and social influence.

The Bass model equation is:

``f(t) = (p + qF(t))(1 − F(t))``

Where:

p = coefficient of innovation
q = coefficient of imitation
M = market potential

---

## Repository Structure

```
dataset_with_cagr.py
bass_estimation.py
utils.py
bass_model_analysis.ipynb


data/
    electric_shaver_market_revenue.csv
    reconstructed_adoption.csv

img/
    diffusion_curve.png
    cumulative_adoption_curve.png

report/
    report_source.md
    report.pdf
```

---

## Scripts

### dataset_with_cagr.py

Generates the historical dataset using CAGR reconstruction.

### preparation_of_adoption.py

Calculates market growth and constructs an adoption index used for modeling.

### bass_estimation.py

Estimates Bass model parameters using nonlinear regression.

### utils.py

Contains the Bass model function used for parameter estimation.

---

## Notebook

The Jupyter notebook contains the full analysis workflow:

* dataset loading
* visualization of market growth
* Bass model estimation
* diffusion prediction
* graphical outputs

---

## Tools

Python
Jupyter Notebook
Pandas
NumPy
SciPy
Matplotlib

---

## Outputs

The project produces the following outputs:

* diffusion curve visualization
* cumulative adoption curve
* estimated Bass model parameters

---

## References

Data Bridge Market Research. Global Electric Shavers Market Report.
https://www.databridgemarketresearch.com/reports/global-electric-shavers-market

TIME Magazine. Best Inventions 2025.
https://time.com/collections/best-inventions-2025/

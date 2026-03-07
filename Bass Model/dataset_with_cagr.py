def GenerateData():

    import pandas as pd
    from loguru import logger

    market_2024 = 12.4   # billion USD

    # CAGR from report (approx)
    cagr = 0.047

    years = list(range(2010, 2025))
    values = []
    current = market_2024

    for year in reversed(years):
        values.insert(0, round(current,2))
        current = current/(1+cagr)

    data = pd.DataFrame({
        "Year": years,
        "Market_Billion_USD": values
    })

    data.to_csv(r"data\electric_shaver_market_revenue.csv", index=False)
    logger.info(data)
    return data

GenerateData()
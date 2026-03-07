import pandas as pd
import numpy as np
from scipy.optimize import curve_fit
from utils import bass_model

data = pd.read_csv("data/reconstructed_adoption.csv")

sales = data["adoption_index"].values
t = np.arange(len(sales))

params,_ = curve_fit(bass_model,t,sales,bounds=(0,[1,1,1000]))

p,q,M = params

print("Bass Model Parameters")
print("p =",p)
print("q =",q)
print("M =",M)
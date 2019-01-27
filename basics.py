import pandas as pd
import matplotlib.pyplot as plt
import utils as utils
df1 = pd.read_excel("1.xlsx")
df2 = pd.read_excel("2.xlsx")
df3 = pd.read_excel("3.xlsx")

print utils.allagecount(df2)
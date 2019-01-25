import pandas as pd
import matplotlib.pyplot as plt
import utils as utils
df1 = pd.read_excel("1.xlsx")
df2 = pd.read_excel("2.xlsx")
df3 = pd.read_excel("3.xlsx")

pos = list(range(len(df1['Survey'])))
width = 1.0/3.0


gender1 = utils.allgendercount(df1)
gender2 = utils.allgendercount(df2)
gender3 = utils.allgendercount(df3)
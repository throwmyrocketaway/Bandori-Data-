import pandas as pd
import matplotlib.pyplot as plt

df3 = pd.read_excel("3.xlsx")
fig = plt.figure(figsize=(18,6))

a=df3.columns.tolist()
print a
plt.subplot2grid((2,3),(0,0))
df3.gender.value_counts(normalize=True).plot(kind="bar",alpha=0.5)
plt.title("Gender")
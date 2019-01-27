import pandas as pd
import matplotlib.pyplot as plt
import utils as utils
from commvar import *
from matplotlib import rcParams
rcParams.update({'figure.autolayout': True})

df = pd.read_excel("3.xlsx")
fig = plt.figure(figsize=(18,6))

nam = utils.locgrab(strnam,df)
sam = utils.locgrab(strsam,df)
eur = utils.locgrab(streur,df)
sea = utils.locgrab(strsea,df)
oce = utils.locgrab(stroce,df)

# Age spread of people from each geographical region

plt.subplot2grid((2,3),(0,0))
nam.Age.value_counts(normalize=True).plot(kind="bar",alpha=0.5)
plt.title("Age spread of people from North America")

plt.subplot2grid((2,3),(0,1))
sam.Age.value_counts(normalize=True).plot(kind="bar",alpha=0.5)
plt.title("Age spread of people from South America")

plt.subplot2grid((2,3),(0,2))
eur.Age.value_counts(normalize=True).plot(kind="bar",alpha=0.5)
plt.title("Age spread of people from Europe")

plt.subplot2grid((2,3),(1,0))
sea.Age.value_counts(normalize=True).plot(kind="bar",alpha=0.5)
plt.title("Age spread of people from Southeast Asia")

plt.subplot2grid((2,3),(1,1))
oce.Age.value_counts(normalize=True).plot(kind="bar",alpha=0.5)
plt.title("Age spread of people from Oceania")

#plt.show(block=True)
plt.clf()

# Gender spread of people from each geographical region

plt.subplot2grid((2,3),(0,0))
nam.gender.value_counts(normalize=True).plot(kind="bar",alpha=0.5)
plt.title("Gender spread of people from North America")

plt.subplot2grid((2,3),(0,1))
sam.gender.value_counts(normalize=True).plot(kind="bar",alpha=0.5)
plt.title("Gender spread of people from South America")

plt.subplot2grid((2,3),(0,2))
eur.gender.value_counts(normalize=True).plot(kind="bar",alpha=0.5)
plt.title("Gender spread of people from Europe")

plt.subplot2grid((2,3),(1,0))
sea.gender.value_counts(normalize=True).plot(kind="bar",alpha=0.5)
plt.title("Gender spread of people from Southeast Asia")

plt.subplot2grid((2,3),(1,1))
oce.gender.value_counts(normalize=True).plot(kind="bar",alpha=0.5)
plt.title("Gender spread of people from Oceania")

#plt.show(block=True)
plt.clf()
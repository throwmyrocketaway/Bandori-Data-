import pandas as pd
import matplotlib.pyplot as plt
import utils as utils
from commvar import *
from matplotlib import rcParams
rcParams.update({'figure.autolayout': True})

df = pd.read_excel("3.xlsx")
fig = plt.figure(figsize=(18,6))
# Grabs all rows in which the relevant band is the respondents favourite
ppa = utils.bandgrab(strppa,df)
aft = utils.bandgrab(straft,df)
ppe = utils.bandgrab(strppe,df)
ros = utils.bandgrab(strros,df)
hhw = utils.bandgrab(strhhw,df)

# Reason why people like each band
plt.subplot2grid((2,3),(0,0))
ppa.Fbandreason.value_counts(normalize=True).plot(kind="bar",alpha=0.5,rot=45)
plt.title("Reasons why Poppin'Party is peoples favourite band")

plt.subplot2grid((2,3),(0,1))
aft.Fbandreason.value_counts(normalize=True).plot(kind="bar",alpha=0.5,rot=45)
plt.title("Reasons why Afterglow is peoples favourite band")

plt.subplot2grid((2,3),(0,2))
ppe.Fbandreason.value_counts(normalize=True).plot(kind="bar",alpha=0.5,rot=45)
plt.title("Reasons why Pastel Palettes is peoples favourite band")

plt.subplot2grid((2,3),(1,0))
ros.Fbandreason.value_counts(normalize=True).plot(kind="bar",alpha=0.5,rot=45)
plt.title("Reasons why Roselia is peoples favourite band")

plt.subplot2grid((2,3),(1,1))
hhw.Fbandreason.value_counts(normalize=True).plot(kind="bar",alpha=0.5,rot=45)
plt.title("Reasons why Hello, Happy World is peoples favourite band")

#plt.show(block=True)
plt.clf()

# Grabs all rows in which the relevant reason is the respondents favourite
mus = utils.reasongrab(strmus,df)
aes = utils.reasongrab(straes,df)
bme = utils.reasongrab(strbme,df)
sty = utils.reasongrab(strsty,df)
non = utils.reasongrab(strnon,df)
oth = utils.reasongrab(stroth,df)

# Bands for people who like each reason
plt.subplot2grid((2,3),(0,0))
mus.Fband.value_counts(normalize=True).plot(kind="bar",alpha=0.5,rot=45)
plt.title("Favourite bands for those focused on band music")

plt.subplot2grid((2,3),(0,1))
aes.Fband.value_counts(normalize=True).plot(kind="bar",alpha=0.5,rot=45)
plt.title("Favourite bands for those focused on band aesthetics")

plt.subplot2grid((2,3),(0,2))
bme.Fband.value_counts(normalize=True).plot(kind="bar",alpha=0.5,rot=45)
plt.title("Favourite bands for those focused on the band members")

plt.subplot2grid((2,3),(1,0))
sty.Fband.value_counts(normalize=True).plot(kind="bar",alpha=0.5,rot=45)
plt.title("Favourite bands for those focused on the band stories")

plt.subplot2grid((2,3),(1,1))
oth.Fband.value_counts(normalize=True).plot(kind="bar",alpha=0.5,rot=45)
plt.title("Favourite bands for those with other reasons")

#plt.show(block=True)
plt.clf()

# Age of people who most like each band

plt.subplot2grid((2,3),(0,0))
ppa.Age.value_counts(normalize=True).plot(kind="bar",alpha=0.5)
plt.title("Age of people who most like Poppin'Party")

plt.subplot2grid((2,3),(0,1))
aft.Age.value_counts(normalize=True).plot(kind="bar",alpha=0.5)
plt.title("Age of people who most like Afterglow")

plt.subplot2grid((2,3),(0,2))
ppe.Age.value_counts(normalize=True).plot(kind="bar",alpha=0.5)
plt.title("Age of people who most like Pastel Palettes")

plt.subplot2grid((2,3),(1,0))
ros.Age.value_counts(normalize=True).plot(kind="bar",alpha=0.5)
plt.title("Age of people who most like Roselia")

plt.subplot2grid((2,3),(1,1))
hhw.Age.value_counts(normalize=True).plot(kind="bar",alpha=0.5)
plt.title("Age of people who most like Hello, Happy World")

#plt.show(block=True)
plt.clf()

# Gender of people who like each band
plt.subplot2grid((2,3),(0,0))
ppa.gender.value_counts(normalize=True).plot(kind="bar",alpha=0.5)
plt.title("Gender of people who most like Poppin'Party")

plt.subplot2grid((2,3),(0,1))
aft.gender.value_counts(normalize=True).plot(kind="bar",alpha=0.5)
plt.title("Gender of people who most like Afterglow")

plt.subplot2grid((2,3),(0,2))
ppe.gender.value_counts(normalize=True).plot(kind="bar",alpha=0.5)
plt.title("Gender of people who most like Pastel Palettes")

plt.subplot2grid((2,3),(1,0))
ros.gender.value_counts(normalize=True).plot(kind="bar",alpha=0.5)
plt.title("Gender of people who most like Roselia")

plt.subplot2grid((2,3),(1,1))
hhw.gender.value_counts(normalize=True).plot(kind="bar",alpha=0.5)
plt.title("Gender of people who most like Hello, Happy World")

#plt.show(block=True)
plt.clf()

# Favourite bands of people in specific geographical regions

nam = utils.locgrab(strnam,df)
sam = utils.locgrab(strsam,df)
eur = utils.locgrab(streur,df)
sea = utils.locgrab(strsea,df)
oce = utils.locgrab(stroce,df)

plt.subplot2grid((2,3),(0,0))
nam.Fband.value_counts(normalize=True).plot(kind="bar",alpha=0.5,rot=45)
plt.title("Reason for liking favourite band of people from North America")

plt.subplot2grid((2,3),(0,1))
sam.Fband.value_counts(normalize=True).plot(kind="bar",alpha=0.5,rot=45)
plt.title("Reason for liking favourite band of people from South America")

plt.subplot2grid((2,3),(0,2))
eur.Fband.value_counts(normalize=True).plot(kind="bar",alpha=0.5,rot=45)
plt.title("Reason for liking favourite band of people from Europe")

plt.subplot2grid((2,3),(1,0))
sea.Fband.value_counts(normalize=True).plot(kind="bar",alpha=0.5,rot=45)
plt.title("Reason for liking favourite band of people from Southeast Asia")

plt.subplot2grid((2,3),(1,1))
oce.Fband.value_counts(normalize=True).plot(kind="bar",alpha=0.5,rot=45)
plt.title("Reason for liking favourite band of people from Oceania")

#plt.show(block=True)
plt.clf()

plt.subplot2grid((2,3),(0,0))
nam.Fbandreason.value_counts(normalize=True).plot(kind="bar",alpha=0.5,rot=45)
plt.title("Reason for liking favourite band of people from North America")

plt.subplot2grid((2,3),(0,1))
sam.Fbandreason.value_counts(normalize=True).plot(kind="bar",alpha=0.5,rot=45)
plt.title("Reason for liking favourite band of people from South America")

plt.subplot2grid((2,3),(0,2))
eur.Fbandreason.value_counts(normalize=True).plot(kind="bar",alpha=0.5,rot=45)
plt.title("Reason for liking favourite band of people from Europe")

plt.subplot2grid((2,3),(1,0))
sea.Fbandreason.value_counts(normalize=True).plot(kind="bar",alpha=0.5,rot=45)
plt.title("Reason for liking favourite band of people from Southeast Asia")

plt.subplot2grid((2,3),(1,1))
oce.Fbandreason.value_counts(normalize=True).plot(kind="bar",alpha=0.5,rot=45)
plt.title("Reason for liking favourite band of people from Oceania")

#plt.show(block=True)
plt.clf()
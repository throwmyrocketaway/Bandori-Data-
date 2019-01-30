import pandas as pd
import matplotlib.pyplot as plt
import utils as utils
from commvar import *
from matplotlib import rcParams
rcParams.update({'figure.autolayout': True})

df = pd.read_excel("3.xlsx")
fig = plt.figure(figsize=(18,6))

rjp = utils.regiongrab(strrjp,df)
rww = utils.regiongrab(strrww,df)
rtw = utils.regiongrab(strrtw,df)
rkr = utils.regiongrab(strrkr,df)

plt.subplot2grid((2,3),(0,0))
rjp.SpendJP.value_counts(normalize=True).plot(kind="bar",alpha=0.5,rot=45)
plt.title("Amount spent by people on JP server")

plt.subplot2grid((2,3),(0,1))
rww.SpendWW.value_counts(normalize=True).plot(kind="bar",alpha=0.5,rot=45)
plt.title("Amount spent by people on WW server")

plt.subplot2grid((2,3),(0,2))
rtw.SpendTW.value_counts(normalize=True).plot(kind="bar",alpha=0.5,rot=45)
plt.title("Amount spent by people on TW server")

plt.subplot2grid((2,3),(1,0))
rkr.SpendKR.value_counts(normalize=True).plot(kind="bar",alpha=0.5,rot=45)
plt.title("Amount spent by people on KR server")

#plt.show(block=True)
plt.clf()

###############################################################################
###                     More in depth habits solely from WW                 ###
###############################################################################

# Spending habits on WW server by favourite band

ppa = utils.bandgrab(strppa,rww)
aft = utils.bandgrab(straft,rww)
ppe = utils.bandgrab(strppe,rww)
ros = utils.bandgrab(strros,rww)
hhw = utils.bandgrab(strhhw,rww)
non = utils.bandgrab(strnon,rww)

#plt.subplot2grid((2,3),(0,0))
#rww.Fband.value_counts(normalize=True).plot(kind="bar",alpha=0.5,rot=45)
#plt.title("Favourite band for WW players")

#plt.show(block=True)
#plt.clf()

utils.plotter23(ppa.SpendWW,"Amount spent by Poppin'Party Fans",True,(0,0))
utils.plotter23(aft.SpendWW,"Amount spent by Afterglow Fans",True,(0,1))
utils.plotter23(ppe.SpendWW,"Amount spent by Pastel Palettes Fans",True,(0,2))
utils.plotter23(ros.SpendWW,"Amount spent by Roselia Fans",True,(1,0))
utils.plotter23(hhw.SpendWW,"Amount spent by Hello, Happy World Fans",True,(1,1))
#plt.show(block=True)
plt.clf()

# Spending habits on WW server by gender

mle = utils.gendergrab(strmle,rww)
fme = utils.gendergrab(strfme,rww)
oge = utils.gendergrab(stroge,rww)
pge = utils.gendergrab(strpge,rww)

utils.plotter23(mle.SpendWW,"Amount spent by Men",True,(0,0))
utils.plotter23(fme.SpendWW,"Amount spent by Women",True,(0,1))
utils.plotter23(oge.SpendWW,"Amount spent by Other",True,(0,2))
utils.plotter23(pge.SpendWW,"Amount spent by 'Prefer not to say'",True,(1,0))
plt.show(block=True)
plt.clf()
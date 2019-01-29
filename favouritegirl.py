import pandas as pd
import matplotlib.pyplot as plt
import utils as utils
from commvar import *
from matplotlib import rcParams
rcParams.update({'figure.autolayout': True})
import numpy as np

df = pd.read_excel("3.xlsx")
# Grab each repsondents favourite band, seperate by answer
ppa = utils.bandgrab(strppa,df)
aft = utils.bandgrab(straft,df)
ppe = utils.bandgrab(strppe,df)
ros = utils.bandgrab(strros,df)
hhw = utils.bandgrab(strhhw,df)

counts,relcounts = utils.bestgirliter(df)
ppacounts,pparelcounts = utils.bestgirliter(ppa)
aftcounts,aftrelcounts = utils.bestgirliter(aft)
ppecounts,pperelcounts = utils.bestgirliter(ppe)
roscounts,rosrelcounts = utils.bestgirliter(ros)
hhwcounts,hhwrelcounts = utils.bestgirliter(hhw)


#plt.subplot2grid((2,3),(0,0))
#y_pos = np.arange(len(counts))
#labels =["Favourite girl is from favourite band", "Favourite girl isn't from favourite band"]
#plt.bar(y_pos,relcounts,align='center',alpha=0.5)
#plt.xticks(y_pos,labels)
#plt.title("Spread of people whose favourite girl is from their favourite band (Overall)")

print relcounts
print pparelcounts
print aftrelcounts
print pperelcounts
print rosrelcounts
print hhwrelcounts

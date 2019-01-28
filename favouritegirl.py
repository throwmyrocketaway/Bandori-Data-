import pandas as pd
import matplotlib.pyplot as plt
import utils as utils
from commvar import *
from matplotlib import rcParams
rcParams.update({'figure.autolayout': True})
import numpy as np

df = pd.read_excel("3.xlsx")

#countyes = 0
#for i in range(len(df)):
 #   a = utils.bandmem(df.Fband[i])
  #  if a != 0:
   #     for k in a:
    #        if k == df.Bestgirl[i]:
     #           countyes += 1
countyes = 913        
countno = totresponses - countyes
relyes = float(countyes)/totresponses
relno = float(countno)/totresponses
counts=[countyes,countno]
relativecounts = [relyes,relno]
y_pos = np.arange(len(counts))
labels =["Favourite girl is from favourite band", "Favourite girl isn't from favourite band"]

plt.bar(y_pos,relativecounts,align='center',alpha=0.5)
plt.xticks(y_pos,labels)
plt.title("Spread of people whose favourite girl is from their favourite band")
plt.show()


    
print df.loc
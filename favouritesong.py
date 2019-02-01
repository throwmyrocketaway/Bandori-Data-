import pandas as pd
import matplotlib.pyplot as plt
import utils as utils
from commvar import *
from matplotlib import rcParams
rcParams.update({'figure.autolayout': True})

df = pd.read_excel("3.xlsx")
fig = plt.figure(figsize=(18,6))

inp = pd.read_excel("song editing.xlsx")
ppa = utils.bandgrab(strppa,inp)
aft = utils.bandgrab(straft,inp)
ppe = utils.bandgrab(strppe,inp)
ros = utils.bandgrab(strros,inp)
hhw = utils.bandgrab(strhhw,inp)

print utils.banditer(inp)
print utils.banditer(ppa)
print utils.banditer(aft)
print utils.banditer(ppe)
print utils.banditer(ros)
print utils.banditer(hhw)

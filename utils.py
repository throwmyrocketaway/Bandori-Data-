import matplotlib.pyplot as plt
from commvar import *
def gendercount(x,y):
    count = 0
    for i in x['gender']:
        if i == y:
            count += 1
    return count

def allgendercount(x):
    male=gendercount(x,'Male')
    female=gendercount(x,'Female')
    other=gendercount(x,'Other')
    pnts=gendercount(x,'Prefer not to say')
    result = [male,female,other,pnts]
    return result

def agecount(x,y):
    count = 0
    for i in x['Age']:
        if i==y:
            count +=1 
    return count


def allagecount(x):
    age1 = agecount(x,'Under 13')
    age2 = agecount(x, '14-19')
    age3 = agecount(x,'20-24')
    age4 = agecount(x,'25-29')
    age5 = agecount(x,'30-34')
    age6 = agecount(x,'35-39')
    age7 = agecount(x,'40+')
    age8 = agecount(x,'Prefer not to say')
    result=[age1,age2,age3,age4,age5,age6,age7,age8]
    return result

def bandgrab(x,y):
    result =y.loc[y['Fband']==x]
    return result

def agegrab(x,y):
    result = y.loc[y['Age']==x]
    return result

def reasongrab(x,y):
    result = y.loc[y['Fbandreason']==x]
    return result

def locgrab(x,y):
    result = y.loc[y['location']==x]
    return result
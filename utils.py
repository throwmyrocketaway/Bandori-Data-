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

def gendergrab(x,y):
    result = y.loc[y['gender']==x]
    return result


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

def regiongrab(x,y):
        if x == strrjp:
            result = y.loc[y['StatusJP']== "Yes"]
        elif x == strrww:
            result = y.loc[y['StatusWW']== "Yes"]
        elif x==strrtw:
            result = y.loc[y['StatusTW']== "Yes"]
        elif x==strrkr:
            result = y.loc[y['StatusKR']== "Yes"]
        return result
def bandmem(x):
    if x == strppa:
        return ppamem
    elif x==strros:
        return rosmem
    elif x==straft:
        return aftmem
    elif x==strppe:
        return ppemem
    elif x==strhhw:
        return hhwmem
    elif x==strras:
        return rasmem
    elif x==strglg:
        return glgmem
    else:
        return 0

def bestgirliter(x):
    tot = len(x)
    resultyes = 0
    for i in range(tot):
        b = bandmem(x.Fband.iloc[i])
        if b != 0:
            for k in b:
                if k==x.Bestgirl.iloc[i]:
                    resultyes += 1
                    break
    resultno = tot - resultyes
    relyes = float(resultyes)/tot
    relno = float(resultno)/tot
    results = [resultyes,resultno]
    relresults = [relyes,relno]
    return results,relresults

def banditer(x):
    tot = len(x)
    resultyes = 0
    for i in range(tot):
        if x.Fband.iloc[i]==x.Csong.iloc[i]:
            resultyes +=1
    resultno = tot-resultyes
    relyes = float(resultyes)/tot
    relno = float(resultno)/tot
    return [resultyes,resultno], [relyes,relno]

def plotter23(x,reason,norm,y):
    plt.subplot2grid((2,3),y)
    x.value_counts(normalize=norm).plot(kind="bar",alpha=0.5,rot=45)
    plt.title(reason)
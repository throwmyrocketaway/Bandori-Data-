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
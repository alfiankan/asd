

def apakahKabisat(thn):
    if thn%4 == 0:
        if thn%4==0 and thn%100!=0:
            return True
        elif thn%100==0 and thn%400!=0:
            return False
        elif thn%100==0 and thn%400==0:
            return True
    else:
        return False

print(apakahKabisat(1896))
print(apakahKabisat(1897))
print(apakahKabisat(1900))
print(apakahKabisat(2000))
print(apakahKabisat(2004))
print(apakahKabisat(2008))
print(apakahKabisat(2012))
print(apakahKabisat(2016))
print(apakahKabisat(2096))
print(apakahKabisat(2100))
print(apakahKabisat(2200))
print(apakahKabisat(2300))
print(apakahKabisat(2400))

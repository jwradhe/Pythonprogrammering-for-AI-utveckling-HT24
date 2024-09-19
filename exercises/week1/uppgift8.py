
def countUpperStr (myStr):
    countUpper = sum(map(str.isupper, myStr))
    if countUpper >= 2:
        return myStr.upper()
    else:
        return myStr

print(countUpperStr("En Sträng"))

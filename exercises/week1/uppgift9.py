def is_reverse(myStr):
    if len(myStr) % 4 == 0:
        return myStr[::-1]
    else: 
        return myStr

print(is_reverse("cyka"))

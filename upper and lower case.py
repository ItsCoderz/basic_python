def string_test(a,b):
    d={"UPPER_CASE":0,"LOWER_CASE":0}
    s="".join([a,b])
    for c in s:
        if c.isupper():
            d["UPPER_CASE"]+=1
        elif c.islower():
            d["LOWER_CASE"]+=1
        else:
            pass
    print ("Original_string : ", a,b)
    print ("No. of Upper case charscters :",d["UPPER_CASE"])
    print ("No. of Lower case charscters :",d["LOWER_CASE"])

string_test('The quick','brow Fox')


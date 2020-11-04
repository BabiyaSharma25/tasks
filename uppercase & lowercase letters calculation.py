def string(s):
    d={"uppercase":0, "lowercase":0}
    for c in s:
        if c.isupper():
           d["uppercase"]+=1
        elif c.islower():
           d["lowercase"]+=1
        else:
           pass
    print ("No. of Upper case characters : ", d["uppercase"])
    print ("No. of Lower case Characters : ", d["lowercase"])

string('The quick Brown Fox')
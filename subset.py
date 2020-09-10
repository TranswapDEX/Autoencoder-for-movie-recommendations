def subset(x):
    m=[]
    if not x:
        m.append(x)
    else:
        A = x[0]
        B = x[1:]
        for z in subset(B):
            m.append(z)
            r = [A] + z
            m.append(r)
    return m

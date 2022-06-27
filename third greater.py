def greater(a):
    i=0
    max=a[0]
    while i<len(a):
        if a[i]>max:
            max=a[i]
        i=i+1
    print("greater number",max)
    i=0
    max1=a[0]
    while i<len(a):
        if a[i]>max1:
            if a[i]!=max:
                max1=a[i]
        i=i+1
    print("second greater",max1)
    i=0
    max2=a[0]
    while i<len(a):
        if a[i]>max2:
            if a[i]!=max and a[i]!=max1:
                max2=a[i]
        i=i+1
    print("third greater",max2)
greater([-21,-34,-86,-1,-57,-5,-67,-7,-6])
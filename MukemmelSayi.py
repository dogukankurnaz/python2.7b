x=[]
for a in range(2,1000):
    t=0
    for i in range(1,a):
        if a%i==0:
            t+=i
    if t==a:
        x.append(a)

print "2-1000 arasýnda",len(x),"adet mükemmel sayi var"
print x

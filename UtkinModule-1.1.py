'''
UtkinModule-1.1
'''
def SumArPr1(a1,an,n):
    '''
SumArPr1(a1,an,n)
Calculates the sum of the arythmetic progression. (float)
a1 - first number (float)
an - last number (float)
n - amount of numbers (int, >0)
    '''
    return (a1+an)*n/2

def SumArPr2(a1,d,n):
    '''
SumArPr2(a1,d,n)
Calculates the sum of the arythmetic progression. (float)
a1 - first number (float)
d - difference between numbers (float, !=0)
n - amount of numbers (int, >0)
    '''
    return (2*a1+d*(n-1))*n/2

def SumGeomPr(b1,q,n):
    '''
SumGeomPr(b1,q,n)
Calculates the sum of the geometric progression. (float)
b1 - first number (float, !=0)
q - factor between numbers (float, !=0, !=1)
n - amount of numbers (int, >0)
    '''
    return b1*(q**n-1)/(q-1)

def SumGeomLim(b1,q):
    '''
SumGeomLim(b1,q)
Calculates the sum of the infinitely decreasing geometric progression. (float)
b1 - first number (float, !=0)
q - factor between numbers (float, 0<q<1)
    '''
    return b1/(1-q)

def bubblesort(a):
    '''
bubblesort(a)
Sorts the list. (list)
a - original list (list)
    '''
    N=len(a)
    for i in range(N-1):
        for j in range(N-i-1):
            if a[j] > a[j+1]:
                a[j],a[j+1]=a[j+1],a[j]
    return a

def quicksort(a):
    '''
quicksort(a)
Sorts the list. (list)
a - original list (list)
    '''
    from random import choice
    if len(a)<=1:
        return a
    else:
        q=choice(a)
        s=[]
        m=[]
        e=[]
        for n in a:
            if n<q:
                s.append(n)
            elif n>q:
                m.append(n)
            else:
                e.append(n)
        return quicksort(s) + e + quicksort(m)
    
def dictsortkeys(d):
    '''
dictsortkeys(d)
Sorts the dict by keys. (dict)
d - original dict (dict)
    '''
    d2=dict()
    d_keys=list(d.keys())
    d_keys.sort()
    for i in d_keys:
        d2[i]=d[i]
    return d2

def dictsortvalues(d):
    '''
dictsortvalues(d)
Sorts the dict by values. (dict)
d - original dict (dict)
    '''
    d2=dict()
    d_list=list()
    for i in d.keys():
        d_list+=[[d[i],i]]
    d_list.sort(key=lambda i: i[0])
    for i in d_list:
        d2[i[1]]=i[0]
    return d2

def listcount(m,el):
    '''
listcount(m,el)
Counts how many copies of the element are in the list. (int)
m - list (list)
el - element (any)
    '''
    if el not in m:
        return 0
    else:
        k=0
        for i in m:
            if el==i:
                k+=1
        return k
    
def listfind(m,el):
    '''
listfind(m,el)
Finds the index of the first copy of the element in the list. (int)
m - list (list)
el - element (any)
    '''
    if el not in m:
        return -1
    else:
        for i in range(len(m)):
            if m[i]==el:
                return i
            
def nod(x,y):
    '''
nod(x,y)
Calculates the greatest common divisor of two numbers. (int)
x,y - numbers (int, >0)
    '''
    x,y=min(x,y),max(x,y)
    if y%x==0:
        return x
    else:
        return nod(x,y%x)
    
def nok(x,y):
    '''
nok(x,y)
Calculates the least common multiple of two numbers. (int)
x,y - numbers (int, >0)
    '''
    return int(x*y/nod(x,y))

def fracred(a,b):
    '''
fracred(a,b)
Reduces the fraction a/b. (tuple)
a,b - numbers (int, b!=0)
    '''
    if a==0:
        return (0,1)
    k=0
    if (a>0 and b>0) or (a<=0 and b<0):
        k=1
    a,b=abs(a),abs(b)
    n=nod(a,b)
    while n!=1:
        a//=n
        b//=n
        n=nod(a,b)
    if k==1:
        return (a,b)
    return (0-a,b)

def TrNumSys(n,s1,s2):
    '''
TrNumSys(n,s1,s2)
Transfers the number to another numeral system. (str)
n - number (str, in n10 >0)
s2,s2 - numeral systems (int, 1<{s1,s2}<36)
    '''
    b=['0','1','2','3','4','5','6','7','8','9','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
    n10=int(n,base=s1)
    if s2==10:
        return n10
    i=''
    while n10>0:
        i=i+b[n10%s2]
        n10//=s2
    return i[::-1]

def dictfilter(d,m):
    '''
dictfilter(d,m)
Filters the dict by keys from the list. (dict)
d - dict (dict)
m - list (list)
    '''
    d2=dict()
    for i in m:
        d2[i]=d[i]
    return d2

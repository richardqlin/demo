word  = input('enter a word')
shift =int(input('enter a shift number'))


alphi = 'abcdefghijklmnopqrstuvwxyz'

num = '1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18  19 20 21 22 23 24 25 26'

al=list(alphi)

num = num.split()

d = dict(zip(al, num))
#print(d)

##d = {'a':1,'b':2,'c':3,'d':4, 'e':5,'f':6,'g':7,'h':8,'i':9,\
##    'j':10,'k':11,'l':12,'m':13,'n':14,'o':15, 'p':16,'q':17,'r':18,\
##     's':19,'t':20,
##     }

def get_key(val):
    global d
    for k, v in d.items():
        if val == int(v):
            return k

def cipher(w, n ):
    global d
    for i in w:
        a = int(d[i]) + n
        b=get_key(a)
        print(a,b)
    
cipher(word,shift)

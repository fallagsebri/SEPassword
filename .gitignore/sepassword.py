import os
os.system('cls' if os.name == 'nt' else 'clear')
def porn():
 print '''
 Social Engineer Attack Password Generator
 Created BY Saber Sebri
 If the needed information is not avaible just write"no" or pass it
 '''
#used wordlists
wd = "123456\n"
ppp = "12345\n"
pp = "1234\n"
wc = "123\n"
em = "\n"
porn()
#inputs
a =raw_input("the victime's name ?\n[>] ")
b =raw_input("the victime's surname?\n[>] ")
c =raw_input("the victime's phone number if avaible\n[>] ")
d =raw_input("the victime's mother name\n[>] ")
e =raw_input("the victime's father name\n[>] ")
f =raw_input("the victime's pet name if avaible\n[>] ")
g =raw_input("the victime's birthday (year)\n[>] ")
h =raw_input("the victime's birthday (month)\n[>] ")
i =raw_input("the victime's birthday (day)\n[>] " )
j =raw_input("the victime's sister name\n[>] ")
k =raw_input("the victime's brother name\n[>] ")
l =raw_input("the victime's best friend name \n[>] ")
m =raw_input("the victime's child name \n[>] ")
n =raw_input("the victime's car type\n[>] ")
o =raw_input("the victime's school name\n[>] ")
p =raw_input("the victime's grandmother name\n[>] ")
q =raw_input("the victime's grandfather name\n[>] ")
#fill
#part1
x = a+wd
ph = c
y = b+wd
z = e+wd
r = f+wd
bi = i+h+g+em
bii = i+"/"+h+"/"+g+em
ss = j+wd
aa = k+wd
bb = l+wd
cc = m+wd
dd = n+wd
ran = a+g+em
ee = o+wd
ff = p+wd
gg = q+wd
ik = a+g+em
#part2
az = a+ppp
ar = b+ppp
at = e+ppp
ay = f+ppp
ao = j+ppp
ap = k+ppp
aq = l+ppp
av = m+ppp
ad = n+ppp
af = o+ppp
ag = p+ppp
ah = q+ppp
#part3
zeb = a+pp
sorm = b+pp
za3ka = e+pp
terma = f+pp
nouna = j+pp
ok = k+pp
aasbtin = l+pp
nika = m+pp
niktin = n+pp
zbuba = o+pp
n9ob = p+pp
love = q+pp
#part4
amin = a+wc
ghaith = b+wc
hamza = e+wc
brahim = f+wc
haithem = j+wc
asser = k+wc
mahdi = l+wc
bilel = m+wc
helmi = n+wc
ayhem = o+wc
louay = p+wc
adem = q+wc
#saving
#part1
tneket = open('GeneratedPasswords.txt','w')
tneket.write(x)
tneket.write(y)
tneket.write(z)
tneket.write(r)
tneket.write(bi)
tneket.write(bii)
tneket.write(gg)
tneket.write(ss)
tneket.write(aa)
tneket.write(bb)
tneket.write(cc)
tneket.write(dd)
tneket.write(ee)
tneket.write(ff)
tneket.write(c)
tneket.write(ik)
#part2
tneket.write(az)
tneket.write(ar)
tneket.write(at)
tneket.write(ay)
tneket.write(ao)
tneket.write(ap)
tneket.write(aq)
tneket.write(av)
tneket.write(ad)
tneket.write(af)
tneket.write(ag)
tneket.write(ah)
tneket.write(ran)
#part3
tneket.write(zeb)
tneket.write(sorm)
tneket.write(za3ka)
tneket.write(terma)
tneket.write(nouna)
tneket.write(ok)
tneket.write(aasbtin)
tneket.write(nika)
tneket.write(niktin)
tneket.write(zbuba)
tneket.write(n9ob)
tneket.write(love)
#part4
tneket.write(amin)
tneket.write(ghaith)
tneket.write(hamza)
tneket.write(brahim)
tneket.write(haithem)
tneket.write(asser)
tneket.write(mahdi)
tneket.write(bilel)
tneket.write(helmi)
tneket.write(ayhem)
tneket.write(louay)
tneket.write(adem)
tneket.close()
print "THANK YOU FOR USING SIR !"
print "if you need other wordlist you will find it with the script file sir!"
print "[1] Repeat"
print "[2] Exit"
ch1=raw_input("\n[>]")
if ch1 == '1':
 os.system('sepassword.py' if os.name == 'nt' else 'python sepassword.py')

 




# Description of this example is provided in NTRU.md

from ntru import *

#Bob
Bob=Ntru(7,29,491531)
f=[1,1,-1,0,-1,1]
g=[-1,0,1,1,0,0,-1]
d=2
Bob.genPublicKey(f,g,2)
pub_key=Bob.getPublicKey()
print "Public Key           :",pub_key

#Alice
M=list()
M.append([1,1])			
M.append([1,1,1])			
M.append([1,0,1])			
M.append([0,1,1])			
M.append([0,1,0,1])
M.append([1])

R=list()
R.append([-1,-1,1,1])			
R.append([1,1,-1,0,-1])			
R.append([1,-1,0,1,0,0,-1])			
R.append([-1,0,0,-1,0,1,1])			
R.append([0,-1,0,0,-1,1,1])			
R.append([1,0,0,-1,-1,1])			


Alice=Ntru(7,29,491531)
Alice.setPublicKey(pub_key)
E=[0]*len(M)
for i in range(0,len(M)):
	E[i]=Alice.encrypt(M[i],R[i])

m1=poly.multPoly(E[0],E[1])
m2=poly.multPoly(E[2],E[3])
m3=poly.multPoly(E[4],E[5])
m1=poly.addPoly(m1,m2)
m1=poly.addPoly(m1,m3)

print "Encrypted Computation: ",m1
#Bob
print "Decrypted Computation: ", Bob.decryptSQ(m1)
print "Results match with those in the paper"

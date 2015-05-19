#Helper Functions 
# Extended Euclidean Algo for Integers
from fractions import Fraction as frac

def egcd(a, b):
    x,y, u,v = 0,1, 1,0
    while a != 0:
        q, r = b//a, b % a
        m, n = x-u * q, y-v * q
        b,a, x,y, u,v = a,r, u,v, m,n
    gcdVal = b
    return gcdVal, x, y


#Modular inverse
#An application of extended GCD algorithm to finding modular inverses:
def modinv(a, m):
    gcdVal, x, y = egcd(a, m)
    if gcdVal != 1:
        return None  # modular inverse does not exist
    else:
        return x % m

#Modulus Function which handles Fractions aswell
def fracMod(f,m):
	[tmp,t1,t2]=egcd(f.denominator,m)
	if tmp!=1:
		print "ERROR GCD of denominator and m is not 1"
		1/0
	else:
		out=modinv(f.denominator,m)*f.numerator % m
		return out


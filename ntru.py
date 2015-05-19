# Implementation of NTRU Homomorphic encryption
import math
from fractions import gcd
import poly

class Ntru:
	N=None
	p=None
	q=None
	d=None
	f=None
	g=None
	h=None
	f_p=None
	f_q=None
	D=None
	def __init__(self,N_new,p_new,q_new):
		self.N=N_new
		self.p=p_new
		self.q=q_new
		D=[0]*(self.N+1)
		D[0]=-1
		D[self.N]=1
		self.D=D
		
	def genPublicKey(self,f_new,g_new,d_new):
		# Using Extended Euclidean Algorithm for Polynomials
		# to get s and t. Note that the gcd must be 1
		self.f=f_new
		self.g=g_new
		self.d=d_new
		[gcd_f,s_f,t_f]=poly.extEuclidPoly(self.f,self.D)
		self.f_p=poly.modPoly(s_f,self.p)
		self.f_q=poly.modPoly(s_f,self.q)
		self.h=self.reModulo(poly.multPoly(self.f_q,self.g),self.D,self.q)
		if not self.runTests():
			print "Failed!"
			quit()
			
	def getPublicKey(self):
		return self.h

	def setPublicKey(self,public_key):
		self.h=public_key
	
	def encrypt(self,message,randPol):
		if self.h!=None:
			e_tilda=poly.addPoly(poly.multPoly(poly.multPoly([self.p],randPol),self.h),message)
			e=self.reModulo(e_tilda,self.D,self.q)
			return e
		else:
			print "Cannot Encrypt Message Public Key is not set!"
			print "Cannot Set Public Key manually or Generate it"

	def decryptSQ(self,encryptedMessage):
		F_p_sq=poly.multPoly(self.f_p,self.f_p)
		f_sq=poly.multPoly(self.f,self.f)
		tmp=self.reModulo(poly.multPoly(f_sq,encryptedMessage),self.D,self.q)
		centered=poly.cenPoly(tmp,self.q)
		m1=poly.multPoly(F_p_sq,centered)
		tmp=self.reModulo(m1,self.D,self.p)
		return poly.trim(tmp) 

	def decrypt(self,encryptedMessage):
		tmp=self.reModulo(poly.multPoly(self.f,encryptedMessage),self.D,self.q)
		centered=poly.cenPoly(tmp,self.q)
		m1=poly.multPoly(self.f_p,centered)
		tmp=self.reModulo(m1,self.D,self.p)
		return poly.trim(tmp) 

	def reModulo(self,num,div,modby):
		[_,remain]=poly.divPoly(num,div)
		return poly.modPoly(remain,modby)

	def printall(self):
		print self.N
		print self.p
		print self.q
		print self.f
		print self.g
		print self.h
		print self.f_p	
		print self.f_q
		print self.D
	
	def isPrime(self):
	    if self.N % 2 == 0 and self.N > 2: 
	        return False
	    return all(self.N % i for i in range(3, int(math.sqrt(self.N)) + 1, 2))
		
	def runTests(self):			
		# Checking if inputs satisfy conditions
		if not self.isPrime() :
			print "Error: N is not prime!"
			return False
	
		if gcd(self.N,self.p) != 1 :
			print "Error: gcd(N,p) is not 1"
			return False

		if gcd(self.N,self.q)!=1 :
			print "Error: gcd(N,q) is not 1"
			return False
	
		if self.q<=(6*self.d+1)*self.p:
			print "Error: q is not > (6*d+1)*p"
			return False
	
		if not poly.isTernary(self.f,self.d+1,self.d):
			print "Error: f does not belong to T(d+1,d)"
			return False
		
		if not poly.isTernary(self.g,self.d,self.d):
			print "Error: g does not belong to T(d,d)"
			return False
	
		return True		
	


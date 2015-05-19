POLY.PY
========
This library allows the user do mathematical operations on rational coefficient polynomials.
Each polynomial is represented by a Python list of coefficients for example:
	* c1=[1,2,3,1] represents the polynomial 1+2x+3x^2+x^3
	* c2=[fraction(1,2),fraction(2,3)] represents the polynomial (1/2)+(2/3)x
fraction is a python standard package can be imported using *from fractions import Fraction*
Operations provided in this package are given below.


Operations/Functions
--------------------
1) addPoly(c1,c2)         :------------------------------------  Returns Addition of polynomials c1 and c2
2) subPoly(c1,c2)         :------------------------------------  Returns Subtraction of c2 from c1
3) multPoly(c1,c2)        :------------------------------------  Returns Product of c1 and c2
4) divPoly(c1,c2)         :------------------------------------  Returns the Quotient and Division of c1 / c2
5) cenPoly(c1,q)          :------------------------------------  Returns the centered lift of the given polynomial 
6) resize(c1,c2)          :------------------------------------  Adds leading zeros to the smaller of the two vectors which represent polynomials.
7) trim(c1)               :------------------------------------  Removes Leading zeros from the input vector representing the polynomial 
8) modPoly(c1,k)          :------------------------------------  Takes the k-modulo of the polynomial c1 by taking the modulo of each coefficient of c1. 
9) isTernary(f,alpha,beta):------------------------------------  Checks if the polynomial is a Ternary polynomial returns a Boolean value
10) extEuclidPoly(a,b)    :------------------------------------- Returns [gcd,s,t] where s and t are Bezout Polynomials
* All functions below work with fraction coefficients (refer to Example 1.2)
* All functions return trimmed output


Detailed Descriptions
---------------------
1) Function :addPoly(c1,c2)
------------------------------------
Input   : Two polynomials c1 and c2
Output: Sum of the two polynomials (c1+c2)
Example 1.1: 
	>>> import poly as p	
	>>> p.addPoly([1,2,3],[2,3,4,5])
	[3,5,7,5]

Example 1.2: 
	>>> import poly as p	
	>>> from fractions import Fraction as frac
	>>> c1=[frac(1,2),frac(1,3),frac(3,5)]
        >>> c2=[frac(-1,2),frac(2,3)]
	>>> p.addPoly(c1,c2)
	[frac(0,1),frac(1,1),frac(3,5)]


2) Function :subPoly(c1,c2)
-----------------------------
Input  : Two polynomials c1 and c2
Output : Difference of the two polynomials that is (c1-c2)
Detail : subPoly is not commutative
Example 2.1: 
	>>> p.subPoly([1,2,3],[2,3,4,5])
	[-1,-1,-1,-5]


3) Function :multPoly(c1,c2)
-----------------------------
Input  : Two polynomials c1 and c2
Output : Product of the two polynomials that is (c1*c2)
Example 3.1: 
	>>> p.multPoly([1,2,3],[2,3,4,5])
	[2, 7, 16, 22, 22, 15]

4) Function :divPoly(c1,c2)
----------------------------
Input : Two polynomials c1 and c2
Ouput : The pair of quotient and remainder from the division; Output Format is [quotient,remainder]
Detail: Implemented long division algorithm
Example 4.1:
	>>> c1=[1,2,3,4]
	>>> c2=[1,1]
	>>> p.divPoly(c1,c2)
	[[Fraction(3, 1), Fraction(-1, 1), Fraction(4, 1)], [Fraction(-2, 1)]]

Example 4.2: In this example we know that (x+1) divides (x^2+2x+1) notice 
	>>> c1=[1,2,1]
	>>> c2=[1,1]
	>>> poly.divPoly(c1,c2)
	[[Fraction(1, 1), Fraction(1, 1)], [Fraction(0, 1)]]


5) Function :cenPoly(c1,q)
--------------------------
Input : A polynomial c1 and and constant q
Output: The returns the centered lift of the given polynomial
Detail: Given polynomial c1(x) and a a constant q. The function will find coefficients such that they lie in the interval (-q/2,q/2] 

Example 5.1:
	>>> p.cenPoly([1,2,3,4,5],4)
        [1, 2, -1, 0, 1]
        >>> p.cenPoly(c1,5)
        [-2, 0, -1, 2]

6) Function :resize(c1,c2)
--------------------------
Input : Two polynomials coefficient vectors c1 and c2
Output: Returns both coefficient vectors in a list of the form [c1,c2] where both have the same size

Example 6.1:
	>>> p.resize([1,2,3],[1,4,5,6])
	[[1,2,3,0],[1,4,5,6]]

7) Function : trim(c1)
----------------------
Input : Takes in a polynomial coefficients vector
Output: Removes the leading zeros.

Example 7.1:
	>>> p.trim([1,2,3,0,0])
	[1,2,3]


8) Function : modPoly(c1,k)
---------------------------
Input : Takes polynomial coefficient vector c1 and constant k as input
Output: Polynomial coefficient vectors c1 (mod k) (All coefficients are integers)
Detail: In case where the input polynomial can have fractions as coefficients, we find their modular inverse.
Example 8.1:
	>>> c1=[frac(1,2),3,4,frac(3,4)]
	>>> poly.modPoly(c1,3)
	[2, 0, 1, 0]

9) Function : isTernary(f,alpha,beta)
-------------------------------------
Input : A polynomial coefficients vector f and parameters alpha and beta
Output: Boolean True/False 
Detail: A Ternary polynomial is one which has coefficients belonging to {-1,0,1}. The number of one coefficients must be alpha, while the number of negative-one coefficients must be beta.
Example 9.1: 
	>>> c1=[1,-1,1,0,0,-1]
	>>> p.isTernary(c1,1,1)
	False
	>>> p.isTernary(c1,2,2)
	True
 
10) extEuclidPoly(a,b)
----------------------
Input : A polynomial coefficients vector of two polynomials a(x) and b(x)
Output: GCD(a,b),s,t
Detail: Returns [gcd,s,t] where s and t are Bezout Polynomials which implies that as+tb = gcd(a,b)


File TestPoly.py tests some functions of this library using randomly generated polynomials. It compares the results to that gotten from numpy Polynomial library	

NTRU for Python 2.7
====================

Description
===========
An important problem in data analytics is how to collect user data and make it available for analysis without compromising user privacy. A recommended solution is to encrypt data using ring homomorphism methods which allows analysis to be performed on encrypted data, allowing the analyst to perform analytics on the data without knowing the individual private data elements used in the analysis. Previous research showed that the existing NTRU encryption system could be modified to provide just this level of functionality, but open source tools do not currently exist to support NTRU on Python.

Our project is the creation of a python library of functions which implement the algorithms necessary for an NTRU. We have built a python package which provides an implementation of NTRU Encryption System. 

To ensure accuracy of the encryption and decryption we required to know polynomials with high accuracy. Since existing polynomial libraries such as the one provided by the Numpy Python Package has coefficients as floats, we could not employ them. Therefore, we implemented a fresh polynomial package which allows us to perform operations on polynomial with rational coefficients(using fraction datatype Python). 

Software:
=========

Polynomial Package
------------------
* poly.py             : Polynomial Library for polynomials with rational coeffiencents
* POLY.md             : Documentation for poly.py
* testPoly.py         : A test for functions defined in our library

Ntru Package
------------
* ntru.py             : Ntru Encryption Class Implimentation for Python 
* NTRU.md             : Documentation for ntru.py
* example_bobalice.py : An example using Ntru given in the Ntru Documentation NTRU.md
* example_enDom.py    : An example using Ntru in context of encrypted domain

Helper Functions
----------------
* fracModulo.py : Contains Implementation of *Extented Euclidean Algorithm for Integers*, *Modular Inverse of an integer* and *x Modulo m* where x can be a fraction or integer. 



Documentation
=============
License and documentation are both provided in the Documentation folder.


Technical Details
=================
Technical details can be found in Presentation and Report folder




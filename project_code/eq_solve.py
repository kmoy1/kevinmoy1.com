import numpy as np
import re
import sys
def find_zeros(s):
    """Given a string s in polynomial form, parse and return solutions."""
    def parse_eq_str(s):
        """Given a string s in polynomial form, parse and return into a list of coefficients."""
        #First, count the number of pluses or minuses = degree of polynomial, ASSUMING in standard form.
        std_degree = s.count('+') + s.count('-')
        #Get leading term of polynomial.
        true_deg = getDegree(s)
        #Edge case one: no var, which means a constant.
        if true_deg == 0:
            return [int(s)]
        #In standard form (ax^i + bx^i-1 + ... + fx + g format)
        if std_degree == true_deg:
            coef_regex = re.compile(r"(?<!x\^)(?<!x\^-)-?\d+")
            coefs = [int(c) for c in coef_regex.findall(s)]
            return coefs
        else:
            return None
    
    coefs = parse_eq_str(s)
    return np.roots(coefs)

def getDegree(poly):
    """Given string polynomial POLY in any form, get its degree.
    >>> getDegree('1')
    0
    >>> getDegree('x')
    1
    >>> getDegree('x+1')
    1
    >>> getDegree('x^5+ 440x^4 + 35x^3 + 220x+1')
    5
    >>> getDegree('x^4+ 440x^10 + 35x^3 + 220x+1')
    10
    """
    import string
    var =  re.findall(r"\d*([a-z])[\^]?\d*", poly)
    if not var:
        return 0
    if re.findall(r'^\s*[a-z]\s*$', poly): #Test y = x
        return 1 
    if re.findall(r'^\s*[a-z]\s*[+-]\s*\d*$', poly): #Test y = x + C
        return 1 
    return max([int(e) for e in re.findall(r"\d*[a-z][\^]?(\d*)", poly) if e])

def test_func(f):
	"""Run f's doctests."""
	import doctest
	doctest.run_docstring_examples(f, globals())

test_func(getDegree)
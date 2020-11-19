import numpy as np
def solve(s):
    """Given a string s in polynomial form, parse and return solutions."""
    def parse_eq_str(s):
        """Given a string s in polynomial form, parse and return into a list of coefficients."""
        #TODO: Use regex to parse out numbers. 
        return ['1']
    coefs = parse_eq_str(s)
    return np.roots(coefs)
#Answer to Greek Sort - https://www.codewars.com/kata/greek-sort/python

greek = ['alpha','beta','gamma','delta','epsilon','zeta',
'eta','theta','iota','kappa','lambda','mu','nu','xi','omicron',
'pi','rho','sigma','tau','upsilon','phi','chi','psi','omega']

def greek_comparator(lhs, rhs):
    return greek.index(lhs)-greek.index(rhs)
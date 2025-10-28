""" Banking Interest calculations"""

from mypackage.interest_calculation import simple_interest, compound_interest

prin = float(input('principal :'))
ny = float(input('year :'))
roi = float(input('rate of interest :'))

si,amt = simple_interest(prin = prin, ny = ny, roi = roi)
print(f'SI :{si} Amount : {amt}')

amt = compound_interest(prin = prin, t = ny, roi = roi)
print(f'Amount : {amt}')

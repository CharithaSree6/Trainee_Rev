

from mypackage.interest_calculation import simple_interest
from mypackage.shape_calculations import area_of_circle,area_of_rect

prin = float(input('principal :'))
ny = float(input('year :'))
roi = float(input('rate of interest :'))

print(f'simple interest: {simple_interest(prin = prin, ny = ny, roi = roi)[0]}'
      f' Amount:{simple_interest(prin = prin, ny = ny, roi = roi)[1]}')

print(f'Area of circle: {area_of_circle(10)} \n'
      f'Area of rect: {area_of_rect(10,5)}')
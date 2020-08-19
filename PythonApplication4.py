'''Even or Odd License Plate
1. Load plate numbers
2. Mondays, Wednesdays and Fridays for odd number plates.
3. Tuesday, Thursday and Saturday for even number plates.
4. Sunday for all plates.'''

car_plates = ['AB01', 'AB02', 'BC18', 'CD71', 'CF95', 'FA82', 'FH65', 'LK19', 'PJ36']
odd_days = ['MO', 'WE', 'FR']
even_days = ['TU', 'TH', 'SA']
pass_list = []
print('MO=Monday, TU=Tuesday, WE=Wednesday, TH=Thursday, FR=Friday, SA=Saturday, SU=Sunday')
today = input('Enter the day: ')
for plate in car_plates:
    last_digit = int(plate[-1])
    if today in odd_days and last_digit % 2 != 0:
        pass_list.append(plate)

    elif today in even_days and last_digit % 2 == 0:
        pass_list.append(plate)

    elif today == 'SU':
        pass_list.append(plate)

print(*pass_list, sep='\n')


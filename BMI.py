#BMI test
def input_user_data():
    while True:
        try:
            weight = float(input('Enter weight in kilograms: '))
            height = float(input('Enter height in meters: '))
        
            if 0 < weight and 0 < height < 2.72:
                return weight, height
            else:
                raise ValueError('Invalid height or weight')
        except ValueError:
            print('Invalid height or weight input')
            continue
            

     
 
import coridors_calc
from Room import Room 


path_rooms_A = r'11692/bA/bA_room_categories.csv'
path_coridors_A = r'11692/bA/bA_coridors.csv'

path_rooms_B = r'11692/bB/bB_room_categories.csv'
path_coridors_B = r'11692/bB/bB_coridors.csv'

path_rooms_C = r'11692/bC/bC_room_categories.csv'
path_coridors_C = r'11692/bC/bC_coridors.csv'

path_rooms_D= r'11692/bD/bD_room_categories.csv'
path_coridors_D = r'11692/bD/bD_coridors.csv'


coridors_calc.calc_coridors_smoke(path_rooms_A, path_coridors_A)
# coridors_calc.calc_coridors_smoke(path_rooms_B, path_coridors_B)
# coridors_calc.calc_coridors_smoke(path_rooms_C, path_coridors_C)
# coridors_calc.calc_coridors_smoke(path_rooms_D, path_coridors_D)




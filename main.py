import pandas as pd

from Room import Room
from Zone import Zone

from Smoke_coridor import smoke_exhaust_coridor
from Starcase_3 import Starcase_3

import A_coridor_1

pd.set_option('display.max_colwidth', None)


A_coridor_1.smoke_system()

for room in Room.items:
    print(room)
    print(room.smoke_consumption_vol)

print(Room.systemname_items["A_coridor_1"][0])



# building_А_rent_floor = Room(name="Арендные помещения БКТ (без конкретной технологии)",
#                              area_m2=1913, high_m=3.9,
#                              fire_load_density=800,
#                              calorific_value_fire_load=14,
#                              calorific_value_fire_load_mass=[])

# data = smoke_exhaust_coridor(room=building_А_rent_floor, opening_list=[2.1 * 0.9], corridor_hight=3.9, corridor_door_hight=2.1,
#                              corridor_door_width=0.9, corridor_area=40, corridor_lenght=20, coef_building_type=1.2)

# data.to_csv(f"{building_А_rent_floor.name}_data.csv")




#подпор в ЛК типа Н2

# strc_1 = Starcase_3(
#     name = "A_starcase_1", 
#     lvl_amount = 5, 
#     lvl_height = [5.7, 9.9, 14.1, 18.3],
#     starcase_area =27.1,
#     lvl_doors_height = [2.1, 2.1, 2.1, 2.1, 2.1], 
#     lvl_doors_widts = [1.4, 1.4, 1.4, 1.4, 1.4], 
#     wind = 2, 
#     Tr = 18,
#     Ta = -26,
#     starcase_local_resistance = 60, 
#     vestibule_local_resistance = 0, 
#     door_local_resistance = 2.44, 
#     n = 1, z = 1, q = 1,
#     Gsm = 5.8)

# strc_1.calc_starcase_all()
# strc_1.create_df()
# strc_1.starcase_df_to_csv()


# strc_2 = Starcase_3(
#     name = "A_starcase_2", 
#     lvl_amount = 5, 
#     lvl_height = [5.7, 9.9, 14.1, 18.3],
#     starcase_area =27.1,
#     lvl_doors_height = [2.1, 2.1, 2.1, 2.1, 2.1], 
#     lvl_doors_widts = [1.4, 1.4, 1.4, 1.4, 1.4], 
#     wind = 2, 
#     Tr = 18,
#     Ta = -26,
#     starcase_local_resistance = 60, 
#     vestibule_local_resistance = 0, 
#     door_local_resistance = 2.44, 
#     n = 1, z = 1, q = 1,
#     Gsm = 5.8)

# strc_2.calc_starcase_all()
# strc_2.create_df()
# strc_2.starcase_df_to_csv()




import pandas as pd

from Room import Room
from Zone import Zone

from Smoke_coridor import smoke_exhaust_coridor
from starcase_3 import Starcase_3


# a = Room(name="БКТ_коридор (типовых этажей)",
#          area_m2=1913,
#          high_m=3.9,
#          fire_load_density=800,
#          calorific_value_fire_load=14,
#          calorific_value_fire_load_mass=[])

# data = smoke_exhaust_coridor(room=a,
#                              opening_list=[2.1 * 0.9],
#                              corridor_hight=3.9,
#                              corridor_door_hight=2.1,
#                              corridor_door_width=0.8,
#                              corridor_area=40,
#                              corridor_lenght=20,
#                              coef_building_type=1.2)

# pd.set_option('display.max_colwidth', None)

# print(data)

# name = "x"
# data.to_csv(f"{name}_data.csv")


strc_1 = Starcase_3(
    name = "starcase_1", 
    lvl_amount = 5, 
    lvl_height = [5.7, 9.9, 14.1, 18.3],
    starcase_area =27.1,
    lvl_doors_height = [2.1, 2.1, 2.1, 2.1, 2.1], 
    lvl_doors_widts = [1.4, 1.4, 1.4, 1.4, 1.4], 
    wind = 2, 
    Tr = 18,
    Ta = -26,
    starcase_local_resistance = 60, 
    vestibule_local_resistance = 0, 
    door_local_resistance = 2.44, 
    n = 1, z = 1, q = 1,
    Gsm = 5.8)


strc_1.calc_pressure_lvl2()
strc_1.calc_Gsa()

print(f"Dns_r - {strc_1.Dns_r}")
print(f"Dns_s - {strc_1.Dns_s}")
print(f"Dns_a - {strc_1.Dns_a}")
print(f"Ts - {strc_1.Ts}")
print(f"Ps2 - {strc_1.Ps2}")
print(f"Gsa - {strc_1.Gsa}")

print(f"lvl_highs - {strc_1.lvl_height[0]}")
print(f"lvl_highs - {strc_1.lvl_doors_height[1]}")
print(f"Dns_s - {strc_1.Dns_s}")
print(f"Dns_r - {strc_1.Dns_r}")

strc_1.calc_max_G()
strc_1.lvl_losses()



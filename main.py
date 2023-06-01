import pandas as pd
import json 

from Room import Room
from Zone import Zone

from Smoke_coridor import Coridor
from Starcase_3 import Starcase_3

import A_coridor_1
import A_coridor_2
import A_coridor_3
import B_coridor_1
import B_coridor_2
import B_coridor_3
import C_coridor_1
import C_coridor_2
import C_coridor_3
import D_coridor_3

pd.set_option('display.max_colwidth', None)

with open('input_A.json') as input_A_file:
    input_A_data = json.loads(input_A_file.read())



print(input_A_data["coridors"][0]["rooms"])

# A_coridor_1.smoke_system_coridor_1()
# A_coridor_2.smoke_system_coridor_2()
# A_coridor_3.smoke_system_coridor_3()

# B_coridor_1.smoke_system_coridor_1()
# B_coridor_2.smoke_system_coridor_2()
# B_coridor_3.smoke_system_coridor_3()

# C_coridor_1.smoke_system_coridor_1()
# C_coridor_2.smoke_system_coridor_2()
# C_coridor_3.smoke_system_coridor_3()

# D_coridor_3.smoke_system_coridor_3()

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

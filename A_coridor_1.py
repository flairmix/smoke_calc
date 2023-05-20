from Room import Room
from Smoke_coridor import smoke_exhaust_coridor

param_temp_inside = 18
param_temp_inside_basement = 10
param_corridor_temp = 18
param_corridor_temp_basement = 10

def smoke_system():

    system = "A_coridor_1"

    А_bsm_c_06 = Room(name="подвал_Мастерская эксплуатации", systemname=system,
                    area_m2=51.62, high_m=3.0,
                    fire_load_density=1400, calorific_value_fire_load=14.5,
                    temp_inside = param_temp_inside, corridor_temp = param_corridor_temp_basement)

    А_bsm_c_07 = Room(name="подвал_ПУИ", systemname=system,
                    area_m2=8.83, high_m=3.0,
                    fire_load_density=180, calorific_value_fire_load=14.5,
                    temp_inside = param_temp_inside_basement, corridor_temp = param_corridor_temp_basement)

    А_bsm_c_13 = Room(name="подвал_Помещение хранения и мойки мусорных контейнеров", systemname=system,
                    area_m2=58.17, high_m=3.0,
                    fire_load_density=1400, calorific_value_fire_load=14.5,
                    temp_inside = param_temp_inside_basement, corridor_temp = param_corridor_temp_basement)

    А_bsm_c_14 = Room(name="подвал_Кладовая уличного инвенторя", systemname=system,
                    area_m2=58.26, high_m=3.0,
                    fire_load_density=1400, calorific_value_fire_load=14.5,
                    temp_inside = param_temp_inside_basement, corridor_temp = param_corridor_temp_basement)

    А_bsm_c_15 = Room(name="подвал_Кладовая бытовых материалов", systemname=system,
                    area_m2=101.13, high_m=3.0,
                    fire_load_density=2200, calorific_value_fire_load=14.5,
                    temp_inside = param_temp_inside_basement, corridor_temp = param_corridor_temp_basement)

    А_bsm_c_16 = Room(name="подвал_Кладовая ТМЦ", systemname=system,
                    area_m2=84.83, high_m=3.0,
                    fire_load_density=2200, calorific_value_fire_load=14.5,
                    temp_inside = param_temp_inside_basement, corridor_temp = param_corridor_temp_basement)

    А_bsm_c_17 = Room(name="подвал_Кладовая люминесцентых ламп", systemname=system,
                    area_m2=15.22, high_m=3.0,
                    fire_load_density=1400, calorific_value_fire_load=14.5,
                    temp_inside = param_temp_inside_basement, corridor_temp = param_corridor_temp_basement)

    А_bsm_c_18 = Room(name="подвал_Кладовая мебели", systemname=system,
                    area_m2=125.89, high_m=3.0,
                    fire_load_density=2200, calorific_value_fire_load=14.5,
                    temp_inside = param_temp_inside_basement, corridor_temp = param_corridor_temp_basement)

    А_bsm_c_19 = Room(name="подвал_Помещение СС", systemname=system,
                    area_m2=6.5, high_m=3.0,
                    fire_load_density=180,calorific_value_fire_load=14.5,
                    temp_inside = param_temp_inside_basement, corridor_temp = param_corridor_temp_basement)
    
    А_grfloor_1 = Room(name="1эт.Помещение СС", systemname=system,
                    area_m2=6.5, high_m=3.0, #уточнить
                    fire_load_density=180,calorific_value_fire_load=14.5, #уточнить
                    temp_inside = param_temp_inside, corridor_temp = param_corridor_temp)

    А_grfloor_2 = Room(name="1эт.ПУИ", systemname=system,
                    area_m2=8.83, high_m=3.0, #уточнить
                    fire_load_density=180, calorific_value_fire_load=14.5, #уточнить
                    temp_inside = param_temp_inside, corridor_temp = param_corridor_temp)

    А_2floor_1 = Room(name="2эт.ПУИ", systemname=system,
                    area_m2=9.99, high_m=3.9, #уточнить
                    fire_load_density=180, calorific_value_fire_load=14.5, #уточнить
                    temp_inside = param_temp_inside, corridor_temp = param_corridor_temp)
    
    А_2floor_2 = Room(name="2эт.Помещение СС", systemname=system,
                    area_m2=9.99, high_m=3.9, #уточнить
                    fire_load_density=180, calorific_value_fire_load=14.5, #уточнить
                    temp_inside = param_temp_inside, corridor_temp = param_corridor_temp)
    
    А_2floor_3 = Room(name="2эт.Помещение ЭОМ", systemname=system,
                    area_m2=9.99, high_m=3.9, #уточнить
                    fire_load_density=180, calorific_value_fire_load=14.5, #уточнить
                    temp_inside = param_temp_inside, corridor_temp = param_corridor_temp)
    
    А_2floor_4 = Room(name="2эт.Помещение складирования мусорных контейнеров", systemname=system,
                    area_m2=9.99, high_m=3.9, #уточнить
                    fire_load_density=180, calorific_value_fire_load=14.5, #уточнить
                    temp_inside = param_temp_inside, corridor_temp = param_corridor_temp)
    
    for room in Room.items:
        data = smoke_exhaust_coridor(room=room, opening_list=[2.1 * 0.95], corridor_hight=3.0, 
                                    corridor_door_hight=2.1, corridor_door_width=0.95, corridor_area=60,                                     
                                    corridor_lenght=30, coef_building_type=1.2)
        
        # data.to_csv(f"{room.name}_data.csv")
        # print(room.smoke_consumption_vol)
from Room import Room
from Smoke_coridor import Coridor

param_temp_inside = 18
param_temp_inside_basement = 10
param_corridor_temp = 18
param_corridor_temp_basement = 10

def smoke_system_coridor_1():

    system = "A_coridor_1"
    data_all_coridors = {}

    А_bsm_c_06 = Room(name="подвал_Мастерская эксплуатации", systemname=system,
                    area_m2=51.62, high_m=3.0,
                    fire_load_density=180, calorific_value_fire_load=14.5,
                    temp_inside = param_temp_inside, corridor_temp = param_corridor_temp_basement)
    
    А_bsm_c_16 = Room(name="подвал_Кладовая ТМЦ", systemname=system,
                    area_m2=84.83, high_m=3.0,
                    fire_load_density=2200, calorific_value_fire_load=14.5,
                    temp_inside = param_temp_inside_basement, corridor_temp = param_corridor_temp_basement)

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


    А_bsm_c_17 = Room(name="подвал_Кладовая люминесцентых ламп", systemname=system,
                    area_m2=15.22, high_m=3.0,
                    fire_load_density=1400, calorific_value_fire_load=14.5,
                    temp_inside = param_temp_inside_basement, corridor_temp = param_corridor_temp_basement)

    А_bsm_c_18 = Room(name="подвал_Кладовая мебели", systemname=system,
                    area_m2=125.89, high_m=3.0,
                    fire_load_density=2200, calorific_value_fire_load=14.5,
                    temp_inside = param_temp_inside_basement, corridor_temp = param_corridor_temp_basement)

    А_bsm_t_1 = Room(name="подвал_Помещение СС", systemname=system,
                    area_m2=6.5, high_m=3.0,
                    fire_load_density=180,calorific_value_fire_load=14.5,
                    temp_inside = param_temp_inside_basement, corridor_temp = param_corridor_temp_basement)
    
    А_grfloor_t1 = Room(name="1эт.Помещение СС", systemname=system,
                    area_m2=6.5, high_m=5.0, 
                    fire_load_density=180,calorific_value_fire_load=14.5,
                    temp_inside = param_temp_inside, corridor_temp = param_corridor_temp)

    А_grfloor_c1 = Room(name="1эт.ПУИ", systemname=system,
                    area_m2=7.42, high_m=5.0, 
                    fire_load_density=180, calorific_value_fire_load=14.5,
                    temp_inside = param_temp_inside, corridor_temp = param_corridor_temp)

    А_2floor_c2 = Room(name="2эт.ПУИ", systemname=system,
                    area_m2=8.0, high_m=3.9, 
                    fire_load_density=180, calorific_value_fire_load=14.5,
                    temp_inside = param_temp_inside, corridor_temp = param_corridor_temp)
    
    А_2floor_t1 = Room(name="2эт.Помещение СС", systemname=system,
                    area_m2=10.65, high_m=3.9,
                    fire_load_density=180, calorific_value_fire_load=14.5, 
                    temp_inside = param_temp_inside, corridor_temp = param_corridor_temp)
    
    А_2floor_t2 = Room(name="2эт.Помещение ЭОМ", systemname=system,
                    area_m2=9.99, high_m=3.9, 
                    fire_load_density=180, calorific_value_fire_load=14.5, 
                    temp_inside = param_temp_inside, corridor_temp = param_corridor_temp)
    
    А_2floor_c1 = Room(name="2эт.Помещение складирования мусорных контейнеров", systemname=system,
                    area_m2=7.45, high_m=3.9, 
                    fire_load_density=1400, calorific_value_fire_load=14.5, 
                    temp_inside = param_temp_inside, corridor_temp = param_corridor_temp)
    
    
    list1 = ["2эт.Помещение ЭОМ","2эт.Помещение СС", "2эт.Помещение складирования мусорных контейнеров", "2эт.ПУИ"]
    list2 = ["1эт.ПУИ", "1эт.Помещение СС"]
    list3 = ["подвал_ПУИ","подвал_Помещение хранения и мойки мусорных контейнеров", "подвал_Кладовая уличного инвенторя", "подвал_Кладовая бытовых материалов",
            "подвал_Кладовая люминесцентых ламп", "подвал_Кладовая мебели", "подвал_Помещение СС"]
    list4 = ["подвал_Кладовая ТМЦ","подвал_Мастерская эксплуатации"]
    
    coridor1 = Coridor(rooms=list1, opening_list=[2.1 * 0.8], corridor_hight=3.0, 
                        corridor_door_hight=2.1, corridor_door_width=0.8, corridor_area=15,corridor_lenght=10, coef_building_type=1.2)
    coridor2 = Coridor(rooms=list2, opening_list=[2.1 * 0.8], corridor_hight=3.0, 
                        corridor_door_hight=2.1, corridor_door_width=0.8, corridor_area=32,corridor_lenght=15, coef_building_type=1.2)
    coridor3 = Coridor(rooms=list3, opening_list=[2.1 * 0.95], corridor_hight=3.0, 
                        corridor_door_hight=2.1, corridor_door_width=0.95, corridor_area=100,corridor_lenght=50, coef_building_type=1.2)
    coridor4 = Coridor(rooms=list4, opening_list=[2.1 * 0.95], corridor_hight=3.0, 
                        corridor_door_hight=2.1, corridor_door_width=0.95, corridor_area=64,corridor_lenght=32, coef_building_type=1.2)

    for i in range (0,len(coridor1.rooms)):
        room = Room.get_rooms_by_system_and_name(system,list1)[i]
        data = coridor1.smoke_exhaust_coridor(room)
        
        data_all_coridors[room.name] = data 
        # data.to_csv(f"11692/{system} - lvl2 - {room.name}_data.csv")
        
    for i in range (0,len(coridor2.rooms)):
        room = Room.get_rooms_by_system_and_name(system,list2)[i]
        data = coridor2.smoke_exhaust_coridor(room)
        data_all_coridors[room.name] = data 
        
        # data.to_csv(f"11692/{system} - lvl1 - {room.name}_data.csv")
        
    for i in range (0,len(coridor3.rooms)):
        room = Room.get_rooms_by_system_and_name(system,list3)[i]
        data = coridor3.smoke_exhaust_coridor(room)
        data_all_coridors[room.name] = data 
        
        # data.to_csv(f"11692/A_coridor_1/{system} - basement1 - {room.name}_data.csv")
        
    for i in range (0,len(coridor4.rooms)):
        room = Room.get_rooms_by_system_and_name(system,list4)[i]
        data = coridor4.smoke_exhaust_coridor(room)
        data_all_coridors[room.name] = data 
        
        # data.to_csv(f"11692/A_coridor_1/basement2 - {system} - {room.name}_data.csv")

    # print(data_all_coridors.keys())
    
    for key, data in data_all_coridors.items():
        name_room = data["Значения"].values[1]
        data.to_csv(f"11692/{system}/{system} - {name_room}_data.csv")
        
    # print(f"{key} - {value['Значения'].values[35]} м3/ч")
        
 
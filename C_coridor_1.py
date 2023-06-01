from Room import Room
from Smoke_coridor import Coridor

param_temp_inside = 18
param_temp_inside_basement = 10
param_corridor_temp = 18
param_corridor_temp_basement = 10

def smoke_system_coridor_1():

    system = "C_coridor_1"
    data_all_coridors = {}
    
    list1 = ["Коридор БКП для офисов"]

    C_2lvl = Room(name="Коридор БКП для офисов", systemname=system,
                area_m2=1919, high_m=3.9,
                fire_load_density=1300, calorific_value_fire_load=14.5,
                temp_inside = param_temp_inside, corridor_temp = param_corridor_temp)
    
    list2 = ["lvl_1_Торговый павильон",
            "lvl_1_Кладовая сухих продуктов",
            "lvl_1_Кладовая хлеба",
            "lvl_1_Кладовая упаковочных материалов",
            "lvl_1_Кладовая товаров длительного хранения",
            "lvl_1_Кладовая напитков",
            "lvl_1_Кладовая непроизводственных товаров",
            "lvl_1_Кладовая спец.одежды",
            "lvl_1_Фасовка овощей и фруктов",
            "lvl_1_Фасовка рыбной гастрономии",
            "lvl_1_Фасовка гастрономии",
            "lvl_1_Кладовая алкогольной продукции",
            "lvl_1_Загрузочная",
            "lvl_1_Кладовая и моечная оборотной тары",
            "lvl_1_ПУИ для подсобных помещений"]

    
    C_lvl1_np_61 = Room(name="lvl_1_Торговый павильон", systemname=system,
                    area_m2=377.81, high_m=5.4,
                    fire_load_density=800, calorific_value_fire_load=14.5,
                    temp_inside = param_temp_inside, corridor_temp = param_corridor_temp)
    
    C_lvl1_np_62 = Room(name=list2[1], systemname=system,
                    area_m2=9.16, high_m=5.4,
                    fire_load_density=180, calorific_value_fire_load=14.5,
                    temp_inside = param_temp_inside, corridor_temp = param_corridor_temp)
    
    C_lvl1_np_63 = Room(name=list2[2], systemname=system,
                    area_m2=3.55, high_m=5.4,
                    fire_load_density=180, calorific_value_fire_load=14.5,
                    temp_inside = param_temp_inside, corridor_temp = param_corridor_temp)
    
    C_lvl1_np_64 = Room(name=list2[3], systemname=system,
                    area_m2=3, high_m=5.4,
                    fire_load_density=180, calorific_value_fire_load=14.5,
                    temp_inside = param_temp_inside, corridor_temp = param_corridor_temp)
    
    C_lvl1_np_65 = Room(name=list2[4], systemname=system,
                    area_m2=10.96, high_m=5.4,
                    fire_load_density=1400, calorific_value_fire_load=14.5,
                    temp_inside = param_temp_inside, corridor_temp = param_corridor_temp)
    
    C_lvl1_np_66 = Room(name=list2[5], systemname=system,
                    area_m2=11.48, high_m=5.4,
                    fire_load_density=1400, calorific_value_fire_load=14.5,
                    temp_inside = param_temp_inside, corridor_temp = param_corridor_temp)
    
    C_lvl1_np_67 = Room(name=list2[6], systemname=system,
                    area_m2=9.4, high_m=5.4,
                    fire_load_density=180, calorific_value_fire_load=14.5,
                    temp_inside = param_temp_inside, corridor_temp = param_corridor_temp)
    
    C_lvl1_np_610 = Room(name=list2[7], systemname=system,
                    area_m2=3.39, high_m=5.4,
                    fire_load_density=180, calorific_value_fire_load=14.5,
                    temp_inside = param_temp_inside, corridor_temp = param_corridor_temp)
    
    C_lvl1_np_622 = Room(name=list2[8], systemname=system,
                    area_m2=6.76, high_m=5.4,
                    fire_load_density=180, calorific_value_fire_load=14.5,
                    temp_inside = param_temp_inside, corridor_temp = param_corridor_temp)
    
    C_lvl1_np_623 = Room(name=list2[9], systemname=system,
                    area_m2=6.49, high_m=5.4,
                    fire_load_density=180, calorific_value_fire_load=14.5,
                    temp_inside = param_temp_inside, corridor_temp = param_corridor_temp)
    
    C_lvl1_np_625 = Room(name=list2[10], systemname=system,
                    area_m2=10.76, high_m=5.4,
                    fire_load_density=180, calorific_value_fire_load=14.5,
                    temp_inside = param_temp_inside, corridor_temp = param_corridor_temp)
    
    C_lvl1_np_626 = Room(name=list2[11], systemname=system,
                    area_m2=13.77, high_m=5.4,
                    fire_load_density=1400, calorific_value_fire_load=14.5,
                    temp_inside = param_temp_inside, corridor_temp = param_corridor_temp)
    
    C_lvl1_np_627 = Room(name=list2[12], systemname=system,
                    area_m2=18.4, high_m=5.4,
                    fire_load_density=1400, calorific_value_fire_load=14.5,
                    temp_inside = param_temp_inside, corridor_temp = param_corridor_temp)
    
    C_lvl1_np_629 = Room(name=list2[13], systemname=system,
                    area_m2=5.64, high_m=5.4,
                    fire_load_density=180, calorific_value_fire_load=14.5,
                    temp_inside = param_temp_inside, corridor_temp = param_corridor_temp)
    
    C_lvl1_np_630 = Room(name=list2[14], systemname=system,
                    area_m2=4.14, high_m=5.4,
                    fire_load_density=180, calorific_value_fire_load=14.5,
                    temp_inside = param_temp_inside, corridor_temp = param_corridor_temp)
       
    list3 = ["подвал_Помещение СС", "подвал_ПУИ", "подвал_Мастерская эксплуатации"]

    C_bsm1_t_1 = Room(name=list3[0], systemname=system,
                    area_m2=6.4, high_m=3.0,
                    fire_load_density=180, calorific_value_fire_load=14.5,
                    temp_inside = param_temp_inside_basement, corridor_temp = param_corridor_temp_basement)
    
    C_bsm1_c_10 = Room(name=list3[1], systemname=system,
                    area_m2=8.2, high_m=3.0,
                    fire_load_density=180, calorific_value_fire_load=14.5,
                    temp_inside = param_temp_inside_basement, corridor_temp = param_corridor_temp_basement)
    
    C_bsm1_c_8 = Room(name=list3[2], systemname=system,
                    area_m2=43.8, high_m=3.0,
                    fire_load_density=180, calorific_value_fire_load=14.5,
                    temp_inside = param_temp_inside_basement, corridor_temp = param_corridor_temp_basement)
    
    
    coridor1 = Coridor(rooms=list1, opening_list=[2.1 * 0.8], corridor_hight=3.9, 
                       corridor_door_hight=2.1, corridor_door_width=0.8, corridor_area=30 ,corridor_lenght=15, coef_building_type=1.2)
    
    coridor2 = Coridor(rooms=list2, opening_list=[2.1 * 0.8], corridor_hight=3.9, 
                       corridor_door_hight=2.1, corridor_door_width=0.8, corridor_area=152.58 ,corridor_lenght=55, coef_building_type=1.2)
    
    coridor3 = Coridor(rooms=list3, opening_list=[2.1 * 0.8], corridor_hight=3.9, 
                       corridor_door_hight=2.1, corridor_door_width=0.8, corridor_area=75.85, corridor_lenght=41, coef_building_type=1.2)

    

    for i in range (0,len(coridor1.rooms)):
        room = Room.get_rooms_by_system_and_name(system,list1)[i]
        data = coridor1.smoke_exhaust_coridor(room)
        data_all_coridors[room.name] = data 
        
        
    for i in range (0,len(coridor2.rooms)):
        room = Room.get_rooms_by_system_and_name(system,list2)[i]
        data = coridor2.smoke_exhaust_coridor(room)
        data_all_coridors[room.name] = data 
        
    
    for i in range (0,len(coridor3.rooms)):
        room = Room.get_rooms_by_system_and_name(system,list3)[i]
        data = coridor3.smoke_exhaust_coridor(room)
        data_all_coridors[room.name] = data 
        

    # print(data_all_coridors.keys())
    
    for key, data in data_all_coridors.items():
        name_room = data["Значения"].values[1]
        data.to_csv(f"11692/{system}/{system} - {name_room}_data.csv")
        
        # print(f"{key} - {data['Значения'].values[35]} м3/ч")
        
 
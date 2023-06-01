from Room import Room
from Smoke_coridor import Coridor

param_temp_inside = 18
param_temp_inside_basement = 10
param_corridor_temp = 18
param_corridor_temp_basement = 10

def smoke_system_coridor_2():

    system = "C_coridor_2"
    data_all_coridors = {}
    
    list1 = ["lvl_2_Помещение ЭОМ",
            "lvl_2_Помещение СС",
            "lvl_2_ПУИ",
            "lvl_2_Помещение накопления мусорных контейнеров"]
    
    list1_area = [5.4, 6.6, 8.3, 4.6]
    list1_fire_load_density = [180, 180, 180, 1400]

    for room in range(len(list1)):
        Room(name=list1[room], systemname=system,
                area_m2=list1_area[room], high_m=3.9,
                fire_load_density=list1_fire_load_density[room], calorific_value_fire_load=14.5,
                temp_inside = param_temp_inside, corridor_temp = param_corridor_temp)
    
    coridor1 = Coridor(rooms=list1, opening_list=[2.1 * 0.8], corridor_hight=3.9, 
                       corridor_door_hight=2.1, corridor_door_width=0.8, corridor_area=15, corridor_lenght=7.6, coef_building_type=1.2)
    
    list2 =["lvl_1_Помещение ЭОМ",
            "lvl_1_Помещение СС",
            "lvl_1_ПУИ",
            "lvl_1_Помещение накопления мусорных контейнеров"]

    list2_area = [5.1, 6.4, 8.0, 4.5]
    list2_fire_load_density = [180, 180, 180, 1400]

    for room in range(len(list2)):
        Room(name=list2[room], systemname=system,
                area_m2=list2_area[room], high_m=3.9,
                fire_load_density=list2_fire_load_density[room], calorific_value_fire_load=14.5,
                temp_inside = param_temp_inside, corridor_temp = param_corridor_temp)
    
    coridor2 = Coridor(rooms=list2, opening_list=[2.1 * 0.8], corridor_hight=5.4, 
                       corridor_door_hight=2.1, corridor_door_width=0.8, corridor_area=33.7, corridor_lenght=22, coef_building_type=1.2)
    
    list3 =["подвал_Помещение хранения и мойки мусорных контейнеров",
            "подвал_Кладовая бытовых материалов",
            "подвал_Кладовая мебели",
            "подвал_Кладовая ТМЦ",
            "подвал_Кладовая уличного инвенторя",
            "подвал_Кладовая люминесцентых ламп"]

    list3_area = [49.84, 134.63, 220.16, 116.54, 43.48, 18.79]
    list3_fire_load_density = [180, 2200, 2200, 2200, 1400, 1400]

    for room in range(len(list3)):
        Room(name=list3[room], systemname=system,
                area_m2=list3_area[room], high_m=3.0,
                fire_load_density=list3_fire_load_density[room], calorific_value_fire_load=14.5,
                temp_inside = param_temp_inside, corridor_temp = param_corridor_temp)
    
    coridor3 = Coridor(rooms=list3, opening_list=[2.1 * 0.8], corridor_hight=3.0, 
                       corridor_door_hight=2.1, corridor_door_width=0.8, corridor_area=77.7, corridor_lenght=42, coef_building_type=1.2)
    

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
        data = coridor2.smoke_exhaust_coridor(room)
        data_all_coridors[room.name] = data 
        

    # print(data_all_coridors.keys())
    
    for key, data in data_all_coridors.items():
        name_room = data["Значения"].values[1]
        data.to_csv(f"11692/{system}/{system} - {name_room}_data.csv")
        
        # print(f"{key} - {data['Значения'].values[35]} м3/ч")
        
 
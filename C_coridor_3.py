from Room import Room
from Smoke_coridor import Coridor

param_temp_inside = 18
param_temp_inside_basement = 10
param_corridor_temp = 18
param_corridor_temp_basement = 10

def smoke_system_coridor_3():

    system = "C_coridor_3"
    data_all_coridors = {}
    
    list1 = ["lvl_1_Торговый павильон 1",
            "lvl_1_Торговый павильон 2",
            "lvl_1_Торговый павильон 3",
            "lvl_1_Кладовая сервисной службы"]

    list1_area = [157.2, 188.9, 153.8, 27.32]
    list1_fire_load_density = [800, 800, 800, 1400]

    for room in range(len(list1)):
        Room(name=list1[room], systemname=system,
                area_m2=list1_area[room], high_m=3.9,
                fire_load_density=list1_fire_load_density[room], calorific_value_fire_load=14.5,
                temp_inside = param_temp_inside, corridor_temp = param_corridor_temp)
    
    coridor1 = Coridor(rooms=list1, opening_list=[2.1 * 0.8], corridor_hight=5.4, 
                       corridor_door_hight=2.1, corridor_door_width=0.8, corridor_area=376.7, corridor_lenght=30, coef_building_type=1.2)

    for i in range (0,len(coridor1.rooms)):
        room = Room.get_rooms_by_system_and_name(system,list1)[i]
        data = coridor1.smoke_exhaust_coridor(room)
        data_all_coridors[room.name] = data 
        

    print(data_all_coridors.keys())
    
    for key, data in data_all_coridors.items():
        name_room = data["Значения"].values[1]
        data.to_csv(f"11692/{system}/{system} - {name_room}_data.csv")
        
        print(f"{key} - {data['Значения'].values[35]} м3/ч")
        
 
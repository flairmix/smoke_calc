from Room import Room
from Smoke_coridor import Coridor

param_temp_inside = 18
param_corridor_temp = 18

def smoke_system_coridor_3():

    system = "D_coridor_3"
    data_all_coridors = {}
    
    list1 = ["lvl_1_Ресторан 1",
            "lvl_1_Ресторан 2"]

    list1_area = [160.17, 98.81]
    list1_fire_load_density = [600, 600]

    for room in range(len(list1)):
        Room(name=list1[room], systemname=system,
                area_m2=list1_area[room], high_m=5.4,
                fire_load_density=list1_fire_load_density[room], calorific_value_fire_load=14.5,
                temp_inside = param_temp_inside, corridor_temp = param_corridor_temp)
    
    coridor1 = Coridor(rooms=list1, opening_list=[2.1 * 0.8], corridor_hight=5.4, 
                       corridor_door_hight=2.1, corridor_door_width=0.8, corridor_area=180.0, corridor_lenght=30, coef_building_type=1.2)

    for i in range (0,len(coridor1.rooms)):
        room = Room.get_rooms_by_system_and_name(system, list1)[i]
        data = coridor1.smoke_exhaust_coridor(room)
        data_all_coridors[room.name] = data 
        

    print(data_all_coridors.keys())
    
    for key, data in data_all_coridors.items():
        name_room = data["Значения"].values[1]
        data.to_csv(f"11692/{system}/{system} - {name_room}_data.csv")
        
        print(f"{key} - {data['Значения'].values[35]} м3/ч")
        
 
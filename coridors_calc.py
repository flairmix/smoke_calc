import pandas as pd
from Room import Room
from Coridor import Coridor


def calc_coridors_smoke(path_rooms, path_coridors):
    #buildig A
    # df_coridors = pd.read_csv (r'11692/bA/bA_coridors.csv', encoding='utf-8')
    # df_rooms = pd.read_csv (r'11692/bA/bA_room_categories.csv', encoding='utf-8')
    
    df_rooms = pd.read_csv (path_rooms, encoding='utf-8')
    df_coridors = pd.read_csv (path_coridors, encoding='utf-8')
    
    # print(df_coridors.info())
    # print(df_rooms.info())

    df_rooms.drop(df_rooms[df_rooms.Coridor_system_name == '-'].index, inplace=True)
    systems_unique = list(df_rooms['Coridor_system_name'].unique())
    levels_unique = list(df_rooms['level'].unique())
    
    # print(systems_unique)
    # print(levels_unique)

    df_list_systems = [(df_rooms.loc[df_rooms['Coridor_system_name'] == i]).reset_index(drop=True) for i in systems_unique]
   # print(df_systems[1])
    
    df_list_coridors = {}
    for i in range(len(df_coridors.index)):
        
        df_list_coridors[df_coridors.Coridor_system_name[i]+"_lvl"+str(df_coridors.level[i])] = (Coridor(rooms=[], 
                                        coridor_system_name=df_coridors.Coridor_system_name[i],
                                        level=df_coridors.level[i],
                                        opening_list=[df_coridors.corridor_door_hight_m[i] * df_coridors.corridor_door_width_m[i]], 
                                        corridor_hight=df_coridors.Coridor_hight_m2[i], 
                                        corridor_door_hight=df_coridors.corridor_door_hight_m[i], 
                                        corridor_door_width=df_coridors.corridor_door_width_m[i], 
                                        corridor_area=df_coridors.Coridor_area_m2[i], 
                                        corridor_lenght=df_coridors.Coridor_lenght_m[i], 
                                        coef_building_type=df_coridors.coef_building_type[i]))
        
    coridors_data_all = {}
    
    for data in df_list_systems:
        for room_number in range(len(data.index)):
            room = Room(name=data.Room_name[room_number], 
                        systemname=data.Coridor_system_name[room_number],
                        level=data.level[room_number],
                        area_m2=data.Room_area_m2[room_number], 
                        high_m=data.Room_hight_m[room_number],
                        fire_load_density=data.Fire_load_by_area_MJ_m2[room_number], 
                        calorific_value_fire_load=data.calorific_value_fire_load_average[room_number],
                        temp_inside = data.room_temperature[room_number], 
                        corridor_temp = data.coridor_temperature[room_number])

            data_to_write = df_list_coridors[room.systemname+"_lvl"+str(int(room.level))].smoke_exhaust_coridor(room)
            coridors_data_all[data.Room_number2[room_number]+"_"+room.name] = data_to_write
            
            folder = f"11692/{data.Coridor_system_name[room_number]}/"
            filename = f"{room.systemname}-{data.Room_number2[room_number]}-{room.level}-{room.name}"
            data_to_write.to_csv(f"{folder}{filename}_data.csv")

    for key, data in coridors_data_all.items():
        name_room = data["Значения"].values[1]
        print(f"{key} - {data['Значения'].values[35]} м3/ч")

    

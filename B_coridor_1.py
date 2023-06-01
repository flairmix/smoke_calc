from Room import Room
from Smoke_coridor import Coridor

param_temp_inside = 18
param_temp_inside_basement = 10
param_corridor_temp = 18
param_corridor_temp_basement = 10


def smoke_system_coridor_1():

    system = "B_coridor_1"
    data_all_coridors = {}

    B_bsm_c_01 = Room(name="подвал_ПУИ",
                      systemname=system,
                      area_m2=23.84,
                      high_m=3.0,
                      fire_load_density=180,
                      calorific_value_fire_load=14.5,
                      temp_inside=param_temp_inside,
                      corridor_temp=param_corridor_temp_basement)

    B_bsm_c_02 = Room(
        name="подвал_Помещение хранения и мойки мусорных контейнеров",
        systemname=system,
        area_m2=26.97,
        high_m=3.0,
        fire_load_density=1400,
        calorific_value_fire_load=14.5,
        temp_inside=param_temp_inside_basement,
        corridor_temp=param_corridor_temp_basement)

    B_bsm_c_10 = Room(name="подвал_Мастерская эксплуатации",
                      systemname=system,
                      area_m2=38.62,
                      high_m=3.0,
                      fire_load_density=180,
                      calorific_value_fire_load=14.5,
                      temp_inside=param_temp_inside_basement,
                      corridor_temp=param_corridor_temp_basement)

    B_bsm_c_11 = Room(name="подвал_Кладовая ТМЦ",
                      systemname=system,
                      area_m2=73.63,
                      high_m=3.0,
                      fire_load_density=1400,
                      calorific_value_fire_load=14.5,
                      temp_inside=param_temp_inside_basement,
                      corridor_temp=param_corridor_temp_basement)

    B_bsm_c_12 = Room(name="подвал_Кладовая мебели",
                      systemname=system,
                      area_m2=132.02,
                      high_m=3.0,
                      fire_load_density=1400,
                      calorific_value_fire_load=14.5,
                      temp_inside=param_temp_inside_basement,
                      corridor_temp=param_corridor_temp_basement)

    B_bsm_c_13 = Room(name="подвал_Кладовая уличного инвенторя",
                      systemname=system,
                      area_m2=39.4,
                      high_m=3.0,
                      fire_load_density=180,
                      calorific_value_fire_load=14.5,
                      temp_inside=param_temp_inside_basement,
                      corridor_temp=param_corridor_temp_basement)

    B_bsm_c_14 = Room(name="подвал_Кладовая люминесцентых ламп",
                      systemname=system,
                      area_m2=13.79,
                      high_m=3.0,
                      fire_load_density=180,
                      calorific_value_fire_load=14.5,
                      temp_inside=param_temp_inside_basement,
                      corridor_temp=param_corridor_temp_basement)

    B_bsm_c_15 = Room(name="подвал_Кладовая бытовых материалов",
                      systemname=system,
                      area_m2=88.62,
                      high_m=3.0,
                      fire_load_density=1400,
                      calorific_value_fire_load=14.5,
                      temp_inside=param_temp_inside_basement,
                      corridor_temp=param_corridor_temp_basement)

    B_2floor_t1 = Room(name="2эт.Помещение ЭОМ",
                       systemname=system,
                       area_m2=6.25,
                       high_m=3.9,
                       fire_load_density=180,
                       calorific_value_fire_load=14.5,
                       temp_inside=param_temp_inside,
                       corridor_temp=param_corridor_temp)

    B_2floor_t2 = Room(name="2эт.Помещение СС",
                       systemname=system,
                       area_m2=6.25,
                       high_m=3.9,
                       fire_load_density=180,
                       calorific_value_fire_load=14.5,
                       temp_inside=param_temp_inside,
                       corridor_temp=param_corridor_temp)

    А_2floor_c2 = Room(name="2эт.Помещение складирования мусорных контейнеров",
                       systemname=system,
                       area_m2=8,
                       high_m=3.9,
                       fire_load_density=1400,
                       calorific_value_fire_load=14.5,
                       temp_inside=param_temp_inside,
                       corridor_temp=param_corridor_temp)

    list1 = [
        "2эт.Помещение ЭОМ", "2эт.Помещение СС",
        "2эт.Помещение складирования мусорных контейнеров"
    ]

    list2 = [
        "подвал_ПУИ", "подвал_Помещение хранения и мойки мусорных контейнеров",
        "подвал_Мастерская эксплуатации", "подвал_Кладовая ТМЦ",
        "подвал_Кладовая мебели", "подвал_Кладовая уличного инвенторя",
        "подвал_Кладовая люминесцентых ламп",
        "подвал_Кладовая бытовых материалов"
    ]

    coridor1 = Coridor(rooms=list1,
                       opening_list=[2.1 * 0.8],
                       corridor_hight=3.9,
                       corridor_door_hight=2.1,
                       corridor_door_width=0.8,
                       corridor_area=6.45,
                       corridor_lenght=4.2,
                       coef_building_type=1.2)
    coridor2 = Coridor(rooms=list2,
                       opening_list=[2.1 * 0.8],
                       corridor_hight=3.0,
                       corridor_door_hight=2.1,
                       corridor_door_width=0.8,
                       corridor_area=101.75,
                       corridor_lenght=55,
                       coef_building_type=1.2)

    for i in range(0, len(coridor1.rooms)):
        room = Room.get_rooms_by_system_and_name(system, list1)[i]
        data = coridor1.smoke_exhaust_coridor(room)
        data_all_coridors[room.name] = data
        # data.to_csv(f"11692/{system} - lvl2 - {room.name}_data.csv")

    for i in range(0, len(coridor2.rooms)):
        room = Room.get_rooms_by_system_and_name(system, list2)[i]
        data = coridor2.smoke_exhaust_coridor(room)
        data_all_coridors[room.name] = data
        # data.to_csv(f"11692/{system} - lvl1 - {room.name}_data.csv")

    # print(data_all_coridors.keys())
    
    for key, data in data_all_coridors.items():
        name_room = data["Значения"].values[1]
        data.to_csv(f"11692/{system}/{system} - {name_room}_data.csv")

        # print(f"{key} - {data['Значения'].values[35]} м3/ч")

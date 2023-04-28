import pandas as pd

from Room import Room


def smoke_exhaust_coridor(room:Room, opening_list, 
                          corridor_hight, corridor_door_hight, corridor_door_width, 
                          corridor_area, corridor_lenght, 
                          coef_building_type
                         ):
    

    room.get_opening_list(opening_list)
    room.calc_A0()
    room.calc_Fw_unit_fire_load_by_walling()
    room.calc_v0_air_for_burn()
    room.calc_room_opening_rate(corridor_door_hight)
    room.calc_unit_fire_load_critical()
    room.calc_unit_fire_load_by_floor_square()
    room.define_type_of_fire()
    room.get_temp_inside()
    room.calc_max_temp()
    room.calc_temp_smoke_coridor()
    room.get_corridor_hight(corridor_hight)
    room.get_corridor_door_hight(corridor_door_hight)
    room.get_corridor_door_width(corridor_door_width)
    room.get_corridor_area(corridor_area)
    room.get_corridor_lenght(corridor_lenght)
    room.calc_corridor_smoke_hight_limit()
    room.get_corridor_temp()
    room.calc_corridor_smoke_temp()
    room.calc_corridor_door_area()
    room.get_coef_building_type(coef_building_type)
    room.calc_smoke_consumption_mass()
    room.calc_smoke_density()
    room.calc_smoke_consumption_vol()


    name_parameter = ["Наименование обслуживаемого помещения",
                    "Площадь пола помещения", 
                    "Высота помещения",
                    "Объём помещения",
                    "Суммарная площадь внутренней поверхности ограждающих строительных конструкций",
                    "Суммарная площадь проемов помещения",
                    "Низшая теплота сгорания древесины",
                    "Плотность пожарной нагрузки помещения", 

                    "Удельная приведенная пожарная нагрузка, отнесенная к площади тепловоспринимающей поверхности ограждающих строительных конструкций помещения",
                    "Средняя теплота сгорания пожарной нагрузки",
                    "Удельное количество воздуха, необходимое для полного сгораняи пожарной нагрузки",
                    "Проемность помещения",
                    "Удельное критическое количество пожарной нагрузки",
                    "Удельная приведенная пожарная нагрузка, отнесенная к площади пола помещения",

                    "Вид объемного пожара",
                    "Начальная температура воздуха в помещении",
                    "Начальная температура воздуха в помещении",
                    "Максимальная среднеобъемная температура в помещении",
                    "Искомое значение температуры газов, поступающих из горящего помещения в коридор",
                    "Высота коридора",
                    "Площадь коридора", 

                    "Длина коридора",
                    "Предельная толщина дымового слоя",
                    "Температура воздуха в коридоре",
                    "Температура воздуха в коридоре",
                    "Средняя температура дымового слоя",
                    "Поправочный коэффициент на тип здания",
                    "Высота двери при выходе из коридора по путям эвакуации",
                    "Ширина двери при выходе из коридора по путям эвакуации",
                    "Площадь двери при выходе из коридора по путям эвакуации",
                    "Массовый расход удаляемых непосредственно из коридоров продуктов горения",
                    "Плотность дымовых газов",
                    "Объемный расход удаляемых непосредственно из коридоров продуктов горения"


                    ]

    parameter = [
                room.name, 
                room.area_m2,
                room.high_m,
                room.room_volume_m3,
                room.Fw,
                room.A0,
                13.8, 
                room.fire_load_density,
                
                room.Fw_unit_fire_load_by_walling,
                room.calorific_value_fire_load,
                room.v0_air_for_burn,
                room.room_opening_rate,
                room.unit_fire_load_critical,
                room.unit_fire_load_by_floor_square,
                
                room.fire_type,
                room.temp_inside,
                room.temp_inside+273,
                room.max_temp,
                room.temp_smoke_coridor, room.corridor_hight, room.corridor_area,
                
                room.corridor_lenght,
                room.corridor_smoke_hight_limit,
                room.corridor_temp_K-273,
                room.corridor_temp_K,
                room.corridor_smoke_temp,
                room.coef_building_type,
                room.corridor_door_hight,
                room.corridor_door_width,
                room.corridor_door_area,
                room.smoke_consumption_mass,
                room.smoke_density,
                room.smoke_consumption_vol         
                ]


    units = ["-",
             "м2",
             "м",
             "м3",
             "м2",
             "м2",
             "МДж/кг",
             "МДж/м2",
             "кг/м2",
             "МДж/кг",
             "м3/кг",
             "м 1/2",
             "кг/м2",
             "кг/м2",
             "-",
             "C",
             "K",
             "K",
             "K",
             "м",
             "м",
             "м",
             "м",
             "C",
             "K",
             "K",
             "-",
             "-",
             "-",
             "м2",
             "кг/с",
             "-",
             "м3/ч",
            ]

    comments = ["-" for i in range(len(name_parameter))]
    formulas = ["-" for i in range(len(name_parameter))]
    sign = ["-" for i in range(len(name_parameter))]


    data = pd.DataFrame(name_parameter, columns=["Характеристика"])
    data["sign"] = sign
    data["Ед.измерения"] = units
    data["formulas"] = formulas
    data["Значения"] = parameter
    data["Примечания"] = comments

    return data
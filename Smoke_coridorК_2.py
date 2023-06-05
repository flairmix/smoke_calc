import pandas as pd
from Room import Room
from Room import CALORIFIC_VALUE_WOOD


class Coridor():

    def __init__(self, rooms, opening_list, corridor_hight,
                 corridor_door_hight, corridor_door_width, corridor_area,
                 corridor_lenght, coef_building_type):

        self.rooms = rooms
        self.opening_list = opening_list
        self.corridor_hight = corridor_hight
        self.corridor_door_hight = corridor_door_hight
        self.corridor_door_width = corridor_door_width
        self.corridor_area = corridor_area
        self.corridor_lenght = corridor_lenght
        self.coef_building_type = coef_building_type
        self.data = pd.DataFrame()

    def smoke_exhaust_coridor(self, room: Room):

        room.get_opening_list(self.opening_list)
        room.calc_A0()
        room.calc_Fw_unit_fire_load_by_walling()
        room.calc_v0_air_for_burn()
        room.calc_room_opening_rate(self.corridor_door_hight)
        room.calc_unit_fire_load_critical()
        room.calc_unit_fire_load_by_floor_square()
        room.define_type_of_fire()
        # room.get_temp_inside()
        room.calc_max_temp()
        room.calc_temp_smoke_coridor()
        room.get_corridor_hight(self.corridor_hight)
        room.get_corridor_door_hight(self.corridor_door_hight)
        room.get_corridor_door_width(self.corridor_door_width)
        room.get_corridor_area(self.corridor_area)
        room.get_corridor_lenght(self.corridor_lenght)
        room.calc_corridor_smoke_hight_limit()
        # room.get_corridor_temp()
        room.calc_corridor_smoke_temp()
        room.calc_corridor_door_area()
        room.get_coef_building_type(self.coef_building_type)
        room.calc_smoke_consumption_mass()
        room.calc_smoke_density()
        room.calc_smoke_consumption_vol()

        name_parameter = [
            "Коридор", "Наименование обслуживаемого помещения",
            "Площадь пола помещения", "Высота помещения", "Объём помещения",
            "Суммарная площадь внутренней поверхности ограждающих строительных конструкций",
            "Проем №1 ширина", "Проем №1 высота",
            "Суммарная площадь проемов помещения",
            "Низшая теплота сгорания древесины",
            "Плотность пожарной нагрузки помещения",
            "Удельная приведенная пожарная нагрузка, отнесенная к площади тепловоспринимающей поверхности ограждающих строительных конструкций помещения",
            "Средняя теплота сгорания пожарной нагрузки",
            "Удельное количество воздуха, необходимое для полного сгорания пожарной нагрузки",
            "Проемность помещения",
            "Удельное критическое количество пожарной нагрузки",
            "Удельная приведенная пожарная нагрузка, отнесенная к площади пола помещения",
            "Вид объемного пожара",
            "Начальная температура воздуха в помещении",
            "Начальная температура воздуха в помещении",
            "Максимальная среднеобъемная температура в помещении",
            "Искомое значение температуры газов, поступающих из горящего помещения в коридор",
            "Высота коридора", "Площадь коридора", "Длина коридора",
            "Предельная толщина дымового слоя",
            "Температура воздуха в коридоре", "Температура воздуха в коридоре",
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
            "-", room.name, room.area_m2, room.high_m, room.room_volume_m3,
            room.Fw, room.corridor_door_width, room.corridor_door_hight,
            room.A0, CALORIFIC_VALUE_WOOD, room.fire_load_density,
            room.Fw_unit_fire_load_by_walling, room.calorific_value_fire_load,
            room.v0_air_for_burn, room.room_opening_rate,
            room.unit_fire_load_critical, room.unit_fire_load_by_floor_square,
            "Регулируемый вентиляцией"
            if room.fire_type.value == 1 else "Регулируемый нагрузкой",
            room.temp_inside, room.temp_inside + 273, room.max_temp,
            room.temp_smoke_coridor, room.corridor_hight, room.corridor_area,
            room.corridor_lenght, room.corridor_smoke_hight_limit,
            room.corridor_temp_K - 273, room.corridor_temp_K,
            room.corridor_smoke_temp, room.coef_building_type,
            room.corridor_door_hight, room.corridor_door_width,
            room.corridor_door_area, room.smoke_consumption_mass,
            room.smoke_density, room.smoke_consumption_vol
        ]

        for i in range(0, len(parameter)):
            if type(parameter[i]) == float:
                parameter[i] = round(parameter[i], 2)

        units = [
            "-",
            "-",
            "м2",
            "м",
            "м3",
            "м2",
            "м",
            "м",
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
            "м2",
            "м",
            "м",
            "C",
            "K",
            "K",
            "-",
            "м",
            "м",
            "м2",
            "кг/с",
            "кг/м3",
            "м3/ч",
        ]

        sign = [
            "-", "-", "Fƒ", "hƒ", "V", "Fw", "-", "-", "A0", "Qнд", "qп", "qk",
            "Qнср", "V0", "П", "qkкр", "q0", "-", "tr", "Tr", "T0max", "T0",
            "H", "Ac", "lc", "hsm", "trk", "Trk", "Tsm", "ksm", "Hd", "bd",
            "Ad", "Gsm", "ρsm", "Lsm"
        ]

        data = pd.DataFrame(name_parameter, columns=["Характеристика"])
        data["Обозначение"] = sign
        data["Ед.измерения"] = units
        data["Значения"] = parameter

        return data

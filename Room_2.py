from enum import Enum
from math import exp
from pydantic import BaseModel

CALORIFIC_VALUE_WOOD = 13.8 #Низшая теплота сгорания древесины


class Fire_type(Enum):
    FIRE_BY_VENT = 1
    FIRE_BY_FIRELOAD = 2

class Coridor(BaseModel):
    def __init__(self, 
                 number: str, 
                 lvl: str, 
                 name: str, 
                 corridor_length: float, 
                 corridor_hight: float, 
                 area: float, 
                 corridor_temp: int, 
                 coef_building_type: float, 
                 rooms: list):
      self.number = number
      self.lvl = lvl
      self.name = name
      self.corridor_length = corridor_length
      self.corridor_hight = corridor_hight
      self.area = area
      self.corridor_temp = corridor_temp
      self.coef_building_type = coef_building_type
      self.rooms = rooms


class Room(BaseModel):
    def __init__(self, 
                name: str, 
                area_m2: float, 
                high_m: float,
                fire_load_density: float, 
                calorific_value_fire_load: list,
                temp_inside: int = 24):
        self.name = name
        self.area_m2 = area_m2
        self.high_m = high_m
        self.fire_load_density = fire_load_density
        self.calorific_value_fire_load = calorific_value_fire_load
        self.temp_inside = temp_inside


class Room():
    id = [0]
    systemname_items = {}
    items = []
    
    def __init__(self, systemname: str, 
                 name, area_m2: float, high_m: float,
                 fire_load_density: float, calorific_value_fire_load: list,
                temp_inside :int = 24,
                corridor_temp : int = 24):
        
        self.systemname = systemname
        self.add_id()
        self.add_systemname_item(self)
        Room.items.append(self)
        self.id = self.id[-1]
        self.name: str = name
        self.area_m2: float = area_m2
        self.high_m: float = high_m
        self.room_volume_m3: float = self.area_m2 * self.high_m
        self.Fw: float = round(6 * pow(self.room_volume_m3, 0.667), 2)
        self.opening_list_m2: list = []
        self.A0: float = 0
        #Плотность пожарной нагрузки помещения
        self.fire_load_density: float = fire_load_density
        self.Fw_Fw_unit_fire_load_by_walling: float = 0
        #Средняя теплота сгорания пожарной нагрузки
        self.calorific_value_fire_load = calorific_value_fire_load
        self.calorific_value_fire_load_mass = []
        # V0 Удельное количество воздуха, необходимое для полного сгораняи пожарной нагрузки
        self.v0_air_for_burn: float = 0
        # Проемность помещения
        self.room_opening_rate: float = 0
        #gkkr Удельное критическое количество пожарной нагрузки
        self.unit_fire_load_critical = 0
        # g0 Удельная приведенная пожарная нагрузка, отнесенная к площади пола помещения
        self.unit_fire_load_by_floor_square = 0
        # Вид объемного пожара
        self.fire_type = Fire_type.FIRE_BY_VENT
        # Начальная температура воздуха в помещении
        self.temp_inside = temp_inside
        self.temp_inside_K: int = 273 + self.temp_inside
        # Максимальная среднеобъемная температура в помещении K
        self.max_temp: int = 0
        # Максимальная среднеобъемная температура в коридоре K
        self.temp_smoke_coridor: int = 0
        self.corridor_hight = 0
        self.corridor_door_hight = 0
        self.corridor_door_width = 0
        self.corridor_area = 0
        self.corridor_lenght = 0
        # Предельная толщина дымового слоя
        self.corridor_smoke_hight_limit = 0
        self.corridor_temp = corridor_temp
        self.corridor_temp_K = self.corridor_temp + 273
        self.corridor_smoke_temp = 0
        self.coef_building_type = 1.2
        self.corridor_door_area = 0
        self.smoke_consumption_mass = 0
        self.smoke_density = 0
        self.smoke_consumption_vol = 0

    def __str__(self):
        return f"class Room: id-{self.id}, system - {self.systemname}, name - {self.name}"

    def get_rooms(self) -> list:
        return [str(room) for room in Room.items]

    def add_id(self) -> None:
        self.id.append(self.id[-1] + 1)

    def add_systemname_item(cls, self) -> None:
        if self.systemname not in cls.systemname_items:
            cls.systemname_items[self.systemname] = [self]
        else:
            cls.systemname_items[self.systemname].append(self)

    @classmethod
    def get_rooms_by_system_and_name(cls, system:str, room_names:list):
        rooms = cls.systemname_items[system]
        rooms_result = []
        for room in rooms: 
            if room.name in room_names:
                rooms_result.append(room)
        # print(rooms_result)
        return rooms_result
    
    def get_area_m2(self, area_m2)-> None:
        self.area_m2 = area_m2

    def get_high_m(self, high_m)-> None:
        self.high_m = high_m

    def calc_room_volume_m3(self)-> None:
        self.room_volume_m3 = self.area_m2 * self.high_m

    def calc_Fw(self)-> None:
        """
        Суммарная площадь внутренней поверхности ограждающих строительных конструкций
        Приложение 1 МР 2013
        """
        self.Fw = round(6 * pow(self.room_volume_m3, 0.667), 2)

    def get_opening_list(self, opening_list_m2: list)-> None:
        self.opening_list_m2 = opening_list_m2

    def calc_A0(self)-> None:
        """
        Суммарная площадь проемов помещения
        Приложение 1 МР 2013. 
        Ai - площадь i-го проема
        """
        self.A0 = sum(self.opening_list_m2)

    def get_fire_load_density(self, fire_load_density: int)-> None:
        """
        Плотность пожарной нагрузки помещения
        q_п
        СИТИС-СПН-1. Пожарная нагрузка. Справочник (Таблица 1)
        """
        self.fire_load_density = fire_load_density

    def calc_Fw_unit_fire_load_by_walling(self)-> None:
        """
        2. gk - удельная приведенная пожарная нагрузка, отнесенная к площади тепловоспринимающей поверхности
        ограждающих строительных конструкций, кг/м2
        Приложение 1 МР 2013
        """
        self.Fw_unit_fire_load_by_walling = (
            self.area_m2 * self.fire_load_density) / (
                (self.Fw - self.A0) * CALORIFIC_VALUE_WOOD)

    def get_calorific_value_fire_load(self, calorific_value_fire_load: float):
        """
        Средняя теплота сгорания пожарной нагрузки МДж/кг
        Приложение 1 МР 2013. А также: СИТИС-СПН-1. Пожарная нагрузка. Справочник (Таблица 2)
        """
        self.calorific_value_fire_load = calorific_value_fire_load

    def calc_v0_air_for_burn(self)-> None:
        """
        V0 - Удельное количество воздуха, необходимое для полного сгорания пожарной нагрузки помещения, 
        м3/кг
        Приложение 1 МР 2013
        """
        # для расчета при списке пожарных нагрузок со списком масс
        # i = 0
        # for f, b in zip(self.calorific_value_fire_load, self.calorific_value_fire_load_mass):
        #     i += b * f/sum(self.calorific_value_fire_load_mass)

        # self.v0_air_for_burn = round((0.263 * i ), 2)

        self.v0_air_for_burn = 0.263 * self.calorific_value_fire_load

    def calc_room_opening_rate(self, hight_opening: float)-> None:
        """
        П - Проемность помещения, pow(м, 0.5)
        """
        self.room_opening_rate = round(self.A0 * pow(hight_opening, 0.5) / pow(self.room_volume_m3, 0.66), 3)

    def calc_unit_fire_load_critical(self)-> None:
        """
        Удельное критическое количество пожарной нагрузки
        кг/м2
        Приложение 1 МР 2013
        """
        self.unit_fire_load_critical = (
            (4500 * self.room_opening_rate**3) /
            (1 + (500 * self.room_opening_rate**3))) + (
                (self.room_volume_m3**0.33) / (6 * self.v0_air_for_burn))

    def calc_unit_fire_load_by_floor_square(self)-> None:
        """
        Удельная приведенная пожарная нагрузка, отнесенная к площади пола помещения
        кг/м2
        Приложение 1 МР 2013
        """
        self.unit_fire_load_by_floor_square = self.fire_load_density / CALORIFIC_VALUE_WOOD

    def define_type_of_fire(self)-> None:
        """
        Вид объемного пожара
        gk > gkкр = ПРВ
        gk < gkкр = ПРН

        FIRE_BY_VENT = 1
        FIRE_BY_FIRELOAD = 2
        """
        self.fire_type.FIRE_BY_VENT if self.Fw_unit_fire_load_by_walling > self.unit_fire_load_critical else self.fire_type.FIRE_BY_FIRELOAD

    def get_temp_inside(self, temp_inside : int)-> None:
        self.temp_inside = temp_inside

    def calc_max_temp(self)-> None:
        """ Максимальная среднеобъемная температура в помещении K"""
        if self.fire_type == Fire_type.FIRE_BY_VENT:
            self.max_temp = self.temp_inside_K + 940 * exp(
                0.0047 * self.unit_fire_load_by_floor_square - 0.141)
        else:
            self.max_temp = self.temp_inside_K + 224 * pow(
                self.Fw_unit_fire_load_by_walling, 0.528)

    def calc_temp_smoke_coridor(self)-> None:
        """	Максимальная среднеобъемная температура в помещении"""
        self.temp_smoke_coridor = 0.8 * self.max_temp

    def get_corridor_hight(self, corridor_hight: float)-> None:
        self.corridor_hight = corridor_hight

    def get_corridor_door_hight(self, corridor_door_hight: float)-> None:
        self.corridor_door_hight = corridor_door_hight

    def get_corridor_door_width(self, corridor_door_width: float)-> None:
        self.corridor_door_width = corridor_door_width

    def get_corridor_area(self, corridor_area: float)-> None:
        self.corridor_area = corridor_area

    def get_corridor_lenght(self, corridor_lenght: float)-> None:
        self.corridor_lenght = corridor_lenght

    def calc_corridor_smoke_hight_limit(self, h=0.55):
        self.corridor_smoke_hight_limit = self.corridor_hight * h

    def get_corridor_temp(self, corridor_temp: float = 24)-> None:
        self.corridor_temp = corridor_temp
        self.corridor_temp_K = self.corridor_temp + 273

    def calc_corridor_smoke_temp(self)-> None:
        a = self.corridor_temp_K
        b = (1.22 * (self.temp_smoke_coridor - self.corridor_temp_K) *
             (2 * self.corridor_smoke_hight_limit +
              (self.corridor_area / self.corridor_lenght))
             ) / self.corridor_lenght
        c = 1 - exp((-0.58 * self.corridor_lenght) /
                    (2 * self.corridor_smoke_hight_limit +
                     (self.corridor_area / self.corridor_lenght)))

        self.corridor_smoke_temp = a + b * c

    def calc_corridor_door_area(self)-> None:
        self.corridor_door_area = self.corridor_door_width * self.corridor_door_hight

    def get_coef_building_type(self, coef_building_type: float = 1.2)-> None:
        self.coef_building_type = coef_building_type

    def calc_smoke_consumption_mass(self)-> None:
        self.smoke_consumption_mass = self.coef_building_type * self.corridor_door_area * pow(
            self.corridor_door_hight, 0.5)

    def calc_smoke_density(self)-> None:
        self.smoke_density = 353 / self.corridor_smoke_temp

    def calc_smoke_consumption_vol(self)-> None:
        self.smoke_consumption_vol = 3600 * (self.smoke_consumption_mass /
                                             self.smoke_density)

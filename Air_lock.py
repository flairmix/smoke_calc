from enum import Enum
import pandas as pd 

class Airlock_type(Enum):
    Airlock_fireteam = 1 
    Airlock_basement = 2


class Airlock():
    id = [0]
    systemname_items = {}
    items = []
    
    def __init__(self, systemname: str, 
                name, 
                description,
                door_hight_m: float, 
                door_width_m: float,
                airlock_lvl_m: float,
                deep_of_building_m: float,
                height_difference_m: float,
                temp_outside_С: int = -26,
                temp_inside_С: int = 18,
                velocity_m_s: float = 1.5,
                other_pressure_Pa = 50
                ):
        
        self.systemname = systemname
        self.name = name
        self.description = description
        self.add_id()
        self.add_systemname_item(self)
        Airlock.items.append(self)
        self.door_hight_m = door_hight_m
        self.door_width_m = door_width_m
        self.door_area_m2 = round(self.door_hight_m * self.door_width_m, 2)
        self.temp_outside_С = temp_outside_С
        self.temp_inside_С = temp_inside_С
        self.air_outside_density = round(353 / (self.temp_outside_С+273.15), 2)
        self.air_inside_density = round(353 / (self.temp_inside_С+273), 2)
        self.Gr_airflow_kg_s = 0
        self.velocity_m_s = velocity_m_s
        self.airlock_lvl_m = airlock_lvl_m
        self.airlock_pressure_Pa = 0
        self.deep_of_building_m = deep_of_building_m
        self.height_difference_m = height_difference_m
        self.other_pressure_Pa = other_pressure_Pa
        self.data = pd.DataFrame()
    
    def __str__(self):
        return f"class Airlock: id-{self.id}, system - {self.systemname}, name - {self.name}"

    def add_id(self) -> None:
        self.id.append(self.id[-1] + 1)

    def add_systemname_item(cls, self) -> None:
        if self.systemname not in cls.systemname_items:
            cls.systemname_items[self.systemname] = [self]
        else:
            cls.systemname_items[self.systemname].append(self)

    @classmethod
    def get_airlocks_by_system_and_name(cls, system:str, airlock_names:list):
        airlocks = cls.systemname_items[system]
        airlocks_result = []
        for airlock in airlocks: 
            if airlock.name in airlock_names:
                airlocks_result.append(airlock)
        return airlocks_result

    def calc_Gr_airflow_kg_s(self) -> float:
        '''
        Calculation airflow for defend air supply in airlock, kg/s 
        '''
        self.Gr_airflow_kg_s = round(self.velocity_m_s * self.air_outside_density * self.door_area_m2, 2)
        return self.Gr_airflow_kg_s 

    def calc_airlock_pressure_Pa(self) -> None:
        if self.airlock_lvl_m < 0:
            self.airlock_pressure_Pa = 20 + \
                9.81 * (self.deep_of_building_m * (self.airlock_lvl_m + 0.5 * self.door_area_m2) * \
                (self.air_outside_density - self.air_inside_density))
        else:
            self.airlock_pressure_Pa = 20 - \
                9.81 * (self.airlock_lvl_m + 0.5 * self.door_area_m2) * \
                (self.air_outside_density - self.air_inside_density)
        return round(self.airlock_pressure_Pa, 2)

    def calc_Lv_airflow_m3_h(self):
        return round(3600 * self.Gr_airflow_kg_s / self.air_outside_density, 2)

    def calc_fan_pressure_Pa(self):
        return round(1.2 * ((self.airlock_pressure_Pa + 9.81*self.height_difference_m*(self.air_outside_density - self.air_inside_density)) +self.other_pressure_Pa / (self.air_outside_density)))

    def create_report_df(self):
        name_parameter = [
            "Наименование", 
            "Описание", 
            "Уровень отметки этажа", 
            "Скорость истечения воздуха через одну открытую дверь защищаемого тамбур-шлюза", 
            "Площадь двери защищаемого тамбур-шлюза", 
            "Температура наружного воздуха", 
            "Плотность воздуха при температуре Ta", 
            "Температура воздуха внутренняя", 
            "Плотность воздуха при температуре Tr", 
            "Массовый расход воздуха, подаваемый в тамбур-шлюз", 
            "Давление в защищаемом тамбур-шлюзе", 
            "Суммарное сопротивление присоединительных воздуховодов", 
            "Вентилятор - Объемный расход воздуха", 
            "Вентилятор - Давление"
        ]

        sign = [
            "-", "-", 
            "h_i",
            "v_r",
            "F_dr",
            "T_a",
            "ρ_a",
            "T_r",
            "ρ_r",
            "G_r",
            "P_(r-i)",
            "P_d",
            "L_v",
            "P_v"
        ]

        units = [
            "-", "-", 
            "м",
            "м/с ",
            "м2",
            "оС",
            "кг/м3",
            "оС",
            "кг/м3",
            "кг/с",
            "Па",
            "Па",
            "m3/h",
            "Па"
        ]

        parameter = [
            self.name, 
            self.description, 
            self.airlock_lvl_m, 
            self.velocity_m_s, 
            self.door_area_m2, 
            self.temp_outside_С, 
            self.air_outside_density, 
            self.temp_inside_С, 
            self.air_inside_density, 
            self.calc_Gr_airflow_kg_s(), 
            self.calc_airlock_pressure_Pa(), 
            self.other_pressure_Pa, 
            self.calc_Lv_airflow_m3_h(), 
            self.calc_fan_pressure_Pa()
        ]
        
        data = pd.DataFrame(name_parameter, columns=["Характеристика"])
        data["Обозначение"] = sign
        data["Ед.измерения"] = units
        data["Значения"] = parameter

        self.data = data
    
    def update_report(self):
        pass

    def create_report_csv(self):
        self.data.to_csv(f"11692/{self.systemname} - {self.name}_data.csv") 

    
        
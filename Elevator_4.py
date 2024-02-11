# WIP

import pandas as pd 


class Elevator_4():
    id = [0]
    items = {}

    @classmethod
    def get_elevators_4(cls):
        return [str(elevators_4) for elevators_4 in Elevator_4.items]
    
    @classmethod
    def get_elevator_4_by_id(cls, id):
        return Elevator_4.items[id]
        
    def __init__(self,
                 name : str,
                 lvl_amount : int,
                 lvl_height: list,
                 elevator_shaft_area : float,
                 elevator_cabin_area : float,
                 lvl_doors_height: list,
                 lvl_doors_widts: list,
                 wind : float = 2,
                 Tr : int = 18,
                 Ta : int = -26
                ):
        self.add_id()
        self.id = self.id[-1]
        Elevator_4.items[self.id] = self
        self.name = name      
        self.lvl_amount = lvl_amount
        self.elevator_shaft_area = elevator_shaft_area
        self.elevator_cabin_area = elevator_cabin_area
        self.lvl_height = lvl_height
        self.lvl_doors_height = lvl_doors_height
        self.lvl_doors_widts = lvl_doors_widts
        self.lvl_doors_area : list = [x * y for x, y in zip(self.lvl_doors_height, self.lvl_doors_widts) ]
        self.wind = wind
        self.Tr, self.Ta, = Tr, Ta
        self.Tl = int(0.5 * (self.Ta + self.Tr))
        self.Dns_r = round(353 / (self.Tr + 273), 2)
        self.Dns_a = round(353 / (self.Ta + 273), 2)
        self.Dns_l = round(353 / (self.Tl + 273), 2)
        self.Pl2 = 0 #pressure on lvl_2 door 
        self.Pli = [0] #pressure on lvl_i door       
        self.Gli = [0] #airflow commulative with losses on lvl_i   
        self.dGli = [0] #airflow through closed doors on lvl_i
        self.fan_G_m3_h = 0 #fan airflow characteristic
        self.fan_P_Pa = 0 #fan pressure characteristic
        self.lvl_height_h0s = 5 #разность между уровнями расположения приемного устройства и верхов ЛК, м
        self.P_h0s_losses = 60 #потери давления в сети от вентилятора до ЛК
        self.data = pd.DataFrame()

    
    def __str__(self) -> str:
        return f"id-{self.id}, name - {self.name}"
    
    def add_id(self) -> None:
        Elevator_4.id.append(self.id[-1] + 1)
        
    def create_elevator(self) -> None:
        Elevator_4.items[self.id] = self 
        
    def delete_elevator(self) -> None:
        del items[self.id] 
        
    #calculations 
    def calc_pressure_lvl2(self) -> None:
        '''Calculation pressure on the close lift door no the second floor, Pa
            Расчет давления на этаже выше первого надземного, Па'''
        self.Pl2 = round(20 - (9.81 * (self.lvl_height[0] + 0.5 * self.lvl_doors_height[1]) * (self.Dns_l - self.Dns_r)) + (0.25 * (1.4) * self.Dns_a * pow(self.wind, 2)), 2)
        self.Pli.append(self.Pl2 for i in range(1, len(self.Pli)))
      
    def calc_Gl1(self) -> None:
        '''Calculation airflow through open lift door on the ground floor, m3/h;
            Расчет расхода воздуха через открытую дверь лифта на первом этаже, м3/ч'''
        self.Gsa = round(
            pow((2 * self.Dns_l / (
                ((4.3+(self.elevator_cabin_area/self.elevator_shaft_area))**2))
                 * (self.Pl2 + 

                0.5 * 9.81 * 0.5 * self.lvl_doors_height[0] *
                (self.Dns_a - self.Dns_s)
            , 0.5)
            , 2)





    def calc_dGsi(self, lvl):
        return round(
            self.lvl_doors_area[lvl] * pow((
                self.Psi[lvl] + 9.81 *
                (self.lvl_height[lvl - 1] + 0.5 * self.lvl_doors_height[lvl]) *
                (self.Dns_s - self.Dns_r)) / (5300 / self.Dns_s), 0.5), 2)

    def lvl_losses(self):

        for lvl in range(1, len(self.lvl_height)):

            self.dGsi.append(self.calc_dGsi(lvl))
            self.Gsi.append(round(self.Gsi[lvl] + self.dGsi[lvl], 2))
            self.Psi.append(
                round(
                    self.Psi[lvl] +
                    (0.5 * self.starcase_local_resistance * self.Dns_s) *
                    (self.Gsi[lvl] / self.Dns_s / self.starcase_area)**2, 2))

        self.dGsi.append(self.calc_dGsi(len(self.lvl_height)))

    def calc_fan_G_m3_h(self):
        '''Расход воздуха для подбора вентилятора подбор ЛК 3, м3/ч'''
        self.fan_G_m3_h = round((3600 * self.Gsi[-1]) / self.Dns_a, 2)

    def calc_fan_P_Pa(self):
        '''Напор для подбора вентилятора подбор ЛК 3, Па'''
        self.fan_P_Pa = round(
            1.2 * (self.Psi[-1] + 
                   9.81*(self.lvl_height[-1] - self.lvl_doors_height[0]) * (self.Dns_a - self.Dns_s) + 
                    9.81*(self.lvl_height_h0s) * (self.Dns_a - self.Dns_s) + 
                   self.P_h0s_losses
                  ) / self.Dns_a
            , 2)

    
    def calc_starcase_all(self):
        
        self.calc_pressure_lvl2()
        self.calc_Gsa()
        self.calc_max_G()
        self.lvl_losses()
        self.calc_fan_G_m3_h()
        self.calc_fan_P_Pa()

    
    def create_df(self):
        name_parameter = [
            "Лестничная шахта № 1",
            "Расположение – в центральном ядре, ",
            "сообщение – только с надземными этажами, ",
            "изолированный наружный выход",
            "Количество этажей:",
            "Высота этажа 2",
            "Высота этажа 3",
            "Высота этажа 4",
            "Высота этажа 5",
            "Площадь проекции лестничной клетки:",
            "Высота дверного проема на этаже",
            "Площадь дверного проема на этаже",
            "Высота дверного проема на выходе",
            "Площадь дверного проема на выходе",
            "Средняя скорость ветра",
            "Температура воздуха внутренняя",
            "Температура наружного воздуха",
            "Значение коэф. местного сопротивления лестничного марша в пределах i-го этажа",
            "Тип тамбура наружного выхода",
            "Значение коэф. местного сопротивления для тамбура",
            "Значение коэф. местного сопротивления для наружной двери",
            "Количество последовательно расположенных дверей наружного выхода лестничной клетки",
            "Коэффициент сопротивления маршей лестничной клетки",
            "Количество лестничных клеток, имеющих выходы в тот же коридор (помещение), защищаемое приточной противодымной вентиляцией ",
            "Расчетное количество лестничных клеток",
            "Массовый расход удаляемых продуктов горения",
            "Температура воздуха в лестничной клетке:",
            "Плотность воздуха при температуре Ts",
            "Плотность воздуха при температуре Tr",
            "Плотность воздуха при температуре Ta",
            "Внутреннее давление на уровне вышележащего этажа",
            "Разница аэродинамических коэффициентов для наветренной и заветренной стороны здания ",
            "Массовый расход воздуха через наружный выход лестничной клетки",
            "Массовый расход воздуха через открытый проем лестничной клетки на уровне второго надземного этажа здания",
            "Внутреннее давление на уровне вышележащего этажа",
            "Давление в лестничной клетке на уровне 3 этажа",
            "Давление в лестничной клетке на уровне 4 этажа",
            "Давление в лестничной клетке на уровне 5 этажа",
            "Массовый расход воздуха через наружный выход лестничной клетки",
            "Утечки через неплотность дверных проёмов на уровне 3 этажа",
            "Массовый расход воздуха на уровне 3 этажа",
            "Утечки через неплотность дверных проёмов на уровне 4 этажа",
            "Массовый расход воздуха на уровне 4 этажа",
            "Утечки через неплотность дверных проёмов на уровне 5 этажа",
            "Массовый расход воздуха на уровне 5 этажа",
            "Объемный расход воздуха в лестничной клетке",
            "Давление вентилятора "
        ]

        sign = [i for i in range(len(name_parameter))]
        units = [i for i in range(len(name_parameter))]
        
        parameter = [
            "",
            "",
            "",
            "",
            self.lvl_amount,
            self.lvl_height[0],
            self.lvl_height[1],
            self.lvl_height[2],
            self.lvl_height[3],
            self.starcase_area,
            self.lvl_doors_height[1],
            self.lvl_doors_area[1],
            self.lvl_doors_height[0],
            self.lvl_doors_area[0],
            self.wind,
            self.Tr,
            self.Ta,
            self.starcase_local_resistance,
            "прямой",
            self.vestibule_local_resistance,
            self.door_local_resistance,
            self.n,
            self.z,
            self.q+1,
            self.q,
            self.Gsm,
            self.Ts,
            self.Dns_s,
            self.Dns_r,
            self.Dns_a,
            self.Psi[1],
            1.4,
            self.Gsa,
            self.G,
            self.Psi[1],
            self.Psi[2],
            self.Psi[3],
            self.Psi[4],
            self.G,
            self.dGsi[2],
            self.Gsi[2],
            self.dGsi[3],
            self.Gsi[3],
            self.dGsi[4],
            self.Gsi[4],
            self.fan_G_m3_h,
            self.fan_P_Pa
        ]
        
        data = pd.DataFrame(name_parameter, columns=["Характеристика"])
        data["sign"] = sign
        data["Ед.измерения"] = [
                                "-",
                                "-",
                                "-",
                                "-",
                                "-",
                                "м",
                                "м",
                                "м",
                                "м",
                                "м",
                                "м",
                                "м2",
                                "м",
                                "м2",
                                "м/с",
                                "С",
                                "С",
                                "-",
                                "-",
                                "-",
                                "-",
                                "шт",
                                "-",
                                "шт",
                                "шт",
                                "кг/с ",
                                "С",
                                "кг/м3",
                                "кг/м3",
                                "кг/м3",
                                "Па",
                                "-",
                                "кг/с ",
                                "кг/с ",
                                "Па",
                                "Па",
                                "Па",
                                "Па",
                                "кг/с ",
                                "кг/с ",
                                "кг/с ",
                                "кг/с ",
                                "кг/с ",
                                "кг/с ",
                                "кг/с ",
                                "м3/ч ",
                                "Па"
        ]
        data["Значения"] = parameter

        self.data = data

    def starcase_df_to_csv(self):
        self.data.to_csv(f"{self.name}_data.csv")
    

       
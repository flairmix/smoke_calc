from enum import Enum
from math import exp


class Fire_type(Enum):
    FIRE_BY_VENT = 1
    FIRE_BY_FIRELOAD = 2


class Zone():
    id = [0]
    items = []

    def __init__(self, name, area_m2:float, high_m:float, 
                 Qr: float, 
                 vQr: float):
                     
        self.add_id() 
        Zone.items.append(self)
        self.id = self.id[-1] 
        self.name:str  = name  
        self.area_m2:float = area_m2
        self.H:float = high_m
        self.h: float = 0
                     
        self.room_volume_m3:float = self.area_m2 * self.H  
        self.Fw:float = round(6 * pow(self.room_volume_m3, 0.667), 2)
            
        self.Qr: float = Qr
        self.vQr: float = vQr
        self.F0: float = 0
        self.z: float = 0

        self.Qf: float = 0
        self.z1_fire_high: float = 0     
        self.Gk_smoke_flow: float = 0

    def __str__(self):
        return f"id-{self.id}, name - {self.name}"

    def add_id(self):
        self.id.append(self.id[-1]+1)
    
    def get_Qr(self, Qr):
        '''средняя теплота сгорания пожарной нагрузки, кДж/кг'''
        self.Qr = Qr
        
    def get_vQr(self, vQr):
        '''средняя скорость потери массы пожарной нагрузки, кг/м²•с'''
        self.vQr = vQr
    
    def get_z(self, z=2.1):
        '''высота незадымленной зоны, м'''
        self.z = z
        
    def get_F0(self, F0=9):
        ''' площадь горения пожарной нагрузки, м².'''
        self.F0 = F0
        
    def calc_Qf(self):
        ''' мощность тепловыделения очага пожара, кВт'''
        self.Qf = round(0.9 * self.Qr * self.vQr * self.F0, 2)
         
    def calc_h(self):
        '''толщина образующегося дымового слоя, м'''
        self.h = self.H - self.z
        
    def calc_z1_fire_high(self):
        '''высота факела пламени'''
        self.z1_fire_high = 0.166 * pow(0.7 * self.Qf, 0.4)

    def calc_Gk_smoke_flow(self):
        '''массовый расход продуктов горения в конвективной колонке'''
        if self.z1_fire_high and self.z1_fire_high > self.z:
            self.Gk_smoke_flow = 0.071 * pow(0.7 * self.Qf, 0.33) * pow(self.H - self.h, 1.666) * 0.0018(0.7 * self.Qf)
        else: 
            self.Gk_smoke_flow = 0.032 * pow(0.7 * self.Qf, 0.6) * (self.H - self.h)
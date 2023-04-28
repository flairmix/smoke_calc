

class Starcase_3():
    id = [0]
    items = []

    def __init__(self, name, 
                lvl_amount, lvl_height:list,
                starcase_area,
                lvl_doors_height:list, lvl_doors_widts:list, 
                Gsm,
                wind = 2, 
                Tr = 18,
                Ta = -26,
                starcase_local_resistance = 60, 
                vestibule_local_resistance = 0, 
                door_local_resistance = 2.44, 
                n = 1, z = 1, q = 1
                ):
                    
        self.add_id()
        Starcase_3.items.append(self)
        self.id = self.id[-1]
        self.name: str = name
        self.lvl_amount: lvl_amount
        self.starcase_area = starcase_area
        self.lvl_height = lvl_height
        self.lvl_doors_height = lvl_doors_height
        self.lvl_doors_widts = lvl_doors_widts     
        self.lvl_doors_area = [x * y for x, y in zip(self.lvl_doors_height, self.lvl_doors_widts)]
        self.starcase_local_resistance = starcase_local_resistance
        self.vestibule_local_resistance = vestibule_local_resistance
        self.door_local_resistance = door_local_resistance
                   
        self.wind = wind
        self.Tr, self.Ta,  = Tr, Ta
        self.Ts = int(0.5 * (self.Ta + self.Tr))
        self.Dns_r = round(353 / (self.Tr+273), 2)
        self.Dns_a = round(353 / (self.Ta+273), 2)
        self.Dns_s = round(353 / (self.Ts+273), 2)
        self.Gsm = Gsm
        self.n = n
        self.z = z
        self.q = q
        self.Ps2 = 0
        self.Gsa = 0
        self.G = 0

        self.Psi = [0]
        self.dPsi = [0]
        self.Gsi = [0]
        self.dGsi = [0]
                    

        self.pressure_lvl2 = 0

    
    def __str__(self):
        return f"id-{self.id}, name - {self.name}"

    def get_starcases(self):
        return [str(starcase) for starcase in Starcase_3.items]

    def add_id(self):
        self.id.append(self.id[-1] + 1)             


    def calc_pressure_lvl2 (self): 
        self.Ps2 =round( 20 - (9.81 * (self.lvl_height[0] + 0.5*self.lvl_doors_height[1]) * (self.Dns_s - self.Dns_r)), 2)
        self.Psi.append(self.Ps2)
        
    
    def calc_Gsa(self):
        self.Gsa = round(
                    pow(
                        (2*self.Dns_s / 
                        ((self.n*self.door_local_resistance+self.vestibule_local_resistance+1) / self.lvl_doors_area[0]**2) +
                        (60*self.z)/self.starcase_area**2) * 
                        (0.25 * (1.4) * self.Dns_a * pow(self.wind, 2)) + 
                        self.Ps2 + 
                        0.5 * 9.81 * 0.5*self.lvl_doors_height[0] * (self.Dns_a - self.Dns_s)
                    ,0.5)
                ,2)

    
    def calc_max_G(self):
        self.G = max(self.Gsa, self.Gsm)
        self.Gsi.append(self.G)

    
    def calc_dGsi(self, lvl):
        return round(self.lvl_doors_area[lvl] * pow(
                                        (self.Psi[lvl] + 9.81*(self.lvl_height[lvl-1]+0.5 * self.lvl_doors_height[lvl])*(self.Dns_s-self.Dns_r)) /
                                        (5300 / self.Dns_s)        
                                        , 0.5)
                     , 2)
        

    def lvl_losses(self):
      
        for lvl in range (1, len(self.lvl_height)): 
            
            self.dGsi.append(self.calc_dGsi(lvl))            
            self.Gsi.append(round(self.Gsi[lvl] + self.dGsi[lvl], 2))
            self.Psi.append(round(self.Psi[lvl] + (0.5*self.starcase_local_resistance * self.Dns_s) * (self.Gsi[lvl]/self.Dns_s/self.starcase_area)**2, 2))

        self.dGsi.append(self.calc_dGsi(len(self.lvl_height))) 
        
        print(f"dGsi - {self.dGsi}")
        print(f"Gsi - {self.Gsi}")
        print(f"Psi - {self.Psi}")


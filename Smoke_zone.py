# WIP


import pandas as pd 


def smoke_exhaust_zone(zone:Zone):             

    zone = Zone(name="zone", area_m2=2000, high_m=3.9, Qr=14000, vQr=0.021)
    
    zone.get_z()
    zone.get_F0()
    zone.calc_Qf()
    zone.calc_h()
    zone.calc_Gk_smoke_flow()
    








    
    name_parameter = []  
    parameter  []   
    units = []
    
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
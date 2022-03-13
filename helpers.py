
def celcius_to_kelvin(temp):
    temp_kelvin = temp + 273.15
    return temp_kelvin

def kelvin_to_celcius(temp):
    temp_celcius = temp - 273.15
    return temp_celcius

def flow_min_to_hour(flow):
    #the flow is given in cubic meter
    cubic_meter_hour = flow*60
    return cubic_meter_hour

def flow_min_to_litersecond(flow):
    liter_per_second = flow*1000/60
    return liter_per_second

def bar_to_pascal(pressure):
    pressure_pascal = pressure * 100000
    return pressure_pascal
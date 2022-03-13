from helpers import celcius_to_kelvin, bar_to_pascal
# air
gas_name = "Air"
gas_isentropic_coeff = 1.41

gas_molar_mass = 28.9647                        # [g/mol]
r_gas_constant = 8.31447                        # [J/mol K]
gas_temperature_cel = 0                         # [C] Celsius
gas_temperature_ke = celcius_to_kelvin(gas_temperature_cel)

# ISO 1217
reference_temperature = 20                      # [C]
reference_pressure_pa = 101325                  # [Pa]

suction_pressure = 0                            # [bar g]
suction_temperature_cel = 20                    # [C]

def density_air():
    density = (reference_pressure_pa*gas_molar_mass)/(r_gas_constant *
                                                  (gas_temperature_ke + reference_temperature))/1000                   # [kg/m3]

    return density

def power_calc(target_discharge_presure_bar):
    target_discharge_presure_pa = bar_to_pascal(target_discharge_presure_bar)
    suction_temperature_ke = celcius_to_kelvin(suction_temperature_cel)
    discharge_temperature_ke = (suction_temperature_ke)*((reference_pressure_pa+target_discharge_presure_pa)/reference_pressure_pa)**((gas_isentropic_coeff-1)/gas_isentropic_coeff)
    return discharge_temperature_ke

def isentropic_power_calc(discharge_temperature_cel, air_mass_flow_rate_hour):
    isentropic_power = 2.31*gas_isentropic_coeff/(gas_isentropic_coeff-1)*(discharge_temperature_cel-suction_temperature_cel)/gas_molar_mass*air_mass_flow_rate_hour/1000
    return isentropic_power


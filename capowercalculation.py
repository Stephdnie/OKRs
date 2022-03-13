""" CA power Calculation 
BKU_Vers8 - AS_Tarkett """
from helpers import *
from airfunctions import *
from kpicalculations import *

# when the gas is Air, based on the type of gas the following values change
gas_name = "Air"

# compressor mass flow capacity, this is based on the gas flow rate entered by the technician
gas_flow_rate_min = float(input(
    'Enter the Gas Flow Rate in minutes as given in the Manufacturer Technical Specifications [m3/min]: '))
# compression required, this is set by the expert
target_discharge_presure_bar = float(input(
    'Enter the Target Discharge Pressure given in the Technical Data "EffectiveWorkingPressure" [barg]: '))
input_actual_power_required = float(input(
    'Enter the Actual Power Required given in the Technical Data "TotalElectricalPowerInput" [k/W]: '))
# for using this, one should enter the actual_power_required instead of eff_compressor
operational_hours = float(input(
    'Enter the number of operational hours per year: '))    # [h/year]

###############################
gas_flow_rate_hour = flow_min_to_hour(gas_flow_rate_min)        # [m3/hour]
gas_flow_rate_sec = flow_min_to_litersecond(gas_flow_rate_min)  # [l/sec]
density = density_air()   # [kg/m3]
air_mass_flow_rate_min = density * gas_flow_rate_min
air_mass_flow_rate_hour = density * gas_flow_rate_hour      # [kg/min]

# Power calculation
discharge_temperature_ke = power_calc(target_discharge_presure_bar)
discharge_temperature_cel = kelvin_to_celcius(discharge_temperature_ke)
isentropic_power = isentropic_power_calc(
    discharge_temperature_cel, air_mass_flow_rate_hour)
desired_eff_compressor = isentropic_power/input_actual_power_required
calculated_energy_consumption = energy_consumption(operational_hours, input_actual_power_required)
[kpi_one_actual,kpi_two_actual, kpi_two_isentropic, kpi_two_actual] = kpi_one_two(isentropic_power, input_actual_power_required, gas_flow_rate_min, operational_hours, calculated_energy_consumption)

print("Actual calcultated energy consumption is ",
      round(calculated_energy_consumption, 2))
print("KPI 1 (actual) is     ", round(kpi_one_actual, 2))
print("KPI 2 (actual) is     ", round(kpi_two_actual, 2))
print("The efficiency of the compressor given the input information is ",
        round(desired_eff_compressor, 2))
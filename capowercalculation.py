""" CA power Calculation 
BKU_Vers8 - AS_Tarkett """

# when the gas is Air, based on the type of gas the following values change
gas_name = "Air"                      
gas_molar_mass = 28.9647
r_gas_constant = 8.31447                        # [J/mol K]
gas_temperature_cel = 0                         # [C] Celsius
gas_temperature_ke = 273.15
gas_isentropic_coeff = 1.41

# ISO 1217
reference_temperature = 20                      # [C]   
reference_pressure_pa = 101325                  # [Pa]

# compressor mass flow capacity, this is based on the gas flow rate entered by the technician
gas_flow_rate_min = float(input('Enter the Gas Flow Rate in minutes as given in the Manufacturer Technical Specifications [m3/min]: '))
gas_flow_rate_hour = gas_flow_rate_min*60       # [m3/hour]
gas_flow_rate_sec = gas_flow_rate_min*1000/60   # [l/sec]

###############################
density = (reference_pressure_pa*gas_molar_mass)/(r_gas_constant*(gas_temperature_ke+reference_temperature))/1000 # [kg/m3]
air_mass_flow_rate_min = density*gas_flow_rate_min 
air_mass_flow_rate_hour = density*gas_flow_rate_hour                                                             # [kg/min]

# compression required, this is set by the expert
target_discharge_presure_bar = float(input('Enter the Target Discharge Pressure given in the Technical Data "EffectiveWorkingPressure" [barg]: '))
target_discharge_presure_pa = target_discharge_presure_bar * 100000
suction_pressure = 0                            # [bar g]
suction_temperature_cel = 20                    # [C]
suction_temperature_ke = suction_temperature_cel + gas_temperature_ke


# Power calculation
discharge_temperature_ke = (suction_temperature_ke)*((reference_pressure_pa+target_discharge_presure_pa)/reference_pressure_pa)**((gas_isentropic_coeff-1)/gas_isentropic_coeff)
discharge_temperature_cel = discharge_temperature_ke - gas_temperature_ke

isentropic_power = 2.31*gas_isentropic_coeff/(gas_isentropic_coeff-1)*(discharge_temperature_cel-suction_temperature_cel)/gas_molar_mass*air_mass_flow_rate_hour/1000
input_actual_power_required = float(input('Enter the Actual Power Required given in the Technical Data "TotalElectricalPowerInput" [k/W]: '))
desired_eff_compressor = isentropic_power/input_actual_power_required # for using this, one should enter the actual_power_required instead of eff_compressor

operational_hours = 8760                        # [h/year]
calculated_energy_consumption = input_actual_power_required * operational_hours
print("Actual calcultated energy consumption is ", round(calculated_energy_consumption,2))

#KPI
kpi_one_isentropic = isentropic_power/gas_flow_rate_min
kpi_two_isentropic = (isentropic_power*operational_hours)/(gas_flow_rate_hour*operational_hours)
#print("KPI 1 (isentropic) is ", kpi_one_isentropic)
#print("KPI 2 (isentropic) is ", kpi_two_isentropic)

kpi_one_actual = input_actual_power_required/gas_flow_rate_min
kpi_two_actual= calculated_energy_consumption/(gas_flow_rate_hour*operational_hours)
print("KPI 1 (actual) is     ", round(kpi_one_actual,2))
print("KPI 2 (actual) is     ", round(kpi_two_actual,2))
print("The efficiency of the compressor given the input information is ", round(desired_eff_compressor,2))
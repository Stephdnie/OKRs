from helpers import flow_min_to_hour

def energy_consumption(operational_hours, input_actual_power_required):
    calculated_energy_consumption = input_actual_power_required * operational_hours
    print("Actual calcultated energy consumption is ",
        round(calculated_energy_consumption, 2))
    return calculated_energy_consumption

def kpi_one_two(isentropic_power, input_actual_power_required, gas_flow_rate_min, operational_hours, calculated_energy_consumption):
    gas_flow_rate_hour = flow_min_to_hour(gas_flow_rate_min)
    # KPI
    kpi_one_isentropic = isentropic_power/gas_flow_rate_min
    kpi_two_isentropic = (isentropic_power*operational_hours) / \
        (gas_flow_rate_hour*operational_hours)
    #print("KPI 1 (isentropic) is ", kpi_one_isentropic)
    #print("KPI 2 (isentropic) is ", kpi_two_isentropic)

    kpi_one_actual = input_actual_power_required/gas_flow_rate_min
    kpi_two_actual = calculated_energy_consumption / \
        (gas_flow_rate_hour*operational_hours)

    return kpi_one_isentropic, kpi_one_actual, kpi_two_isentropic, kpi_two_actual


# Import from openfisca-core the common Python objects used to code the legislation in OpenFisca
from openfisca_core.model_api import *
# Import the Entities specifically defined for this tax and benefit system
from openfisca_nsw_base.entities import *


class F1_1_electricity_savings(Variable):
    value_type = float
    entity = Building
    definition_period = ETERNITY
    label = 'What is the electricity savings for the activity conducted within' \
            ' Activity Definition F1.1?'

    def formula(buildings, period, parameters):
        product_class = buildings('F1_product_class', period)
        baseline_EEI = parameters(period).HEAB.F1.F1_1_baseline_EEIs.EEI[product_class]
        total_electricity_consumption = buildings('F1_1_daily_total_electricity_consumption', period)
        total_display_area = buildings('F1_1_total_display_area', period)
        m_coefficient = parameters(period).HEAB.F1.F1_1_coefficients.M[product_class]
        n_coefficient = parameters(period).HEAB.F1.F1_1_coefficients.N[product_class]
        days_in_year = parameters(period).general_ESS.days_in_year
        less_than_three_point_three_TDA = where(total_display_area < 3.3,
        "tda_less_than_three_point_three", "tda_more_than_three_point_three")
        lifetime = parameters(period).HEAB.F1.F1_1_lifetime[product_class][less_than_three_point_three_TDA]
        MWh_conversion = parameters(period).general_ESS.unit_conversion_factors['kWh_to_MWh']
        return ((baseline_EEI * ((m_coefficient + (n_coefficient
        * total_display_area)) / 100) - total_electricity_consumption)
        * days_in_year * lifetime / MWh_conversion)


class F1_1_daily_total_electricity_consumption(Variable):
    value_type = float
    entity = Building
    definition_period = ETERNITY
    label = 'What is the daily total energy consumption for the new RDC, as' \
            ' determined using GEMS 2019 s12 and recorded in the GEMS Registry?'


class F1_1_total_display_area(Variable):
    value_type = float
    entity = Building
    definition_period = ETERNITY
    label = 'What is the total display area for the new RDC, as determined' \
            ' using GEMS 2019 s12 and recorded in the GEMS Registry?'

# Import from openfisca-core the common Python objects used to code the legislation in OpenFisca
from openfisca_core.model_api import *
# Import the Entities specifically defined for this tax and benefit system
from openfisca_nsw_base.entities import *
import time
import numpy as np
import datetime
from datetime import datetime as py_datetime


epoch = time.gmtime(0).tm_year
today_date_and_time = np.datetime64(datetime.datetime.now())
today = today_date_and_time.astype('datetime64[D]')

# note because this activity definition requires calculation based off years, \
# you need to import the above libraries to make it work

class F8_gas_savings(Variable):
    value_type = float
    entity = Building
    definition_period = ETERNITY
    label = 'What is the electricity savings for the activity conducted within' \
            ' Activity Definition F8?'

    def formula(buildings, period, parameters):
        replacement_capacity = buildings('F8_replacement_equipment_nameplate_capacity', period)
        existing_capacity = buildings('F8_existing_equipment_nameplate_capacity', period)
        nameplate_capacity = where(replacement_capacity > existing_capacity,
                                   existing_capacity,
                                   replacement_capacity)
        F8_existing_equipment_installation_date = buildings('F8_existing_equipment_installation_date', period)
        installation_year = (F8_existing_equipment_installation_date.astype('datetime64[Y]') + epoch).astype('int')
        installed_before_1990 = where((installation_year < 1990),
                                      'boiler_installed_pre_1990',
                                      'boiler_installed_1990_or_later')
        burner_replacement_date = buildings('F8_existing_equipment_burner_replacement_date', period)
        burner_replacement_age_in_days = (today.astype('datetime64[D]') - burner_replacement_date.astype('datetime64[D]'))
        burner_replacement_age = (burner_replacement_age_in_days.astype('datetime64[Y]')).astype('int')
        burner_less_than_10_years_old = where(burner_replacement_age > 10,
                                              'burner_more_than_10_years_old',
                                              'burner_10_or_fewer_years_old')
        default_efficiency_improvement = parameters(period).HEAB.F8.table_F8_1.default_efficiency_improvement[installed_before_1990][burner_less_than_10_years_old]
        load_utilisation_factor = parameters(period).HEAB.F8.table_F8_2.load_utilisation_factor
        lifetime = parameters(period).HEAB.F8.table_F8_3.lifetime
        hours_in_year = parameters(period).general_ESS.hours_in_year
        MWh_conversion = parameters(period).general_ESS.unit_conversion_factors['kWh_to_MWh']
        return (nameplate_capacity * default_efficiency_improvement * load_utilisation_factor
                * lifetime * hours_in_year / MWh_conversion)
        # need to make the burner replacement age calc more efficient


class F8_existing_equipment_installation_date(Variable):
    value_type = date
    entity = Building
    definition_period = ETERNITY
    label = 'What is the installation date for the existing equipment?'


class F8_existing_equipment_burner_replacement_date(Variable):
    value_type = date
    entity = Building
    definition_period = ETERNITY
    label = 'What is the replacement date for the burner in the existing equipment?'


class F8_existing_equipment_nameplate_capacity(Variable):
    value_type = float
    entity = Building
    definition_period = ETERNITY
    label = 'What is the nameplate capacity for the existing equipment, in kW?'


class F8_replacement_equipment_nameplate_capacity(Variable):
    value_type = float
    entity = Building
    definition_period = ETERNITY
    label = 'What is the nameplate capacity for the new equipment, in kW?'


class F8_replacement_equipment_has_linkageless_burner_minimum_4_1(Variable):
    value_type = bool
    entity = Building
    definition_period = ETERNITY
    label = 'Does the new equipment have a linkageless burner with a ratio of' \
            ' of at least 4:1?'


class F8_replacement_equipment_has_oxygen_trim_system(Variable):
    value_type = bool
    entity = Building
    definition_period = ETERNITY
    label = 'Does the new equipment have an oxygen trim system?'


class fuel_to_fluid_efficiency_at_high_fire_conditions(Variable):
    value_type = float
    entity = Building
    definition_period = ETERNITY
    label = 'What is the fuel to fluid efficiency of the the replacement end '\
            ' user equipment, at high fire conditions, as a percentage?'
    # there's probably a formula for this we could code in?
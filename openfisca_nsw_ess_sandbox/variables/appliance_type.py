import numpy as np

# Import from openfisca-core the common Python objects used to code the legislation in OpenFisca
from openfisca_core.model_api import *
from openfisca_nsw_base.entities import *

class ApplianceType(Enum):
    washing_machine = u'Washing machine'
    clothes_dryer = u'Clothes dryer'
    combination_washer_dryer = u'Combo washer/dryer'
    dishwasher = u'Dish washer'
    one_door_refrigerator = u'One door fridge'
    two_door_refrigerator = u'Two door fridge'
    chest_freezer = u'Chest freezer'
    upright_freezer = u'Upright freezer'
    none = u'None'

class appliance_type(Variable):
    value_type = Enum
    possible_values = ApplianceType
    default_value = ApplianceType.none
    entity = Building
    definition_period = ETERNITY
    label = "Label ABC"
    reference = "XXX FIXME"



class StarRating(Enum):
    zero_star = u'zero star'
    four_star = u'four star'
    four_pt_five_star = u'four pt five star'
    five_star = u'five star'

class star_rating(Variable):
    value_type = Enum
    possible_values = StarRating
    default_value = StarRating.zero_star
    entity = Building
    definition_period = ETERNITY
    label = "Label ABC"
    reference = "XXX FIXME"


class washer_load(Variable):
    value_type = float
    default_value = 0
    entity = Building
    definition_period = ETERNITY
    label = "Washer load in kg"
    reference = "XXX FIXME"
    unit = "kilograms (kg)"


class WasherType(Enum):
    top_loader = u'top loader'
    front_loader = u'front loader'

class washer_type(Variable):
    value_type = Enum
    possible_values = WasherType
    default_value = WasherType.top_loader
    entity = Building
    definition_period = ETERNITY
    label = "Label ABC"
    reference = "XXX FIXME"

class is_combination_washer_dryer(Variable):
    value_type = bool
    default_value = False
    entity = Building
    definition_period = ETERNITY
    label = "Label ABC"
    reference = "XXX FIXME"

class is_washer_eligible(Variable):
    value_type = bool
    default_value = False
    entity = Building
    definition_period = ETERNITY
    label = "Label ABC"
    reference = "XXX FIXME"

    def formula(building, period, parameters):
      star_rating = building('star_rating', period).decode_to_str()[0] # enum
      washer_load = building('washer_load', period) # float
      washer_type = building('washer_type', period).decode_to_str()[0] # enum

      return ( star_rating is not "zero_star") and (washer_load > 0) and (washer_type in ['top_loader','front_loader'])


class washer_energy_saving(Variable):
    value_type = float
    default_value = 0
    entity = Building
    definition_period = ETERNITY
    label = "Label ABC"
    reference = "XXX FIXME"

    def formula(building, period, parameters):
      star_rating = building('star_rating', period).decode_to_str()[0] # enum
      washer_load = building('washer_load', period) # float

      deemed_energy_saving = parameters(period).table_b1[star_rating].calc(washer_load, right=True) # placeholder

      return deemed_energy_saving


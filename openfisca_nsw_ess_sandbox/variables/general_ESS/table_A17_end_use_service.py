# Import from openfisca-core the common Python objects used to code the legislation in OpenFisca
from openfisca_core.model_api import *
# Import the Entities specifically defined for this tax and benefit system
# from openfisca_nsw_base.entities import *


# class EndUseService(Enum):
#     air_heating_and_cooling = 'The end use service is for air heating and cooling.'
#     air_handling = 'The end use service is for air handling, fans and ventilation.'
#     water_heating = 'The end use service is for water heating.'
#     water_or_liquid_pumping = 'The end use service is for water or liquid pumping.'
#     refrigeration_and_freezing = 'The end use service is for refrigeration and freezing.'
#     lighting = 'The end use service is for lighting.'
#     cooking = 'The end use service is for cooking.'
#     home_entertainment = 'The end use service is for entertainment.'
#     computers_and_office_equipment = 'The end use service is for computers and office equipment.'
#     communications = 'The end use service is for communications.'
#     cleaning_or_washing = 'The end use service is for cleaning or washing.'
#     process_heat = 'The end use service is for process heat.'
#     air_compression = 'The end use service is for air compression.'
#     process_drives = 'The end use service is for process drives.'
#     milling_mixing_or_grinding = 'The end use service is for milling, mixing or grinding.'
#     transport = 'The end use service is for transport.'
#     people_movement_lifts_or_escalators = 'The end use service is for people movement' \
#                                           ' such as lifts or escalators.'
#     material_handling = 'The end use service is for material handling or conveying.'
#     other_machines = 'The end use service is for other machines.'
#     electricity_supply = 'The end use service is for electricity supply.'
#     unknown = 'The end use service is unknown.'
#     other_end_use_service = 'The end use service is known, but is not listed above.'


# class end_use_service(Variable):
#     value_type = Enum
#     entity = Building
#     possible_values = EndUseService
#     default_value = EndUseService.unknown
#     definition_period = ETERNITY
#     label = 'What is the End Use Service - the primary service as provided by the' \
#             ' End Use Equipment?'

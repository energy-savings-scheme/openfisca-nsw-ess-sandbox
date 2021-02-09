# Import from openfisca-core the common Python objects used to code the legislation in OpenFisca
from openfisca_core.model_api import *
# Import the Entities specifically defined for this tax and benefit system
# from openfisca_nsw_base.entities import *


# class BusinessClassification(Enum):
#     Division_A = 'Business classification is Agriculture, Forestry and Fishing.'
#     Division_B = 'Business classification is Mining.'
#     Division_C = 'Business classification is Manufacturing.'
#     Division_D = 'Business classification is Electricity, Gas, Water and Waste' \
#                  ' Services.'
#     Division_E = 'Business classification is Construction.'
#     Division_F = 'Business classification is Wholesale Trade.'
#     Division_G = 'Business classification is Retail Trade.'
#     Division_H = 'Business classification is Accomodation and Food Services.'
#     Division_I = 'Business classification is Transport, Postal and Warehousing.'
#     Division_J = 'Business classification is Information Media and Telecommunications.'
#     Division_K = 'Business classification is Financial and Insurance Services.'
#     Division_L = 'Business classification is Rental, Hiring and Real Estate Services.'
#     Division_M = 'Business classification is Professional, Scientific and Technical' \
#                  ' Services.'
#     Division_N = 'Business classification is Administrative and Support Services.'
#     Division_O = 'Business classification is Public Administration and Safety.'
#     Division_P = 'Business classification is Education and Training.'
#     Division_Q = 'Business classification is Health Care and Social Assistance.'
#     Division_R = 'Business classification is Arts and Recreation Services.'
#     Division_S = 'Business classification is Other Services.'
#     Residential = 'Business classification is Residential.'
#     Unknown = 'Business classification is unknown.'


# class business_classification(Variable):
#     value_type = Enum
#     entity = Building
#     possible_values = BusinessClassification
#     default_value = BusinessClassification.Division_A
#     definition_period = ETERNITY
#     label = 'What is the building class for the implementation?'

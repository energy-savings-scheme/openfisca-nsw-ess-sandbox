# Import from openfisca-core the common Python objects used to code the legislation in OpenFisca
from openfisca_core.model_api import *
# Import the Entities specifically defined for this tax and benefit system
# from openfisca_nsw_base.entities import *


# class BCABuildingClass(Enum):
#     BCA_Class_1a = 'A single dwelling, i.e. a detached house.'
#     BCA_Class_1b = 'A boarding house, guest house, hostel or the like.'
#     BCA_Class_2 = 'A building containing two or more sole-occupancy units, with' \
#                   ' each being a separate dwelling.'
#     BCA_Class_3 = 'A residential building, which is a common place for long term' \
#                   ' or transient living for a number of unrelated persons. '
#     BCA_Class_4 = 'A dwelling in a Class 5, 6, 7, 8 or 9 building, which is the' \
#                   ' only dwelling in the building.'
#     BCA_Class_5 = 'An office building used for professional or commercial' \
#                   ' purposes, excluding buildings in Class 6, 7, 8 or 9.'
#     BCA_Class_6_shop = 'A shop, shopping centre or other building used for the' \
#                        ' sale of good by retail,' \
#                        ' or supply of services direct to the public.'
#     BCA_Class_6_cafe_or_rest = 'A cafe or restaurant.'
#     BCA_Class_7a = 'A building which is a car park.'
#     BCA_Class_7b = 'A building which is for storage or display of goods or' \
#                    ' produce for sale by wholesale.'
#     BCA_Class_8 = 'A laboratory, or building in which a handicraft or the process' \
#                   ' for for the production of godd or produce is carried on for' \
#                   ' trade, sale or gain.'
#     BCA_Class_9a_clinic = 'A clinic, including those parts of the' \
#                           ' building set aside as a laboratory.'
#     BCA_Class_9a_hospital = 'A clinic, including those parts of the' \
#                             ' building set aside as a laboratory.'
#     BCA_Class_9b_schools = 'A school.'
#     BCA_Class_9b_theatres = 'An assembly building, including a trade workshop, laboratory' \
#                             ' or the like, in a primary or secondary school - but excluding' \
#                             ' other parts of the building that are of another class.'
#     BCA_Class_10a = 'A private garage, carport, shed or the like.'
#     BCA_Class_10b = 'A structure being a fence, mast, antenna, retaining or' \
#                     ' free standing wall, swimming pool or the like.'
#     BCA_Class_10c = 'A private bushfire shelter.'


# class BCA_building_class(Variable):
#     value_type = Enum
#     entity = Building
#     possible_values = BCABuildingClass
#     default_value = BCABuildingClass.BCA_Class_1a
#     definition_period = ETERNITY
#     label = 'What is the building class for the implementation?'

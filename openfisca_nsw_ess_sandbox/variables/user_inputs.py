# Import from openfisca-core the common Python objects used to code the legislation in OpenFisca
from openfisca_core.model_api import *
# Import the Entities specifically defined for this tax and benefit system
from openfisca_nsw_base.entities import *


# class F1ProductClass(Enum):
#     product_class_one = 'RDC is in product class 1.'
#     product_class_two = 'RDC is in product class 2.'
#     product_class_three = 'RDC is in product class 3.'
#     product_class_four = 'RDC is in product class 4.'
#     product_class_five = 'RDC is in product class 5.'
#     product_class_six = 'RDC is in product class 6.'
#     product_class_seven = 'RDC is in product class 7.'
#     product_class_eight = 'RDC is in product class 8.'
#     product_class_nine = 'RDC is in product class 9.'
#     product_class_ten = 'RDC is in product class 10.'
#     product_class_eleven = 'RDC is in product class 11.'
#     product_class_twelve = 'RDC is in product class 12.'
#     product_class_thirteen = 'RDC is in product class 13.'
#     product_class_fourteen = 'RDC is in product class 14.'
#     product_class_fifteen = 'RDC is in product class 15.'


# class F1_product_class(Variable):
#     value_type = Enum
#     entity = Building
#     possible_values = F1ProductClass
#     default_value = F1ProductClass.product_class_one
#     definition_period = ETERNITY
#     label = 'What is the product class for the RDC installed in Activity' \
#             ' Definition F1?'


# class DutyClass(Enum):
#     light_duty = 'cabinet is a light duty cabinet.'
#     normal_duty = 'cabinet is a normal duty cabinet.'
#     heavy_duty = 'cabinet is a heavy duty cabinet.'


# class duty_class(Variable):
#     value_type = Enum
#     entity = Building
#     possible_values = DutyClass
#     default_value = DutyClass.light_duty
#     definition_period = ETERNITY
#     label = 'What is the duty class of the Refrigerated Cabinet, as tested in' \
#             ' accordance with EN 16825?'

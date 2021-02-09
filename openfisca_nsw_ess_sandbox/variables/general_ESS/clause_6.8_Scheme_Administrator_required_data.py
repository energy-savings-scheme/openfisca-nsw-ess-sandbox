# Import from openfisca-core the common Python objects used to code the legislation in OpenFisca
from openfisca_core.model_api import *
# Import the Entities specifically defined for this tax and benefit system
# from openfisca_nsw_base.entities import *


# class ACP_identifier(Variable):
#     value_type = float
#     entity = Building
#     definition_period = ETERNITY
#     label = 'The Accredited Certificate provider identifier, as required and' \
#             ' and defined by the Scheme Administrator. As prescribed by' \
#             ' clause 6.8 (a)'


# class RESA_identifier(Variable):
#     value_type = float
#     entity = Building
#     definition_period = ETERNITY
#     label = 'The Recognised Energy Saving Activity identifier, as prescribed' \
#             ' by clause 6.8 (b).'


# class implementation_site_address(Variable):
#     value_type = str
#     entity = Building
#     definition_period = ETERNITY
#     label = 'The address of the site or sites where the Implementation took' \
#             ' place. As prescribed by clause 6.8 (c).'


# class implementation_date(Variable):
#     value_type = date
#     entity = Building
#     definition_period = ETERNITY
#     label = 'The Implementation Date of the Implementation, as prescribed by' \
#             ' clause 6.8 (e).'  # need to build in logic for specific methods i.e. HEAB implementation date = installation date


# class australian_business_number(Variable):
#     value_type = int
#     entity = Building
#     definition_period = ETERNITY
#     label = 'the Australian Business Number of the entity utilising the' \
#             ' End-Use-Service, or for the purpose of clause 9.3, the Appliance' \
#             ' Retailer. As prescribed in 6.8 (g).'


# class goods_or_services_cost(Variable):
#     value_type = float
#     entity = Building
#     definition_period = ETERNITY
#     label = 'The cost to the person who pays for the goods or services that' \
#             ' that comprise the Implementation, excluding GST. As prescribed' \
#             ' by Clause 6.8 (h).'


# class end_use_service_type(Variable):
#     value_type = str
#     entity = Building
#     definition_period = ETERNITY
#     label = 'The type of End-Use Service for which energy was saved, in' \
#             ' accordance with Table A17 of Schedule A. As prescribed by' \
#             ' Clause 6.8 (i).'


# class end_use_service_business_classification(Variable):
#     value_type = str
#     entity = Building
#     definition_period = ETERNITY
#     label = 'the Business Classification of the entity utilising the End-Use' \
#             ' Service in accordance with Table A18 of Schedule A. As' \
#             ' prescribed by Clause 6.8 (j).'


# class energy_savings_method_used(Variable):
#     value_type = str
#     entity = Building
#     definition_period = ETERNITY
#     label = 'the Method used to calculate the Energy Savings. As prescribed by' \
#             ' Clause 6.8 (k).'


# class energy_savings_sub_method_used(Variable):
#     value_type = str
#     entity = Building
#     definition_period = ETERNITY
#     label = 'the Sub-Method used to calculate the Energy Savings, where' \
#             ' relevant. As prescribed by Clause 6.8 (k).'


# class energy_savings_activity_definition_used(Variable):
#     value_type = str
#     entity = Building
#     definition_period = ETERNITY
#     label = 'the Activity Definition used to calculate the Energy Savings, where' \
#             ' relevant. As prescribed by Clause 6.8 (k).'

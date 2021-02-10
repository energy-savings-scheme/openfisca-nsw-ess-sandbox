import numpy as np

# Import from openfisca-core the common Python objects used to code the legislation in OpenFisca
from openfisca_core.model_api import *

# Import the Entities specifically defined for this tax and benefit system
from openfisca_nsw_ess_sandbox.entities import *
# from openfisca_nsw_base.entities import *

class electricity_savings(Variable):
    value_type = float
    # entity = Building
    entity = Appliance
    default_value = 0
    definition_period = YEAR
    label = 'What is the electricity savings per year?'


class gas_savings(Variable):
    value_type = float
    # entity = Building
    entity = Appliance
    default_value = 0
    definition_period = YEAR
    label = 'What is the gas savings per year?'


class number_of_certificates(Variable):
    value_type = float
    # entity = Building
    entity = Appliance
    definition_period = ETERNITY
    label = 'Equation 1 of the ESS Rule 2009, used to calculate the number' \
            ' of ESCs generated from a Recognised Energy Savings Activity.' \
            ' As defined in Clause 6.5 of the ESS Rule 2009.'

    def formula(self, period, parameters):
        elec_savings = self('electricity_savings', period)
        electricity_cert_conversion_factor = parameters(period).general_ESS.electricity_certificate_conversion_factor

        gas_savings = self('gas_savings', period)
        gas_cert_conversion_factor = parameters(period).general_ESS.gas_certificate_conversion_factor

        return np.floor((elec_savings * electricity_cert_conversion_factor) + (gas_savings * gas_cert_conversion_factor))
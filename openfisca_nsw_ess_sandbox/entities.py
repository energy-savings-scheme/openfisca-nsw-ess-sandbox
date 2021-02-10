# -*- coding: utf-8 -*-

"""
 This file defines the entities needed by our legislation.
 """

from openfisca_core.entities import build_entity

Appliance = build_entity(
    key = "appliance",
    plural = "appliances",
    label = u'Appliance',
    doc = '''
    ''',
    roles = [
        {
            'key': 'representative',
            'plural': 'representatives',
            'label': u'Representative',
            'doc': u'A person authorised to represent the building'
            },
        {
            'key': 'other',
            'plural': 'others',
            'label': u'Other',
            'doc': u'Other representatives who are not a person - such as Strata bodies'
            }
        ]
    )

Person = build_entity(
    key = "person",
    plural = "persons",
    label = u'An individual. The minimal legal entity on which a legislation might be applied.',
    doc = '''
    Variables like 'salary' and 'income_tax' are usually defined for the entity 'Person'.
    Usage:
    Calculate a variable applied to a 'Person' (e.g. access the 'salary' of a specific month with
    person('salary', "2017-05")).
    Check the role of a 'Person' in a group entity (e.g. check if a the 'Person' is a 'first_parent'
    in a 'Family' entity with person.has_role(Family.PARENT)).
    For more information, see: https://openfisca.org/doc/coding-the-legislation/50_entities.html
    ''',
    is_person = True
    )

# NB - there must be at least one `entity` for which `entity.is_person` == True
#      or else Exception will be thrown...
# see: https://github.com/openfisca/openfisca-core/blob/de4e35a7a15e3ef5cbb547dc70828f6d420b0a07/openfisca_core/taxbenefitsystems.py#L68
entities = [Appliance, Person]

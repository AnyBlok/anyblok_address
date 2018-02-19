"""Address model
"""
from datetime import datetime
import uuid
from uuid import uuid1

from pycountry import countries

from anyblok import Declarations
from anyblok.column import String, DateTime, UUID, Selection

from logging import getLogger


logger = getLogger(__name__)
Model = Declarations.Model
Mixin = Declarations.Mixin


@Declarations.register(Mixin)
class UuidColumn:
    """ `UUID` id primary key mixin
    """
    uuid = UUID(primary_key=True, default=uuid1, binary=False)


@Declarations.register(Mixin)
class TrackModel:
    """ A mixin to store record creation and edition date
    """
    create_date = DateTime(default=datetime.now, nullable=False)
    edit_date = DateTime(default=datetime.now, nullable=False,
                         auto_update=True)


@Declarations.register(Declarations.Model)
class Address(Mixin.UuidColumn, Mixin.TrackModel):
    """ Postal address for delivery
    """
    countries = dict((country.alpha_3, country.name) for country in countries)

    first_name = String(label="First name", nullable=False)
    last_name = String(label="Last name", nullable=False)
    company_name = String(label="Company name")
    street1 = String(label="Street line 1", nullable=False)
    street2 = String(label="Street line 2")
    street3 = String(label="Street line 3")
    zip_code = String(label="Postal Code")
    state = String(label="State")
    city = String(label="City", nullable=False)
    country = Selection(label="Country", selections=countries, nullable=False)
    phone1 = String(label="Phone 1")
    phone2 = String(label="Phone 2")
    email = String(label="Email")

    def __str__(self):
        return ('{self.uuid}').format(self=self)

    def __repr__(self):
        msg = ('<Address: {self.uuid}, {self.first_name}, {self.last_name}, '
               '{self.company_name}, {self.zip_code}, {self.country}>')

        return msg.format(self=self)
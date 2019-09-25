# This file is a part of the AnyBlok / Address project
#
#    Copyright (C) 2018 Franck Bret <f.bret@sensee.com>
#    Copyright (C) 2018 Hugo Quezada <h.quezada@sensee.com>
#    Copyright (C) 2019 Jean-Sébastien Suzanne <js.suzanne@gmail.com>
#
# This Source Code Form is subject to the terms of the Mozilla Public License,
# v. 2.0. If a copy of the MPL was not distributed with this file,You can
# obtain one at http://mozilla.org/MPL/2.0/.
import pytest


@pytest.mark.usefixtures('rollback_registry')
class TestAddressModel:
    """ Test address model"""

    @pytest.fixture(autouse=True, scope='function')
    def define_registry(self, rollback_registry):
        self.registry = rollback_registry

    def create_sender_address(self):
        address = self.registry.Address.insert(
            first_name="Shipping",
            last_name="services",
            company_name="Acme",
            street1="1 company street",
            zip_code="00000",
            state="",
            city="There",
            country="FRA"
        )
        return address

    def create_recipient_address(self):
        address = self.registry.Address.insert(
            first_name="Jon",
            last_name="Doe",
            street1="1 street",
            street2="crossroad",
            street3="♥",
            zip_code="99999",
            state="A region",
            city="Nowhere",
            country="ESP"
        )
        return address

    def test_str(self):
        address = self.create_sender_address()
        str(address)

    def test_repr(self):
        address = self.create_sender_address()
        repr(address)

    def test_addresses(self):
        sender_address = self.create_sender_address()
        recipient_address = self.create_recipient_address()

        assert sender_address != recipient_address
        assert self.registry.Address.query().count() == 2

        assert (
            self.registry.Address.query().filter_by(country="FRA").count() == 1
        )

        assert (
            self.registry.Address.query().filter_by(country="ESP").count() == 1
        )

        assert (
            self.registry.Address.query().filter_by(country="USA").count() == 0
        )

from anyblok.tests.testcase import BlokTestCase


class TestAddressModel(BlokTestCase):
    """ Test address model"""

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

    def test_addresses(self):
        sender_address = self.create_sender_address()
        recipient_address = self.create_recipient_address()

        self.assertNotEqual(
            sender_address,
            recipient_address
        )
        self.assertEqual(
            self.registry.Address.query().count(),
            2
        )

        from pycountry import countries
        countries = dict((country.alpha_3, country.name) for country in countries)

        self.assertEqual(
            len(list(set(self.registry.Address.query().all().country).intersection(set(countries.keys())))),
            2
        )
        self.assertEqual(
            len(list(set(self.registry.Address.query().all().country).difference(set(countries.keys())))),
            0
        )

        self.assertEqual(
            self.registry.Address.query().filter_by(country="FRA").count(),
            1
        )

        self.assertEqual(
            self.registry.Address.query().filter_by(country="ESP").count(),
            1
        )

        self.assertEqual(
            self.registry.Address.query().filter_by(country="USA").count(),
            0
        )
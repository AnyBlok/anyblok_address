from anyblok.blok import Blok
from logging import getLogger
logger = getLogger(__name__)


class AddressBlok(Blok):
    """Address blok
    """
    version = "0.1.0"
    author = "Franck BRET"

    @classmethod
    def import_declaration_module(cls):
        from . import address # noqa

    @classmethod
    def reload_declaration_module(cls, reload):
        from . import address
        reload(address)

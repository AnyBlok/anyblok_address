from anyblok.blok import Blok
from logging import getLogger


logger = getLogger(__name__)


def includeme(config):
    """For now that's the only way I found to include those views in an
    external project using a route prefix
    """
    config.scan('anyblok_address.bloks.rest_api.views')


class AddressRestApiBlok(Blok):
    """Address blok
    """
    version = "0.1.0"
    author = "Franck BRET"
    required = ['anyblok-core', 'address']

    def load(self):
        import anyblok_pyramid_rest_api  # noqa

    @classmethod
    def pyramid_load_config(cls, config):
        """Pyramid http server configuration / initialization
        """
        try:
            import anyblok_pyramid_rest_api  # noqa
        except ImportError:
            logger.warning("You need to install 'anyblok_pyramid_rest api' to"
                           "use address_rest_api views")

        # Scan available views
        config.scan(cls.__module__ + '.views')

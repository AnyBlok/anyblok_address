from cornice.resource import resource

from anyblok_pyramid_rest_api.validator import model_schema_validator
from anyblok_pyramid_rest_api.crud_resource import CrudResource
from anyblok_pyramid import current_blok


MODEL = 'Model.Address'


@resource(
    collection_path='addresses',
    path='addresses/{uuid}',
    validators=(model_schema_validator,),
    installed_blok=current_blok()
)
class AddressResource(CrudResource):
    model = MODEL

# This file is a part of the AnyBlok / Address project
#
#    Copyright (C) 2018 Franck Bret <f.bret@sensee.com>
#    Copyright (C) 2018 Hugo Quezada <h.quezada@sensee.com>
#
# This Source Code Form is subject to the terms of the Mozilla Public License,
# v. 2.0. If a copy of the MPL was not distributed with this file,You can
# obtain one at http://mozilla.org/MPL/2.0/.
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

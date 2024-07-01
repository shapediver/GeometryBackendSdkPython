# coding: utf-8

"""
    Geometry Backend API v2

    The ShapeDiver Geometry Backend system is used to: * host Grasshopper models in a secure, reliable, scalable, and performant way, * run computations of Grasshopper models, * and cache and output the results of computations and exports.

    The version of the OpenAPI document: 2.13.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from shapediver.geometry_api_v2.client.models.res_output_chunk import ResOutputChunk
from shapediver.geometry_api_v2.client.models.res_output_definition_group import ResOutputDefinitionGroup
from typing import Optional, Set
from typing_extensions import Self

class ResOutputDefinition(BaseModel):
    """
    Output definition WITHOUT results as exposed on the API.
    """ # noqa: E501
    id: StrictStr = Field(description="ID of the output, dependent on model ID, and therefore changing each time a model gets uploaded.")
    uid: Optional[StrictStr] = Field(default=None, description="Constant ID of the output, not dependent on model ID, and therefore NOT changing each time a model gets uploaded. Might be undefined because this property was introduced in summer 2020 and does not exist for outputs of older models.")
    name: StrictStr = Field(description="Name of the output.")
    material: Optional[StrictStr] = Field(default=None, description="Optional ID of the output holding material information for this output.")
    chunks: Optional[List[ResOutputChunk]] = Field(default=None, description="Information about which chunks exist in the asset/sdTF.")
    dependency: List[StrictStr] = Field(description="List of IDs of parameters influencing this output.")
    group: Optional[ResOutputDefinitionGroup] = None
    order: Optional[StrictInt] = Field(default=None, description="Ordering of the output in client applications.")
    tooltip: Optional[StrictStr] = Field(default=None, description="Description that is shown as a tooltip in the clients.")
    displayname: Optional[StrictStr] = Field(default=None, description="Parameter name to display instead of `name`.")
    hidden: StrictBool = Field(description="Controls whether the parameter should be hidden in the UI.")
    version: Optional[StrictBool] = Field(default=None, description="This property is never set.")
    __properties: ClassVar[List[str]] = ["id", "uid", "name", "material", "chunks", "dependency", "group", "order", "tooltip", "displayname", "hidden", "version"]

    model_config = ConfigDict(
        populate_by_name=True,
        validate_assignment=True,
        protected_namespaces=(),
    )


    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        # TODO: pydantic v2: use .model_dump_json(by_alias=True, exclude_unset=True) instead
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Optional[Self]:
        """Create an instance of ResOutputDefinition from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        """
        excluded_fields: Set[str] = set([
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        # override the default output from pydantic by calling `to_dict()` of each item in chunks (list)
        _items = []
        if self.chunks:
            for _item in self.chunks:
                if _item:
                    _items.append(_item.to_dict())
            _dict['chunks'] = _items
        # override the default output from pydantic by calling `to_dict()` of group
        if self.group:
            _dict['group'] = self.group.to_dict()
        # set to None if version (nullable) is None
        # and model_fields_set contains the field
        if self.version is None and "version" in self.model_fields_set:
            _dict['version'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of ResOutputDefinition from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "id": obj.get("id"),
            "uid": obj.get("uid"),
            "name": obj.get("name"),
            "material": obj.get("material"),
            "chunks": [ResOutputChunk.from_dict(_item) for _item in obj["chunks"]] if obj.get("chunks") is not None else None,
            "dependency": obj.get("dependency"),
            "group": ResOutputDefinitionGroup.from_dict(obj["group"]) if obj.get("group") is not None else None,
            "order": obj.get("order"),
            "tooltip": obj.get("tooltip"),
            "displayname": obj.get("displayname"),
            "hidden": obj.get("hidden"),
            "version": obj.get("version")
        })
        return _obj


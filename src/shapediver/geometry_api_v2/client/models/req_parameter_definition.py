# coding: utf-8

"""
    Geometry Backend API v2

    The ShapeDiver Geometry Backend system is used to: * host Grasshopper models in a secure, reliable, scalable, and performant way, * run computations of Grasshopper models, * and cache and output the results of computations and exports.

    The version of the OpenAPI document: 1.8.2
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from shapediver.geometry_api_v2.client.models.req_parameter_definition_group import ReqParameterDefinitionGroup
from typing import Optional, Set
from typing_extensions import Self

class ReqParameterDefinition(BaseModel):
    """
    Data for a single parameter definition.
    """ # noqa: E501
    displayname: Optional[StrictStr] = Field(default=None, description="Parameter name to display instead of `name`.")
    group: Optional[ReqParameterDefinitionGroup] = None
    hidden: Optional[StrictBool] = Field(default=None, description="Controls whether the parameter should be hidden in the UI.")
    order: Optional[StrictInt] = Field(default=None, description="Ordering of the parameter in client applications.")
    tooltip: Optional[StrictStr] = Field(default=None, description="Description that is shown as a tooltip in the clients.")
    settings: Optional[Dict[str, Any]] = Field(default=None, description="Holds parameter-type specific information.")
    __properties: ClassVar[List[str]] = ["displayname", "group", "hidden", "order", "tooltip", "settings"]

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
        """Create an instance of ReqParameterDefinition from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of group
        if self.group:
            _dict['group'] = self.group.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of ReqParameterDefinition from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "displayname": obj.get("displayname"),
            "group": ReqParameterDefinitionGroup.from_dict(obj["group"]) if obj.get("group") is not None else None,
            "hidden": obj.get("hidden"),
            "order": obj.get("order"),
            "tooltip": obj.get("tooltip"),
            "settings": obj.get("settings")
        })
        return _obj



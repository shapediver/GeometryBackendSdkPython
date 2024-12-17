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

from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictStr
from typing import Any, ClassVar, Dict, List
from shapediver.geometry_api_v2.client.models.res_parameter_value import ResParameterValue
from typing import Optional, Set
from typing_extensions import Self

class ResModelStateInfo(BaseModel):
    """
    Basic information about a Model-State.
    """ # noqa: E501
    id: StrictStr = Field(description="ID of the Model-State.")
    parameters: Dict[str, ResParameterValue] = Field(description="A directory of parameter IDs and values.")
    has_image: StrictBool = Field(description="Indicates whether the Model-State includes an image.", alias="hasImage")
    has_gltf: StrictBool = Field(description="Indicates whether the Model-State includes a glTF asset.", alias="hasGltf")
    has_usdz: StrictBool = Field(description="Indicates whether the Model-State includes a USDZ asset.", alias="hasUsdz")
    __properties: ClassVar[List[str]] = ["id", "parameters", "hasImage", "hasGltf", "hasUsdz"]

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
        """Create an instance of ResModelStateInfo from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each value in parameters (dict)
        _field_dict = {}
        if self.parameters:
            for _key_parameters in self.parameters:
                if self.parameters[_key_parameters]:
                    _field_dict[_key_parameters] = self.parameters[_key_parameters].to_dict()
            _dict['parameters'] = _field_dict
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of ResModelStateInfo from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "id": obj.get("id"),
            "parameters": dict(
                (_k, ResParameterValue.from_dict(_v))
                for _k, _v in obj["parameters"].items()
            )
            if obj.get("parameters") is not None
            else None,
            "hasImage": obj.get("hasImage"),
            "hasGltf": obj.get("hasGltf"),
            "hasUsdz": obj.get("hasUsdz")
        })
        return _obj



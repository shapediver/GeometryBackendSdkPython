# coding: utf-8

"""
    Geometry Backend API v2

    The ShapeDiver Geometry Backend system is used to: * host Grasshopper models in a secure, reliable, scalable, and performant way, * run computations of Grasshopper models, * and cache and output the results of computations and exports.

    The version of the OpenAPI document: 1.7.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictFloat, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional, Union
from typing_extensions import Annotated
from typing import Optional, Set
from typing_extensions import Self

class ResOutputContent(BaseModel):
    """
    An item of the `content` array for outputs.
    """ # noqa: E501
    href: Optional[StrictStr] = Field(default=None, description="Optional link to asset.")
    size: Optional[Annotated[int, Field(strict=True, ge=0)]] = Field(default=None, description="Size in bytes for parts of type `asset`.")
    name: Optional[StrictStr] = Field(default=None, description="Optionally used for type `data`.")
    transformations: Optional[List[List[Union[StrictFloat, StrictInt]]]] = Field(default=None, description="Transformations to be applied in case of type `external` or `asset`.")
    format: StrictStr = Field(description="Format of part, used by all types of parts. * File ending for parts of type `asset`. * `material` (data contains a material definition). * `data` (data contains arbitrary data). * `external` (href or storage information that refer to an external asset).")
    msg: Optional[StrictStr] = Field(default=None, description="This was used by legacy `transform_content_array` in case of an error in getting texture URLs.")
    data: Optional[Any] = Field(default=None, description="Used for types `material` and `data`.")
    content_type: Optional[StrictStr] = Field(default=None, description="Optional Content-Type for parts of type `asset`.", alias="contentType")
    __properties: ClassVar[List[str]] = ["href", "size", "name", "transformations", "format", "msg", "data", "contentType"]

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
        """Create an instance of ResOutputContent from a JSON string"""
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
        # set to None if data (nullable) is None
        # and model_fields_set contains the field
        if self.data is None and "data" in self.model_fields_set:
            _dict['data'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of ResOutputContent from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "href": obj.get("href"),
            "size": obj.get("size"),
            "name": obj.get("name"),
            "transformations": obj.get("transformations"),
            "format": obj.get("format"),
            "msg": obj.get("msg"),
            "data": obj.get("data"),
            "contentType": obj.get("contentType")
        })
        return _obj



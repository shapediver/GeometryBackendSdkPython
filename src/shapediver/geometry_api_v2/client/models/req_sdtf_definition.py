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

from pydantic import BaseModel, ConfigDict, Field, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from typing_extensions import Annotated
from shapediver.geometry_api_v2.client.models.req_sdtf_type import ReqSdtfType
from typing import Optional, Set
from typing_extensions import Self

class ReqSdtfDefinition(BaseModel):
    """
    Data for a single sdTF parameter.
    """ # noqa: E501
    content_encoding: Optional[StrictStr] = Field(default=None, description="Encoding of the sdTF to be uploaded.")
    content_length: Annotated[int, Field(strict=True, ge=0)] = Field(description="Size of the sdTF to be uploaded, in bytes.")
    content_type: ReqSdtfType = Field(description="Content-type of the sdTF to be uploaded.")
    namespace: StrictStr = Field(description="Namespace the asset shall be created in.")
    __properties: ClassVar[List[str]] = ["content_encoding", "content_length", "content_type", "namespace"]

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
        """Create an instance of ReqSdtfDefinition from a JSON string"""
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
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of ReqSdtfDefinition from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "content_encoding": obj.get("content_encoding"),
            "content_length": obj.get("content_length"),
            "content_type": obj.get("content_type"),
            "namespace": obj.get("namespace")
        })
        return _obj



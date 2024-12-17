# coding: utf-8

"""
    Geometry Backend API v2

    The ShapeDiver Geometry Backend system is used to: * host Grasshopper models in a secure, reliable, scalable, and performant way, * run computations of Grasshopper models, * and cache and output the results of computations and exports.

    The version of the OpenAPI document: 1.8.1
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, field_validator
from typing import Any, ClassVar, Dict, List, Optional
from typing_extensions import Annotated
from shapediver.geometry_api_v2.client.models.res_model_cleanup_process_type import ResModelCleanupProcessType
from typing import Optional, Set
from typing_extensions import Self

class ResModelCleanupProcess(BaseModel):
    """
    Information about a model cleanup process.
    """ # noqa: E501
    type: ResModelCleanupProcessType = Field(description="Type of the model cleanup process.")
    timestamp_enqueued: Annotated[str, Field(strict=True)] = Field(description="The timestamp when the deletion job has been enqueued.")
    total: Optional[Annotated[int, Field(strict=True, ge=0)]] = Field(default=None, description="The total number of items of this type that are going to be deleted.")
    deleted: Optional[Annotated[int, Field(strict=True, ge=0)]] = Field(default=None, description="The number of already deleted items of this type.")
    __properties: ClassVar[List[str]] = ["type", "timestamp_enqueued", "total", "deleted"]

    @field_validator('timestamp_enqueued')
    def timestamp_enqueued_validate_regular_expression(cls, value):
        """Validates the regular expression"""
        if not re.match(r"^\d{17}$", value):
            raise ValueError(r"must validate the regular expression /^\d{17}$/")
        return value

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
        """Create an instance of ResModelCleanupProcess from a JSON string"""
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
        """Create an instance of ResModelCleanupProcess from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "type": obj.get("type"),
            "timestamp_enqueued": obj.get("timestamp_enqueued"),
            "total": obj.get("total"),
            "deleted": obj.get("deleted")
        })
        return _obj



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

from pydantic import BaseModel, ConfigDict, Field, field_validator
from typing import Any, ClassVar, Dict, List, Optional
from typing_extensions import Annotated
from shapediver.geometry_api_v2.client.models.at_least_one_any_date_extended import AtLeastOneAnyDateExtended
from shapediver.geometry_api_v2.client.models.at_least_one_uuid import AtLeastOneUuid
from typing import Optional, Set
from typing_extensions import Self

class ReqModelStatistic(BaseModel):
    """
    Parameters of a single model-session analytics request. When multiple model IDs or timestamps are requested, the resulting response-item represents an aggregation of the requested data.
    """ # noqa: E501
    modelid: AtLeastOneUuid
    timestamp: Optional[AtLeastOneAnyDateExtended] = Field(default=None, description="Multiple timestamps are aggregated and result in a single statistic object.")
    timestamp_from: Optional[Annotated[str, Field(strict=True)]] = Field(default=None, description="Allows to define the beginning of a time range, instead of specifying individual timestamps.")
    timestamp_to: Optional[Annotated[str, Field(strict=True)]] = Field(default=None, description="Allows to define the ending of a time range, instead of specifying individual timestamps.")
    __properties: ClassVar[List[str]] = ["modelid", "timestamp", "timestamp_from", "timestamp_to"]

    @field_validator('timestamp_from')
    def timestamp_from_validate_regular_expression(cls, value):
        """Validates the regular expression"""
        if value is None:
            return value

        if not re.match(r"^(\d{4}|\d{6}|\d{8}|\d{10})$", value):
            raise ValueError(r"must validate the regular expression /^(\d{4}|\d{6}|\d{8}|\d{10})$/")
        return value

    @field_validator('timestamp_to')
    def timestamp_to_validate_regular_expression(cls, value):
        """Validates the regular expression"""
        if value is None:
            return value

        if not re.match(r"^(\d{4}|\d{6}|\d{8}|\d{10})$", value):
            raise ValueError(r"must validate the regular expression /^(\d{4}|\d{6}|\d{8}|\d{10})$/")
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
        """Create an instance of ReqModelStatistic from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of modelid
        if self.modelid:
            _dict['modelid'] = self.modelid.to_dict()
        # override the default output from pydantic by calling `to_dict()` of timestamp
        if self.timestamp:
            _dict['timestamp'] = self.timestamp.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of ReqModelStatistic from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "modelid": AtLeastOneUuid.from_dict(obj["modelid"]) if obj.get("modelid") is not None else None,
            "timestamp": AtLeastOneAnyDateExtended.from_dict(obj["timestamp"]) if obj.get("timestamp") is not None else None,
            "timestamp_from": obj.get("timestamp_from"),
            "timestamp_to": obj.get("timestamp_to")
        })
        return _obj



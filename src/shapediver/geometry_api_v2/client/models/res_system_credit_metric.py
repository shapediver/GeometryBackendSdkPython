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

from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictStr
from typing import Any, ClassVar, Dict, List
from shapediver.geometry_api_v2.client.models.res_ar_credit_metric import ResArCreditMetric
from shapediver.geometry_api_v2.client.models.res_default_credit_metric import ResDefaultCreditMetric
from shapediver.geometry_api_v2.client.models.res_limited_credit_metric import ResLimitedCreditMetric
from shapediver.geometry_api_v2.client.models.res_loading_credit_metric import ResLoadingCreditMetric
from typing import Optional, Set
from typing_extensions import Self

class ResSystemCreditMetric(BaseModel):
    """
    Aggregated credit metrics for a system.
    """ # noqa: E501
    timestamp: StrictStr = Field(description="Either an extended date-time or a 'merged'-specifier.")
    is_compilation_done: StrictBool = Field(description="Aggregation for this timestamp has finished.", alias="isCompilationDone")
    ar: ResArCreditMetric
    loading: ResLoadingCreditMetric
    limited: ResLimitedCreditMetric
    default: ResDefaultCreditMetric
    system: StrictBool = Field(description="Requested system.")
    __properties: ClassVar[List[str]] = ["timestamp", "isCompilationDone", "ar", "loading", "limited", "default", "system"]

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
        """Create an instance of ResSystemCreditMetric from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of ar
        if self.ar:
            _dict['ar'] = self.ar.to_dict()
        # override the default output from pydantic by calling `to_dict()` of loading
        if self.loading:
            _dict['loading'] = self.loading.to_dict()
        # override the default output from pydantic by calling `to_dict()` of limited
        if self.limited:
            _dict['limited'] = self.limited.to_dict()
        # override the default output from pydantic by calling `to_dict()` of default
        if self.default:
            _dict['default'] = self.default.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of ResSystemCreditMetric from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "timestamp": obj.get("timestamp"),
            "isCompilationDone": obj.get("isCompilationDone"),
            "ar": ResArCreditMetric.from_dict(obj["ar"]) if obj.get("ar") is not None else None,
            "loading": ResLoadingCreditMetric.from_dict(obj["loading"]) if obj.get("loading") is not None else None,
            "limited": ResLimitedCreditMetric.from_dict(obj["limited"]) if obj.get("limited") is not None else None,
            "default": ResDefaultCreditMetric.from_dict(obj["default"]) if obj.get("default") is not None else None,
            "system": obj.get("system")
        })
        return _obj



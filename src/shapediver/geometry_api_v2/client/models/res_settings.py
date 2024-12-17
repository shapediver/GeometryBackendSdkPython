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

from pydantic import BaseModel, ConfigDict
from typing import Any, ClassVar, Dict, List, Optional
from shapediver.geometry_api_v2.client.models.res_authorization_settings import ResAuthorizationSettings
from shapediver.geometry_api_v2.client.models.res_compute_settings import ResComputeSettings
from shapediver.geometry_api_v2.client.models.res_model_settings import ResModelSettings
from typing import Optional, Set
from typing_extensions import Self

class ResSettings(BaseModel):
    """
    Definition of settings.
    """ # noqa: E501
    auth: Optional[ResAuthorizationSettings] = None
    compute: Optional[ResComputeSettings] = None
    model: Optional[ResModelSettings] = None
    __properties: ClassVar[List[str]] = ["auth", "compute", "model"]

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
        """Create an instance of ResSettings from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of auth
        if self.auth:
            _dict['auth'] = self.auth.to_dict()
        # override the default output from pydantic by calling `to_dict()` of compute
        if self.compute:
            _dict['compute'] = self.compute.to_dict()
        # override the default output from pydantic by calling `to_dict()` of model
        if self.model:
            _dict['model'] = self.model.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of ResSettings from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "auth": ResAuthorizationSettings.from_dict(obj["auth"]) if obj.get("auth") is not None else None,
            "compute": ResComputeSettings.from_dict(obj["compute"]) if obj.get("compute") is not None else None,
            "model": ResModelSettings.from_dict(obj["model"]) if obj.get("model") is not None else None
        })
        return _obj



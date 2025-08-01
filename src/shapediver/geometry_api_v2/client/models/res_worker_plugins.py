# coding: utf-8

"""
    Geometry Backend API v2

    The ShapeDiver Geometry Backend system is used to: * host Grasshopper models in a secure, reliable, scalable, and performant way, * run computations of Grasshopper models, * and cache and output the results of computations and exports.

    The version of the OpenAPI document: 1.12.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictStr
from typing import Any, ClassVar, Dict, List
from shapediver.geometry_api_v2.client.models.res_allowed_worker_plugin import ResAllowedWorkerPlugin
from shapediver.geometry_api_v2.client.models.res_installed_worker_plugin import ResInstalledWorkerPlugin
from typing import Optional, Set
from typing_extensions import Self

class ResWorkerPlugins(BaseModel):
    """
    Holds information of all installed and allowed Grasshopper plugins.
    """ # noqa: E501
    installed: List[ResInstalledWorkerPlugin] = Field(description="Contains information about all installed Grasshopper plugins.")
    allowed: List[ResAllowedWorkerPlugin] = Field(description="Contains the model checking configuration for the Grasshopper plugins.")
    inconsistent: List[StrictStr] = Field(description="Contains information about plugin inconsistencies.")
    __properties: ClassVar[List[str]] = ["installed", "allowed", "inconsistent"]

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
        """Create an instance of ResWorkerPlugins from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in installed (list)
        _items = []
        if self.installed:
            for _item_installed in self.installed:
                if _item_installed:
                    _items.append(_item_installed.to_dict())
            _dict['installed'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in allowed (list)
        _items = []
        if self.allowed:
            for _item_allowed in self.allowed:
                if _item_allowed:
                    _items.append(_item_allowed.to_dict())
            _dict['allowed'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of ResWorkerPlugins from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "installed": [ResInstalledWorkerPlugin.from_dict(_item) for _item in obj["installed"]] if obj.get("installed") is not None else None,
            "allowed": [ResAllowedWorkerPlugin.from_dict(_item) for _item in obj["allowed"]] if obj.get("allowed") is not None else None,
            "inconsistent": obj.get("inconsistent")
        })
        return _obj



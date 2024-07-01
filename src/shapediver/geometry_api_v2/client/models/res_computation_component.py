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

from pydantic import BaseModel, ConfigDict, Field
from typing import Any, ClassVar, Dict, List
from shapediver.geometry_api_v2.client.models.res_computed_component import ResComputedComponent
from shapediver.geometry_api_v2.client.models.res_computing_component import ResComputingComponent
from shapediver.geometry_api_v2.client.models.res_error_component import ResErrorComponent
from shapediver.geometry_api_v2.client.models.res_warning_component import ResWarningComponent
from typing import Optional, Set
from typing_extensions import Self

class ResComputationComponent(BaseModel):
    """
    Information about the components taking most computation time in the model computations log.
    """ # noqa: E501
    computed: List[ResComputedComponent] = Field(description="Components which were computed, ordered by descending processor time.")
    computing: List[ResComputingComponent] = Field(description="Components which were currently computing at the time the computation was stopped.")
    errors: List[ResErrorComponent] = Field(description="Component Errors.")
    warnings: List[ResWarningComponent] = Field(description="Component Warnings.")
    __properties: ClassVar[List[str]] = ["computed", "computing", "errors", "warnings"]

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
        """Create an instance of ResComputationComponent from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in computed (list)
        _items = []
        if self.computed:
            for _item in self.computed:
                if _item:
                    _items.append(_item.to_dict())
            _dict['computed'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in computing (list)
        _items = []
        if self.computing:
            for _item in self.computing:
                if _item:
                    _items.append(_item.to_dict())
            _dict['computing'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in errors (list)
        _items = []
        if self.errors:
            for _item in self.errors:
                if _item:
                    _items.append(_item.to_dict())
            _dict['errors'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in warnings (list)
        _items = []
        if self.warnings:
            for _item in self.warnings:
                if _item:
                    _items.append(_item.to_dict())
            _dict['warnings'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of ResComputationComponent from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "computed": [ResComputedComponent.from_dict(_item) for _item in obj["computed"]] if obj.get("computed") is not None else None,
            "computing": [ResComputingComponent.from_dict(_item) for _item in obj["computing"]] if obj.get("computing") is not None else None,
            "errors": [ResErrorComponent.from_dict(_item) for _item in obj["errors"]] if obj.get("errors") is not None else None,
            "warnings": [ResWarningComponent.from_dict(_item) for _item in obj["warnings"]] if obj.get("warnings") is not None else None
        })
        return _obj


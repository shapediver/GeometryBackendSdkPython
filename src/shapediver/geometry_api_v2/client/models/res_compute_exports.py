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

from pydantic import BaseModel, ConfigDict, Field, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from shapediver.geometry_api_v2.client.models.res_action import ResAction
from shapediver.geometry_api_v2.client.models.res_export_or_definition import ResExportOrDefinition
from shapediver.geometry_api_v2.client.models.res_output_or_definition import ResOutputOrDefinition
from shapediver.geometry_api_v2.client.models.res_template import ResTemplate
from typing import Optional, Set
from typing_extensions import Self

class ResComputeExports(BaseModel):
    """
    ResComputeExports
    """ # noqa: E501
    actions: Optional[List[ResAction]] = Field(default=None, description="Actions the client may take.")
    exports: Optional[Dict[str, ResExportOrDefinition]] = Field(default=None, description="Exports of the model for the given parameter values. A directory of export-IDs and exports.")
    message: Optional[StrictStr] = Field(default=None, description="Contains urgent information about the system.")
    outputs: Optional[Dict[str, ResOutputOrDefinition]] = Field(default=None, description="Outputs of the model for the given parameter values. A directory of output-IDs and outputs.")
    templates: Optional[List[ResTemplate]] = Field(default=None, description="Request templates for actions.")
    version: StrictStr = Field(description="Version of the Geometry Backend API.")
    __properties: ClassVar[List[str]] = ["actions", "exports", "message", "outputs", "templates", "version"]

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
        """Create an instance of ResComputeExports from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in actions (list)
        _items = []
        if self.actions:
            for _item_actions in self.actions:
                if _item_actions:
                    _items.append(_item_actions.to_dict())
            _dict['actions'] = _items
        # override the default output from pydantic by calling `to_dict()` of each value in exports (dict)
        _field_dict = {}
        if self.exports:
            for _key_exports in self.exports:
                if self.exports[_key_exports]:
                    _field_dict[_key_exports] = self.exports[_key_exports].to_dict()
            _dict['exports'] = _field_dict
        # override the default output from pydantic by calling `to_dict()` of each value in outputs (dict)
        _field_dict = {}
        if self.outputs:
            for _key_outputs in self.outputs:
                if self.outputs[_key_outputs]:
                    _field_dict[_key_outputs] = self.outputs[_key_outputs].to_dict()
            _dict['outputs'] = _field_dict
        # override the default output from pydantic by calling `to_dict()` of each item in templates (list)
        _items = []
        if self.templates:
            for _item_templates in self.templates:
                if _item_templates:
                    _items.append(_item_templates.to_dict())
            _dict['templates'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of ResComputeExports from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "actions": [ResAction.from_dict(_item) for _item in obj["actions"]] if obj.get("actions") is not None else None,
            "exports": dict(
                (_k, ResExportOrDefinition.from_dict(_v))
                for _k, _v in obj["exports"].items()
            )
            if obj.get("exports") is not None
            else None,
            "message": obj.get("message"),
            "outputs": dict(
                (_k, ResOutputOrDefinition.from_dict(_v))
                for _k, _v in obj["outputs"].items()
            )
            if obj.get("outputs") is not None
            else None,
            "templates": [ResTemplate.from_dict(_item) for _item in obj["templates"]] if obj.get("templates") is not None else None,
            "version": obj.get("version")
        })
        return _obj



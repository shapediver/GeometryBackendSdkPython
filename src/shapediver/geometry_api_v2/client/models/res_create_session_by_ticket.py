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

from pydantic import BaseModel, ConfigDict, Field, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from shapediver.geometry_api_v2.client.models.res_action import ResAction
from shapediver.geometry_api_v2.client.models.res_export_or_definition import ResExportOrDefinition
from shapediver.geometry_api_v2.client.models.res_model import ResModel
from shapediver.geometry_api_v2.client.models.res_output_or_definition import ResOutputOrDefinition
from shapediver.geometry_api_v2.client.models.res_parameter import ResParameter
from shapediver.geometry_api_v2.client.models.res_statistic import ResStatistic
from shapediver.geometry_api_v2.client.models.res_template import ResTemplate
from shapediver.geometry_api_v2.client.models.res_viewer import ResViewer
from typing import Optional, Set
from typing_extensions import Self

class ResCreateSessionByTicket(BaseModel):
    """
    ResCreateSessionByTicket
    """ # noqa: E501
    actions: List[ResAction] = Field(description="Actions the client may take.")
    exports: Optional[Dict[str, ResExportOrDefinition]] = Field(default=None, description="Exports of the model for the given parameter values. A directory of export-IDs and exports.")
    message: Optional[StrictStr] = Field(default=None, description="Contains urgent information about the system.")
    model: ResModel = Field(description="The definitions of a ShapeDiver model.")
    outputs: Optional[Dict[str, ResOutputOrDefinition]] = Field(default=None, description="Outputs of the model for the given parameter values. A directory of output-IDs and outputs.")
    parameters: Optional[Dict[str, ResParameter]] = Field(default=None, description="Parameter definitions, not contained with every response. A directory of parameter-IDs and parameters.")
    session_id: StrictStr = Field(description="The ID of the created session.", alias="sessionId")
    statistic: ResStatistic = Field(description="Statistics of a model.")
    templates: List[ResTemplate] = Field(description="Request templates for actions.")
    version: StrictStr = Field(description="Version of the Geometry Backend API.")
    viewer: ResViewer = Field(description="Viewer specific data.")
    viewer_settings_version: StrictStr = Field(description="The current version of the viewer settings.", alias="viewerSettingsVersion")
    __properties: ClassVar[List[str]] = ["actions", "exports", "message", "model", "outputs", "parameters", "sessionId", "statistic", "templates", "version", "viewer", "viewerSettingsVersion"]

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
        """Create an instance of ResCreateSessionByTicket from a JSON string"""
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
            for _item in self.actions:
                if _item:
                    _items.append(_item.to_dict())
            _dict['actions'] = _items
        # override the default output from pydantic by calling `to_dict()` of each value in exports (dict)
        _field_dict = {}
        if self.exports:
            for _key in self.exports:
                if self.exports[_key]:
                    _field_dict[_key] = self.exports[_key].to_dict()
            _dict['exports'] = _field_dict
        # override the default output from pydantic by calling `to_dict()` of model
        if self.model:
            _dict['model'] = self.model.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each value in outputs (dict)
        _field_dict = {}
        if self.outputs:
            for _key in self.outputs:
                if self.outputs[_key]:
                    _field_dict[_key] = self.outputs[_key].to_dict()
            _dict['outputs'] = _field_dict
        # override the default output from pydantic by calling `to_dict()` of each value in parameters (dict)
        _field_dict = {}
        if self.parameters:
            for _key in self.parameters:
                if self.parameters[_key]:
                    _field_dict[_key] = self.parameters[_key].to_dict()
            _dict['parameters'] = _field_dict
        # override the default output from pydantic by calling `to_dict()` of statistic
        if self.statistic:
            _dict['statistic'] = self.statistic.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in templates (list)
        _items = []
        if self.templates:
            for _item in self.templates:
                if _item:
                    _items.append(_item.to_dict())
            _dict['templates'] = _items
        # override the default output from pydantic by calling `to_dict()` of viewer
        if self.viewer:
            _dict['viewer'] = self.viewer.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of ResCreateSessionByTicket from a dict"""
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
            "model": ResModel.from_dict(obj["model"]) if obj.get("model") is not None else None,
            "outputs": dict(
                (_k, ResOutputOrDefinition.from_dict(_v))
                for _k, _v in obj["outputs"].items()
            )
            if obj.get("outputs") is not None
            else None,
            "parameters": dict(
                (_k, ResParameter.from_dict(_v))
                for _k, _v in obj["parameters"].items()
            )
            if obj.get("parameters") is not None
            else None,
            "sessionId": obj.get("sessionId"),
            "statistic": ResStatistic.from_dict(obj["statistic"]) if obj.get("statistic") is not None else None,
            "templates": [ResTemplate.from_dict(_item) for _item in obj["templates"]] if obj.get("templates") is not None else None,
            "version": obj.get("version"),
            "viewer": ResViewer.from_dict(obj["viewer"]) if obj.get("viewer") is not None else None,
            "viewerSettingsVersion": obj.get("viewerSettingsVersion")
        })
        return _obj



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
from typing import Any, ClassVar, Dict, List, Optional
from shapediver.geometry_api_v2.client.models.res_export_or_definition import ResExportOrDefinition
from shapediver.geometry_api_v2.client.models.res_file import ResFile
from shapediver.geometry_api_v2.client.models.res_model import ResModel
from shapediver.geometry_api_v2.client.models.res_output_or_definition import ResOutputOrDefinition
from shapediver.geometry_api_v2.client.models.res_parameter import ResParameter
from shapediver.geometry_api_v2.client.models.res_plugins import ResPlugins
from shapediver.geometry_api_v2.client.models.res_settings import ResSettings
from shapediver.geometry_api_v2.client.models.res_statistic import ResStatistic
from typing import Optional, Set
from typing_extensions import Self

class ResGetModel(BaseModel):
    """
    ResGetModel
    """ # noqa: E501
    exports: Optional[Dict[str, ResExportOrDefinition]] = Field(default=None, description="Exports of the model for the given parameter values. A directory of export-IDs and exports.")
    file: ResFile = Field(description="Links regarding the model file.")
    message: Optional[StrictStr] = Field(default=None, description="Contains urgent information about the system.")
    model: ResModel = Field(description="The definitions of a ShapeDiver model.")
    outputs: Optional[Dict[str, ResOutputOrDefinition]] = Field(default=None, description="Outputs of the model for the given parameter values. A directory of output-IDs and outputs.")
    parameters: Optional[Dict[str, ResParameter]] = Field(default=None, description="Parameter definitions, not contained with every response. A directory of parameter-IDs and parameters.")
    plugins: Optional[ResPlugins] = None
    setting: ResSettings = Field(description="Various settings.")
    statistic: ResStatistic = Field(description="Statistics of a model.")
    version: StrictStr = Field(description="Version of the Geometry Backend API.")
    __properties: ClassVar[List[str]] = ["exports", "file", "message", "model", "outputs", "parameters", "plugins", "setting", "statistic", "version"]

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
        """Create an instance of ResGetModel from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each value in exports (dict)
        _field_dict = {}
        if self.exports:
            for _key_exports in self.exports:
                if self.exports[_key_exports]:
                    _field_dict[_key_exports] = self.exports[_key_exports].to_dict()
            _dict['exports'] = _field_dict
        # override the default output from pydantic by calling `to_dict()` of file
        if self.file:
            _dict['file'] = self.file.to_dict()
        # override the default output from pydantic by calling `to_dict()` of model
        if self.model:
            _dict['model'] = self.model.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each value in outputs (dict)
        _field_dict = {}
        if self.outputs:
            for _key_outputs in self.outputs:
                if self.outputs[_key_outputs]:
                    _field_dict[_key_outputs] = self.outputs[_key_outputs].to_dict()
            _dict['outputs'] = _field_dict
        # override the default output from pydantic by calling `to_dict()` of each value in parameters (dict)
        _field_dict = {}
        if self.parameters:
            for _key_parameters in self.parameters:
                if self.parameters[_key_parameters]:
                    _field_dict[_key_parameters] = self.parameters[_key_parameters].to_dict()
            _dict['parameters'] = _field_dict
        # override the default output from pydantic by calling `to_dict()` of plugins
        if self.plugins:
            _dict['plugins'] = self.plugins.to_dict()
        # override the default output from pydantic by calling `to_dict()` of setting
        if self.setting:
            _dict['setting'] = self.setting.to_dict()
        # override the default output from pydantic by calling `to_dict()` of statistic
        if self.statistic:
            _dict['statistic'] = self.statistic.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of ResGetModel from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "exports": dict(
                (_k, ResExportOrDefinition.from_dict(_v))
                for _k, _v in obj["exports"].items()
            )
            if obj.get("exports") is not None
            else None,
            "file": ResFile.from_dict(obj["file"]) if obj.get("file") is not None else None,
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
            "plugins": ResPlugins.from_dict(obj["plugins"]) if obj.get("plugins") is not None else None,
            "setting": ResSettings.from_dict(obj["setting"]) if obj.get("setting") is not None else None,
            "statistic": ResStatistic.from_dict(obj["statistic"]) if obj.get("statistic") is not None else None,
            "version": obj.get("version")
        })
        return _obj



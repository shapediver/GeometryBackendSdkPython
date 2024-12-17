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
from shapediver.geometry_api_v2.client.models.res_file import ResFile
from shapediver.geometry_api_v2.client.models.res_model import ResModel
from shapediver.geometry_api_v2.client.models.res_settings import ResSettings
from shapediver.geometry_api_v2.client.models.res_statistic import ResStatistic
from typing import Optional, Set
from typing_extensions import Self

class ResUpdateModel(BaseModel):
    """
    ResUpdateModel
    """ # noqa: E501
    file: ResFile = Field(description="Links regarding the model file.")
    message: Optional[StrictStr] = Field(default=None, description="Contains urgent information about the system.")
    model: ResModel = Field(description="The definitions of a ShapeDiver model.")
    setting: ResSettings = Field(description="Various settings.")
    statistic: ResStatistic = Field(description="Statistics of a model.")
    version: StrictStr = Field(description="Version of the Geometry Backend API.")
    __properties: ClassVar[List[str]] = ["file", "message", "model", "setting", "statistic", "version"]

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
        """Create an instance of ResUpdateModel from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of file
        if self.file:
            _dict['file'] = self.file.to_dict()
        # override the default output from pydantic by calling `to_dict()` of model
        if self.model:
            _dict['model'] = self.model.to_dict()
        # override the default output from pydantic by calling `to_dict()` of setting
        if self.setting:
            _dict['setting'] = self.setting.to_dict()
        # override the default output from pydantic by calling `to_dict()` of statistic
        if self.statistic:
            _dict['statistic'] = self.statistic.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of ResUpdateModel from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "file": ResFile.from_dict(obj["file"]) if obj.get("file") is not None else None,
            "message": obj.get("message"),
            "model": ResModel.from_dict(obj["model"]) if obj.get("model") is not None else None,
            "setting": ResSettings.from_dict(obj["setting"]) if obj.get("setting") is not None else None,
            "statistic": ResStatistic.from_dict(obj["statistic"]) if obj.get("statistic") is not None else None,
            "version": obj.get("version")
        })
        return _obj



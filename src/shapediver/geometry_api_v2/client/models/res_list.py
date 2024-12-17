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

from pydantic import BaseModel, ConfigDict, Field
from typing import Any, ClassVar, Dict, List, Optional
from shapediver.geometry_api_v2.client.models.res_export import ResExport
from shapediver.geometry_api_v2.client.models.res_file_info import ResFileInfo
from shapediver.geometry_api_v2.client.models.res_model import ResModel
from shapediver.geometry_api_v2.client.models.res_model_state_info import ResModelStateInfo
from shapediver.geometry_api_v2.client.models.res_output import ResOutput
from shapediver.geometry_api_v2.client.models.res_sdtf_info import ResSdtfInfo
from shapediver.geometry_api_v2.client.models.res_texture import ResTexture
from typing import Optional, Set
from typing_extensions import Self

class ResList(BaseModel):
    """
    ShapeDiver API response of a list-request.
    """ # noqa: E501
    file: Optional[List[ResFileInfo]] = Field(default=None, description="A directory of file objects.")
    sdtf: Optional[List[ResSdtfInfo]] = Field(default=None, description="A directory of sdTF objects.")
    model: Optional[List[ResModel]] = Field(default=None, description="A directory of ShapeDiver models.")
    model_state: Optional[List[ResModelStateInfo]] = Field(default=None, description="A directory of Model-States.", alias="modelState")
    output: Optional[List[ResOutput]] = Field(default=None, description="A directory of output versions.")
    export: Optional[List[ResExport]] = Field(default=None, description="A directory of export versions.")
    texture: Optional[List[ResTexture]] = Field(default=None, description="A directory of model textures.")
    __properties: ClassVar[List[str]] = ["file", "sdtf", "model", "modelState", "output", "export", "texture"]

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
        """Create an instance of ResList from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in file (list)
        _items = []
        if self.file:
            for _item_file in self.file:
                if _item_file:
                    _items.append(_item_file.to_dict())
            _dict['file'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in sdtf (list)
        _items = []
        if self.sdtf:
            for _item_sdtf in self.sdtf:
                if _item_sdtf:
                    _items.append(_item_sdtf.to_dict())
            _dict['sdtf'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in model (list)
        _items = []
        if self.model:
            for _item_model in self.model:
                if _item_model:
                    _items.append(_item_model.to_dict())
            _dict['model'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in model_state (list)
        _items = []
        if self.model_state:
            for _item_model_state in self.model_state:
                if _item_model_state:
                    _items.append(_item_model_state.to_dict())
            _dict['modelState'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in output (list)
        _items = []
        if self.output:
            for _item_output in self.output:
                if _item_output:
                    _items.append(_item_output.to_dict())
            _dict['output'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in export (list)
        _items = []
        if self.export:
            for _item_export in self.export:
                if _item_export:
                    _items.append(_item_export.to_dict())
            _dict['export'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in texture (list)
        _items = []
        if self.texture:
            for _item_texture in self.texture:
                if _item_texture:
                    _items.append(_item_texture.to_dict())
            _dict['texture'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of ResList from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "file": [ResFileInfo.from_dict(_item) for _item in obj["file"]] if obj.get("file") is not None else None,
            "sdtf": [ResSdtfInfo.from_dict(_item) for _item in obj["sdtf"]] if obj.get("sdtf") is not None else None,
            "model": [ResModel.from_dict(_item) for _item in obj["model"]] if obj.get("model") is not None else None,
            "modelState": [ResModelStateInfo.from_dict(_item) for _item in obj["modelState"]] if obj.get("modelState") is not None else None,
            "output": [ResOutput.from_dict(_item) for _item in obj["output"]] if obj.get("output") is not None else None,
            "export": [ResExport.from_dict(_item) for _item in obj["export"]] if obj.get("export") is not None else None,
            "texture": [ResTexture.from_dict(_item) for _item in obj["texture"]] if obj.get("texture") is not None else None
        })
        return _obj



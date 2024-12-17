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

from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from typing_extensions import Annotated
from shapediver.geometry_api_v2.client.models.res_computation_status import ResComputationStatus
from shapediver.geometry_api_v2.client.models.res_export_content import ResExportContent
from shapediver.geometry_api_v2.client.models.res_export_definition_group import ResExportDefinitionGroup
from shapediver.geometry_api_v2.client.models.res_export_definition_type import ResExportDefinitionType
from shapediver.geometry_api_v2.client.models.res_export_result import ResExportResult
from typing import Optional, Set
from typing_extensions import Self

class ResExport(BaseModel):
    """
    Export definition WITH results as exposed on the API.
    """ # noqa: E501
    id: StrictStr = Field(description="ID of the export, dependent on model ID, and therefore changing each time a model gets uploaded.")
    uid: Optional[StrictStr] = Field(default=None, description="Constant ID of the export, not dependent on model ID, and therefore NOT changing each time a model gets uploaded. Might be undefined because this property was introduced in summer 2020 and does not exist for exports of older models.")
    name: StrictStr = Field(description="Name of the export.")
    type: ResExportDefinitionType = Field(description="Type of export.")
    dependency: List[StrictStr] = Field(description="List of IDs of parameters influencing this export.")
    group: Optional[ResExportDefinitionGroup] = None
    order: Optional[StrictInt] = Field(default=None, description="Ordering of the export in client applications.")
    tooltip: Optional[StrictStr] = Field(default=None, description="Description that is shown as a tooltip in the clients.")
    displayname: Optional[StrictStr] = Field(default=None, description="Parameter name to display instead of `name`.")
    hidden: StrictBool = Field(description="Controls whether the parameter should be hidden in the UI.")
    version: StrictStr = Field(description="Requested version of the export.")
    delay: Optional[Annotated[int, Field(strict=True, ge=0)]] = Field(default=None, description="The delay in milliseconds after which an export cache request shall be sent to check again for this export version. This property is used ONLY if the export version has not been computed yet.  Note that the existence of this property does not necessarily imply the presence of an active or queued computation for the respective export version.")
    content: Optional[List[ResExportContent]] = Field(default=None, description="Result parts. In case this array does not exist, this means that the workers have not finished computation for this output version.")
    msg: Optional[StrictStr] = Field(default=None, description="In case computation of the export version (temporarily) failed. Contains a message explaining what went wrong.")
    filename: Optional[StrictStr] = Field(default=None, description="Optional suggested filename for the files to be downloaded.")
    result: Optional[ResExportResult] = None
    status_computation: Optional[ResComputationStatus] = Field(default=None, description="Status of the computation which resulted in the export version.")
    status_collect: Optional[ResComputationStatus] = Field(default=None, description="Status of collecting results for the export version.")
    __properties: ClassVar[List[str]] = ["id", "uid", "name", "type", "dependency", "group", "order", "tooltip", "displayname", "hidden", "version", "delay", "content", "msg", "filename", "result", "status_computation", "status_collect"]

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
        """Create an instance of ResExport from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of group
        if self.group:
            _dict['group'] = self.group.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in content (list)
        _items = []
        if self.content:
            for _item_content in self.content:
                if _item_content:
                    _items.append(_item_content.to_dict())
            _dict['content'] = _items
        # override the default output from pydantic by calling `to_dict()` of result
        if self.result:
            _dict['result'] = self.result.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of ResExport from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "id": obj.get("id"),
            "uid": obj.get("uid"),
            "name": obj.get("name"),
            "type": obj.get("type"),
            "dependency": obj.get("dependency"),
            "group": ResExportDefinitionGroup.from_dict(obj["group"]) if obj.get("group") is not None else None,
            "order": obj.get("order"),
            "tooltip": obj.get("tooltip"),
            "displayname": obj.get("displayname"),
            "hidden": obj.get("hidden"),
            "version": obj.get("version"),
            "delay": obj.get("delay"),
            "content": [ResExportContent.from_dict(_item) for _item in obj["content"]] if obj.get("content") is not None else None,
            "msg": obj.get("msg"),
            "filename": obj.get("filename"),
            "result": ResExportResult.from_dict(obj["result"]) if obj.get("result") is not None else None,
            "status_computation": obj.get("status_computation"),
            "status_collect": obj.get("status_collect")
        })
        return _obj



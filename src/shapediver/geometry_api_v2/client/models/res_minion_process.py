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
from shapediver.geometry_api_v2.client.models.res_minion_task import ResMinionTask
from typing import Optional, Set
from typing_extensions import Self

class ResMinionProcess(BaseModel):
    """
    System information a single Geometry Minions process.
    """ # noqa: E501
    tasks: Dict[str, ResMinionTask] = Field(description="Information about completed tasks, listed per task type.")
    __properties: ClassVar[List[str]] = ["tasks"]

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
        """Create an instance of ResMinionProcess from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each value in tasks (dict)
        _field_dict = {}
        if self.tasks:
            for _key in self.tasks:
                if self.tasks[_key]:
                    _field_dict[_key] = self.tasks[_key].to_dict()
            _dict['tasks'] = _field_dict
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of ResMinionProcess from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "tasks": dict(
                (_k, ResMinionTask.from_dict(_v))
                for _k, _v in obj["tasks"].items()
            )
            if obj.get("tasks") is not None
            else None
        })
        return _obj



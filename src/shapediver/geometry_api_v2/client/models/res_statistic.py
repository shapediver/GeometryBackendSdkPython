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

from pydantic import BaseModel, ConfigDict, Field, field_validator
from typing import Any, ClassVar, Dict, List, Optional
from typing_extensions import Annotated
from typing import Optional, Set
from typing_extensions import Self

class ResStatistic(BaseModel):
    """
    Model statistic object.
    """ # noqa: E501
    comptime: Optional[Annotated[int, Field(strict=True, ge=0)]] = Field(default=None, description="Cumulative time (msec) which has been spent for processing computation requests by the workers (pure computation time).")
    lastsession: Optional[Annotated[str, Field(strict=True)]] = Field(default=None, description="Timestamp of last session created for the model.")
    lastview: Optional[Annotated[str, Field(strict=True)]] = Field(default=None, description="Timestamp of last view of the model.")
    mem_usage: Optional[Annotated[int, Field(strict=True, ge=0)]] = Field(default=None, description="Approximate memory usage of model on workers, in bytes.", alias="memUsage")
    numcomp: Optional[Annotated[int, Field(strict=True, ge=0)]] = Field(default=None, description="Number of computations which have been carried out for the model by the workers so far.")
    numsessions: Optional[Annotated[int, Field(strict=True, ge=0)]] = Field(default=None, description="Number of sessions which have been opened for the model so far.")
    requesttime: Optional[Annotated[int, Field(strict=True, ge=0)]] = Field(default=None, description="Cumulative time (msec) which has been spent for processing computation requests by the workers (computation time plus overheads).")
    size: Optional[Annotated[int, Field(strict=True, ge=0)]] = Field(default=None, description="File size of the model file in bytes.")
    __properties: ClassVar[List[str]] = ["comptime", "lastsession", "lastview", "memUsage", "numcomp", "numsessions", "requesttime", "size"]

    @field_validator('lastsession')
    def lastsession_validate_regular_expression(cls, value):
        """Validates the regular expression"""
        if value is None:
            return value

        if not re.match(r"^\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}.\d{3}Z$", value):
            raise ValueError(r"must validate the regular expression /^\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}.\d{3}Z$/")
        return value

    @field_validator('lastview')
    def lastview_validate_regular_expression(cls, value):
        """Validates the regular expression"""
        if value is None:
            return value

        if not re.match(r"^\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}.\d{3}Z$", value):
            raise ValueError(r"must validate the regular expression /^\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}.\d{3}Z$/")
        return value

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
        """Create an instance of ResStatistic from a JSON string"""
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
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of ResStatistic from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "comptime": obj.get("comptime"),
            "lastsession": obj.get("lastsession"),
            "lastview": obj.get("lastview"),
            "memUsage": obj.get("memUsage"),
            "numcomp": obj.get("numcomp"),
            "numsessions": obj.get("numsessions"),
            "requesttime": obj.get("requesttime"),
            "size": obj.get("size")
        })
        return _obj



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

from pydantic import BaseModel, ConfigDict, Field, StrictFloat, StrictInt, StrictStr, field_validator
from typing import Any, ClassVar, Dict, List, Optional, Union
from typing_extensions import Annotated
from shapediver.geometry_api_v2.client.models.res_computation_limits import ResComputationLimits
from shapediver.geometry_api_v2.client.models.res_computation_status import ResComputationStatus
from shapediver.geometry_api_v2.client.models.res_model_computation_stats import ResModelComputationStats
from typing import Optional, Set
from typing_extensions import Self

class ResModelComputation(BaseModel):
    """
    Components of a model computation request.
    """ # noqa: E501
    id: StrictStr = Field(description="ID of the model.")
    timestamp: StrictInt = Field(description="Numeric timestamp in format `YYYYMMDDHHMMSSMMM`.  Deprecated: Use `timestamp_str` instead.")
    timestamp_str: Annotated[str, Field(strict=True)] = Field(description="Timestamp.")
    compute_request_id: StrictStr = Field(description="The ID of the compute request that was processed.")
    exports: Dict[str, StrictStr] = Field(description="Requested export versions.")
    outputs: Dict[str, StrictStr] = Field(description="Requested output versions.")
    params: Dict[str, Any] = Field(description="Parameter values.")
    stats: ResModelComputationStats = Field(description="The stats of the computation request.")
    status: ResComputationStatus = Field(description="Result of processing request.")
    timestamp_fin: Annotated[str, Field(strict=True)] = Field(description="Timestamp when the computation request was finished.")
    timestamp_req: Annotated[str, Field(strict=True)] = Field(description="Timestamp when the work request was filed.")
    timestamp_req_iso: Annotated[str, Field(strict=True)] = Field(description="Timestamp when the computation request was filed.")
    timestamp_resp: Annotated[str, Field(strict=True)] = Field(description="Timestamp when the computation request was picked up.")
    msg: Optional[StrictStr] = Field(default=None, description="Message containing information about the computation process.")
    limit: Optional[ResComputationLimits] = Field(default=None, description="Model's limits at the time of the computation process.")
    credits: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="The number of credits that are charged for this computation.")
    __properties: ClassVar[List[str]] = ["id", "timestamp", "timestamp_str", "compute_request_id", "exports", "outputs", "params", "stats", "status", "timestamp_fin", "timestamp_req", "timestamp_req_iso", "timestamp_resp", "msg", "limit", "credits"]

    @field_validator('timestamp_str')
    def timestamp_str_validate_regular_expression(cls, value):
        """Validates the regular expression"""
        if not re.match(r"^\d{17}$", value):
            raise ValueError(r"must validate the regular expression /^\d{17}$/")
        return value

    @field_validator('timestamp_fin')
    def timestamp_fin_validate_regular_expression(cls, value):
        """Validates the regular expression"""
        if not re.match(r"^\d{17}$", value):
            raise ValueError(r"must validate the regular expression /^\d{17}$/")
        return value

    @field_validator('timestamp_req')
    def timestamp_req_validate_regular_expression(cls, value):
        """Validates the regular expression"""
        if not re.match(r"^\d{13}$", value):
            raise ValueError(r"must validate the regular expression /^\d{13}$/")
        return value

    @field_validator('timestamp_req_iso')
    def timestamp_req_iso_validate_regular_expression(cls, value):
        """Validates the regular expression"""
        if not re.match(r"^\d{17}$", value):
            raise ValueError(r"must validate the regular expression /^\d{17}$/")
        return value

    @field_validator('timestamp_resp')
    def timestamp_resp_validate_regular_expression(cls, value):
        """Validates the regular expression"""
        if not re.match(r"^\d{17}$", value):
            raise ValueError(r"must validate the regular expression /^\d{17}$/")
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
        """Create an instance of ResModelComputation from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of stats
        if self.stats:
            _dict['stats'] = self.stats.to_dict()
        # override the default output from pydantic by calling `to_dict()` of limit
        if self.limit:
            _dict['limit'] = self.limit.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of ResModelComputation from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "id": obj.get("id"),
            "timestamp": obj.get("timestamp"),
            "timestamp_str": obj.get("timestamp_str"),
            "compute_request_id": obj.get("compute_request_id"),
            "exports": obj.get("exports"),
            "outputs": obj.get("outputs"),
            "params": obj.get("params"),
            "stats": ResModelComputationStats.from_dict(obj["stats"]) if obj.get("stats") is not None else None,
            "status": obj.get("status"),
            "timestamp_fin": obj.get("timestamp_fin"),
            "timestamp_req": obj.get("timestamp_req"),
            "timestamp_req_iso": obj.get("timestamp_req_iso"),
            "timestamp_resp": obj.get("timestamp_resp"),
            "msg": obj.get("msg"),
            "limit": ResComputationLimits.from_dict(obj["limit"]) if obj.get("limit") is not None else None,
            "credits": obj.get("credits")
        })
        return _obj



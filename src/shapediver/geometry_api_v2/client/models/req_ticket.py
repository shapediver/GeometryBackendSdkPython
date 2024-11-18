# coding: utf-8

"""
    Geometry Backend API v2

    The ShapeDiver Geometry Backend system is used to: * host Grasshopper models in a secure, reliable, scalable, and performant way, * run computations of Grasshopper models, * and cache and output the results of computations and exports.

    The version of the OpenAPI document: 1.7.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictStr, field_validator
from typing import Any, ClassVar, Dict, List, Optional
from typing_extensions import Annotated
from shapediver.geometry_api_v2.client.models.req_ticket_type import ReqTicketType
from typing import Optional, Set
from typing_extensions import Self

class ReqTicket(BaseModel):
    """
    Body of a ticket request.
    """ # noqa: E501
    accessdomains: Optional[List[StrictStr]] = Field(default=None, description="List of domains (origins) this ticket should be limited to; may be empty.")
    author: Optional[StrictBool] = Field(default=None, description="Should this ticket provide access to model authoring (allows to change configuration)?")
    pub: StrictBool = Field(description="Should this ticket allow public access (ignore the model's `accessdomains` property)?")
    until: Annotated[str, Field(strict=True)] = Field(description="The timestamp until which the ticket should be valid.")
    use_id2: Optional[StrictBool] = Field(default=None, description="Does this ticket identify the model via its secondary ID (model property `id2`)?")
    type: ReqTicketType
    __properties: ClassVar[List[str]] = ["accessdomains", "author", "pub", "until", "use_id2", "type"]

    @field_validator('until')
    def until_validate_regular_expression(cls, value):
        """Validates the regular expression"""
        if not re.match(r"^\d{14}$", value):
            raise ValueError(r"must validate the regular expression /^\d{14}$/")
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
        """Create an instance of ReqTicket from a JSON string"""
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
        """Create an instance of ReqTicket from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "accessdomains": obj.get("accessdomains"),
            "author": obj.get("author"),
            "pub": obj.get("pub"),
            "until": obj.get("until"),
            "use_id2": obj.get("use_id2"),
            "type": obj.get("type")
        })
        return _obj



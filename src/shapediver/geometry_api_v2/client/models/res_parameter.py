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

from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictFloat, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional, Union
from typing_extensions import Annotated
from shapediver.geometry_api_v2.client.models.res_parameter_group import ResParameterGroup
from shapediver.geometry_api_v2.client.models.res_parameter_type import ResParameterType
from shapediver.geometry_api_v2.client.models.res_structure_type import ResStructureType
from shapediver.geometry_api_v2.client.models.res_visualization_type import ResVisualizationType
from typing import Optional, Set
from typing_extensions import Self

class ResParameter(BaseModel):
    """
    Definition of a parameter of a ShapeDiver Model.
    """ # noqa: E501
    id: StrictStr = Field(description="Unique ID of parameter, stays constant each time a model gets uploaded.")
    choices: Optional[List[StrictStr]] = Field(default=None, description="Choice of parameter values for types `STRINGLIST`.")
    decimalplaces: Optional[Annotated[int, Field(strict=True, ge=0)]] = Field(default=None, description="Number of decimal places for numeric types.")
    defval: Optional[StrictStr] = Field(default=None, description="Default value of parameter, stringified.")
    expression: Optional[StrictStr] = Field(default=None, description="Optional expression to be applied to value for visualisation.")
    format: Optional[List[StrictStr]] = Field(default=None, description="List of file formats (content types) supported, used for type `FILE`.")
    min: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="Minimum value (stringified) for numeric types.")
    max: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="Maximum: * value (stringified) for numeric types. * string length for type `STRING`. * file size allowed (stringified) for type FILE.")
    umin: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="Minimum `u` value for two dimensional domain parameters.")
    umax: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="Maximum `u` value for two dimensional domain parameters.")
    vmin: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="Minimum `v` value for two dimensional domain parameters.")
    vmax: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="Maximum `v` value for two dimensional domain parameters.")
    interval: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="Step size used for domain parameters.")
    name: StrictStr = Field(description="Name of the parameter.")
    type: ResParameterType = Field(description="Type of parameter.")
    visualization: Optional[ResVisualizationType] = Field(default=None, description="Optional preferred visualization for parameters of type `FILE` and `STRINGLIST`.")
    structure: Optional[ResStructureType] = Field(default=None, description="Structure of a parameter.")
    group: Optional[ResParameterGroup] = None
    hint: Optional[StrictStr] = Field(default=None, description="Technical hint for the UI implementation.")
    order: Optional[StrictInt] = Field(default=None, description="Ordering of the parameter in client applications.")
    tooltip: Optional[StrictStr] = Field(default=None, description="Description that is shown as a tooltip in the clients.")
    displayname: Optional[StrictStr] = Field(default=None, description="Parameter name to display instead of `name`.")
    hidden: StrictBool = Field(description="Controls whether the parameter should be hidden in the UI.")
    __properties: ClassVar[List[str]] = ["id", "choices", "decimalplaces", "defval", "expression", "format", "min", "max", "umin", "umax", "vmin", "vmax", "interval", "name", "type", "visualization", "structure", "group", "hint", "order", "tooltip", "displayname", "hidden"]

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
        """Create an instance of ResParameter from a JSON string"""
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
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of ResParameter from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "id": obj.get("id"),
            "choices": obj.get("choices"),
            "decimalplaces": obj.get("decimalplaces"),
            "defval": obj.get("defval"),
            "expression": obj.get("expression"),
            "format": obj.get("format"),
            "min": obj.get("min"),
            "max": obj.get("max"),
            "umin": obj.get("umin"),
            "umax": obj.get("umax"),
            "vmin": obj.get("vmin"),
            "vmax": obj.get("vmax"),
            "interval": obj.get("interval"),
            "name": obj.get("name"),
            "type": obj.get("type"),
            "visualization": obj.get("visualization"),
            "structure": obj.get("structure"),
            "group": ResParameterGroup.from_dict(obj["group"]) if obj.get("group") is not None else None,
            "hint": obj.get("hint"),
            "order": obj.get("order"),
            "tooltip": obj.get("tooltip"),
            "displayname": obj.get("displayname"),
            "hidden": obj.get("hidden")
        })
        return _obj



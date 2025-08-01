# coding: utf-8

"""
    Geometry Backend API v2

    The ShapeDiver Geometry Backend system is used to: * host Grasshopper models in a secure, reliable, scalable, and performant way, * run computations of Grasshopper models, * and cache and output the results of computations and exports.

    The version of the OpenAPI document: 1.12.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import json
import pprint
from pydantic import BaseModel, ConfigDict, Field, StrictStr, ValidationError, field_validator
from typing import Any, List, Optional
from shapediver.geometry_api_v2.client.models.res_export import ResExport
from shapediver.geometry_api_v2.client.models.res_export_definition import ResExportDefinition
from pydantic import StrictStr, Field
from typing import Union, List, Set, Optional, Dict
from typing_extensions import Literal, Self

RESEXPORTORDEFINITION_ONE_OF_SCHEMAS = ["ResExport", "ResExportDefinition"]

class ResExportOrDefinition(BaseModel):
    """
    Either a full export or it's definition.
    """
    # data type: ResExportDefinition
    oneof_schema_1_validator: Optional[ResExportDefinition] = None
    # data type: ResExport
    oneof_schema_2_validator: Optional[ResExport] = None
    actual_instance: Optional[Union[ResExport, ResExportDefinition]] = None
    one_of_schemas: Set[str] = { "ResExport", "ResExportDefinition" }

    model_config = ConfigDict(
        validate_assignment=True,
        protected_namespaces=(),
    )


    def __init__(self, *args, **kwargs) -> None:
        if args:
            if len(args) > 1:
                raise ValueError("If a position argument is used, only 1 is allowed to set `actual_instance`")
            if kwargs:
                raise ValueError("If a position argument is used, keyword arguments cannot be used.")
            super().__init__(actual_instance=args[0])
        else:
            super().__init__(**kwargs)

    @field_validator('actual_instance')
    def actual_instance_must_validate_oneof(cls, v):
        instance = ResExportOrDefinition.model_construct()
        error_messages = []
        match = 0
        # validate data type: ResExportDefinition
        if not isinstance(v, ResExportDefinition):
            error_messages.append(f"Error! Input type `{type(v)}` is not `ResExportDefinition`")
        else:
            match += 1
        # validate data type: ResExport
        if not isinstance(v, ResExport):
            error_messages.append(f"Error! Input type `{type(v)}` is not `ResExport`")
        else:
            match += 1
        if match > 1:
            # more than 1 match
            raise ValueError("Multiple matches found when setting `actual_instance` in ResExportOrDefinition with oneOf schemas: ResExport, ResExportDefinition. Details: " + ", ".join(error_messages))
        elif match == 0:
            # no match
            raise ValueError("No match found when setting `actual_instance` in ResExportOrDefinition with oneOf schemas: ResExport, ResExportDefinition. Details: " + ", ".join(error_messages))
        else:
            return v

    @classmethod
    def from_dict(cls, obj: Union[str, Dict[str, Any]]) -> Self:
        return cls.from_json(json.dumps(obj))

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Returns the object represented by the json string"""
        instance = cls.model_construct()
        error_messages = []
        match = 0

        # deserialize data into ResExportDefinition
        try:
            instance.actual_instance = ResExportDefinition.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into ResExport
        try:
            instance.actual_instance = ResExport.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))

        if match > 1:
            # more than 1 match
            raise ValueError("Multiple matches found when deserializing the JSON string into ResExportOrDefinition with oneOf schemas: ResExport, ResExportDefinition. Details: " + ", ".join(error_messages))
        elif match == 0:
            # no match
            raise ValueError("No match found when deserializing the JSON string into ResExportOrDefinition with oneOf schemas: ResExport, ResExportDefinition. Details: " + ", ".join(error_messages))
        else:
            return instance

    def to_json(self) -> str:
        """Returns the JSON representation of the actual instance"""
        if self.actual_instance is None:
            return "null"

        if hasattr(self.actual_instance, "to_json") and callable(self.actual_instance.to_json):
            return self.actual_instance.to_json()
        else:
            return json.dumps(self.actual_instance)

    def to_dict(self) -> Optional[Union[Dict[str, Any], ResExport, ResExportDefinition]]:
        """Returns the dict representation of the actual instance"""
        if self.actual_instance is None:
            return None

        if hasattr(self.actual_instance, "to_dict") and callable(self.actual_instance.to_dict):
            return self.actual_instance.to_dict()
        else:
            # primitive type
            return self.actual_instance

    def to_str(self) -> str:
        """Returns the string representation of the actual instance"""
        return pprint.pformat(self.model_dump())



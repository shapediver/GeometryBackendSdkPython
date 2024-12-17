# coding: utf-8

"""
    Geometry Backend API v2

    The ShapeDiver Geometry Backend system is used to: * host Grasshopper models in a secure, reliable, scalable, and performant way, * run computations of Grasshopper models, * and cache and output the results of computations and exports.

    The version of the OpenAPI document: 1.8.1
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import json
import pprint
from pydantic import BaseModel, ConfigDict, Field, StrictStr, ValidationError, field_validator
from typing import Any, List, Optional
from shapediver.geometry_api_v2.client.models.res_model_credit_metric import ResModelCreditMetric
from shapediver.geometry_api_v2.client.models.res_model_organization_credit_metric import ResModelOrganizationCreditMetric
from shapediver.geometry_api_v2.client.models.res_model_user_credit_metric import ResModelUserCreditMetric
from shapediver.geometry_api_v2.client.models.res_organization_credit_metric import ResOrganizationCreditMetric
from shapediver.geometry_api_v2.client.models.res_system_credit_metric import ResSystemCreditMetric
from shapediver.geometry_api_v2.client.models.res_user_credit_metric import ResUserCreditMetric
from pydantic import StrictStr, Field
from typing import Union, List, Set, Optional, Dict
from typing_extensions import Literal, Self

RESANYCREDITMETRIC_ONE_OF_SCHEMAS = ["ResModelCreditMetric", "ResModelOrganizationCreditMetric", "ResModelUserCreditMetric", "ResOrganizationCreditMetric", "ResSystemCreditMetric", "ResUserCreditMetric"]

class ResAnyCreditMetric(BaseModel):
    """
    The ID of any type of credit metric.
    """
    # data type: ResModelCreditMetric
    oneof_schema_1_validator: Optional[ResModelCreditMetric] = None
    # data type: ResUserCreditMetric
    oneof_schema_2_validator: Optional[ResUserCreditMetric] = None
    # data type: ResOrganizationCreditMetric
    oneof_schema_3_validator: Optional[ResOrganizationCreditMetric] = None
    # data type: ResSystemCreditMetric
    oneof_schema_4_validator: Optional[ResSystemCreditMetric] = None
    # data type: ResModelUserCreditMetric
    oneof_schema_5_validator: Optional[ResModelUserCreditMetric] = None
    # data type: ResModelOrganizationCreditMetric
    oneof_schema_6_validator: Optional[ResModelOrganizationCreditMetric] = None
    actual_instance: Optional[Union[ResModelCreditMetric, ResModelOrganizationCreditMetric, ResModelUserCreditMetric, ResOrganizationCreditMetric, ResSystemCreditMetric, ResUserCreditMetric]] = None
    one_of_schemas: Set[str] = { "ResModelCreditMetric", "ResModelOrganizationCreditMetric", "ResModelUserCreditMetric", "ResOrganizationCreditMetric", "ResSystemCreditMetric", "ResUserCreditMetric" }

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
        instance = ResAnyCreditMetric.model_construct()
        error_messages = []
        match = 0
        # validate data type: ResModelCreditMetric
        if not isinstance(v, ResModelCreditMetric):
            error_messages.append(f"Error! Input type `{type(v)}` is not `ResModelCreditMetric`")
        else:
            match += 1
        # validate data type: ResUserCreditMetric
        if not isinstance(v, ResUserCreditMetric):
            error_messages.append(f"Error! Input type `{type(v)}` is not `ResUserCreditMetric`")
        else:
            match += 1
        # validate data type: ResOrganizationCreditMetric
        if not isinstance(v, ResOrganizationCreditMetric):
            error_messages.append(f"Error! Input type `{type(v)}` is not `ResOrganizationCreditMetric`")
        else:
            match += 1
        # validate data type: ResSystemCreditMetric
        if not isinstance(v, ResSystemCreditMetric):
            error_messages.append(f"Error! Input type `{type(v)}` is not `ResSystemCreditMetric`")
        else:
            match += 1
        # validate data type: ResModelUserCreditMetric
        if not isinstance(v, ResModelUserCreditMetric):
            error_messages.append(f"Error! Input type `{type(v)}` is not `ResModelUserCreditMetric`")
        else:
            match += 1
        # validate data type: ResModelOrganizationCreditMetric
        if not isinstance(v, ResModelOrganizationCreditMetric):
            error_messages.append(f"Error! Input type `{type(v)}` is not `ResModelOrganizationCreditMetric`")
        else:
            match += 1
        if match > 1:
            # more than 1 match
            raise ValueError("Multiple matches found when setting `actual_instance` in ResAnyCreditMetric with oneOf schemas: ResModelCreditMetric, ResModelOrganizationCreditMetric, ResModelUserCreditMetric, ResOrganizationCreditMetric, ResSystemCreditMetric, ResUserCreditMetric. Details: " + ", ".join(error_messages))
        elif match == 0:
            # no match
            raise ValueError("No match found when setting `actual_instance` in ResAnyCreditMetric with oneOf schemas: ResModelCreditMetric, ResModelOrganizationCreditMetric, ResModelUserCreditMetric, ResOrganizationCreditMetric, ResSystemCreditMetric, ResUserCreditMetric. Details: " + ", ".join(error_messages))
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

        # deserialize data into ResModelCreditMetric
        try:
            instance.actual_instance = ResModelCreditMetric.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into ResUserCreditMetric
        try:
            instance.actual_instance = ResUserCreditMetric.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into ResOrganizationCreditMetric
        try:
            instance.actual_instance = ResOrganizationCreditMetric.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into ResSystemCreditMetric
        try:
            instance.actual_instance = ResSystemCreditMetric.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into ResModelUserCreditMetric
        try:
            instance.actual_instance = ResModelUserCreditMetric.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into ResModelOrganizationCreditMetric
        try:
            instance.actual_instance = ResModelOrganizationCreditMetric.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))

        if match > 1:
            # more than 1 match
            raise ValueError("Multiple matches found when deserializing the JSON string into ResAnyCreditMetric with oneOf schemas: ResModelCreditMetric, ResModelOrganizationCreditMetric, ResModelUserCreditMetric, ResOrganizationCreditMetric, ResSystemCreditMetric, ResUserCreditMetric. Details: " + ", ".join(error_messages))
        elif match == 0:
            # no match
            raise ValueError("No match found when deserializing the JSON string into ResAnyCreditMetric with oneOf schemas: ResModelCreditMetric, ResModelOrganizationCreditMetric, ResModelUserCreditMetric, ResOrganizationCreditMetric, ResSystemCreditMetric, ResUserCreditMetric. Details: " + ", ".join(error_messages))
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

    def to_dict(self) -> Optional[Union[Dict[str, Any], ResModelCreditMetric, ResModelOrganizationCreditMetric, ResModelUserCreditMetric, ResOrganizationCreditMetric, ResSystemCreditMetric, ResUserCreditMetric]]:
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



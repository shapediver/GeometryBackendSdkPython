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
from shapediver.geometry_api_v2.client.models.req_model_credit_metric_id import ReqModelCreditMetricId
from shapediver.geometry_api_v2.client.models.req_model_organization_credit_metric_id import ReqModelOrganizationCreditMetricId
from shapediver.geometry_api_v2.client.models.req_model_user_credit_metric_id import ReqModelUserCreditMetricId
from shapediver.geometry_api_v2.client.models.req_organization_credit_metric_id import ReqOrganizationCreditMetricId
from shapediver.geometry_api_v2.client.models.req_system_credit_metric_id import ReqSystemCreditMetricId
from shapediver.geometry_api_v2.client.models.req_user_credit_metric_id import ReqUserCreditMetricId
from pydantic import StrictStr, Field
from typing import Union, List, Set, Optional, Dict
from typing_extensions import Literal, Self

REQANYCREDITMETRICID_ONE_OF_SCHEMAS = ["ReqModelCreditMetricId", "ReqModelOrganizationCreditMetricId", "ReqModelUserCreditMetricId", "ReqOrganizationCreditMetricId", "ReqSystemCreditMetricId", "ReqUserCreditMetricId"]

class ReqAnyCreditMetricId(BaseModel):
    """
    Either a single or multiple IDs. Multiple IDs are aggregated and result in a single credit metrics object.
    """
    # data type: ReqModelCreditMetricId
    oneof_schema_1_validator: Optional[ReqModelCreditMetricId] = None
    # data type: ReqUserCreditMetricId
    oneof_schema_2_validator: Optional[ReqUserCreditMetricId] = None
    # data type: ReqOrganizationCreditMetricId
    oneof_schema_3_validator: Optional[ReqOrganizationCreditMetricId] = None
    # data type: ReqSystemCreditMetricId
    oneof_schema_4_validator: Optional[ReqSystemCreditMetricId] = None
    # data type: ReqModelUserCreditMetricId
    oneof_schema_5_validator: Optional[ReqModelUserCreditMetricId] = None
    # data type: ReqModelOrganizationCreditMetricId
    oneof_schema_6_validator: Optional[ReqModelOrganizationCreditMetricId] = None
    actual_instance: Optional[Union[ReqModelCreditMetricId, ReqModelOrganizationCreditMetricId, ReqModelUserCreditMetricId, ReqOrganizationCreditMetricId, ReqSystemCreditMetricId, ReqUserCreditMetricId]] = None
    one_of_schemas: Set[str] = { "ReqModelCreditMetricId", "ReqModelOrganizationCreditMetricId", "ReqModelUserCreditMetricId", "ReqOrganizationCreditMetricId", "ReqSystemCreditMetricId", "ReqUserCreditMetricId" }

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
        instance = ReqAnyCreditMetricId.model_construct()
        error_messages = []
        match = 0
        # validate data type: ReqModelCreditMetricId
        if not isinstance(v, ReqModelCreditMetricId):
            error_messages.append(f"Error! Input type `{type(v)}` is not `ReqModelCreditMetricId`")
        else:
            match += 1
        # validate data type: ReqUserCreditMetricId
        if not isinstance(v, ReqUserCreditMetricId):
            error_messages.append(f"Error! Input type `{type(v)}` is not `ReqUserCreditMetricId`")
        else:
            match += 1
        # validate data type: ReqOrganizationCreditMetricId
        if not isinstance(v, ReqOrganizationCreditMetricId):
            error_messages.append(f"Error! Input type `{type(v)}` is not `ReqOrganizationCreditMetricId`")
        else:
            match += 1
        # validate data type: ReqSystemCreditMetricId
        if not isinstance(v, ReqSystemCreditMetricId):
            error_messages.append(f"Error! Input type `{type(v)}` is not `ReqSystemCreditMetricId`")
        else:
            match += 1
        # validate data type: ReqModelUserCreditMetricId
        if not isinstance(v, ReqModelUserCreditMetricId):
            error_messages.append(f"Error! Input type `{type(v)}` is not `ReqModelUserCreditMetricId`")
        else:
            match += 1
        # validate data type: ReqModelOrganizationCreditMetricId
        if not isinstance(v, ReqModelOrganizationCreditMetricId):
            error_messages.append(f"Error! Input type `{type(v)}` is not `ReqModelOrganizationCreditMetricId`")
        else:
            match += 1
        if match > 1:
            # more than 1 match
            raise ValueError("Multiple matches found when setting `actual_instance` in ReqAnyCreditMetricId with oneOf schemas: ReqModelCreditMetricId, ReqModelOrganizationCreditMetricId, ReqModelUserCreditMetricId, ReqOrganizationCreditMetricId, ReqSystemCreditMetricId, ReqUserCreditMetricId. Details: " + ", ".join(error_messages))
        elif match == 0:
            # no match
            raise ValueError("No match found when setting `actual_instance` in ReqAnyCreditMetricId with oneOf schemas: ReqModelCreditMetricId, ReqModelOrganizationCreditMetricId, ReqModelUserCreditMetricId, ReqOrganizationCreditMetricId, ReqSystemCreditMetricId, ReqUserCreditMetricId. Details: " + ", ".join(error_messages))
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

        # deserialize data into ReqModelCreditMetricId
        try:
            instance.actual_instance = ReqModelCreditMetricId.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into ReqUserCreditMetricId
        try:
            instance.actual_instance = ReqUserCreditMetricId.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into ReqOrganizationCreditMetricId
        try:
            instance.actual_instance = ReqOrganizationCreditMetricId.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into ReqSystemCreditMetricId
        try:
            instance.actual_instance = ReqSystemCreditMetricId.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into ReqModelUserCreditMetricId
        try:
            instance.actual_instance = ReqModelUserCreditMetricId.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into ReqModelOrganizationCreditMetricId
        try:
            instance.actual_instance = ReqModelOrganizationCreditMetricId.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))

        if match > 1:
            # more than 1 match
            raise ValueError("Multiple matches found when deserializing the JSON string into ReqAnyCreditMetricId with oneOf schemas: ReqModelCreditMetricId, ReqModelOrganizationCreditMetricId, ReqModelUserCreditMetricId, ReqOrganizationCreditMetricId, ReqSystemCreditMetricId, ReqUserCreditMetricId. Details: " + ", ".join(error_messages))
        elif match == 0:
            # no match
            raise ValueError("No match found when deserializing the JSON string into ReqAnyCreditMetricId with oneOf schemas: ReqModelCreditMetricId, ReqModelOrganizationCreditMetricId, ReqModelUserCreditMetricId, ReqOrganizationCreditMetricId, ReqSystemCreditMetricId, ReqUserCreditMetricId. Details: " + ", ".join(error_messages))
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

    def to_dict(self) -> Optional[Union[Dict[str, Any], ReqModelCreditMetricId, ReqModelOrganizationCreditMetricId, ReqModelUserCreditMetricId, ReqOrganizationCreditMetricId, ReqSystemCreditMetricId, ReqUserCreditMetricId]]:
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



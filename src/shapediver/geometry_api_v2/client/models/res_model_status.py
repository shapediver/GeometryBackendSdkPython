# coding: utf-8

"""
    Geometry Backend API v2

    The ShapeDiver Geometry Backend system is used to: * host Grasshopper models in a secure, reliable, scalable, and performant way, * run computations of Grasshopper models, * and cache and output the results of computations and exports.

    The version of the OpenAPI document: 2.13.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import json
from enum import Enum
from typing_extensions import Self


class ResModelStatus(str, Enum):
    """
    Status of the model.
    """

    """
    allowed enum values
    """
    UNKNOWN = 'unknown'
    NOT_UPLOADED = 'not_uploaded'
    UPLOADED = 'uploaded'
    PENDING = 'pending'
    CONFIRMED = 'confirmed'
    DENIED = 'denied'
    DELETED = 'deleted'

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of ResModelStatus from a JSON string"""
        return cls(json.loads(json_str))



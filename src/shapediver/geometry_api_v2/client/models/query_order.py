# coding: utf-8

"""
    Geometry Backend API v2

    The ShapeDiver Geometry Backend system is used to: * host Grasshopper models in a secure, reliable, scalable, and performant way, * run computations of Grasshopper models, * and cache and output the results of computations and exports.

    The version of the OpenAPI document: 1.8.2
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import json
from enum import Enum
from typing_extensions import Self


class QueryOrder(str, Enum):
    """
    Specifies the order of the results.
    """

    """
    allowed enum values
    """
    ASC = 'asc'
    DESC = 'desc'

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of QueryOrder from a JSON string"""
        return cls(json.loads(json_str))



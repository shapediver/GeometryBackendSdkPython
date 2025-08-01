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
from enum import Enum
from typing_extensions import Self


class QueryGltfConversion(str, Enum):
    """
    Conversion type of a glTF upoad: * `none`: no further processing of the file. * `usdz`: converts the glTF into the USDZ format. * `scene`: creates a temporary AR scene that holds both, a glTF and a USDZ file.
    """

    """
    allowed enum values
    """
    NONE = 'none'
    SCENE = 'scene'
    USDZ = 'usdz'

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of QueryGltfConversion from a JSON string"""
        return cls(json.loads(json_str))



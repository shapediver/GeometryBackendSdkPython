# coding: utf-8

"""
    Geometry Backend API v2

    The ShapeDiver Geometry Backend system is used to: * host Grasshopper models in a secure, reliable, scalable, and performant way, * run computations of Grasshopper models, * and cache and output the results of computations and exports.

    The version of the OpenAPI document: 1.7.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import json
from enum import Enum
from typing_extensions import Self


class QueryComputationStatus(str, Enum):
    """
    Filter by model computation status.
    """

    """
    allowed enum values
    """
    SUCCESS = 'success'
    TIMEOUT = 'timeout'
    CHECKCONFIRMED = 'checkconfirmed'
    CHECKDENIED = 'checkdenied'
    CHECKPENDING = 'checkpending'
    MAXCOMBINEDASSETSIZEEXCEEDED = 'maxcombinedassetsizeexceeded'
    MAXDBSIZEPEROUTPUTEXCEEDED = 'maxdbsizeperoutputexceeded'
    MAXPARTSPEROUTPUTEXCEEDED = 'maxpartsperoutputexceeded'
    MAXASSETPARTSPEROUTPUTEXCEEDED = 'maxassetpartsperoutputexceeded'
    MAXTRANSFORMATIONSPEROUTPUTEXCEEDED = 'maxtransformationsperoutputexceeded'
    MAXPARTSEXCEEDED = 'maxpartsexceeded'
    MAXASSETPARTSEXCEEDED = 'maxassetpartsexceeded'
    RECOVERABLEERROR = 'recoverableerror'
    UNRECOVERABLEERROR = 'unrecoverableerror'
    NOOUTPUTDATAFORDEFAULTPARAMETERVALUES = 'nooutputdatafordefaultparametervalues'
    MODELWITHOUTGEOMETRYOUTPUT = 'modelwithoutgeometryoutput'
    UNKNOWN = 'unknown'

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of QueryComputationStatus from a JSON string"""
        return cls(json.loads(json_str))



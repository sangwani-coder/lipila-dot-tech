# coding: utf-8

"""
    Payments V1

    To facilitate the capability for consumers to make a payment or refund to service providers.

    The version of the OpenAPI document: v1.0
    Contact: developer-support@mtn.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import json
from enum import Enum
from typing_extensions import Self


class TransactionTypeEnum(str, Enum):
    """
    The transaction type that is associated with the payment transaction.
    """

    """
    allowed enum values
    """
    PAYMENT = 'Payment'
    DEBIT = 'Debit'
    TRANSFER = 'Transfer'
    REFUND = 'Refund'

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of TransactionTypeEnum from a JSON string"""
        return cls(json.loads(json_str))



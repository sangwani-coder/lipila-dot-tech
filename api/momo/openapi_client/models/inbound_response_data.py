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
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from openapi_client.models.fee_elements import FeeElements
from typing import Optional, Set
from typing_extensions import Self

class InboundResponseData(BaseModel):
    """
    InboundResponseData
    """ # noqa: E501
    status_code: Optional[StrictStr] = Field(default=None, description="message", alias="statusCode")
    provider_transaction_id: Optional[StrictStr] = Field(default=None, alias="providerTransactionId")
    status_message: Optional[StrictStr] = Field(default=None, alias="statusMessage")
    fee_details: Optional[List[FeeElements]] = Field(default=None, alias="feeDetails")
    __properties: ClassVar[List[str]] = ["statusCode", "providerTransactionId", "statusMessage", "feeDetails"]

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
        """Create an instance of InboundResponseData from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in fee_details (list)
        _items = []
        if self.fee_details:
            for _item_fee_details in self.fee_details:
                if _item_fee_details:
                    _items.append(_item_fee_details.to_dict())
            _dict['feeDetails'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of InboundResponseData from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "statusCode": obj.get("statusCode"),
            "providerTransactionId": obj.get("providerTransactionId"),
            "statusMessage": obj.get("statusMessage"),
            "feeDetails": [FeeElements.from_dict(_item) for _item in obj["feeDetails"]] if obj.get("feeDetails") is not None else None
        })
        return _obj



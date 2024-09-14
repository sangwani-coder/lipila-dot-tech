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
from openapi_client.models.additional_information import AdditionalInformation
from openapi_client.models.loyalty_balances import LoyaltyBalances
from openapi_client.models.money_type import MoneyType
from typing import Optional, Set
from typing_extensions import Self

class Data(BaseModel):
    """
    Data
    """ # noqa: E501
    approval_id: Optional[StrictStr] = Field(default=None, description="Unique identifier in the client for the payment in case it is needed to correlate. Generated by back-end system. This can be blank if the payment has previously been pre-approved.", alias="approvalId")
    transaction_fee: Optional[MoneyType] = Field(default=None, alias="transactionFee")
    discount: Optional[MoneyType] = None
    new_balance: Optional[MoneyType] = Field(default=None, alias="newBalance")
    payer_note: Optional[StrictStr] = Field(default=None, description="A descriptive note for sender transaction history.", alias="payerNote")
    status: Optional[StrictStr] = Field(default=None, description="Status of the payment method.")
    correlator_id: Optional[StrictStr] = Field(default=None, description="Unique identifier in the client for the payment in case it is needed to correlate.", alias="correlatorId")
    status_date: Optional[StrictStr] = Field(default=None, description="Time the status of the payment changed.", alias="statusDate")
    additional_information: Optional[AdditionalInformation] = Field(default=None, alias="additionalInformation")
    meta_data: Optional[List[AdditionalInformation]] = Field(default=None, description="An array of additional information related to the payment", alias="metaData")
    loyalty_information: Optional[LoyaltyBalances] = Field(default=None, alias="loyaltyInformation")
    external_code: Optional[StrictStr] = Field(default=None, description="This is the external reference code. This can be the bank institution code for the NIMBS payments usecases", alias="externalCode")
    __properties: ClassVar[List[str]] = ["approvalId", "transactionFee", "discount", "newBalance", "payerNote", "status", "correlatorId", "statusDate", "additionalInformation", "metaData", "loyaltyInformation", "externalCode"]

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
        """Create an instance of Data from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of transaction_fee
        if self.transaction_fee:
            _dict['transactionFee'] = self.transaction_fee.to_dict()
        # override the default output from pydantic by calling `to_dict()` of discount
        if self.discount:
            _dict['discount'] = self.discount.to_dict()
        # override the default output from pydantic by calling `to_dict()` of new_balance
        if self.new_balance:
            _dict['newBalance'] = self.new_balance.to_dict()
        # override the default output from pydantic by calling `to_dict()` of additional_information
        if self.additional_information:
            _dict['additionalInformation'] = self.additional_information.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in meta_data (list)
        _items = []
        if self.meta_data:
            for _item_meta_data in self.meta_data:
                if _item_meta_data:
                    _items.append(_item_meta_data.to_dict())
            _dict['metaData'] = _items
        # override the default output from pydantic by calling `to_dict()` of loyalty_information
        if self.loyalty_information:
            _dict['loyaltyInformation'] = self.loyalty_information.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of Data from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "approvalId": obj.get("approvalId"),
            "transactionFee": MoneyType.from_dict(obj["transactionFee"]) if obj.get("transactionFee") is not None else None,
            "discount": MoneyType.from_dict(obj["discount"]) if obj.get("discount") is not None else None,
            "newBalance": MoneyType.from_dict(obj["newBalance"]) if obj.get("newBalance") is not None else None,
            "payerNote": obj.get("payerNote"),
            "status": obj.get("status"),
            "correlatorId": obj.get("correlatorId"),
            "statusDate": obj.get("statusDate"),
            "additionalInformation": AdditionalInformation.from_dict(obj["additionalInformation"]) if obj.get("additionalInformation") is not None else None,
            "metaData": [AdditionalInformation.from_dict(_item) for _item in obj["metaData"]] if obj.get("metaData") is not None else None,
            "loyaltyInformation": LoyaltyBalances.from_dict(obj["loyaltyInformation"]) if obj.get("loyaltyInformation") is not None else None,
            "externalCode": obj.get("externalCode")
        })
        return _obj



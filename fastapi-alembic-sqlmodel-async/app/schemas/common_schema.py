from typing import Generic, List, Optional, TypeVar
from pydantic.generics import GenericModel
from pydantic import BaseModel
from app.schemas.role_schema import IRoleRead
from enum import Enum

DataType = TypeVar("DataType")

# In order to declare a generic model, you perform the following steps:
#   - Declare one or more typing.TypeVar instances to use to parameterize your model.
#   - Declare a pydantic model that inherits from pydantic.generics.GenericModel and typing.Generic,
#   where you pass the TypeVar instances as parameters to typing.Generic.
#   - Use the TypeVar instances as annotations where you will want to replace them with other types
#   or pydantic models.
# ref: https://pydantic-docs.helpmanual.io/usage/models/#generic-models
class IResponseBase(GenericModel, Generic[DataType]):
    message: str = ""
    meta: dict = {}
    data: Optional[DataType] = None

# To inherit from a GenericModel without replacing the TypeVar instance,
# a class must also inherit from typing.Generic
# ref: https://pydantic-docs.helpmanual.io/usage/models/#generic-models
class IGetResponseBase(IResponseBase[DataType], Generic[DataType]):
    message: str = "Data got correctly"

class IPostResponseBase(IResponseBase[DataType], Generic[DataType]):
    message: str = "Data created correctly"

class IPutResponseBase(IResponseBase[DataType], Generic[DataType]):
    message: str = "Data updated correctly"

class IDeleteResponseBase(IResponseBase[DataType], Generic[DataType]):
    message: str = "Data deleted correctly"

class IMetaGeneral(BaseModel):
    roles: List[IRoleRead]

class IOrderEnum(str, Enum):
    ascendent = 'ascendent'
    descendent = 'descendent'
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class QuadraticRequest(_message.Message):
    __slots__ = ("a", "b", "c")
    A_FIELD_NUMBER: _ClassVar[int]
    B_FIELD_NUMBER: _ClassVar[int]
    C_FIELD_NUMBER: _ClassVar[int]
    a: float
    b: float
    c: float
    def __init__(self, a: _Optional[float] = ..., b: _Optional[float] = ..., c: _Optional[float] = ...) -> None: ...

class Solution(_message.Message):
    __slots__ = ("solution",)
    SOLUTION_FIELD_NUMBER: _ClassVar[int]
    solution: str
    def __init__(self, solution: _Optional[str] = ...) -> None: ...

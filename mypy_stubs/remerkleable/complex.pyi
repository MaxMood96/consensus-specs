from collections.abc import Sequence as ColSequence
from remerkleable.basic import uint256 as uint256, uint32 as uint32, uint8 as uint8
from remerkleable.core import BasicTypeDef as BasicTypeDef, BasicView as BasicView, OFFSET_BYTE_LENGTH as OFFSET_BYTE_LENGTH, View as View, ViewHook as ViewHook
from remerkleable.subtree import SubtreeView as SubtreeView
from remerkleable.tree import Gindex as Gindex, NavigationError as NavigationError, Node as Node, PairNode as PairNode, get_depth as get_depth, subtree_fill_to_contents as subtree_fill_to_contents, subtree_fill_to_length as subtree_fill_to_length, to_gindex as to_gindex, zero_node as zero_node
from typing import Any, BinaryIO, Dict, List as PyList, NamedTuple, Optional, Type, TypeVar

V = TypeVar('V', bound=View)

def decode_offset(stream: BinaryIO) -> uint32: ...
def encode_offset(stream: BinaryIO, offset: int) -> Any: ...

class ComplexView(SubtreeView):
    def encode_bytes(self) -> bytes: ...
    @classmethod
    def decode_bytes(cls: Type[V], bytez: bytes) -> V: ...

class MonoSubtreeView(ColSequence, ComplexView):
    def length(self) -> int: ...
    @classmethod
    def coerce_view(cls: Type[V], v: Any) -> V: ...
    @classmethod
    def element_cls(cls: Any) -> Type[View]: ...
    @classmethod
    def item_elem_cls(cls: Any, i: int) -> Type[View]: ...
    @classmethod
    def to_chunk_length(cls: Any, elems_length: int) -> int: ...
    @classmethod
    def views_into_chunks(cls: Any, views: PyList[View]) -> PyList[Node]: ...
    @classmethod
    def is_valid_count(cls: Any, count: int) -> bool: ...
    def __iter__(self) -> Any: ...
    def readonly_iter(self): ...
    @classmethod
    def deserialize(cls: Type[V], stream: BinaryIO, scope: int) -> V: ...
    def serialize(self, stream: BinaryIO) -> int: ...
    @classmethod
    def navigate_type(cls: Any, key: Any) -> Type[View]: ...
    @classmethod
    def key_to_static_gindex(cls: Any, key: Any) -> Gindex: ...
    def navigate_view(self, key: Any) -> View: ...
    def __len__(self): ...
    def __add__(self, other: Any): ...
    def __getitem__(self, k: Any): ...
    def __setitem__(self, k: Any, v: Any) -> None: ...

class List(MonoSubtreeView):
    def __new__(cls: Any, *args: Any, backing: Optional[Node]=..., hook: Optional[ViewHook]=..., **kwargs: Any) -> Any: ...
    def __class_getitem__(cls: Any, params: Any) -> Type[List]: ...
    def length(self) -> int: ...
    def value_byte_length(self) -> int: ...
    def append(self, v: View) -> Any: ...
    def pop(self) -> None: ...
    def get(self, i: int) -> View: ...
    def set(self, i: int, v: View) -> None: ...
    @classmethod
    def type_repr(cls: Any) -> str: ...
    @classmethod
    def is_packed(cls: Any) -> bool: ...
    @classmethod
    def contents_depth(cls: Any) -> int: ...
    @classmethod
    def tree_depth(cls: Any) -> int: ...
    @classmethod
    def item_elem_cls(cls: Any, i: int) -> Type[V]: ...
    @classmethod
    def limit(cls: Any) -> int: ...
    @classmethod
    def is_valid_count(cls: Any, count: int) -> bool: ...
    @classmethod
    def navigate_type(cls: Any, key: Any) -> Type[View]: ...
    @classmethod
    def key_to_static_gindex(cls: Any, key: Any) -> Gindex: ...
    @classmethod
    def default_node(cls: Any) -> Node: ...
    @classmethod
    def is_fixed_byte_length(cls: Any) -> bool: ...
    @classmethod
    def min_byte_length(cls: Any) -> int: ...
    @classmethod
    def max_byte_length(cls: Any) -> int: ...

class Vector(MonoSubtreeView):
    def __new__(cls: Any, *args: Any, backing: Optional[Node]=..., hook: Optional[ViewHook]=..., **kwargs: Any) -> Any: ...
    def __class_getitem__(cls: Any, params: Any) -> Type[Vector]: ...
    def get(self, i: int) -> View: ...
    def set(self, i: int, v: View) -> None: ...
    def length(self) -> int: ...
    def value_byte_length(self) -> int: ...
    @classmethod
    def type_repr(cls: Any) -> str: ...
    @classmethod
    def vector_length(cls: Any) -> int: ...
    @classmethod
    def is_valid_count(cls: Any, count: int) -> bool: ...
    @classmethod
    def navigate_type(cls: Any, key: Any) -> Type[View]: ...
    @classmethod
    def key_to_static_gindex(cls: Any, key: Any) -> Gindex: ...
    @classmethod
    def default_node(cls: Any) -> Node: ...
    @classmethod
    def is_fixed_byte_length(cls: Any) -> bool: ...
    @classmethod
    def min_byte_length(cls: Any) -> int: ...
    @classmethod
    def max_byte_length(cls: Any) -> int: ...
Fields = Dict[str, Type[View]]

class FieldOffset(NamedTuple):
    key: str
    typ: Type[View]
    offset: int

class _ContainerLike:
    @classmethod
    def fields(cls: Any) -> Fields: ...

class Container(ComplexView):
    def __new__(cls: Any, *args: Any, backing: Optional[Node]=..., hook: Optional[ViewHook]=..., **kwargs: Any) -> Any: ...
    @classmethod
    def coerce_view(cls: Type[V], v: Any) -> V: ...
    @classmethod
    def fields(cls: Any) -> Fields: ...
    @classmethod
    def is_fixed_byte_length(cls: Any) -> bool: ...
    @classmethod
    def type_byte_length(cls: Any) -> int: ...
    @classmethod
    def min_byte_length(cls: Any) -> int: ...
    @classmethod
    def max_byte_length(cls: Any) -> int: ...
    @classmethod
    def is_packed(cls: Any) -> bool: ...
    @classmethod
    def tree_depth(cls: Any) -> int: ...
    @classmethod
    def item_elem_cls(cls: Any, i: int) -> Type[View]: ...
    @classmethod
    def default_node(cls: Any) -> Node: ...
    def value_byte_length(self) -> int: ...
    def __getattr__(self, item: Any): ...
    def __setattr__(self, key: Any, value: Any) -> None: ...
    @classmethod
    def type_repr(cls: Any) -> str: ...
    @classmethod
    def decode_bytes(cls: Type[V], bytez: bytes) -> V: ...
    @classmethod
    def deserialize(cls: Type[V], stream: BinaryIO, scope: int) -> V: ...
    def serialize(self, stream: BinaryIO) -> int: ...
    @classmethod
    def key_to_static_gindex(cls: Any, key: Any) -> Gindex: ...
    @classmethod
    def navigate_type(cls: Any, key: Any) -> Type[View]: ...
    def navigate_view(self, key: Any) -> View: ...
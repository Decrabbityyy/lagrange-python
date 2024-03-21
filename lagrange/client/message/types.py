from typing import TypeVar, TYPE_CHECKING

if TYPE_CHECKING:
    from .elems import Text, At, AtAll, Image, Emoji, Json, Quote, Raw, Audio, Poke

T = TypeVar(
    "T",
    "Text",
    "AtAll",
    "At",
    "Image",
    "Emoji",
    "Json",
    "Quote",
    "Raw",
    "Audio",
    "Poke",
)

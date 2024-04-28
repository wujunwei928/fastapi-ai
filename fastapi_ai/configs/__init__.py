from enum import Enum


class OpenAiWhisperModelSize(Enum):
    # Multilingual models
    TINY = "tiny"
    BASE = "base"
    SMALL = "small"
    MEDIUM = "medium"
    LARGE = "large"
    LARGE_V2 = "large-v2"
    LARGE_V3 = "large-v3"

    # English-only models
    TINY_ENGLISH = "tiny.en"
    BASE_ENGLISH = "base.en"
    SMALL_ENGLISH = "small.en"
    MEDIUM_ENGLISH = "medium.en"

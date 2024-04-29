from enum import Enum


class OpenAiWhisperModelSize(Enum):
    # Multilingual models
    TINY = "tiny"
    BASE = "base"
    SMALL = "small"
    MEDIUM = "medium"
    LARGE = "large"  # 目前是 LARGE_V3:
    LARGE_V1 = "large-v1"
    LARGE_V2 = "large-v2"
    LARGE_V3 = "large-v3"

    # English-only models
    TINY_ENGLISH = "tiny.en"
    BASE_ENGLISH = "base.en"
    SMALL_ENGLISH = "small.en"
    MEDIUM_ENGLISH = "medium.en"

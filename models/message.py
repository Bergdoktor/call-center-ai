from datetime import datetime
from enum import Enum
from pydantic import BaseModel, Field
from typing import List


class StyleEnum(str, Enum):
    """
    Voice styles the Azure AI Speech Service supports.

    Doc:
    - Speaking styles: https://learn.microsoft.com/en-us/azure/ai-services/speech-service/speech-synthesis-markup-voice#use-speaking-styles-and-roles
    - Support by language: https://learn.microsoft.com/en-us/azure/ai-services/speech-service/language-support?tabs=tts#voice-styles-and-roles
    """

    CHEERFUL = "cheerful"
    NONE = "none"  # This is not a valid style, but we use it in the code to indicate no style
    SAD = "sad"


class ActionEnum(str, Enum):
    CALL = "call"
    HANGUP = "hangup"
    SMS = "sms"
    TALK = "talk"


class PersonaEnum(str, Enum):
    ASSISTANT = "assistant"
    HUMAN = "human"
    TOOL = "tool"


class ToolModel(BaseModel):
    content: str
    function_arguments: str
    function_name: str
    tool_id: str


class MessageModel(BaseModel):
    # Immutable fields
    created_at: datetime = Field(default_factory=datetime.utcnow, frozen=True)
    # Editable fields
    action: ActionEnum = ActionEnum.TALK
    content: str
    persona: PersonaEnum
    style: StyleEnum = StyleEnum.NONE
    tool_calls: List[ToolModel] = []

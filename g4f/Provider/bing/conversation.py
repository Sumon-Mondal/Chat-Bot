from __future__ import annotations

from aiohttp import ClientSession
from ...requests import raise_for_status

class Conversation:
    """
    Represents a conversation with specific attributes.
    """
    def __init__(self, conversationId: str, clientId: str, conversationSignature: str) -> None:
        """
        Initialize a new conversation instance.

        Args:
        conversationId (str): Unique identifier for the conversation.
        clientId (str): Client identifier.
        conversationSignature (str): Signature for the conversation.
        """
        self.conversationId = conversationId
        self.clientId = clientId
        self.conversationSignature = conversationSignature

async def create_conversation(session: ClientSession, headers: dict) -> Conversation:
    """
    Create a new conversation asynchronously.

    Args:
    session (ClientSession): An instance of aiohttp's ClientSession.
    proxy (str, optional): Proxy URL. Defaults to None.

    Returns:
    Conversation: An instance representing the created conversation.
    """
    url = "https://www.bing.com/turing/conversation/create?bundleVersion=1.1626.1"
    async with session.get(url, headers=headers) as response:
        await raise_for_status(response, "Failed to create conversation")
        data = await response.json()
    conversationId = data.get('conversationId')
    clientId = data.get('clientId')
    conversationSignature = response.headers.get('X-Sydney-Encryptedconversationsignature')
    if not conversationId or not clientId or not conversationSignature:
        raise RuntimeError('Empty fields: Failed to create conversation')
    return Conversation(conversationId, clientId, conversationSignature)
        
async def list_conversations(session: ClientSession) -> list:
    """
    List all conversations asynchronously.

    Args:
    session (ClientSession): An instance of aiohttp's ClientSession.

    Returns:
    list: A list of conversations.
    """
    url = "https://www.bing.com/turing/conversation/chats"
    async with session.get(url) as response:
        response = await response.json()
        return response["chats"]

async def delete_conversation(session: ClientSession, conversation: Conversation, headers: dict) -> bool:
    """
    Delete a conversation asynchronously.

    Args:
    session (ClientSession): An instance of aiohttp's ClientSession.
    conversation (Conversation): The conversation to delete.
    proxy (str, optional): Proxy URL. Defaults to None.

    Returns:
    bool: True if deletion was successful, False otherwise.
    """
    url = "https://sydney.bing.com/sydney/DeleteSingleConversation"
    json = {
        "conversationId": conversation.conversationId,
        "conversationSignature": conversation.conversationSignature,
        "participant": {"id": conversation.clientId},
        "source": "cib",
        "optionsSets": ["autosave"]
    }
    try:
        async with session.post(url, json=json, headers=headers) as response:
            response = await response.json()
            return response["result"]["value"] == "Success"
    except:
        return False
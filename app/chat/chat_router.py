from typing import List

from fastapi import APIRouter, WebSocket, WebSocketDisconnect, Depends

from schemas import SMessages
from service import ChatService
from ws_manager import manager

router = APIRouter(
    prefix="/chat",
    tags=["Chat"]
)


@router.get("/last_messages")
async def get_last_messages():
    return await ChatService.get_last_messages()


@router.websocket("/ws/{client_id}")
async def websocket_endpoint(websocket: WebSocket, client_id: int):
    await manager.connect(websocket)
    try:
        while True:
            data = await websocket.receive_text()
            await manager.broadcast(f"Client #{client_id} says: {data}", add_to_db=True)
    except WebSocketDisconnect:
        manager.disconnect(websocket)
        await manager.broadcast(f"Client #{client_id} left the chat", add_to_db=False)

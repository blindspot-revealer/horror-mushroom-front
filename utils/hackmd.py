import os
import httpx
from typing import Optional

HACKMD_API_BASE = "https://api.hackmd.io/v1"

class HackMDClient:
    def __init__(self, token: Optional[str] = None):
        self.token = token or os.getenv("HACKMD_API_TOKEN").strip(" \"'\n\r")
        self.headers = {
            "Authorization": f"Bearer {self.token}",
            "Content-Type": "application/json"
        }

    async def read_note(self, note_id: str) -> str:
        """讀取指定 HackMD 筆記內容"""
        if not note_id:
            return ""
        async with httpx.AsyncClient() as client:
            resp = await client.get(f"{HACKMD_API_BASE}/notes/{note_id}", headers=self.headers)
            if resp.status_code == 200:
                return resp.json().get("content", "")
            return ""

    async def update_note(self, note_id: str, content: str) -> bool:
        """覆寫指定 HackMD 筆記內容"""
        if not note_id:
            return False
        async with httpx.AsyncClient() as client:
            resp = await client.patch(
                f"{HACKMD_API_BASE}/notes/{note_id}",
                headers=self.headers,
                json={"content": content}
            )
            return resp.status_code in [200, 202]
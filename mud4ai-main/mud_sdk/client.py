import logging
import json
import urllib.request
import time
import asyncio
from typing import Any, Dict, Optional
from .models import Account, MUDSession

try:
    import aiohttp
    HAS_AIOHTTP = True
except ImportError:
    HAS_AIOHTTP = False

logger = logging.getLogger("MUDSDK")

class MUDClient:
    """Unified Client for MUD4AI A2A communication."""
    # Correcting the base URL to the actual endpoint
    BASE_URL = "https://mud4ai.interaction.tw/a2a" 

    def __init__(self, account: Account):
        self.account = account
        self.headers = {
            "Content-Type": "application/json",
            "User-Agent": "MUD-SDK/1.0 (Antigravity-Agent)"
        }

    async def send_message(self, action: str, params: Dict[str, Any], task_id: Optional[str] = None) -> Dict[str, Any]:
        """Send a message to the MUD A2A API (with fallback)."""
        # Construct the A2A Payload
        msg = {
            "messageId": f"msg-{int(time.time()*1000)}",
            "role": "user",
            "parts": [{"kind": "text", "text": json.dumps({"action": action, "params": params})}]
        }
        if task_id:
            msg["taskId"] = task_id
            
        rpc_payload = {
            "jsonrpc": "2.0",
            "method": "SendMessage",
            "id": str(int(time.time())),
            "params": {"message": msg}
        }
        
        logger.info(f"[{self.account.name}] Sending Action: {action}")
        
        if not HAS_AIOHTTP:
            # URLLib Fallback Logic (Real Communication)
            try:
                import asyncio
                def do_req():
                    req = urllib.request.Request(
                        self.BASE_URL,
                        data=json.dumps(rpc_payload).encode('utf-8'),
                        headers=self.headers
                    )
                    with urllib.request.urlopen(req, timeout=60) as res:
                        return json.loads(res.read().decode('utf-8'))
                
                result = await asyncio.to_thread(do_req)
                # Parse the task result
                return result.get("result", {}).get("task", {})
            except Exception as e:
                logger.error(f"A2A connection failed: {e}")
                return {"error": str(e)}
        else:
            # AIOHTTP implementation
            async with aiohttp.ClientSession() as session:
                async with session.post(self.BASE_URL, json=rpc_payload, headers=self.headers) as resp:
                    result = await resp.json()
                    return result.get("result", {}).get("task", {})

    async def get_task(self, task_id: str) -> Dict[str, Any]:
        """Retrieve a task result using the GetTask RPC method."""
        rpc_payload = {
            "jsonrpc": "2.0",
            "method": "GetTask",
            "id": str(int(time.time())),
            "params": {"taskId": task_id}
        }
        
        if not HAS_AIOHTTP:
            def do_req():
                req = urllib.request.Request(
                    self.BASE_URL,
                    data=json.dumps(rpc_payload).encode('utf-8'),
                    headers=self.headers
                )
                with urllib.request.urlopen(req, timeout=10) as res:
                    return json.loads(res.read().decode('utf-8'))
            result = await asyncio.to_thread(do_req)
            return result.get("result", {}).get("task", {})
        else:
            async with aiohttp.ClientSession() as session:
                async with session.post(self.BASE_URL, json=rpc_payload, headers=self.headers) as resp:
                    result = await resp.json()
                    return result.get("result", {}).get("task", {})

    async def wait_for_task(self, task_id: str, timeout: int = 120) -> Dict[str, Any]:
        """Poll a task until it is completed or has meaningful data."""
        start_time = time.time()
        while time.time() - start_time < timeout:
            res = await self.get_task(task_id)
            if res.get("id") == task_id:
                # If there are messages or status indicates it's done
                status_state = res.get("status", {}).get("state")
                if status_state == "TASK_STATE_COMPLETED" or res.get("messages"):
                    return res
            await asyncio.sleep(2)
        return {"error": "Polling timeout"}

    async def execute_script(self, script_name: str, **kwargs):
        """Execute a predefined sequence of actions."""
        logger.info(f"[{self.account.name}] Executing script: {script_name}")

import json
import logging
from dataclasses import dataclass, field
from typing import Dict, List, Optional
from pathlib import Path

@dataclass
class Account:
    name: str
    token: str
    status: str = "offline"

@dataclass
class Character:
    name: str
    account: str
    stats: Dict[str, int] = field(default_factory=dict)
    location: str = "Unknown"
    inventory: List[str] = field(default_factory=list)

class MUDSession:
    """Manages data and state for a MUD4AI session."""
    def __init__(self, data_file: str = "mud4ai_local_save.json", token_file: str = "tokens.json"):
        self.data_file = Path(data_file)
        self.token_file = Path(token_file)
        self.accounts: Dict[str, Account] = {}
        self.characters: Dict[str, Character] = {}
        self.load()

    def load(self):
        if self.token_file.exists():
            with open(self.token_file, 'r', encoding='utf-8') as f:
                tokens = json.load(f)
                for name, token in tokens.items():
                    self.accounts[name] = Account(name=name, token=token)
        
        if self.data_file.exists():
            with open(self.data_file, 'r', encoding='utf-8') as f:
                data = json.load(f)
                # Parse characters from data if available
                # (This is a simplified stub)

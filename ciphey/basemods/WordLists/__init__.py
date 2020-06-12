from typing import Optional, Dict, Any

import ciphey
import cipheydists

from ciphey.iface import T

for i in ["english", "english1000"]:
    class CipheyDistsTmpList(ciphey.iface.WordList[str]):
        @staticmethod
        def getName() -> str:
            return f"cipheydists::{i}"

        @staticmethod
        def getArgs() -> Optional[Dict[str, Dict[str, Any]]]:
            return None

        def get_wordlist(self) -> T:
            return cipheydists.get_list(i)

        def __init__(self, config: Dict[str, object]):
            super().__init__(config)

    ciphey.iface.registry.register(CipheyDistsTmpList, ciphey.iface.WordList[str])

class Json:
    @staticmethod
    def getName() -> str:
        return "json"

    @staticmethod
    def getArgs() -> Optional[Dict[str, Dict[str, Any]]]:
        return None

    def get_wordlist(self) -> T:
        return cipheydists.get_list(i)

    def __init__(self, config: Dict[str, object]):
        super().__init__(config)
from typing import Optional, Dict, Any

import ciphey
import cipheydists

from ciphey.iface import T, id_lambda

for i in ["english", "english1000"]:
    t = type(i, (ciphey.iface.WordList,), {
        "get_wordlist": lambda self: cipheydists.get_list(i),
        "getArgs": id_lambda(None),
        "getName": id_lambda(f"cipheydists::{i}"),
        "__init__": lambda self, config: super(type(self), self).__init__(config)
    })

    ciphey.iface.registry.register(t, ciphey.iface.WordList[str])

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
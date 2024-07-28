from typing import Dict, Set
from BaseClasses import Region


class LWNRegion(Region):
    game: str = "Little Witch Nobeta"


lwn_regions: Dict[str, Set[str]] = {
    "Menu": {"Shrine - Start"},
    "Shrine - Start": {"Shrine - Armor Hall"},
    "Shrine - Armor Hall": {"Shrine - Secret Passage", "Underground - Start"},
    "Shrine - Secret Passage": {"Dark Tunnel - Start"},
    "Underground - Start": {"Underground - Tania"},
    "Underground - Tania": {"Shrine - Start", "Lava Ruins - Start"},
    "Lava Ruins - Start": {"Lava Ruins - After Fire Barrier"},
    "Lava Ruins - After Fire Barrier": {"Underground - Start", "Dark Tunnel - Start"},
    "Dark Tunnel - Start": {"Dark Tunnel - After Thunder"},
    "Dark Tunnel - After Thunder": {"Shrine - Start", "Spirit Realm - Start"},
    "Spirit Realm - Start": {"Spirit Realm - After Arcane Barrier"},
    "Spirit Realm - After Arcane Barrier": {"Spirit Realm - After Teleport"},
    "Spirit Realm - After Teleport": {"Abyss"},
    "Abyss": {"Abyss Trials"},
    "Abyss Trials": set(),
}

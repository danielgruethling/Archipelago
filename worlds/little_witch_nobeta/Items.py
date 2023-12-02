from typing import Dict

base_id = 345600000

attack_magics: Dict[str, int] = {
    "Arcane": base_id,
    "Ice": base_id + 1,
    "Fire": base_id + 2,
    "Thunder": base_id + 3,
}

useful_items: Dict[str, int] = {
    "Wind": base_id + 4,
    "Mana Absorption": base_id + 5,
    "Progressive Bag Upgrade": base_id + 6,
}

boss_souls: Dict[str, int] = {
    "Specter Armor Soul": base_id + 7,
    "Tania Soul": base_id + 8,
    "Monica Soul": base_id + 9,
    "Enraged Armor Soul": base_id + 10,
    "Vanessa Soul": base_id + 11,
    "Queen Vanessa V2 Soul": base_id + 12,
}

filler_items: Dict[str, int] = {
    "HPCure": base_id + 13,
    "HPCureMiddle": base_id + 14,
    "HPCureBig": base_id + 15,
    "MPCure": base_id + 16,
    "MPCureMiddle": base_id + 17,
    "MPCureBig": base_id + 18,
    "Defense": base_id + 19,
    "DefenseMiddle": base_id + 20,
    "DefenseBig": base_id + 21,
    "Souls": base_id + 22,
}

lwn_items: Dict[str, int] = {
    **attack_magics,
    **useful_items,
    **boss_souls,
    **filler_items,
    "Teleport": base_id + 23,
}

lookup_id_to_name: Dict[int, str] = {id: name for name, id in lwn_items.items()}

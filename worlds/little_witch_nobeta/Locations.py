from typing import Dict

base_id = 345600000

shrine_start_locations: Dict[str, int] = {
    #"Shrine - Chest Room03_01": base_id,
    #"Shrine - Chest Room03_02": base_id + 1,
    "TreasureBox_Room03": base_id,
    "TreasureBox02_Room03": base_id + 1,
}

shrine_armor_locations: Dict[str, int] = {
    "Shrine - Chest Room05": base_id + 2,
    "Shrine - Specter Armor": base_id + 3,
}

shrine_secret_passage_locations: Dict[str, int] = {
    "Secret Passage - Chest Room07": base_id + 4,
    "Secret Passage - Chest Room07To08": base_id + 5,
    "Secret Passage - Chest Room08": base_id + 6,
    "Secret Passage - Chest Room09": base_id + 7,
    "Secret Passage - Chest Room10": base_id + 8,
    "Secret Passage - Enraged Armor": base_id + 9,
}

underground_start_locations: Dict[str, int] = {
    "Underground - Chest Room01": base_id + 10,
    "Underground - Chest Room03": base_id + 11,
    "Underground - Chest Room04": base_id + 12,
    "Underground - Chest Room05_01": base_id + 13,
    "Underground - Chest Room05_02": base_id + 14,
    "Underground - Cat": base_id + 15,
}

underground_tania_locations: Dict[str, int] = {
    "Underground - Chest Room08": base_id + 16,
    "Underground - Tania": base_id + 17,
}

lava_ruins_start_locations: Dict[str, int] = {
    "Lava Ruins - Chest Room02_01": base_id + 18,
    "Lava Ruins - Chest Room02_02": base_id + 19,
    "Lava Ruins - Chest Room03_01": base_id + 20,
    "Lava Ruins - Chest Room03_02": base_id + 21,
    "Lava Ruins - Chest Room02To04": base_id + 22,
    "Lava Ruins - Chest Room05To06": base_id + 23,
    "Lava Ruins - Chest Room06": base_id + 24,
}

lava_ruins_after_fire_barrier_locations: Dict[str, int] = {
    "Lava Ruins - Chest Room07": base_id + 25,
    "Lava Ruins - Chest Room08": base_id + 26,
    "Lava Ruins - Monica": base_id + 27,
    "Lava Ruins - Chest Room01": base_id + 28,
}

dark_tunnel_start_locations: Dict[str, int] = {
    "Dark Tunnel - Chest Room02": base_id + 29,
    "Dark Tunnel - Chest Room03_01": base_id + 30,
    "Dark Tunnel - Chest Room03_02": base_id + 31,
    "Dark Tunnel - Chest Room04": base_id + 32,
    "Dark Tunnel - Chest Room05": base_id + 33,
}

dark_tunnel_after_thunder_locations: Dict[str, int] = {
    "Dark Tunnel - Chest Room06To07": base_id + 34,
    "Dark Tunnel - Chest Room07": base_id + 35,
    "Dark Tunnel - Chest Room08": base_id + 36,
    "Dark Tunnel - Chest Room09To10": base_id + 37,
    "Dark Tunnel - Vanessa": base_id + 38,
}

spirit_realm_start_locations: Dict[str, int] = {
    "Spirit Realm - Chest Room02": base_id + 39,
    "Spirit Realm - Chest Room03": base_id + 40,
    "Spirit Realm - Chest Room04To01": base_id + 41,
}

spirit_realm_after_arcane_barrier_locations: Dict[str, int] = {
    "Spirit Realm - Chest Room04To02": base_id + 42,
    "Spirit Realm - Chest Room06": base_id + 43,
    "Spirit Realm - Chest Room07": base_id + 44,
}

spirit_realm_after_teleport_locations: Dict[str, int] = {
    "Spirit Realm - Chest Room08": base_id + 45,
    "Spirit Realm - Queen Vanessa V2": base_id + 46,
}

abyss_locations: Dict[str, int] = {
    "Abyss - Chest Room04": base_id + 47,
    "Abyss - Chest Room05": base_id + 48,
}

abyss_trials_locations: Dict[str, int] = {
    "Abyss - Chest Underground Trial": base_id + 49,
    "Abyss - Chest Lava Ruins Trial": base_id + 50,
    "Abyss - Chest Dark Tunnel Trial": base_id + 51,
    "Abyss - Nonota": None,
}

lwn_locations: Dict[str, int] = {
    **shrine_start_locations,
    **shrine_armor_locations,
    **shrine_secret_passage_locations,
    **underground_start_locations,
    **underground_tania_locations,
    **lava_ruins_start_locations,
    **lava_ruins_after_fire_barrier_locations,
    **dark_tunnel_start_locations,
    **dark_tunnel_after_thunder_locations,
    **spirit_realm_start_locations,
    **spirit_realm_after_arcane_barrier_locations,
    **spirit_realm_after_teleport_locations,
    **abyss_locations,
    **abyss_trials_locations
}

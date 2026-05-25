from typing import Any

# for UT poptracker integration map tab switching
def map_page_index(data: Any) -> int:
    mapping: dict[int, int] = {
        2: 0,
        3: 1,
        4: 2,
        5: 3,
        6: 4,
        7: 5,
    }
    return mapping.get(data, 0)

lwn_tracker_world = {
    #"map_page_folder": "tracker",  # JSONs loaded from here in the apworld
    "external_pack_key": "ut_pack_path",  # Images loaded from here
    "map_page_setting_key": "Slot:{player}:lwn_map",
    "map_page_index": map_page_index,
    "map_page_maps": "maps/maps.json",
    "map_page_locations": ["locations/okun_shrine.json", "locations/underground.json", "locations/lava_ruins.json",
                           "locations/dark_tunnel.json", "locations/spirit_realm.json", "locations/abyss.json"]
}
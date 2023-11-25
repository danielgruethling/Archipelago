from typing import List

from BaseClasses import Location, Item, ItemClassification
from worlds.AutoWorld import World
from .Options import LWNOptions, NoArcane
from .Items import lwn_items, attack_magics, boss_souls, useful_items, filler_items
from .Locations import lwn_locations, shrine_start_locations, shrine_armor_locations, \
    shrine_secret_passage_locations, underground_start_locations, \
    underground_tania_locations, lava_ruins_start_locations, \
    lava_ruins_after_fire_barrier_locations, dark_tunnel_start_locations, \
    dark_tunnel_after_thunder_locations, spirit_realm_start_locations, \
    spirit_realm_after_arcane_barrier_locations, spirit_realm_after_teleport_locations, \
    abyss_locations, abyss_trials_locations
from .Regions import LWNRegion

class LWNItem(Item):
    game: str = "Little Witch Nobeta"

class LWNLocation(Location):
    game: str = "Little Witch Nobeta"

    # override constructor to automatically mark event locations as such
    def __init__(self, player: int, name = "", code = None, parent = None):
        super(LWNLocation, self).__init__(player, name, code, parent)
        self.event = code is None

class LWNWorld(World):
    game: str = "Little Witch Nobeta"
    options_dataclass = LWNOptions
    options: LWNOptions
    topology_present = True

    # The following two dicts are required for the generation to know which
    # items exist. They could be generated from json or something else. They can
    # include events, but don't have to since events will be placed manually.
    item_name_to_id = lwn_items
    location_name_to_id = lwn_locations

    # Items can be grouped using their names to allow easy checking if any item
    # from that group has been collected. Group names can also be used for !hint
    item_name_groups = {
        "attack_magics": attack_magics,
        "boss_souls": boss_souls,
        "useful_items": useful_items,
        "filler_items": filler_items,
    }

    def create_item(self, item: str) -> LWNItem:
        item_class = ItemClassification.filler
        if(item in attack_magics):
            item_class = ItemClassification.progression
        if(item in boss_souls):
            item_class = ItemClassification.progression
        elif(item in useful_items):
            item_class = ItemClassification.useful
        elif(item in filler_items):
            item_class = ItemClassification.filler
        return LWNItem(item, item_class, self.item_name_to_id.get(item, None), self.player)
    
    def create_event(self, event: str) -> LWNItem:
        return LWNItem(event, ItemClassification.progression, None, self.player)
    
    def create_regions(self):
        # Add regions to the multiworld. "Menu" is the required starting point.
        # Arguments to Region() are name, player, world, and optionally hint_text
        menu_region = LWNRegion("Menu", self.player, self.multiworld)
        self.multiworld.regions.append(menu_region)

        # Shrine start
        shrine_start_region = LWNRegion("Shrine - Start", self.player, self.multiworld)
        shrine_start_region.add_locations(shrine_start_locations, LWNLocation)
        self.multiworld.regions.append(shrine_start_region)

        # Shrine armor hall
        shrine_armor_region = LWNRegion("Shrine - Armor Hall", self.player, self.multiworld)
        shrine_armor_region.add_locations(shrine_armor_locations, LWNLocation)
        self.multiworld.regions.append(shrine_armor_region)

        # Shrine secret passage
        shrine_secret_passage_region = LWNRegion("Shrine - Secret Passage", self.player, self.multiworld)
        shrine_secret_passage_region.add_locations(shrine_secret_passage_locations, LWNLocation)
        self.multiworld.regions.append(shrine_secret_passage_region)

        # Underground start
        underground_start_region = LWNRegion("Underground - Start", self.player, self.multiworld)
        underground_start_region.add_locations(underground_start_locations, LWNLocation)
        self.multiworld.regions.append(underground_start_region)

        # Underground tania
        underground_tania_region = LWNRegion("Underground - Tania", self.player, self.multiworld)
        underground_tania_region.add_locations(underground_tania_locations, LWNLocation)
        self.multiworld.regions.append(underground_tania_region)

        # Lava ruins start
        lava_ruins_start_region = LWNRegion("Lava Ruins - Start", self.player, self.multiworld)
        lava_ruins_start_region.add_locations(lava_ruins_start_locations, LWNLocation)
        self.multiworld.regions.append(lava_ruins_start_region)

        # Lava ruins after fire barrier
        lava_ruins_after_fire_barrier_region = LWNRegion("Lava Ruins - After Fire Barrier", self.player, self.multiworld)
        lava_ruins_after_fire_barrier_region.add_locations(lava_ruins_after_fire_barrier_locations, LWNLocation)
        self.multiworld.regions.append(lava_ruins_after_fire_barrier_region)

        # Dark tunnel start
        dark_tunnel_start_region = LWNRegion("Dark Tunnel - Start", self.player, self.multiworld)
        dark_tunnel_start_region.add_locations(dark_tunnel_start_locations, LWNLocation)
        self.multiworld.regions.append(dark_tunnel_start_region)

        # Dark tunnel after thunder
        dark_tunnel_after_thunder_region = LWNRegion("Dark Tunnel - After Thunder", self.player, self.multiworld)
        dark_tunnel_after_thunder_region.add_locations(dark_tunnel_after_thunder_locations, LWNLocation)
        self.multiworld.regions.append(dark_tunnel_after_thunder_region)

        # Spirit realm start
        spirit_realm_start_region = LWNRegion("Spirit Realm - Start", self.player, self.multiworld)
        spirit_realm_start_region.add_locations(spirit_realm_start_locations, LWNLocation)
        self.multiworld.regions.append(spirit_realm_start_region)

        # Spirit realm after arcane barrier
        spirit_realm_after_arcane_barrier_region = LWNRegion("Spirit Realm - After Arcane Barrier", self.player, self.multiworld)
        spirit_realm_after_arcane_barrier_region.add_locations(spirit_realm_after_arcane_barrier_locations, LWNLocation)
        self.multiworld.regions.append(spirit_realm_after_arcane_barrier_region)

        # Spirit realm after teleport
        spirit_realm_after_teleport_region = LWNRegion("Spirit Realm - After Teleport", self.player, self.multiworld)
        spirit_realm_after_teleport_region.add_locations(spirit_realm_after_teleport_locations, LWNLocation)
        self.multiworld.regions.append(spirit_realm_after_teleport_region)

        # Abyss
        abyss_region = LWNRegion("Abyss", self.player, self.multiworld)
        abyss_region.add_locations(abyss_locations, LWNLocation)
        self.multiworld.regions.append(abyss_region)

        # Abyss trials
        abyss_trials_region = LWNRegion("Abyss Trials", self.player, self.multiworld)
        abyss_trials_region.add_locations(abyss_trials_locations, LWNLocation)
        self.multiworld.regions.append(abyss_trials_region)

        # Connect regions
        menu_region.connect(shrine_start_region)

        shrine_start_region.add_exits({"Shrine - Armor Hall": "Shrine Arcane Barrier"}, \
            {"Shrine - Armor Hall": lambda state: state.has("Arcane", self.player) or \
            state.has("Thunder", self.player)})

        shrine_armor_region.connect(underground_start_region)
        shrine_armor_region.add_exits({"Shrine - Secret Passage": "Secret Passage Fire Barrier"}, \
            {"Shrine - Secret Passage": lambda state: state.has("Fire", self.player) or \
            state.has("Thunder", self.player)})

        shrine_secret_passage_region.connect(dark_tunnel_start_region)
        
        underground_start_region.add_exits({"Underground - Tania": "Underground Fire"}, \
            {"Underground - Tania": lambda state: state.has("Ice", self.player)})
        
        underground_tania_region.connect(shrine_start_region)
        underground_tania_region.connect(lava_ruins_start_region)
        
        lava_ruins_start_region.add_exits({"Lava Ruins - After Fire Barrier": "Lava Ruins Fire Barrier"}, \
            {"Lava Ruins - After Fire Barrier": lambda state: state.has("Fire", self.player) or \
            state.has("Thunder", self.player)})

        lava_ruins_after_fire_barrier_region.connect(underground_start_region)
        lava_ruins_after_fire_barrier_region.connect(dark_tunnel_start_region)
        
        dark_tunnel_start_region.add_exits({"Dark Tunnel - After Thunder": "Dark Tunnel Thunder Barrier"}, \
            {"Dark Tunnel - After Thunder": lambda state: state.has("Thunder", self.player)})

        dark_tunnel_after_thunder_region.connect(shrine_start_region)
        dark_tunnel_after_thunder_region.connect(spirit_realm_start_region)
        
        spirit_realm_start_region.add_exits( \
            {"Spirit Realm - After Arcane Barrier": "Spirit Realm Arcane Barrier"}, \
            {"Spirit Realm - After Arcane Barrier": lambda state: state.has("Arcane", self.player)})

        spirit_realm_after_arcane_barrier_region.add_exits( \
            {"Spirit Realm - After Teleport": "Spirit Realm Teleport Switch"}, \
            {"Spirit Realm - After Teleport": lambda state: state.has("Ice", self.player) and \
            state.has("Thunder", self.player)})

        spirit_realm_after_teleport_region.connect(abyss_region)
        
        abyss_region.add_exits({"Abyss Trials": "Abyss Trial Fire Barrier"}, \
            {"Abyss Trials": lambda state: state.has("Fire", self.player) or \
            state.has("Thunder", self.player)})

    def set_rules(self):
        self.multiworld.completion_condition[self.player] = lambda state: state.has("Victory", self.player)

    def create_items(self):
        # Generate item pool
        item_pool: List[LWNItem] = []
        for item in attack_magics.keys():
            # Generate 4 of all progressive items
            for _ in range(4):
                lwn_item = self.create_item(item)
                item_pool.append(lwn_item)
        
        if self.options.no_arcane.value == NoArcane.option_true:
            item_pool.append(self.create_item("Arcane"))
        item_pool.append(self.create_item("Fire"))
        item_pool.append(self.create_item("Ice"))
        item_pool.append(self.create_item("Thunder"))

                
        for item in useful_items.keys():
            # Generate 5 of all useful items
            for _ in range(5):
                lwn_item = self.create_item(item)
                item_pool.append(lwn_item)
        
        # Generate remaining filler items
        empty_locations = len(self.multiworld.get_unfilled_locations(self.player))
        remaining_items_needed = empty_locations - len(item_pool)
        item_pool += [
            self.create_item(self.get_filler_item_name())
                for _ in range(remaining_items_needed)
        ]

        self.multiworld.itempool += item_pool
    
    def get_filler_item_name(self) -> str:
        return self.multiworld.random.choice(list(filler_items.keys()))

    def generate_basic(self):
        # place "Victory" at "Nonota" and set collection as win condition
        self.multiworld.get_location("Abyss - Nonota", self.player).place_locked_item(self.create_event("Victory"))

        # give out starter items
        self.multiworld.push_precollected(self.create_item("Teleport"))
        if self.options.no_arcane.value == NoArcane.option_false:
            self.multiworld.push_precollected(self.create_item("Arcane"))

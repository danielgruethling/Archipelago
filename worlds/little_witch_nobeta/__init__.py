import dataclasses
from typing import Any, Dict, List

from BaseClasses import Location, Item, ItemClassification, Tutorial
from worlds.AutoWorld import World, WebWorld
from .Options import PerGameCommonOptions, LWNOptions, Toggle
from .Items import lwn_items, attack_magics, boss_souls, useful_items, filler_items
from .Locations import lwn_locations, shrine_start_locations, shrine_armor_locations, \
    shrine_secret_passage_locations, underground_start_locations, \
    underground_tania_locations, lava_ruins_start_locations, \
    lava_ruins_after_fire_barrier_locations, dark_tunnel_start_locations, \
    dark_tunnel_after_thunder_locations, spirit_realm_start_locations, \
    spirit_realm_after_arcane_barrier_locations, spirit_realm_after_teleport_locations, \
    abyss_locations, abyss_trials_locations
from .Regions import LWNRegion

class LingoWebWorld(WebWorld):
    theme = "grass"
    tutorials = [Tutorial(
        "Multiworld Setup Guide",
        "A guide to playing Little Witch Nobeta with Archipelago.",
        "English",
        "setup_en.md",
        "setup/en",
        ["fragger"]
    )]

class LWNItem(Item):
    game: str = "Little Witch Nobeta"


class LWNLocation(Location):
    game: str = "Little Witch Nobeta"

    # override constructor to automatically mark event locations as such
    def __init__(self, player: int, name="", code=None, parent=None):
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
        if item in attack_magics:
            item_class = ItemClassification.progression
        if item in boss_souls:
            item_class = ItemClassification.progression
        elif item == "Trial Key":
            item_class = ItemClassification.progression
        elif item in useful_items:
            item_class = ItemClassification.useful
        elif item in filler_items:
            item_class = ItemClassification.filler
        return LWNItem(item, item_class, self.item_name_to_id.get(item, None), self.player)

    def create_event(self, event: str) -> LWNItem:
        return LWNItem(event, ItemClassification.progression, None, self.player)

    def create_region(self, region_name: str, locations=None) -> LWNRegion:
        region = LWNRegion(region_name, self.player, self.multiworld)
        if locations != None:
            region.add_locations(locations, LWNLocation)
        self.multiworld.regions.append(region)
        return region

    def create_regions(self):
        # Add regions to the multiworld. "Menu" is the required starting point.
        # Arguments to Region() are name, player, world, and optionally hint_text
        menu_region = self.create_region("Menu")

        # Shrine start
        shrine_start_region = self.create_region("Shrine - Start", shrine_start_locations)

        # Shrine armor hall
        shrine_armor_region = self.create_region("Shrine - Armor Hall", shrine_armor_locations)

        # Shrine secret passage
        shrine_secret_passage_region = self.create_region("Shrine - Secret Passage", shrine_secret_passage_locations)

        # Underground start
        underground_start_region = self.create_region("Underground - Start", underground_start_locations)

        # Underground tania
        underground_tania_region = self.create_region("Underground - Tania", underground_tania_locations)

        # Lava ruins start
        lava_ruins_start_region = self.create_region("Lava Ruins - Start", lava_ruins_start_locations)

        # Lava ruins after fire barrier
        lava_ruins_after_fire_barrier_region = self.create_region("Lava Ruins - After Fire Barrier", lava_ruins_after_fire_barrier_locations)

        # Dark tunnel start
        dark_tunnel_start_region = self.create_region("Dark Tunnel - Start", dark_tunnel_start_locations)

        # Dark tunnel after thunder
        dark_tunnel_after_thunder_region = self.create_region("Dark Tunnel - After Thunder", dark_tunnel_after_thunder_locations)

        # Spirit realm start
        spirit_realm_start_region = self.create_region("Spirit Realm - Start", spirit_realm_start_locations)

        # Spirit realm after arcane barrier
        spirit_realm_after_arcane_barrier_region = self.create_region("Spirit Realm - After Arcane Barrier", spirit_realm_after_arcane_barrier_locations)

        # Spirit realm after teleport
        spirit_realm_after_teleport_region = self.create_region("Spirit Realm - After Teleport", spirit_realm_after_teleport_locations)

        # Abyss
        abyss_region = self.create_region("Abyss", abyss_locations)

        # Abyss trials
        abyss_trials_region = self.create_region("Abyss Trials", abyss_trials_locations)

        # Connect regions
        menu_region.connect(shrine_start_region)

        shrine_start_region.add_exits({"Shrine - Armor Hall": "Shrine Arcane Barrier"},
            {"Shrine - Armor Hall": lambda state: state.has("Arcane", self.player)
                or state.has("Thunder", self.player)})

        shrine_armor_region.connect(underground_start_region)
        shrine_armor_region.add_exits({"Shrine - Secret Passage": "Secret Passage Fire Barrier"},
            {"Shrine - Secret Passage": lambda state: state.has("Fire", self.player)
                or state.has("Thunder", self.player)})

        shrine_secret_passage_region.connect(dark_tunnel_start_region)

        underground_start_region.add_exits({"Underground - Tania": "Underground Fire"},
            {"Underground - Tania": lambda state: state.has("Ice", self.player)})

        underground_tania_region.connect(shrine_start_region)
        underground_tania_region.connect(lava_ruins_start_region)

        lava_ruins_start_region.add_exits({"Lava Ruins - After Fire Barrier": "Lava Ruins Fire Barrier"},
            {"Lava Ruins - After Fire Barrier": lambda state:
                state.has("Fire", self.player) or state.has("Thunder", self.player)})

        lava_ruins_after_fire_barrier_region.connect(underground_start_region)
        lava_ruins_after_fire_barrier_region.connect(dark_tunnel_start_region)

        dark_tunnel_start_region.add_exits({"Dark Tunnel - After Thunder": "Dark Tunnel Thunder Barrier"},
            {"Dark Tunnel - After Thunder": lambda state: state.has("Thunder", self.player)})

        dark_tunnel_after_thunder_region.connect(shrine_start_region)
        dark_tunnel_after_thunder_region.connect(spirit_realm_start_region)

        spirit_realm_start_region.add_exits(
            {"Spirit Realm - After Arcane Barrier": "Spirit Realm Arcane Barrier"},
            {"Spirit Realm - After Arcane Barrier": lambda state: state.has("Arcane", self.player)})

        spirit_realm_after_arcane_barrier_region.add_exits(
            {"Spirit Realm - After Teleport": "Spirit Realm Teleport Switch"},
            {"Spirit Realm - After Teleport": lambda state: state.has("Ice", self.player) and
                state.has("Thunder", self.player)})

        spirit_realm_after_teleport_region.connect(abyss_region)

        if self.options.trial_keys.value == Toggle.option_true:
            abyss_region.add_exits({"Abyss Trials": "Abyss Trial Fire Barrier"},
                {"Abyss Trials": lambda state: (state.has("Fire", self.player) or state.has("Thunder", self.player))
                    and state.has("Trial Key", self.player, 3)})
        else:
            abyss_region.add_exits({"Abyss Trials": "Abyss Trial Fire Barrier"},
                {"Abyss Trials": lambda state: state.has("Fire", self.player) or state.has("Thunder", self.player)})

    def set_rules(self):
        if self.options.goal.value == self.options.goal.option_boss_hunt:
            self.multiworld.completion_condition[self.player] = lambda state: state.has("Victory", self.player) \
                and state.has("Specter Armor Soul", self.player) and state.has("Tania Soul", self.player) \
                and state.has("Monica Soul", self.player) and state.has("Enraged Armor Soul", self.player) \
                and state.has("Vanessa Soul", self.player) and state.has("Queen Vanessa V2 Soul", self.player)
        elif self.options.goal.value == self.options.goal.option_magic_master:
            self.multiworld.completion_condition[self.player] = lambda state: state.has("Victory", self.player) \
                and state.has("Arcane", self.player, 5) and state.has("Ice", self.player, 5) \
                and state.has("Fire", self.player, 5) and state.has("Thunder", self.player, 5)
        else:
            self.multiworld.completion_condition[self.player] = lambda state: state.has("Victory", self.player)

    def create_items(self):
        # Generate item pool
        item_pool: List[LWNItem] = []

        # Generate base level for progressive items
        if self.options.no_arcane.value == Toggle.option_true:
            item_pool.append(self.create_item("Arcane"))
        item_pool.append(self.create_item("Fire"))
        item_pool.append(self.create_item("Ice"))
        item_pool.append(self.create_item("Thunder"))

        # Generate 4 extra of all progressive and useful items
        if self.options.accessibility.value != self.options.accessibility.option_minimal:
            for item in attack_magics.keys():
                for _ in range(4):
                    lwn_item = self.create_item(item)
                    item_pool.append(lwn_item)

            for item in useful_items.keys():
                for _ in range(4):
                    lwn_item = self.create_item(item)
                    item_pool.append(lwn_item)

        # Generate boss souls
        if self.options.randomize_boss_souls.value == Toggle.option_true:
            for item in boss_souls.keys():
                lwn_item = self.create_item(item)
                item_pool.append(lwn_item)

        # Generate trial keys
        if self.options.trial_keys.value == Toggle.option_true:
            for _ in range(self.options.trial_key_amount.value):
                lwn_item = self.create_item("Trial Key")
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
        # Place "Victory" at "Nonota" and set collection as win condition
        self.multiworld.get_location("Abyss - Nonota", self.player).place_locked_item(self.create_event("Victory"))

        # Place boss souls at bosses when not randomized
        if self.options.randomize_boss_souls.value == Toggle.option_false:
            (self.multiworld.get_location("Shrine - Specter Armor", self.player)
                .place_locked_item(self.create_item("Specter Armor Soul")))

            (self.multiworld.get_location("Secret Passage - Enraged Armor", self.player)
                .place_locked_item(self.create_item("Enraged Armor Soul")))

            (self.multiworld.get_location("Underground - Tania", self.player)
                .place_locked_item(self.create_item("Tania Soul")))

            (self.multiworld.get_location("Lava Ruins - Monica", self.player)
                .place_locked_item(self.create_item("Monica Soul")))

            (self.multiworld.get_location("Dark Tunnel - Vanessa", self.player)
                .place_locked_item(self.create_item("Vanessa Soul")))

            (self.multiworld.get_location("Spirit Realm - Queen Vanessa V2", self.player)
                .place_locked_item(self.create_item("Queen Vanessa V2 Soul")))

    def fill_slot_data(self) -> Dict[str, Any]:
        slot_data = dict()

        for option_name in (attr.name for attr in dataclasses.fields(LWNOptions)
                            if attr not in dataclasses.fields(PerGameCommonOptions)):
            option = getattr(self.options, option_name)
            slot_data[option_name] = bool(option.value) if isinstance(option, Toggle) else option.value

        return slot_data

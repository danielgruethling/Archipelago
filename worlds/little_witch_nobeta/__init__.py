import dataclasses
from typing import Any, Dict, List

from BaseClasses import Item, ItemClassification, Tutorial, Region
from worlds.AutoWorld import World, WebWorld
from .options import PerGameCommonOptions, LWNOptions, Toggle
from .items import (lwn_items, item_name_to_id, attack_magics, boss_souls, useful_items, filler_items,
                    lore_items, barrier_items, gate_items, item_name_groups)
from .locations import LWNLocation, location_name_groups, location_name_to_id, append_locations
from .regions import LWNRegion, lwn_regions
from .rules import set_region_rules, set_location_rules


class LWNWebWorld(WebWorld):
    theme = "grass"
    tutorials = [
        Tutorial(
            "Multiworld Setup Guide",
            "A guide to playing Little Witch Nobeta with Archipelago.",
            "English",
            "setup_en.md",
            "setup/en",
            ["fragger"]
        )
    ]


class LWNItem(Item):
    game: str = "Little Witch Nobeta"


class LWNWorld(World):
    game: str = "Little Witch Nobeta"
    options_dataclass = LWNOptions
    options: LWNOptions
    topology_present = True

    # The following two dicts are required for the generation to know which
    # items exist. They could be generated from json or something else. They can
    # include events, but don't have to since events will be placed manually.
    item_name_to_id = item_name_to_id
    location_name_to_id = location_name_to_id

    # Items can be grouped using their names to allow easy checking if any item
    # from that group has been collected. Group names can also be used for !hint
    item_name_groups = item_name_groups

    location_name_groups = location_name_groups

    def create_item(self, item: str) -> LWNItem:
        item_class = ItemClassification.filler
        if item in attack_magics or item in boss_souls:
            item_class = ItemClassification.progression
        elif item == "Trial Key":
            item_class = ItemClassification.progression
        elif item in useful_items:
            item_class = ItemClassification.useful
        elif item in filler_items:
            item_class = ItemClassification.filler
        elif item in lore_items:
            item_class = ItemClassification.filler
        elif item in barrier_items:
            if self.options.barrier_behaviour.value \
                    == self.options.barrier_behaviour.option_randomized:
                item_class = ItemClassification.progression
            else:
                item_class = ItemClassification.filler
        elif item in gate_items:
            if self.options.shortcut_gate_behaviour.value \
                    == self.options.shortcut_gate_behaviour.option_randomized:
                item_class = ItemClassification.progression
            else:
                item_class = ItemClassification.filler

        return LWNItem(item, item_class, self.item_name_to_id.get(item, None), self.player)

    def create_event(self, event: str) -> LWNItem:
        return LWNItem(event, ItemClassification.progression, None, self.player)

    def create_region(self, region_name: str, locations=None) -> LWNRegion:
        region = LWNRegion(region_name, self.player, self.multiworld)
        if locations is not None:
            region.add_locations(locations, LWNLocation)
        self.multiworld.regions.append(region)
        return region

    def create_regions(self):

        for region_name in lwn_regions:
            region = Region(region_name, self.player, self.multiworld)
            self.multiworld.regions.append(region)

        for region_name, exits in lwn_regions.items():
            region = self.multiworld.get_region(region_name, self.player)
            region.add_exits(exits)

        append_locations(self)

    def set_rules(self):

        # Set exit rules
        set_region_rules(self)

        # Set location rules
        set_location_rules(self)

        # Set goal rules
        if self.options.goal.value == self.options.goal.option_boss_hunt:
            self.multiworld.completion_condition[self.player] = lambda state: state.has \
                and state.has("Specter Armor Soul", self.player) and state.has("Tania Soul", self.player) \
                and state.has("Monica Soul", self.player) and state.has("Enraged Armor Soul", self.player) \
                and state.has("Vanessa Soul", self.player) and state.has("Vanessa V2 Soul", self.player)
        elif self.options.goal.value == self.options.goal.option_magic_master:
            if self.options.no_arcane.value == Toggle.option_false:
                self.multiworld.completion_condition[self.player] = lambda state: state.has("Victory", self.player) \
                    and state.has("Arcane", self.player, 4) and state.has("Ice", self.player, 5) \
                    and state.has("Fire", self.player, 5) and state.has("Thunder", self.player, 5)
            else:
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

        # Generate a progression counter and double jump
        counter_spell = self.create_item("Mana Absorption")
        counter_spell.classification = ItemClassification.progression
        item_pool.append(counter_spell)

        wind_spell = self.create_item("Wind")
        wind_spell.classification = ItemClassification.progression
        item_pool.append(wind_spell)

        # Generate 4 extra of all progressive and useful items
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

        # Generate lore items
        if self.options.randomize_lore.value == Toggle.option_true:
            for lore_item_name in lore_items.keys():
                lwn_item = self.create_item(lore_item_name)
                item_pool.append(lwn_item)

        # Generate barrier items
        if self.options.barrier_behaviour.value == self.options.barrier_behaviour.option_randomized:
            for barrier_item_name in barrier_items.keys():
                lwn_item = self.create_item(barrier_item_name)
                item_pool.append(lwn_item)

        # Generate barrier items
        if self.options.shortcut_gate_behaviour.value == self.options.shortcut_gate_behaviour.option_randomized:
            for gate_item_name in gate_items.keys():
                lwn_item = self.create_item(gate_item_name)
                item_pool.append(lwn_item)

        # Generate remaining filler items
        empty_locations = len(self.multiworld.get_unfilled_locations(self.player))
        remaining_items_needed = empty_locations - len(item_pool) - 1
        # Subtract local boss souls if not randomized
        if self.options.randomize_boss_souls.value == Toggle.option_false:
            remaining_items_needed -= len(boss_souls)

        item_pool += [
            self.create_item(self.get_filler_item_name())
            for _ in range(remaining_items_needed)
        ]

        self.multiworld.itempool += item_pool

    def get_filler_item_name(self) -> str:
        return self.multiworld.random.choice(list(filler_items))

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

            (self.multiworld.get_location("Spirit Realm - Vanessa V2", self.player)
                .place_locked_item(self.create_item("Vanessa V2 Soul")))

    def fill_slot_data(self) -> Dict[str, Any]:
        slot_data = dict()

        for option_name in (attr.name for attr in dataclasses.fields(LWNOptions)
                            if attr not in dataclasses.fields(PerGameCommonOptions)):
            option = getattr(self.options, option_name)
            slot_data[option_name] = bool(option.value) if isinstance(option, Toggle) else option.value

        return slot_data

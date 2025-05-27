from typing import TYPE_CHECKING

from .Options import LWNOptions, Toggle
if TYPE_CHECKING:
    from . import LWNWorld


def set_region_rules(world: "LWNWorld") -> None:
    multiworld = world.multiworld
    player = world.player
    options = world.options

    multiworld.get_entrance("Menu -> Shrine - Start", player).access_rule = \
        lambda state: True
    multiworld.get_entrance("Shrine - Start -> Shrine - Armor Hall", player).access_rule = \
        lambda state: state.has("Arcane", player) or state.has("Thunder", player)
    multiworld.get_entrance("Shrine - Armor Hall -> Shrine - Secret Passage", player).access_rule = \
        lambda state: state.has("Fire", player) or state.has("Thunder", player)
    multiworld.get_entrance("Shrine - Armor Hall -> Underground - Start", player).access_rule = \
        lambda state: True
    multiworld.get_entrance("Shrine - Secret Passage -> Dark Tunnel - Start", player).access_rule = \
        lambda state: True
    multiworld.get_entrance("Underground - Start -> Underground - Tania", player).access_rule = \
        lambda state: state.has("Ice", player)
    multiworld.get_entrance("Underground - Tania -> Shrine - Start", player).access_rule = \
        lambda state: True
    multiworld.get_entrance("Underground - Tania -> Lava Ruins - Start", player).access_rule = \
        lambda state: True
    multiworld.get_entrance("Lava Ruins - Start -> Lava Ruins - After Fire Barrier", player).access_rule = \
        lambda state: state.has("Fire", player) or state.has("Thunder", player)
    multiworld.get_entrance("Lava Ruins - After Fire Barrier -> Underground - Start", player).access_rule = \
        lambda state: True
    multiworld.get_entrance("Lava Ruins - After Fire Barrier -> Dark Tunnel - Start", player).access_rule = \
        lambda state: True
    multiworld.get_entrance("Dark Tunnel - Start -> Dark Tunnel - After Thunder", player).access_rule = \
        lambda state: state.has("Thunder", player)
    multiworld.get_entrance("Dark Tunnel - After Thunder -> Shrine - Start", player).access_rule = \
        lambda state: True
    multiworld.get_entrance("Dark Tunnel - After Thunder -> Spirit Realm - Start", player).access_rule = \
        lambda state: True
    multiworld.get_entrance("Spirit Realm - Start -> Spirit Realm - After Arcane Barrier", player).access_rule = \
        lambda state: state.has("Arcane", player)
    multiworld.get_entrance("Spirit Realm - After Arcane Barrier -> Spirit Realm - After Teleport", player).access_rule = \
        lambda state: state.has("Ice", player) and state.has("Thunder", player)
    multiworld.get_entrance("Spirit Realm - After Teleport -> Abyss", player).access_rule = \
        lambda state: True
    multiworld.get_entrance("Abyss -> Abyss Trials", player).access_rule = \
        lambda state: (state.has("Fire", player) or state.has("Thunder", player)) and (state.has("Trial Key", player, 3) or options.trial_keys.value == Toggle.option_false)
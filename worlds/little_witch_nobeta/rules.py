from typing import TYPE_CHECKING

from .options import LWNOptions, Toggle
from worlds.generic.Rules import set_rule
if TYPE_CHECKING:
    from . import LWNWorld


def set_region_rules(world: "LWNWorld") -> None:
    multiworld = world.multiworld
    player = world.player
    options = world.options

    multiworld.get_entrance("Menu -> Shrine - Start", player).access_rule = \
        lambda state: True
    multiworld.get_entrance("Shrine - Start -> Shrine - After first magic switch", player).access_rule = \
        lambda state: state.has("Shrine First Magic Barrier", player)
    multiworld.get_entrance("Shrine - After first magic switch -> Shrine - Armor Hall", player).access_rule = \
        lambda state: state.has("Shrine Second Magic Barrier", player)
    multiworld.get_entrance("Shrine - After first magic switch -> Shrine - Start", player).access_rule = \
        lambda state: state.has("Shrine First Magic Barrier", player)
    multiworld.get_entrance("Shrine - Armor Hall -> Secret passage - Start", player).access_rule = \
        lambda state: state.has("Secret Passage Entrance Magic Barrier", player)
    multiworld.get_entrance("Shrine - Armor Hall -> Secret passage - After first fire barrier", player).access_rule = \
        lambda state: state.has("Shrine Secret Area Shortcut Gate", player)
    multiworld.get_entrance("Shrine - Armor Hall -> Secret Passage - Boss Shortcut", player).access_rule = \
        lambda state: state.has("Shrine Secret Boss Shortcut Gate", player)
    multiworld.get_entrance("Shrine - Armor Hall -> Shrine - Underground shortcut", player).access_rule = \
        lambda state: state.has("Shrine Underground Shortcut Gate", player)
    multiworld.get_entrance("Shrine - Armor Hall -> Shrine - After first magic switch", player).access_rule = \
        lambda state: state.has("Shrine Second Magic Barrier", player)
    multiworld.get_entrance("Shrine - Underground shortcut -> Shrine - Armor Hall", player).access_rule = \
        lambda state: state.has("Shrine Underground Shortcut Gate", player)
    multiworld.get_entrance("Shrine - Underground shortcut -> Underground - Shrine shortcut", player).access_rule = \
        lambda state: True
    multiworld.get_entrance("Secret passage - Start -> Shrine - Armor Hall", player).access_rule = \
        lambda state: state.has("Secret Passage Entrance Magic Barrier", player)
    multiworld.get_entrance("Secret passage - Start -> Secret passage - After first fire barrier", player).access_rule = \
        lambda state: state.has("Secret Passage First Fire Barrier", player)
    multiworld.get_entrance("Secret passage - After first fire barrier -> Secret passage - Start", player).access_rule = \
        lambda state: state.has("Secret Passage First Fire Barrier", player)
    multiworld.get_entrance("Secret passage - After first fire barrier -> Secret Passage - Dark Tunnel shortcut", player).access_rule = \
        lambda state: state.has("Secret Passage Dark Tunnel Shortcut Gate", player)
    multiworld.get_entrance("Secret passage - After first fire barrier -> Shrine - Armor Hall", player).access_rule = \
        lambda state: state.has("Shrine Secret Area Shortcut Gate", player)
    multiworld.get_entrance("Secret passage - After first fire barrier -> Secret Passage - Enraged Armor", player).access_rule = \
        lambda state: state.has("Secret Passage Second Fire Barrier", player)
    multiworld.get_entrance("Secret Passage - Enraged Armor -> Secret Passage - Boss Shortcut", player).access_rule = \
        lambda state: state.has("Defeat Enraged Armor Barrier", player)
    multiworld.get_entrance("Secret Passage - Enraged Armor -> Secret passage - After first fire barrier", player).access_rule = \
        lambda state: state.has("Secret Passage Second Fire Barrier", player)
    multiworld.get_entrance("Secret Passage - Boss Shortcut -> Shrine - Armor Hall", player).access_rule = \
        lambda state: state.has("Shrine Secret Boss Shortcut Gate", player)
    multiworld.get_entrance("Secret Passage - Boss Shortcut -> Secret Passage - Enraged Armor", player).access_rule = \
        lambda state: state.has("Defeat Enraged Armor Barrier", player)
    multiworld.get_entrance("Secret Passage - Dark Tunnel shortcut -> Dark Tunnel - After bridge collapse", player).access_rule = \
        lambda state: True
    multiworld.get_entrance("Secret Passage - Dark Tunnel shortcut -> Secret passage - After first fire barrier", player).access_rule = \
        lambda state: state.has("Secret Passage Dark Tunnel Shortcut Gate", player)
    multiworld.get_entrance("Underground - Start -> Underground - After wind", player).access_rule = \
        lambda state: state.has("Wind", player) or options.less_wind_requirements.value == Toggle.option_true
    multiworld.get_entrance("Underground - After wind -> Underground - Grand Hall", player).access_rule = \
        lambda state: state.has("Underground Magic Barrier At Maid Enemy", player)
    multiworld.get_entrance("Underground - After wind -> Underground - Start", player).access_rule = \
        lambda state: True
    multiworld.get_entrance("Underground - Grand Hall -> Underground - After fire", player).access_rule = \
        lambda state: state.has("Ice", player)
    multiworld.get_entrance("Underground - Grand Hall -> Underground - After wind", player).access_rule = \
        lambda state: state.has("Underground Magic Barrier At Maid Enemy", player)
    multiworld.get_entrance("Underground - Grand Hall -> Underground - Lava ruins shortcut", player).access_rule = \
        lambda state: state.has("Underground Lava Ruins Shortcut Gate", player)
    multiworld.get_entrance("Underground - Grand Hall -> Underground - Shrine shortcut", player).access_rule = \
        lambda state: state.has("Underground Lava Ruins Shortcut Gate", player)
    multiworld.get_entrance("Underground - Grand Hall -> Underground - Tania shortcut", player).access_rule = \
        lambda state: state.has("Underground Tania Shortcut Gate On Grand Hall Side", player)
    multiworld.get_entrance("Underground - Lava ruins shortcut -> Underground - Grand Hall", player).access_rule = \
        lambda state: state.has("Underground Lava Ruins Shortcut Gate", player)
    multiworld.get_entrance("Underground - Lava ruins shortcut -> Underground - Shrine shortcut", player).access_rule = \
        lambda state: state.has("Underground Lava Ruins Shortcut Gate", player)
    multiworld.get_entrance("Underground - Lava ruins shortcut -> Lava Ruins - Path to dark tunnel", player).access_rule = \
        lambda state: True
    multiworld.get_entrance("Underground - Shrine shortcut -> Underground - Grand Hall", player).access_rule = \
        lambda state: True
    multiworld.get_entrance("Underground - Shrine shortcut -> Underground - Lava ruins shortcut", player).access_rule = \
        lambda state: state.has("Underground Lava Ruins Shortcut Gate", player)
    multiworld.get_entrance("Underground - Shrine shortcut -> Shrine - Underground shortcut", player).access_rule = \
        lambda state: True
    multiworld.get_entrance("Underground - Tania shortcut -> Underground - Grand Hall", player).access_rule = \
        lambda state: state.has("Underground Tania Shortcut Gate On Grand Hall Side", player)
    multiworld.get_entrance("Underground - Tania shortcut -> Underground - Tania", player).access_rule = \
        lambda state: state.has("Underground Tania Shortcut Gate On Tania Side", player)
    multiworld.get_entrance("Underground - After fire -> Underground - After fire magic switch barrier", player).access_rule = \
        lambda state: state.has("Underground Fire Barrier Magic Barrier", player)
    multiworld.get_entrance("Underground - After fire -> Underground - Grand Hall", player).access_rule = \
        lambda state: state.has("Ice", player)
    multiworld.get_entrance("Underground - After fire magic switch barrier -> Underground - Tania", player).access_rule = \
        lambda state: state.has("Underground Enemy Magic Barrier", player)
    multiworld.get_entrance("Underground - After fire magic switch barrier -> Underground - After fire", player).access_rule = \
        lambda state: state.has("Underground Fire Barrier Magic Barrier", player)
    multiworld.get_entrance("Underground - Tania -> Underground - Tania shortcut", player).access_rule = \
        lambda state: state.has("Underground Tania Shortcut Gate On Tania Side", player)
    multiworld.get_entrance("Underground - Tania -> Underground - After fire magic switch barrier", player).access_rule = \
        lambda state: state.has("Underground Enemy Magic Barrier", player)
    multiworld.get_entrance("Underground - Tania -> Lava Ruins - Start", player).access_rule = \
        lambda state: state.has("Mana Absorption", player)
    multiworld.get_entrance("Lava Ruins - Start -> Lava Ruins - After magic platforms", player).access_rule = \
        lambda state: state.has("Lava Ruins Magic Platforms", player) or state.has("Lava Ruins Fake Floor Shortcut Gate", player)
    multiworld.get_entrance("Lava Ruins - Start -> Lava Ruins - Monica warp", player).access_rule = \
        lambda state: state.has("Lava Ruins Monica Warp Gate")
    multiworld.get_entrance("Lava Ruins - After magic platforms -> Lava Ruins - After scissor enemy barrier", player).access_rule = \
        lambda state: state.has("Lava Ruins Scissor Enemy Barrier", player)
    multiworld.get_entrance("Lava Ruins - After magic platforms -> Lava Ruins - Start", player).access_rule = \
        lambda state: state.has("Lava Ruins Magic Platforms", player) or state.has("Lava Ruins Fake Floor Shortcut Gate", player)
    multiworld.get_entrance("Lava Ruins - After scissor enemy barrier -> Lava Ruins - After magic platforms", player).access_rule = \
        lambda state: state.has("Lava Ruins Scissor Enemy Lift", player)
    multiworld.get_entrance("Lava Ruins - After scissor enemy barrier -> Lava Ruins - After Fire Barrier", player).access_rule = \
        lambda state: state.has("Lava Ruins Fire Magic Barrier", player) or state.has("Lava Ruins Monica Shortcut Gate", player)
    multiworld.get_entrance("Lava Ruins - After Fire Barrier -> Lava Ruins - After scissor enemy barrier", player).access_rule = \
        lambda state: state.has("Lava Ruins Fire Magic Barrier", player) or state.has("Lava Ruins Monica Shortcut Gate", player)
    multiworld.get_entrance("Lava Ruins - After Fire Barrier -> Lava Ruins - Monica", player).access_rule = \
        lambda state: state.has("Wind", player) or (options.less_wind_requirements.value == Toggle.option_true and state.has("Fire", player))
    multiworld.get_entrance("Lava Ruins - Monica -> Lava Ruins - After Fire Barrier", player).access_rule = \
        lambda state: True
    multiworld.get_entrance("Lava Ruins - Monica -> Lava Ruins - Monica warp", player).access_rule = \
        lambda state: True
    multiworld.get_entrance("Lava Ruins - Monica warp -> Lava Ruins - Path to dark tunnel", player).access_rule = \
        lambda state: state.has("Lava Ruins Monica Warp Gate")
    multiworld.get_entrance("Lava Ruins - Monica warp -> Lava Ruins - Start", player).access_rule = \
        lambda state: state.has("Lava Ruins Monica Warp Gate")
    multiworld.get_entrance("Lava Ruins - Path to dark tunnel -> Underground - Lava ruins shortcut", player).access_rule = \
        lambda state: True
    multiworld.get_entrance("Lava Ruins - Path to dark tunnel -> Dark Tunnel - Start", player).access_rule = \
        lambda state: True
    multiworld.get_entrance("Dark Tunnel - Start -> Dark Tunnel - After first magic barrier", player).access_rule = \
        lambda state: state.has("Dark Tunnel First Magic Barrier", player)
    multiworld.get_entrance("Dark Tunnel - Start -> Lava Ruins - Path to dark tunnel", player).access_rule = \
        lambda state: True
    multiworld.get_entrance("Dark Tunnel - Start -> Dark Tunnel - After light switch barrier", player).access_rule = \
        lambda state: state.has("Dark Tunnel Light Switch Barrier", player)
    multiworld.get_entrance("Dark Tunnel - After first magic barrier -> Dark Tunnel - Start", player).access_rule = \
        lambda state: state.has("Dark Tunnel First Magic Barrier", player)
    multiworld.get_entrance("Dark Tunnel - After first magic barrier -> Dark Tunnel - After first gate", player).access_rule = \
        lambda state: state.has("Dark Tunnel First Gate", player)
    multiworld.get_entrance("Dark Tunnel - After first gate -> Dark Tunnel - After first magic barrier", player).access_rule = \
        lambda state: state.has("Dark Tunnel First Gate", player)
    multiworld.get_entrance("Dark Tunnel - After light switch barrier -> Dark Tunnel - After thunder barrier", player).access_rule = \
        lambda state: state.has("Dark Tunnel Thunder Barrier", player)
    multiworld.get_entrance("Dark Tunnel - After light switch barrier -> Dark Tunnel - Start", player).access_rule = \
        lambda state: state.has("Dark Tunnel Light Switch Barrier", player)
    multiworld.get_entrance("Dark Tunnel - After thunder barrier -> Dark Tunnel - After light switch barrier", player).access_rule = \
        lambda state: state.has("Dark Tunnel Thunder Barrier", player)
    multiworld.get_entrance("Dark Tunnel - After thunder barrier -> Dark Tunnel - After floating platforms", player).access_rule = \
        lambda state: (state.has("Dark Tunnel Floating Platform One", player) and state.has("Dark Tunnel Floating Platform Two", player) and state.has("Dark Tunnel Floating Platform Three", player)) or state.has("Wind", player)
    multiworld.get_entrance("Dark Tunnel - After floating platforms -> Dark Tunnel - After thunder barrier", player).access_rule = \
        lambda state: (state.has("Dark Tunnel Floating Platform One", player) and state.has("Dark Tunnel Floating Platform Two", player) and state.has("Dark Tunnel Floating Platform Three", player)) or state.has("Wind", player)
    multiworld.get_entrance("Dark Tunnel - After floating platforms -> Dark Tunnel - After bridge collapse", player).access_rule = \
        lambda state: True
    multiworld.get_entrance("Dark Tunnel - After bridge collapse -> Spirit Realm - Start", player).access_rule = \
        lambda state: True
    multiworld.get_entrance("Dark Tunnel - After bridge collapse -> Secret Passage - Dark Tunnel shortcut", player).access_rule = \
        lambda state: True
    multiworld.get_entrance("Spirit Realm - Start -> Spirit Realm - After platforms", player).access_rule = \
        lambda state: state.has("Wind", player)
    multiworld.get_entrance("Spirit Realm - After platforms -> Spirit Realm - Start", player).access_rule = \
        lambda state: True
    multiworld.get_entrance("Spirit Realm - After platforms -> Spirit Realm - After second Seal", player).access_rule = \
        lambda state: state.has("Spirit Realm Statue Shortcut Gate", player)
    multiworld.get_entrance("Spirit Realm - After platforms -> Spirit Realm - After arcane barrier", player).access_rule = \
        lambda state: state.has("Spirit Realm Arcane Barrier", player)
    multiworld.get_entrance("Spirit Realm - After arcane barrier -> Spirit Realm - After platforms", player).access_rule = \
        lambda state: True
    multiworld.get_entrance("Spirit Realm - After arcane barrier -> Spirit Realm - Seal", player).access_rule = \
        lambda state: True
    multiworld.get_entrance("Spirit Realm - Seal -> Spirit Realm - After first Seal", player).access_rule = \
        lambda state: state.has("Spirit Realm First Seal Magic Barrier", player)
    multiworld.get_entrance("Spirit Realm - After first Seal -> Spirit Realm - Seal", player).access_rule = \
        lambda state: state.has("Spirit Realm First Seal Magic Barrier", player)
    multiworld.get_entrance("Spirit Realm - After first Seal -> Spirit Realm - After second Seal", player).access_rule = \
        lambda state: state.has("Spirit Realm Second Seal Magic Barrier", player)
    multiworld.get_entrance("Spirit Realm - After second Seal -> Spirit Realm - After first Seal", player).access_rule = \
        lambda state: state.has("Spirit Realm Second Seal Magic Barrier", player)
    multiworld.get_entrance("Spirit Realm - After second Seal -> Spirit Realm - After elevator", player).access_rule = \
        lambda state: state.has("Spirit Realm Elevator", player)
    multiworld.get_entrance("Spirit Realm - After second Seal -> Spirit Realm - After platforms", player).access_rule = \
        lambda state: state.has("Spirit Realm Statue Shortcut Gate", player)
    multiworld.get_entrance("Spirit Realm - After elevator -> Spirit Realm - After teleport", player).access_rule = \
        lambda state: state.has("Spirit Realm Teleporter", player)
    multiworld.get_entrance("Spirit Realm - After elevator -> Spirit Realm - After second Seal", player).access_rule = \
        lambda state: True
    multiworld.get_entrance("Spirit Realm - After teleport -> Spirit Realm - After elevator", player).access_rule = \
        lambda state: True
    multiworld.get_entrance("Spirit Realm - After teleport -> Abyss", player).access_rule = \
        lambda state: True
    multiworld.get_entrance("Abyss -> Abyss - After first teleport", player).access_rule = \
        lambda state: True
    multiworld.get_entrance("Abyss - After first teleport -> Abyss Trials", player).access_rule = \
        lambda state: state.has("Abyss First Gate", player)
    multiworld.get_entrance("Abyss - After first gate -> Abyss - After giant maid barrier", player).access_rule = \
        lambda state: state.has("Abyss After Giant Maid Barrier", player)
    multiworld.get_entrance("Abyss - After first gate -> Abyss - Left gate at trap", player).access_rule = \
        lambda state: state.has("Abyss Left Trap Gate", player)
    multiworld.get_entrance("Abyss - Left gate at trap -> Abyss - After first gate", player).access_rule = \
        lambda state: state.has("Abyss Left Trap Gate", player)
    multiworld.get_entrance("Abyss - After giant maid barrier -> Abyss - Trials Lobby", player).access_rule = \
        lambda state: True
    multiworld.get_entrance("Abyss - Trials Lobby -> Abyss - Underground Trial", player).access_rule = \
        lambda state: state.has("Trial Key", player, 3) or options.trial_keys.value == Toggle.option_false
    multiworld.get_entrance("Abyss - Trials Lobby -> Abyss - Lava Ruins Trial", player).access_rule = \
        lambda state: state.has("Trial Key", player, 3) or options.trial_keys.value == Toggle.option_false
    multiworld.get_entrance("Abyss - Trials Lobby -> Abyss - Dark Tunnel Trial", player).access_rule = \
        lambda state: state.has("Trial Key", player, 3) or options.trial_keys.value == Toggle.option_false
    multiworld.get_entrance("Abyss - Trials Lobby -> Abyss - Nonota", player).access_rule = \
        lambda state: state.has("Abyss Underground Trial Magic Switch", player) and state.has("Abyss Lava Ruins Trial Magic Switch", player) and state.has("Abyss Dark Tunnel Trial Magic Switch", player)
    multiworld.get_entrance("Abyss - Underground Trial -> Abyss - Underground Trial magic switch", player).access_rule = \
        lambda state: state.has("Abyss After Scissor Enemy Barrier", player)
    multiworld.get_entrance("Abyss - Underground Trial magic switch -> Abyss - Trials Lobby", player).access_rule = \
        lambda state: state.has("Abyss Underground Trial Magic Switch", player)
    multiworld.get_entrance("Abyss - Dark Tunnel Trial -> Abyss - Dark Tunnel Trial magic switch", player).access_rule = \
        lambda state: state.has("Abyss Dark Tunnel Trial Maid Enemy Barrier", player)
    multiworld.get_entrance("Abyss - Dark Tunnel Trial magic switch -> Abyss - Trials Lobby", player).access_rule = \
        lambda state: state.has("Abyss Dark Tunnel Trial Magic Switch", player)
    multiworld.get_entrance("Abyss - Lava Ruins Trial -> Abyss - Lava Ruins Trial magic switch", player).access_rule = \
        lambda state: state.has("Abyss Lava Ruins Trial Maid Enemy Barrier", player)
    multiworld.get_entrance("Abyss - Lava Ruins Trial magic switch -> Abyss - Trials Lobby", player).access_rule = \
        lambda state: state.has("Abyss Lava Ruins Trial Magic Switch", player)


def set_location_rules(world: "LWNWorld") -> None:
    multiworld = world.multiworld
    player = world.player
    options = world.options

    set_rule(multiworld.get_location("Shrine - Second magic switch", player),
             lambda state: state.has("Arcane", player) or state.has("Thunder", player))
    set_rule(multiworld.get_location("Shrine - Secret passage magic switch", player),
             lambda state: state.has("Fire", player) or state.has("Thunder", player))
    set_rule(multiworld.get_location("Secret Passage - First fire barrier magic switch", player),
             lambda state: state.has("Fire", player) or state.has("Thunder", player))
    set_rule(multiworld.get_location("Secret Passage - Second fire barrier magic switch", player),
             lambda state: state.has("Fire", player) or state.has("Thunder", player))
    set_rule(multiworld.get_location("Secret Passage - Enraged Armor", player),
             lambda state: state.has("Mana Absorption", player))
    set_rule(multiworld.get_location("Secret Passage - 56. Knight Kingdom Crown from Enraged Armor", player),
             lambda state: state.has("Mana Absorption", player))
    set_rule(multiworld.get_location("Secret Passage - Teleport from Enraged Armor", player),
             lambda state: state.has("Mana Absorption", player))
    set_rule(multiworld.get_location("Secret Passage - Defeat Enraged Armor barrier", player),
             lambda state: state.has("Mana Absorption", player))
    set_rule(multiworld.get_location("Underground - Arcane chest at bridge jumping puzzle", player),
             lambda state: state.has("Wind", player) or options.less_wind_requirements.value == Toggle.option_true)
    set_rule(multiworld.get_location("Underground - Magic barrier switches at maid enemy", player),
             lambda state: state.has("Ice", player))
    set_rule(multiworld.get_location("Underground - After fire magic switch", player),
             lambda state: state.has("Ice", player))
    set_rule(multiworld.get_location("Underground - Tania", player),
             lambda state: state.has("Mana Absorption", player))
    set_rule(multiworld.get_location("Underground - 98. Lost Maiden's Soul Shard from Tania", player),
             lambda state: state.has("Mana Absorption", player))
    set_rule(multiworld.get_location("Lava Ruins - Chest on scaffolding", player),
             lambda state: state.has("Wind", player) or (options.less_wind_requirements.value == Toggle.option_true and state.has("Fire", player)))
    set_rule(multiworld.get_location("Lava Ruins - Fire magic switch", player),
             lambda state: state.has("Fire", player) or state.has("Thunder", player))
    set_rule(multiworld.get_location("Lava Ruins - Jumping puzzle arcane chest at moving ring gauntlet", player),
             lambda state: state.has("Wind", player))
    set_rule(multiworld.get_location("Lava Ruins - Monica", player),
             lambda state: state.has("Mana Absorption", player))
    set_rule(multiworld.get_location("Lava Ruins - 34. Bestian Ear from Monica", player),
             lambda state: state.has("Mana Absorption", player))
    set_rule(multiworld.get_location("Lava Ruins - 33. Bestian Palm from Monica", player),
             lambda state: state.has("Mana Absorption", player))
    set_rule(multiworld.get_location("Lava Ruins - 99. Child's Soul Shard from Monica", player),
             lambda state: state.has("Mana Absorption", player))
    set_rule(multiworld.get_location("Dark Tunnel - 39. Dark Elf's Short Bow from barrel on scaffolding", player),
             lambda state: state.has("Wind", player) or (options.less_wind_requirements.value == Toggle.option_true and state.has("Fire", player)))
    set_rule(multiworld.get_location("Dark Tunnel - 45. Golden Coin from first mimic", player),
             lambda state: state.has("Fire", player))
    set_rule(multiworld.get_location("Dark Tunnel - 48. Chief's Skull from right mimic in mimic room", player),
             lambda state: state.has("Fire", player))
    set_rule(multiworld.get_location("Dark Tunnel - 49. Chief's Skull from straight mimic in mimic room", player),
             lambda state: state.has("Fire", player))
    set_rule(multiworld.get_location("Dark Tunnel - Thunder spell chest in mimic room", player),
             lambda state: state.has("Wind", player) or (options.less_wind_requirements.value == Toggle.option_true and state.has("Fire", player)))
    set_rule(multiworld.get_location("Dark Tunnel - Thunder barrier magic switches", player),
             lambda state: state.has("Thunder", player))
    set_rule(multiworld.get_location("Dark Tunnel - Floating platform switch one", player),
             lambda state: state.has("Thunder", player) or state.can_reach("Dark Tunnel - After floating platforms", player))
    set_rule(multiworld.get_location("Dark Tunnel - Floating platform switch two", player),
             lambda state: state.has("Thunder", player) or state.can_reach("Dark Tunnel - After floating platforms", player))
    set_rule(multiworld.get_location("Dark Tunnel - Floating platform switch three", player),
             lambda state: state.has("Thunder", player) or state.can_reach("Dark Tunnel - After floating platforms", player))
    set_rule(multiworld.get_location("Dark Tunnel - 71. Apocalypse Knight Record from knight enemy", player),
             lambda state: state.has("Wind", player) or (options.less_wind_requirements.value == Toggle.option_true and state.has("Fire", player)))
    set_rule(multiworld.get_location("Dark Tunnel - 103. Loyal Soul Shard from knight enemy", player),
             lambda state: state.has("Wind", player) or (options.less_wind_requirements.value == Toggle.option_true and state.has("Fire", player)))
    set_rule(multiworld.get_location("Dark Tunnel - Chest after knight enemy", player),
             lambda state: state.has("Wind", player) or (options.less_wind_requirements.value == Toggle.option_true and state.has("Fire", player)))
    set_rule(multiworld.get_location("Dark Tunnel - Vanessa", player),
             lambda state: state.has("Mana Absorption", player))
    set_rule(multiworld.get_location("Dark Tunnel - 100. King's Final Honor from Vanessa", player),
             lambda state: state.has("Mana Absorption", player))
    set_rule(multiworld.get_location("Dark Tunnel - 78. Ancient Throne Rune from Vanessa", player),
             lambda state: state.has("Mana Absorption", player))
    set_rule(multiworld.get_location("Dark Tunnel - 77. The Throne from Vanessa", player),
             lambda state: state.has("Mana Absorption", player))
    set_rule(multiworld.get_location("Spirit Realm - Ice spell chest in right side alcove", player),
             lambda state: state.has("Wind", player))
    set_rule(multiworld.get_location("Spirit Realm - Ice spell chest gate switch in right side alcove", player),
             lambda state: state.has("Wind", player))
    set_rule(multiworld.get_location("Spirit Realm - Arcane barrier magic switches", player),
             lambda state: state.has("Arcane", player))
    set_rule(multiworld.get_location("Spirit Realm - Platform shortcut switch", player),
             lambda state: state.has("Fire", player) and state.has("Thunder", player))
    set_rule(multiworld.get_location("Spirit Realm - Fire control magic switch", player),
             lambda state: state.has("Ice", player) or state.has("Thunder", player) or state.has("Spirit Realm Fire Deactivation", player))
    set_rule(multiworld.get_location("Spirit Realm - Magic switch barrier switch", player),
             lambda state: state.has("Spirit Realm Fire Deactivation", player))
    set_rule(multiworld.get_location("Spirit Realm - Teleporter magic switch", player),
             lambda state: (state.has("Spirit Realm Magic Switch Barrier", player) or (options.barrier_rando.value == Toggle.option_false and state.has("Thunder", player))) or state.has("Fire", player))
    set_rule(multiworld.get_location("Spirit Realm - Vanessa V2", player),
             lambda state: state.has("Mana Absorption", player))
    set_rule(multiworld.get_location("Spirit Realm - 101. Proud King's Crafted Soul Shard from Vanessa V2", player),
             lambda state: state.has("Mana Absorption", player))
    set_rule(multiworld.get_location("Spirit Realm - Thunder spell from Vanessa V2", player),
             lambda state: state.has("Mana Absorption", player))
    set_rule(multiworld.get_location("Abyss - 83. Castle Blueprint from crystal on brittle ledge", player),
             lambda state: state.has("Wind", player))
    set_rule(multiworld.get_location("Abyss - Underground trial magic switch", player),
             lambda state: state.has("Fire", player) or state.has("Thunder", player))
    set_rule(multiworld.get_location("Abyss - 91. Gaseous Soul Essence from scissor enemy in underground trial", player),
             lambda state: state.has("Fire", player) or state.has("Thunder", player))
    set_rule(multiworld.get_location("Abyss - Underground trial scissor enemy magic gate", player),
             lambda state: state.has("Fire", player) or state.has("Thunder", player))
    set_rule(multiworld.get_location("Abyss - Underground trial magic switch", player),
             lambda state: state.has("Fire", player) or state.has("Thunder", player))
    set_rule(multiworld.get_location("Abyss - Thunder spell chest dark tunnel trial", player),
             lambda state: state.has("Wind", player) or options.less_wind_requirements.value == Toggle.option_true)
    set_rule(multiworld.get_location("Abyss - 95. Refined Soul Shard from maid enemy in dark tunnel trial", player),
             lambda state: state.has("Thunder", player))
    set_rule(multiworld.get_location("Abyss - Dark tunnel trial maid enemy barrier", player),
             lambda state: state.has("Thunder", player))
    set_rule(multiworld.get_location("Abyss - Dark Tunnel trial magic switch", player),
             lambda state: state.has("Fire", player) or state.has("Thunder", player))
    set_rule(multiworld.get_location("Abyss - 93. Enchanted Soul Shard from maid enemy in lava ruins trial", player),
             lambda state: state.has("Fire", player) or state.has("Thunder", player) or state.has("Ice", player))
    set_rule(multiworld.get_location("Abyss - Lava Ruins trial defeat maids enemy barrier", player),
             lambda state: state.has("Fire", player) or state.has("Thunder", player) or state.has("Ice", player))
    set_rule(multiworld.get_location("Abyss - Lava Ruins trial magic switch", player),
             lambda state: state.has("Fire", player) or state.has("Thunder", player))
    set_rule(multiworld.get_location("Abyss - 102. Lost Maiden's Crafted Soul Shard from Nonota", player),
             lambda state: state.has("Mana Absorption", player))
    set_rule(multiworld.get_location("Abyss - Nonota", player),
             lambda state: state.has("Mana Absorption", player))

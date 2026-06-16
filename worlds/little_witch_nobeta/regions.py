from typing import Dict, Set, TYPE_CHECKING
from BaseClasses import Region

if TYPE_CHECKING:
    from . import LWNWorld


class LWNRegion(Region):
    game: str = "Little Witch Nobeta"


lwn_regions: Dict[str, Set[str]] = {
    "Shrine - Start": {"Shrine - After first magic switch"},
    "Shrine - After first magic switch": {"Shrine - Cat Room", "Shrine - Start"},
    "Shrine - Cat Room": {"Shrine - After first magic switch", "Shrine - Armor Hall"},
    "Shrine - Armor Hall": {"Secret passage - Start", "Secret passage - After first fire barrier", "Secret Passage - Boss Shortcut", "Shrine - Underground shortcut", "Shrine - Cat Room", "Underground - Start"},
    "Shrine - Underground shortcut": {"Shrine - Armor Hall", "Underground - Shrine shortcut"},
    "Secret passage - Start": {"Shrine - Armor Hall", "Secret passage - After first fire barrier"},
    "Secret passage - After first fire barrier": {"Secret passage - Start", "Secret Passage - Dark Tunnel shortcut", "Shrine - Armor Hall", "Secret Passage - Before Enraged Armor"},
    "Secret Passage - Before Enraged Armor": {"Secret passage - After first fire barrier", "Secret Passage - Enraged Armor"},
    "Secret Passage - Enraged Armor": {"Secret Passage - Boss Shortcut", "Secret Passage - Before Enraged Armor"},
    "Secret Passage - Boss Shortcut": {"Shrine - Armor Hall", "Secret Passage - Enraged Armor"},
    "Secret Passage - Dark Tunnel shortcut": {"Dark Tunnel - After bridge collapse", "Secret passage - After first fire barrier"},
    "Underground - Start": {"Underground - After wind", "Shrine - Armor Hall"},
    "Underground - After wind": {"Underground - Grand Hall", "Underground - Start"},
    "Underground - Grand Hall": {"Underground - After fire", "Underground - After wind", "Underground - Lava ruins shortcut", "Underground - Shrine shortcut", "Underground - Tania shortcut"},
    "Underground - Lava ruins shortcut": {"Underground - Grand Hall", "Underground - Shrine shortcut", "Lava Ruins - Path to dark tunnel"},
    "Underground - Shrine shortcut": {"Underground - Grand Hall", "Underground - Lava ruins shortcut", "Shrine - Underground shortcut"},
    "Underground - Tania shortcut": {"Underground - Grand Hall", "Underground - Tania"},
    "Underground - After fire": {"Underground - After fire magic switch barrier", "Underground - Grand Hall"},
    "Underground - After fire magic switch barrier": {"Underground - Tania", "Underground - After fire"},
    "Underground - Tania": {"Underground - Tania shortcut", "Underground - After fire magic switch barrier", "Lava Ruins - Start"},
    "Lava Ruins - Start": {"Lava Ruins - After magic platforms", "Lava Ruins - Monica warp", "Lava Ruins - Path to dark tunnel"},
    "Lava Ruins - After magic platforms": {"Lava Ruins - After scissor enemy barrier", "Lava Ruins - Start", "Lava Ruins - Scissor Enemy Room"},
    "Lava Ruins - Scissor Enemy Room": {"Lava Ruins - After magic platforms", "Lava Ruins - After scissor enemy barrier", "Lava Ruins - Lift Magic Switch Room", "Lava Ruins - Scissor Enemy Battle"},
    "Lava Ruins - Scissor Enemy Battle": set(),
    "Lava Ruins - Lift Magic Switch Room": set(),
    "Lava Ruins - After scissor enemy barrier": {"Lava Ruins - After Fire Barrier", "Lava Ruins - After Moving Ring", "Lava Ruins - Scissor Enemy Room", "Lava Ruins - Lift Magic Switch Room", "Lava Ruins - Scissor Enemy Battle"},
    "Lava Ruins - After Fire Barrier": {"Lava Ruins - After scissor enemy barrier", "Lava Ruins - Lava Ring Activation", "Lava Ruins - After Moving Ring"},
    "Lava Ruins - Lava Ring Activation": set(),
    "Lava Ruins - After Moving Ring": {"Lava Ruins - After Fire Barrier", "Lava Ruins - After scissor enemy barrier", "Lava Ruins - Monica", "Lava Ruins - Lava Ring Activation"},
    "Lava Ruins - Monica": {"Lava Ruins - After Fire Barrier", "Lava Ruins - Monica warp"},
    "Lava Ruins - Monica warp": {"Lava Ruins - Path to dark tunnel", "Lava Ruins - Start"},
    "Lava Ruins - Path to dark tunnel": {"Underground - Lava ruins shortcut", "Lava Ruins - Start", "Dark Tunnel - Start", "Underground - Tania"},
    "Dark Tunnel - Start": {"Dark Tunnel - After first magic barrier", "Lava Ruins - Path to dark tunnel", "Dark Tunnel - After first gate"},
    "Dark Tunnel - After first magic barrier": {"Dark Tunnel - Start", "Dark Tunnel - After first gate"},
    "Dark Tunnel - After first gate": {"Dark Tunnel - After first magic barrier", "Dark Tunnel - After light switch barrier", "Dark Tunnel - Start"},
    "Dark Tunnel - After light switch barrier": {"Dark Tunnel - Thunder barrier", "Dark Tunnel - Start"},
    "Dark Tunnel - Thunder barrier": {"Dark Tunnel - After light switch barrier", "Dark Tunnel - After thunder barrier"},
    "Dark Tunnel - After thunder barrier": {"Dark Tunnel - Thunder barrier", "Dark Tunnel - After floating platforms", "Dark Tunnel - Floating platform switches"},
    "Dark Tunnel - Floating platform switches": set(),
    "Dark Tunnel - After floating platforms": {"Dark Tunnel - After thunder barrier", "Dark Tunnel - After bridge collapse", "Dark Tunnel - Floating platform switches"},
    "Dark Tunnel - After bridge collapse": {"Spirit Realm - Start", "Secret Passage - Dark Tunnel shortcut", "Dark Tunnel - After floating platforms"},
    "Spirit Realm - Start": {"Spirit Realm - After platforms"},
    "Spirit Realm - After platforms": {"Spirit Realm - Start", "Spirit Realm - After second Seal", "Spirit Realm - After arcane barrier"},
    "Spirit Realm - After arcane barrier": {"Spirit Realm - After platforms", "Spirit Realm - Seal"},
    "Spirit Realm - Seal": {"Spirit Realm - After first Seal"},
    "Spirit Realm - After first Seal": {"Spirit Realm - Seal", "Spirit Realm - After second Seal"},
    "Spirit Realm - After second Seal": {"Spirit Realm - After first Seal", "Spirit Realm - After elevator", "Spirit Realm - After platforms"},
    "Spirit Realm - After elevator": {"Spirit Realm - After teleport", "Spirit Realm - After second Seal"},
    "Spirit Realm - After teleport": {"Spirit Realm - After elevator", "Abyss"},
    "Abyss": {"Abyss - After first teleport"},
    "Abyss - After first teleport": {"Abyss - After first gate"},
    "Abyss - After first gate": {"Abyss - After giant maid barrier", "Abyss - Trap gate"},
    "Abyss - Trap gate": {"Abyss - After first gate"},
    "Abyss - After giant maid barrier": {"Abyss - Trials Lobby"},
    "Abyss - Trials Lobby": {"Abyss - Underground Trial", "Abyss - Lava Ruins Trial", "Abyss - Dark Tunnel Trial", "Abyss - Nonota"},
    "Abyss - Underground Trial": {"Abyss - Underground Trial magic switch"},
    "Abyss - Underground Trial magic switch": {"Abyss - Trials Lobby"},
    "Abyss - Dark Tunnel Trial": {"Abyss - Dark Tunnel Trial magic switch"},
    "Abyss - Dark Tunnel Trial magic switch": {"Abyss - Trials Lobby"},
    "Abyss - Lava Ruins Trial": {"Abyss - Lava Ruins Trial magic switch"},
    "Abyss - Lava Ruins Trial magic switch": {"Abyss - Trials Lobby"},
    "Abyss - Nonota": set(),
}


def set_start_region(world: "LWNWorld"):
    options = world.options

    if options.starting_area.value == options.starting_area.option_shrine:
        world.origin_region_name = "Shrine - Start"
    elif options.starting_area.value == options.starting_area.option_underground:
        world.origin_region_name = "Underground - Start"
    elif options.starting_area.value == options.starting_area.option_lava_ruins:
        world.origin_region_name = "Lava Ruins - Start"
    elif options.starting_area.value == options.starting_area.option_dark_tunnel:
        world.origin_region_name = "Dark Tunnel - Start"

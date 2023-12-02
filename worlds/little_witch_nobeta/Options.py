from typing import Dict, Union
from dataclasses import dataclass
from BaseClasses import MultiWorld
from Options import Choice, Toggle, Range, PerGameCommonOptions

DefaultOffToggle = Toggle


class Goal(Choice):
    """
    The Goal of the game.
    [Vanilla] Reaching and beating Nonota will end the game.
    [Magic Master] All attack magics (arcane, ice, fire and thunder) must be level 5 before Nonota can be reached.
    [Boss Hunt] All bosses need to be killed before Nonota can be reached.
    """
    display_name = "Goal"
    option_vanilla = 1
    option_magic_master = 2
    option_boss_hunt = 3

    default = option_vanilla


class RandomizeBossSouls(DefaultOffToggle):
    """
    This option will itemize killed bosses into soul items that are added to the item pool.
    Only relevant for Boss Hunt goal. Does nothing for other goals.
    """
    display_name = "Randomize Boss Souls"


class TrialKeys(Range):
    """
    This setting will add keys to the item pool which are needed to open the teleports to each trial.
    Opening a trial is done by dropping a key on a trial path.
    Three keys are needed to end the game. Putting more keys in the item pool will speed up progression.
    """
    display_name = "Trial keys"
    range_start = 3
    range_end = 10
    default = 5


class NoArcane(DefaultOffToggle):
    """
    Nobeta will not be able to fire arcane magic. Only melee attack are possible until some form of magic is found.
    Arcane will still show up in the UI, but it will be impossible to fire arcane shots.
    """
    display_name = "Start without magic"


class EntranceRandomization(DefaultOffToggle):
    """
    Randomizes the start level and the destinations of doors/post-custcene level changes.
    """
    display_name = "Entrance randomization"


lwn_options: Dict[str, type] = {
    "goal": Goal,
    "randomizebosssouls": RandomizeBossSouls,
    "trialkeysamount": TrialKeys,
    "noarcane": NoArcane,
    "entrancerandomization": EntranceRandomization,
}


def get_option_value(world: MultiWorld, player: int, name: str) -> Union[bool, int]:
    option = getattr(world, name, None)

    if option is None:
        return 0

    if issubclass(lwn_options[name], Toggle):
        return bool(option[player].value)
    return option[player].value


@dataclass
class LWNOptions(PerGameCommonOptions):
    goal: Goal
    randomize_boss_souls: RandomizeBossSouls
    trial_keys: TrialKeys
    no_arcane: NoArcane
    entrance_randomization: EntranceRandomization

"""Module used to handle setting and randomizing bonus barrels."""
import random

import randomizer.Lists.Exceptions as Ex
from randomizer.Enums.Minigames import Minigames
from randomizer.Enums.Settings import MinigameBarrels, MinigamesListSelected
from randomizer.Lists.MapsAndExits import Maps
from randomizer.Lists.Minigame import BarrelMetaData, MinigameRequirements
from randomizer.Settings import Settings
from randomizer.Enums.Locations import Locations
from typing import List


def Reset(barrelLocations: List[Locations]) -> None:
    """Reset bonus barrel associations."""
    for key in barrelLocations:
        BarrelMetaData[key].minigame = Minigames.NoGame


def ShuffleBarrels(settings: Settings, barrelLocations: List[Locations], minigamePool: List[Minigames]) -> None:
    """Shuffle minigames to different barrels."""
    random.shuffle(barrelLocations)
    while len(barrelLocations) > 0:
        random.shuffle(minigamePool)
        location = barrelLocations.pop()
        # Don't bother shuffling or validating barrel locations which are skipped
        if BarrelMetaData[location].map == Maps.HideoutHelm and settings.helm_barrels == MinigameBarrels.skip:
            continue
        elif BarrelMetaData[location].map != Maps.HideoutHelm and settings.bonus_barrels == MinigameBarrels.skip:
            continue
        # Check each remaining minigame to see if placing it will produce a valid world
        success = False
        helm_minigame_available = False
        for minigame in minigamePool:
            # Check if any minigames can be placed in helm
            if MinigameRequirements[minigame].helm_enabled:
                helm_minigame_available = True
        for minigame in minigamePool:
            # If this minigame isn't a minigame for the kong of this location, don't use it
            if BarrelMetaData[location].kong not in MinigameRequirements[minigame].kong_list:
                continue
            # If there is a minigame that can be placed in Helm, skip banned minigames, otherwise continue as normal
            if not MinigameRequirements[minigame].helm_enabled and BarrelMetaData[location].map == Maps.HideoutHelm and helm_minigame_available is True:
                continue
            # Place the minigame
            BarrelMetaData[location].minigame = minigame
            success = True
        if not success:
            raise Ex.BarrelOutOfMinigames


def BarrelShuffle(settings: Settings) -> None:
    """Facilitate shuffling of barrels."""
    # First make master copies of locations and minigames
    barrelLocations = list(BarrelMetaData.keys())
    if settings.bonus_barrels == MinigameBarrels.selected or (settings.helm_barrels == MinigameBarrels.random and settings.minigames_list_selected):
        minigame_dict = {
            MinigamesListSelected.batty_barrel_bandit: [Minigames.BattyBarrelBanditVEasy, Minigames.BattyBarrelBanditEasy, Minigames.BattyBarrelBanditNormal, Minigames.BattyBarrelBanditHard],
            MinigamesListSelected.big_bug_bash: [Minigames.BigBugBashVEasy, Minigames.BigBugBashEasy, Minigames.BigBugBashNormal, Minigames.BigBugBashHard],
            MinigamesListSelected.busy_barrel_barrage: [Minigames.BusyBarrelBarrageEasy, Minigames.BusyBarrelBarrageNormal, Minigames.BusyBarrelBarrageHard],
            MinigamesListSelected.mad_maze_maul: [Minigames.MadMazeMaulEasy, Minigames.MadMazeMaulNormal, Minigames.MadMazeMaulHard, Minigames.MadMazeMaulInsane],
            MinigamesListSelected.minecart_mayhem: [Minigames.MinecartMayhemEasy, Minigames.MinecartMayhemNormal, Minigames.MinecartMayhemHard],
            MinigamesListSelected.beaver_bother: [Minigames.BeaverBotherEasy, Minigames.BeaverBotherNormal, Minigames.BeaverBotherHard],
            MinigamesListSelected.teetering_turtle_trouble: [
                Minigames.TeeteringTurtleTroubleVEasy,
                Minigames.TeeteringTurtleTroubleEasy,
                Minigames.TeeteringTurtleTroubleNormal,
                Minigames.TeeteringTurtleTroubleHard,
            ],
            MinigamesListSelected.stealthy_snoop: [Minigames.StealthySnoopVEasy, Minigames.StealthySnoopEasy, Minigames.StealthySnoopNormal, Minigames.StealthySnoopHard],
            MinigamesListSelected.stash_snatch: [Minigames.StashSnatchEasy, Minigames.StashSnatchNormal, Minigames.StashSnatchHard, Minigames.StashSnatchInsane],
            MinigamesListSelected.splish_splash_salvage: [Minigames.SplishSplashSalvageEasy, Minigames.SplishSplashSalvageNormal, Minigames.SplishSplashSalvageHard],
            MinigamesListSelected.speedy_swing_sortie: [Minigames.SpeedySwingSortieEasy, Minigames.SpeedySwingSortieNormal, Minigames.SpeedySwingSortieHard],
            MinigamesListSelected.krazy_kong_klamour: [Minigames.KrazyKongKlamourEasy, Minigames.KrazyKongKlamourNormal, Minigames.KrazyKongKlamourHard, Minigames.KrazyKongKlamourInsane],
            MinigamesListSelected.searchlight_seek: [Minigames.SearchlightSeekVEasy, Minigames.SearchlightSeekEasy, Minigames.SearchlightSeekNormal, Minigames.SearchlightSeekHard],
            MinigamesListSelected.kremling_kosh: [Minigames.KremlingKoshVEasy, Minigames.KremlingKoshEasy, Minigames.KremlingKoshNormal, Minigames.KremlingKoshHard],
            MinigamesListSelected.peril_path_panic: [Minigames.PerilPathPanicVEasy, Minigames.PerilPathPanicEasy, Minigames.PerilPathPanicNormal, Minigames.PerilPathPanicHard],
            MinigamesListSelected.helm_minigames: [
                Minigames.DonkeyRambi,
                Minigames.DonkeyTarget,
                Minigames.DiddyKremling,
                Minigames.DiddyRocketbarrel,
                Minigames.LankyMaze,
                Minigames.LankyShooting,
                Minigames.TinyMushroom,
                Minigames.TinyPonyTailTwirl,
                Minigames.ChunkyHiddenKremling,
                Minigames.ChunkyShooting,
            ],
            MinigamesListSelected.arenas: [Minigames.RambiArena, Minigames.EnguardeArena],
        }
        minigamePool = []
        for name, value in minigame_dict.items():
            if name in settings.minigames_list_selected:
                minigamePool.extend([x for x in MinigameRequirements.keys() if x in value])
    else:
        minigamePool = [x for x in MinigameRequirements.keys() if x != Minigames.NoGame]
    # Shuffle barrels
    Reset(barrelLocations)
    ShuffleBarrels(settings, barrelLocations.copy(), minigamePool.copy())
    return

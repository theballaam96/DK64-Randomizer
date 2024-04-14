"""Randomize Boss Locations."""

import random
from array import array

from randomizer.Enums.Items import Items
from randomizer.Enums.Kongs import Kongs
from randomizer.Enums.Locations import Locations
from randomizer.Enums.Settings import HardModeSelected
from randomizer.Lists.Exceptions import BossOutOfLocationsException, FillException, ItemPlacementException
from randomizer.Enums.Maps import Maps
from randomizer.Patching.Lib import IsItemSelected

BossMapList = [Maps.JapesBoss, Maps.AztecBoss, Maps.FactoryBoss, Maps.GalleonBoss, Maps.FungiBoss, Maps.CavesBoss, Maps.CastleBoss]
KRoolMaps = [Maps.KroolDonkeyPhase, Maps.KroolDiddyPhase, Maps.KroolLankyPhase, Maps.KroolTinyPhase, Maps.KroolChunkyPhase]

def getBosses(settings) -> list:
    """Get list of bosses."""
    boss_maps = BossMapList.copy()
    if settings.krool_in_boss_pool:
        boss_maps.extend(KRoolMaps.copy())
    return [x for x in boss_maps if x not in settings.krool_order]


def ShuffleBosses(boss_location_rando: bool, settings):
    """Shuffle boss locations."""
    boss_maps = getBosses(settings)
    if boss_location_rando:
        random.shuffle(boss_maps)
    return boss_maps


def HardBossesEnabled(settings) -> bool:
    """Return whether the hard bosses setting is on."""
    return IsItemSelected(settings.hard_mode, settings.hard_mode_selected, HardModeSelected.hard_bosses)


def ShuffleBossKongs(settings):
    """Shuffle the kongs required for the bosses."""
    vanillaBossKongs = {
        Maps.JapesBoss: Kongs.donkey,
        Maps.AztecBoss: Kongs.diddy,
        Maps.FactoryBoss: Kongs.tiny,
        Maps.GalleonBoss: Kongs.lanky,
        Maps.FungiBoss: Kongs.chunky,
        Maps.CavesBoss: Kongs.donkey,
        Maps.CastleBoss: Kongs.lanky,
        Maps.KroolDonkeyPhase: Kongs.donkey,
        Maps.KroolDiddyPhase: Kongs.diddy,
        Maps.KroolLankyPhase: Kongs.lanky,
        Maps.KroolTinyPhase: Kongs.tiny,
        Maps.KroolChunkyPhase: Kongs.chunky,
    }

    boss_kongs = []
    for level in range(7):
        boss_map = settings.boss_maps[level]
        if settings.boss_kong_rando:
            kong = SelectRandomKongForBoss(boss_map, HardBossesEnabled(settings))
        else:
            kong = vanillaBossKongs[boss_map]
        boss_kongs.append(kong)

    return boss_kongs


def SelectRandomKongForBoss(boss_map: Maps, hard_bosses: bool):
    """Randomly choses from the allowed list for the boss."""
    possibleKongs = []
    if boss_map == Maps.JapesBoss:
        possibleKongs = [Kongs.donkey, Kongs.diddy, Kongs.lanky, Kongs.tiny, Kongs.chunky]
    elif boss_map == Maps.AztecBoss:
        possibleKongs = [Kongs.donkey, Kongs.diddy, Kongs.lanky, Kongs.tiny, Kongs.chunky]
    elif boss_map == Maps.FactoryBoss:
        if hard_bosses:
            possibleKongs = [Kongs.donkey, Kongs.tiny, Kongs.chunky]
        else:
            possibleKongs = [Kongs.tiny]
    elif boss_map == Maps.GalleonBoss:
        possibleKongs = [Kongs.donkey, Kongs.diddy, Kongs.lanky, Kongs.tiny, Kongs.chunky]
    elif boss_map == Maps.FungiBoss:
        possibleKongs = [Kongs.chunky]
    elif boss_map == Maps.CavesBoss:
        possibleKongs = [Kongs.donkey, Kongs.diddy, Kongs.lanky, Kongs.tiny, Kongs.chunky]
    elif boss_map == Maps.CastleBoss:
        possibleKongs = [Kongs.donkey, Kongs.diddy, Kongs.lanky, Kongs.tiny, Kongs.chunky]
    elif boss_map in (Maps.KroolDonkeyPhase, Maps.KroolDiddyPhase, Maps.KroolLankyPhase, Maps.KroolTinyPhase, Maps.KroolChunkyPhase):
        # Not possible right now to make any other kong beat another's phase, however, if we were to do so:
        # DK Phase - Make all kongs enter cannon barrels
        # Other phases - ????????
        possibleKongs = [Kongs.donkey + (boss_map - Maps.KroolDonkeyPhase)]
    return random.choice(possibleKongs)


def ShuffleKutoutKongs(boss_maps: array, boss_kongs: array, boss_kong_rando: bool):
    """Shuffle the Kutout kong order."""
    vanillaKutoutKongs = [Kongs.lanky, Kongs.tiny, Kongs.chunky, Kongs.donkey, Kongs.diddy]
    kutout_kongs = []
    if boss_kong_rando:
        if Maps.CastleBoss in boss_maps:
            kutoutLocation = boss_maps.index(Maps.CastleBoss)
            if kutoutLocation < 0 or kutoutLocation >= len(boss_kongs):
                starting_kong = random.choice(vanillaKutoutKongs)
            else:
                starting_kong = boss_kongs[kutoutLocation]
        else:
            starting_kong = random.choice(vanillaKutoutKongs)
        kongPool = vanillaKutoutKongs.copy()
        kongPool.remove(starting_kong)
        random.shuffle(kongPool)

        kutout_kongs.append(starting_kong)
        kutout_kongs.extend(kongPool)
    else:
        kutout_kongs = vanillaKutoutKongs
    return kutout_kongs


def ShuffleKKOPhaseOrder(settings):
    """Shuffle the phase order in King Kut Out."""
    kko_phases = [0, 1, 2, 3]
    random.shuffle(kko_phases)
    kko_phase_subset = []
    for phase_slot in range(3):
        kko_phase_subset.append(kko_phases[phase_slot])
    return kko_phase_subset.copy()


def ShuffleBossesBasedOnOwnedItems(settings, ownedKongs: dict, ownedMoves: dict):
    """Perform Boss Location & Boss Kong rando, ensuring each first boss can be beaten with an unlocked kong and owned moves."""
    try:
        bossLevelOptions = {0, 1, 2, 3, 4, 5, 6}
        # Find levels we can place Dogadon 2 (most restrictive)
        forestBossOptions = [x for x in bossLevelOptions if Kongs.chunky in ownedKongs[x] and Items.HunkyChunky in ownedMoves[x] and Items.Barrels in ownedMoves[x]]
        if not settings.kong_rando and not settings.boss_location_rando and 4 not in forestBossOptions:
            raise ItemPlacementException("Items not placed to allow vanilla Dogadon 2.")
        # Then find levels we can place Mad jack (next most restrictive)
        tinyFactoryBossOptions = [
            x for x in bossLevelOptions if Kongs.tiny in ownedKongs[x] and Items.PonyTailTwirl in ownedMoves[x] and (settings.start_with_slam or Items.ProgressiveSlam in ownedMoves[x])
        ]
        donkeyFactoryBossOptions = []
        chunkyFactoryBossOptions = []
        if HardBossesEnabled(settings):
            if settings.krusha_kong != Kongs.tiny:
                tinyFactoryBossOptions = [x for x in bossLevelOptions if Kongs.tiny in ownedKongs[x] and (settings.start_with_slam or Items.ProgressiveSlam in ownedMoves[x])]
            if settings.krusha_kong != Kongs.donkey:
                donkeyFactoryBossOptions = [x for x in bossLevelOptions if Kongs.donkey in ownedKongs[x] and (settings.start_with_slam or Items.ProgressiveSlam in ownedMoves[x])]
            if settings.krusha_kong != Kongs.chunky:
                chunkyFactoryBossOptions = [x for x in bossLevelOptions if Kongs.chunky in ownedKongs[x] and (settings.start_with_slam or Items.ProgressiveSlam in ownedMoves[x])]
        factoryBossOptions = list(set(tinyFactoryBossOptions + donkeyFactoryBossOptions + chunkyFactoryBossOptions))
        # This sequence of placing Dogadon 2 and Mad Jack will only fail if both Hunky Chunky and Twirl are placed in level 7
        # If we have fewer options for Dogadon 2, place that first
        forestBossKong = None
        bossTryingToBePlaced = "Dogadon 2"
        if len(forestBossOptions) < len(factoryBossOptions):
            forestBossIndex = random.choice(forestBossOptions)
            forestBossKong = Kongs.chunky
            if forestBossIndex in factoryBossOptions:
                factoryBossOptions.remove(forestBossIndex)
        # Otherwise place Factory first
        bossTryingToBePlaced = "Mad Jack"
        if HardBossesEnabled(settings):
            factoryBossIndex = random.choice(factoryBossOptions)
            factoryBossKongOptions = []
            if factoryBossIndex in tinyFactoryBossOptions:
                factoryBossKongOptions.append(Kongs.tiny)
            if factoryBossIndex in donkeyFactoryBossOptions:
                factoryBossKongOptions.append(Kongs.donkey)
            if factoryBossIndex in chunkyFactoryBossOptions:
                factoryBossKongOptions.append(Kongs.chunky)
            factoryBossKong = random.choice(factoryBossKongOptions)
        else:
            factoryBossIndex = random.choice(factoryBossOptions)
            factoryBossKong = Kongs.tiny
        if factoryBossIndex in forestBossOptions:
            forestBossOptions.remove(factoryBossIndex)
        # Then place Dogadon 2 (if Mad Jack was placed first)
        if forestBossKong is None:
            bossTryingToBePlaced = "Dogadon 2 (second)"
            forestBossIndex = random.choice(forestBossOptions)
            forestBossKong = Kongs.chunky

        bossLevelOptions.remove(forestBossIndex)
        bossLevelOptions.remove(factoryBossIndex)

        # Place the barrels-required bosses
        bossTryingToBePlaced = "barrels-locked bosses"
        barrelsBossOptions = [x for x in bossLevelOptions if Items.Barrels in ownedMoves[x]]
        random.shuffle(barrelsBossOptions)
        cavesBossIndex = barrelsBossOptions.pop()
        cavesBossKong = random.choice(ownedKongs[cavesBossIndex])
        bossLevelOptions.remove(cavesBossIndex)
        japesBossIndex = barrelsBossOptions.pop()
        japesBossKong = random.choice(ownedKongs[japesBossIndex])
        bossLevelOptions.remove(japesBossIndex)
        aztecBossIndex = barrelsBossOptions.pop()
        aztecBossKong = random.choice(ownedKongs[aztecBossIndex])
        bossLevelOptions.remove(aztecBossIndex)

        # Place the last 2 freely
        bossTryingToBePlaced = "the easy bosses to place (if this breaks here something REALLY strange happened)"
        remainingBosses = list(bossLevelOptions)
        random.shuffle(remainingBosses)
        galleonBossIndex = remainingBosses.pop()
        galleonBossKong = random.choice(ownedKongs[galleonBossIndex])
        castleBossIndex = remainingBosses.pop()
        castleBossKong = random.choice(ownedKongs[castleBossIndex])
        newBossMaps = []
        newBossKongs = []
        for level in range(0, 7):
            if level == japesBossIndex:
                newBossMaps.append(Maps.JapesBoss)
                newBossKongs.append(japesBossKong)
            elif level == aztecBossIndex:
                newBossMaps.append(Maps.AztecBoss)
                newBossKongs.append(aztecBossKong)
            elif level == factoryBossIndex:
                newBossMaps.append(Maps.FactoryBoss)
                newBossKongs.append(factoryBossKong)
            elif level == galleonBossIndex:
                newBossMaps.append(Maps.GalleonBoss)
                newBossKongs.append(galleonBossKong)
            elif level == forestBossIndex:
                newBossMaps.append(Maps.FungiBoss)
                newBossKongs.append(forestBossKong)
            elif level == cavesBossIndex:
                newBossMaps.append(Maps.CavesBoss)
                newBossKongs.append(cavesBossKong)
            elif level == castleBossIndex:
                newBossMaps.append(Maps.CastleBoss)
                newBossKongs.append(castleBossKong)
        # print("New Boss Order: " + str(newBossMaps))
        # print("New Boss Kongs: " + str(newBossKongs))
        if len(newBossMaps) < 7:
            raise FillException("Invalid boss order with fewer than the 7 required main levels.")
    except Exception as ex:
        if isinstance(ex.args[0], str) and "index out of range" in ex.args[0]:
            print("Unlucky move placement fill :(")
            raise BossOutOfLocationsException("No valid locations to place " + bossTryingToBePlaced)
        if isinstance(ex.args[0], str) and "pop from empty list" in ex.args[0]:
            print("Barrels bad.")
            raise BossOutOfLocationsException("No valid locations to place " + bossTryingToBePlaced)
        raise FillException("Something went wrong while assigning bosses.")

    # Only apply this shuffle if the settings permit it
    # If kongs are random we have to shuffle bosses and locations or else we might break logic
    if settings.kong_rando or settings.boss_location_rando:
        settings.boss_maps = newBossMaps
    else:
        settings.boss_maps = getBosses(settings)
    if settings.kong_rando or settings.boss_kong_rando:
        # If we shuffle kongs but not locations, we must forcibly sort the array with the known valid kongs
        if not settings.boss_location_rando:
            settings.boss_kongs = [japesBossKong, aztecBossKong, factoryBossKong, galleonBossKong, forestBossKong, cavesBossKong, castleBossKong]
        else:
            settings.boss_kongs = newBossKongs
    else:
        settings.boss_kongs = ShuffleBossKongs(settings)
    settings.kutout_kongs = ShuffleKutoutKongs(settings.boss_maps, settings.boss_kongs, settings.boss_kong_rando)


def ShuffleTinyPhaseToes():
    """Generate random assortment of toes for Tiny Phase."""
    toe_sequence = []
    previous_toe = 1  # Use 1 as the index as it's within distance of all toes, so all toes for the first in the sequence will be valid
    for toe in range(10):
        mode = random.randint(0, 10)
        if (toe % 5) == 0:
            # Prevent player position mode on the first toe
            mode += 1
        if mode == 0:
            # Use player position
            toe_sequence.append(0xFF)
            previous_toe = 1
        else:
            # Determine random assortment
            toe_list = list(range(4))
            if (toe % 5) == 0:
                # First toe
                toe_list = [0, 2, 3]
            toe_list = [x for x in toe_list if abs(x - previous_toe) < 3]  # Prevent toes being selected that
            toe_count = random.randint(1, min(3, len(toe_list) - 1))
            if len(toe_list) <= 1:
                toe_bitfield = 0
            else:
                activated_toes = random.sample(toe_list, toe_count)
                unactivated_toes = [x for x in list(range(4)) if x not in activated_toes]
                picked_toe = False
                for t in (1, 2):
                    if t in unactivated_toes:
                        previous_toe = t
                        picked_toe = True
                if not picked_toe:
                    previous_toe = random.choice(unactivated_toes)
                toe_bitfield = 0
                for toe in activated_toes:
                    toe_bitfield |= 1 << toe
            toe_sequence.append(toe_bitfield)
    return toe_sequence.copy()


def CorrectBossKongLocations(spoiler):
    """Correct the Kong assigned to each boss Location for more accurate hints."""
    spoiler.LocationList[Locations.JapesKey].kong = spoiler.settings.boss_kongs[0]
    spoiler.LocationList[Locations.AztecKey].kong = spoiler.settings.boss_kongs[1]
    spoiler.LocationList[Locations.FactoryKey].kong = spoiler.settings.boss_kongs[2]
    spoiler.LocationList[Locations.GalleonKey].kong = spoiler.settings.boss_kongs[3]
    spoiler.LocationList[Locations.ForestKey].kong = spoiler.settings.boss_kongs[4]
    spoiler.LocationList[Locations.CavesKey].kong = spoiler.settings.boss_kongs[5]
    spoiler.LocationList[Locations.CastleKey].kong = spoiler.settings.boss_kongs[6]

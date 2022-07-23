"""Region enum."""
from enum import IntEnum, auto


class Regions(IntEnum):
    """Region enum."""

    # DK Isles Regions
    Treehouse = auto()
    TrainingGrounds = auto()
    IslesMain = auto()
    IslesMainUpper = auto()
    Prison = auto()
    BananaFairyRoom = auto()
    JungleJapesLobby = auto()
    AngryAztecLobby = auto()
    CrocodileIsleBeyondLift = auto()
    IslesSnideRoom = auto()
    FranticFactoryLobby = auto()
    GloomyGalleonLobby = auto()
    CabinIsle = auto()
    FungiForestLobby = auto()
    CrystalCavesLobby = auto()
    CreepyCastleLobby = auto()
    HideoutHelmLobby = auto()
    KRool = auto()

    # Jungle Japes Regions
    JungleJapesMain = auto()
    JapesBeyondPeanutGate = auto()
    JapesBeyondCoconutGate1 = auto()
    JapesBeyondFeatherGate = auto()
    TinyHive = auto()
    JapesBeyondCoconutGate2 = auto()
    BeyondRambiGate = auto()
    JapesLankyCave = auto()
    Mine = auto()
    JapesTopOfMountain = auto()
    JapesMinecarts = auto()
    JapesCatacomb = auto()
    JapesBossLobby = auto()
    JapesBoss = auto()
    JapesBaboonBlast = auto()

    # Angry Aztec Regions
    AngryAztecStart = auto()
    TempleStart = auto()
    TempleUnderwater = auto()
    AngryAztecMain = auto()
    AztecDonkeyQuicksandCave = auto()
    DonkeyTemple = auto()
    DiddyTemple = auto()
    LankyTemple = auto()
    TinyTemple = auto()
    ChunkyTemple = auto()
    AztecTinyRace = auto()
    LlamaTemple = auto()
    LlamaTempleBack = auto()
    AztecBossLobby = auto()
    AztecBoss = auto()
    AztecBaboonBlast = auto()

    # Frantic Factory Regions
    FranticFactoryStart = auto()
    Testing = auto()
    RandD = auto()
    FactoryTinyRaceLobby = auto()
    FactoryTinyRace = auto()
    ChunkyRoomPlatform = auto()
    PowerHut = auto()
    BeyondHatch = auto()
    InsideCore = auto()
    MainCore = auto()
    FactoryBossLobby = auto()
    FactoryBoss = auto()
    FactoryBaboonBlast = auto()

    # Gloomy Galleon Regions
    GloomyGalleonStart = auto()
    GalleonBeyondPineappleGate = auto()
    LighthouseArea = auto()
    Lighthouse = auto()
    MermaidRoom = auto()
    SickBay = auto()
    Shipyard = auto()
    SealRace = auto()
    TreasureRoom = auto()
    TreasureRoomDiddyGoldTower = auto()
    TinyChest = auto()
    Submarine = auto()
    Mechafish = auto()
    LankyShip = auto()
    TinyShip = auto()
    BongosShip = auto()
    GuitarShip = auto()
    TromboneShip = auto()
    SaxophoneShip = auto()
    TriangleShip = auto()
    GalleonBossLobby = auto()
    GalleonBoss = auto()
    GalleonBaboonBlast = auto()

    # Fungi Forest Regions
    FungiForestStart = auto()
    ForestMinecarts = auto()
    GiantMushroomArea = auto()
    MushroomLower = auto()
    MushroomLowerExterior = auto()
    MushroomUpper = auto()
    MushroomNightDoor = auto()
    MushroomNightExterior = auto()
    MushroomUpperExterior = auto()
    MushroomChunkyRoom = auto()
    MushroomLankyZingersRoom = auto()
    MushroomLankyMushroomsRoom = auto()
    HollowTreeArea = auto()
    Anthill = auto()
    MillArea = auto()
    MillChunkyArea = auto()
    MillTinyArea = auto()
    SpiderRoom = auto()
    GrinderRoom = auto()
    MillRafters = auto()
    WinchRoom = auto()
    MillAttic = auto()
    ThornvineArea = auto()
    ThornvineBarn = auto()
    WormArea = auto()
    ForestBossLobby = auto()
    ForestBoss = auto()
    ForestBaboonBlast = auto()

    # Crystal Caves Regions
    CrystalCavesMain = auto()
    CavesBlueprintCave = auto()
    CavesBonusCave = auto()
    CavesBlueprintPillar = auto()
    CavesBananaportSpire = auto()
    BoulderCave = auto()
    CavesLankyRace = auto()
    FrozenCastle = auto()
    IglooArea = auto()
    GiantKosha = auto()
    DonkeyIgloo = auto()
    DiddyIgloo = auto()
    LankyIgloo = auto()
    TinyIgloo = auto()
    ChunkyIgloo = auto()
    CabinArea = auto()
    RotatingCabin = auto()
    DonkeyCabin = auto()
    DiddyLowerCabin = auto()
    DiddyUpperCabin = auto()
    LankyCabin = auto()
    TinyCabin = auto()
    ChunkyCabin = auto()
    CavesBossLobby = auto()
    CavesBoss = auto()
    CavesBaboonBlast = auto()

    # Creepy Castle Regions
    CreepyCastleMain = auto()
    CastleWaterfall = auto()
    CastleTree = auto()
    Library = auto()
    Ballroom = auto()
    MuseumBehindGlass = auto()
    CastleTinyRace = auto()
    Tower = auto()
    Greenhouse = auto()
    TrashCan = auto()
    Shed = auto()
    Museum = auto()
    LowerCave = auto()
    Crypt = auto()
    CastleMinecarts = auto()
    Mausoleum = auto()
    UpperCave = auto()
    Dungeon = auto()
    CastleBossLobby = auto()
    CastleBoss = auto()
    CastleBaboonBlast = auto()

    # Hideout Helm Regions
    HideoutHelmStart = auto()
    HideoutHelmMain = auto()

    # Shop Regions
    FunkyGeneric = auto()
    FunkyJapes = auto()
    FunkyAztec = auto()
    FunkyFactory = auto()
    FunkyGalleon = auto()
    FunkyForest = auto()
    FunkyCaves = auto()
    FunkyCastle = auto()
    CandyGeneric = auto()
    CandyAztec = auto()
    CandyFactory = auto()
    CandyGalleon = auto()
    CandyCaves = auto()
    CandyCastle = auto()
    CrankyGeneric = auto()
    CrankyJapes = auto()
    CrankyAztec = auto()
    CrankyFactory = auto()
    CrankyGalleon = auto()
    CrankyForest = auto()
    CrankyCaves = auto()
    CrankyCastle = auto()
    Snide = auto()

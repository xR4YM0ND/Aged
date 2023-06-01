*****
# Known Bugs / To Do
*****
## Mods

### AdditionZ
- Normal Oxidization (when placed normal 1 next to another 1 should be same speed as vanilla 1 block 3 air 1 block)
- Fast Oxidization (with lava & water - should be 4x of the vanilla 1 block 3 space 1 block speed)
- **[IDEA]** TNT Tennis (2023 April Fools update)
- Shield Cooldown compatible with the mod Guarding ? - Needs testing
- waterbottles can be emptyed underwater (no block facing) -> Purified Water Bottle empty when right click in water instead of consume
- **[IDEA]** While holding the sprint key you can't jump...
- **[IDEA]** Hydration radius from liquid water (flowing & still source) changeable via config

### Another World
- Disable Nether Portal creation (diable flint/steel on portal frame, disable creation (from nether to another:world))
- deny outgoing nether portal connection
- deny incoming nether portal connection

### BackSlot
- Backslot overlaps with environmentz (move Backslot HUD x coordinate)

### Dehydration
- **[IDEA]** combine purified water bottle & flask to fill the flask in crafting table -> bottle gets destroyed
- **[IDEA]** Enchantment for Flasks (Purification) -> rare find
- **[IDEA]** bubbled water (soulsand/magma) gives you purified water
- **[IDEA]** Copper Cauldron Campfire holds more water

### Early Stage
- **[IDEA]** Clay Bucket (Clay Brick Bucket for lava one time use)
- **[IDEA]** When you stripp log they drop bark which acts as *Zunder* (needed for starting campfires)
- **[IDEA]** Fire Starting Sticks with durability and chance to lit the campfire (When you place a campfire it's unlit)
- **[IDEA]** Fire Wood -> 1 Wood gives 4 Fire wood in the stonecutter (1 Firewood smelts the same as 1 Wood)
- **[IDEA]** Campfires are crafted with Fire wood
- **[IDEA]** Campfires run out of fire wood after x amount of time
- **[IDEA]** Stick scaffolding (with sticks instead of bamboo)

### EnvironmentZ
- Item value is actually doubled (Ice pack -20, Heating stones +20, ...)

### InmisAddon
- Inmis Addon tab centers mouse when clicked on

### Numismatic Claim
- **[IDEA]** A Trading Block that acts like a special trader where you can ask outer cities for resources (costs coins and takes time till they answer) (different cities offer/ask different trades which update every x ticks) (like an outer connection trades for boat / harbor)

### DungeonZ
- **[Idea]** Boss phases (Boss is damage 2/3 , monsters spawn & you have to kill all mobs first to damage the Boss again) (like different stages for the boss fight)
- **[Idea]** Add barrels as separate loot table \(eg. *Food Supply*)

### LevelZ
- Max Mobs kill drops in a chunk (exlude some mobs (ender dragon / bosses / ...))
- add hoe in github readme (3.Item (5 different not 4 different, you forgot the hoe))
- clicking in sub categorys on the name (upper left) takes you back to the main levelz screen (same as pressing "E")
- add outline to icons in levelz screen when they are hovered (second icon texture)
- mining locked xp blocks (like calcite coal ore), they don't drop items but xp
- Sometimes the Level before the name (over the player) is 0

### TieredZ
- Items (Swords/Axes/..) that are placed in item frames on generation (BetterDungeons / BetterDesertTemples / ..) are vanilla , they dont have tiers - Done
- same for armor in armor stands on generation - Done
- Extra slot in Anvil (Addition Slot -> items for rarity that get used once when place in (1 item always makes rare on upgrade, other always epic, etc..))
- TieredZ aint working with Crafting Rock
- Wooden shield don't get modifiers (maybe cause of shild tag error with fabric shield lib)
- if inventory is full you can see the output modifiers of items before crafting (https://discord.com/channels/745451299713056791/745454651536834630/1108890383594836012)
- **[IDEA]** Extra attributes for elytras (maybe increased rocket duration, durability, speed) cause now they use armor attributes

### SpoiledZ
- \(Cooking folder) - Bowl use on Blocks - Stuffed Pumpkin Block from Farmer's Delight not spoiled
- Food Blocks you place down ( Cake , Apple Pie(Vinery Mod) , other modded ) dont get spoiled
- Crash with [Farmers Respite "Rose Hip Pie"](https://beta.curseforge.com/minecraft/mc-mods/farmers-respite-fabric) -> [latest.log](https://gist.github.com/SpigotDE/1d055f0e746194d5c284b9ef9bd99ef7) -> [updated latest.log with xaero ?](https://gist.github.com/SpigotDE/67ff7c6e4791a89cce6aa7342dce8d23)
- **[IDEA]** combine food with salt / sugar (only some foods) to increase the duration upon combining
- **[IDEA]** Farmland needs crop rotation (maybe seasons compat / every season another crop so the soil stays fresh (3 years max cicle))
- **[IDEA]** Farmland desease (crops can get infected / maybe combine with crop rotation) (you can leave farmland without crops for better values (brach legen))
- **[IDEA]** The Composter acutally produces compost which can raise the farmlands fertile value (increases farmland fertile value more than sand)
- **[IDEA]** Farmland has a Fertile Values which can be decreased slightly with clay and increased slightly with sand (different crops grow better at different feritle values / also the more the wrong fertile value for the crop, the more likely the crop will get desease)

### FarmZ
- **[IDEA]** Adjust Water Hydration range in config (vanilla = 4 , FarmZ default = 1)
- **[IDEA]** Watering Can's (Radius: Copper = 1, Iron = 2, Gold = 3, Diamond = 4, Netherite = 5) (Inspired by Stardew Valley)
- **[IDEA]** Add Sprinklers that trigger after x amount of ticks (Tiers: Copper, Iron, Gold, Diamond, Netherite) (Same Range as Watering Can's) (need to have access to Water pipes)
- **[IDEA]** Sprinklers facing south / placed at ceeling with pipes and sprinkle down
- **[IDEA]** Water pipes (Wood channel where top is opened, Stone channel where to is opened, Copper pipes, Iron, gold, diamond, netherite)
- **[IDEA]** Mechanical pump for pipes going upwards (Norht South) which is powered by mechanical power
- **[IDEA]** Windwheel
- **[IDEA]** Waterwheel
- **[IDEA]** Wildlife can eat crops (Fences / Walls would be a good counter)
- **[IDEA]** Well (has a x amount of water and fills up a x amount over a x ticks if not full)

### Unknown
- give effect comfort on startup
- Allow different mobs in different biomes to spawn \(*Enderman / Endermite / Stray / Skeleton / Soul Reaper / Withered Necromancer / Wither Puppet / ..*)

```json
{
    "entitys_in_other_biomes": {
        "modid:biome_id": [
            {
                "entity": "minecraft:stray",
                "weight": 8,
                "idk": ""
            },
            {
                "entity": "",
                "weight": 1,
                "idk": ""
            }
        ]
    }
}
```

*****
## Datapack
- Change polymorph position (asked on their dc)
- (TieredZ) Narwhal Tusk Sword uses tools instead of melee weapons
- (TieredZ) Hammers don't work ?
- Spyglass in trinket slot with hotkey (still levelz bound)
- In EMI (Combat Roll & Move Mod still work)
- Dehydration River works with WWOO? maybe tag thing
- check animal spawn with WWOO
- animals respawn?
- make river/water animals respawn less
- restrict hay bale to wheat crafting recipe behind farming level

*****
## Others
- Disable Phantoms / Gamerule
- No permission for openpac-parties command ?

### On update
change version numbers in
- Main Menu x2
- Loading Screen x2
- Aged Window

change Changelog in
- Loading Screen
- Main Menu

check if config options are disabled
- environmentz
- rpgdifficulty
- nameplate
- dehydration
- fancymenu

is LICENSE.md there?

## Only Server configs
- numismaticclaim.json
- voicechat/voicechat-server.properties
- time-and-wind/time-data.json
- seasons.json
- another world rpgdifficulty datapack

*****
### Mods for Aged
- [Custom Spawns](https://www.curseforge.com/minecraft/mc-mods/custom-spawns)

### Maybe mods for Aged
- [Dimension Mutability](https://beta.curseforge.com/minecraft/mc-mods/dimension-mutability)
- [Xaeros Minimap Fair Play Edition](https://beta.curseforge.com/minecraft/mc-mods/xaeros-minimap-fair-play-edition) \(*only for other people to use on the server, not for the modpack itself*)
- [Vanity Slots](https://beta.curseforge.com/minecraft/mc-mods/vanityslots)
- [Craftify](https://www.curseforge.com/minecraft/mc-mods/craftify)
- [Accurate Maps](https://www.curseforge.com/minecraft/mc-mods/accurate-maps) \(*BETA , some bugs*)
- [Extended Drawers](https://beta.curseforge.com/minecraft/mc-mods/extended-drawers)
- [Immersive Aircraft](https://beta.curseforge.com/minecraft/mc-mods/immersive-aircraft)
- [Show me your skin](https://www.curseforge.com/minecraft/mc-mods/show-me-your-skin)
- [Vulkan Render](https://www.curseforge.com/minecraft/mc-mods/vulkanmod) \(*instead of Sodium / needs testing / beta*)
- [DropZ](https://www.curseforge.com/minecraft/mc-mods/dropz) \(*instead of Interactic / 1.19.2 version ??*)
- [Chefs Delight](https://www.curseforge.com/minecraft/mc-mods/chefs-delight-fabric) \(Numismatic Overhaul works??)
- [Convenient Decor](https://modrinth.com/mod/convenient-decor)
- [Damage Tilt](https://www.curseforge.com/minecraft/mc-mods/damage-tilt)
- [Awesome Dungeon Ocean Edition](https://www.curseforge.com/minecraft/mc-mods/awesome-dungeon-edition-ocean-fabric)
- [Neruina - Ticking Entity Fixer](https://modrinth.com/mod/neruina)
- [Vanilla Zoom](https://modrinth.com/mod/vanilla-zoom)

### Mod Ideas
- Potion that takes you to your last death

- If you die X times in a X period of time you get a health boost or armor boost or both for a x amount of time (like a status effect maybe)

- Continue Breaking a Block when you shortly lift \(~3sec)

- Schriftrollen \(*teleport zum spawn nach 10 sec ohne damage*)

- Juwlery ( Rings / Necklace / Gloves / .. ) - Different Sets: Farmer , Boat Speed , Dodge Chance , Walk Speed

- Elfs

- Dwarfs

- Lord of the Rings

- Horses

- Goblins

- Campfire scare agressive wolfs ( maybe such a mechanic for other entitys as well )

- Max Iron Golem from the same Villagers

- chew on bark ( willow ) to get medical benefits

- [Wood Cart with Chest](https://i.ytimg.com/vi/KgLK0sIKl_w/maxresdefault.jpg)

- Bigger cart than wood cart which is pulled by a horse or 2 horses with plenty of storage & 1 or 2 seats (4 wheels) (reference: Red Dead Redemption 2, Farthest Frontier)

### Mods which Globox disables
- Smooth Swapping
- Legendary Tooltips
- EquipmentCompare
- AdvancementPlaques
- DynamicCrossair
- DynamicCrosshairCompat
- ExtraSounds
- ShoulderSurfing
- ChunkFadeIn

### Aged 2.0.0 Bugs
## General
- null

## Server
- null
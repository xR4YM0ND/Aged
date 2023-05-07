*****
# Known Bugs / To Do
*****
## Mods

### Farmers Delight
- Milk Bottle - Does not remove Effects

### Spice of Fabric
- test on server (Beta 4)

### EnvironmentZ
- **[Idea]** Armor that saves Water Level \(for hot biomes)
- **[Idea]** In the desert water drys out \(sandstone cracks)

### OPAC
- Doors / Fencegates only open when empty handed, when functional item in hand it doesnt work
- Allow flask any time
- Allow purified water bottles any time

### Dehydration
- Sneak Right click with flask actually fills cauldrons & campfire cauldron - Done
- Sneak Right click with Vanilla Water bottles emptys the bottle - Done
- Dirty Water Bottle smeltable in Furnace & Campfire (lot of people mentioned that) - Removed furnace info
- Water protection - Done
- Brewing Charcoal with Dirty Water (nomrla water bottles) to Purified Water Bottles - Done

### DungeonZ
- **[Idea]** Boss phases (Boss is damage 2/3 , monsters spawn & you have to kill all mobs first to damage the Boss again) (like different stages for the boss fight)
- **[Idea]** Add barrels as separate loot table

### RPG Difficulty / Nameplate
- per Dimension Datapack -> Starting Location (xyz) - Done
- Wandering Trader has lvl's - ??? Needs testing
- Nameplate / Give Traders their Level (/ Novice / Apprentice / Journeyman / Expert / Master) - Needs testing

### Medieval Weapons
- Better Combat -> Lance ausgangsposition nach vorne gerichtet nicht nach oben - Imo current is better for view
- Better Combat -> Javelin das selbe

### LevelZ
- Max Mobs kill drops in a chunk (exlude some mobs (ender dragon / bosses / ...))
- add hoe in github readme (3.Item (5 different not 4 different, you forgot the hoe))
- clicking in sub categorys on the name (upper left) takes you back to the main levelz screen (same as pressing "E")

### AdditionZ
- **[Idea]** TNT Tennis (2023 April Fools update)
- Shield Cooldown compatible with the mod Guarding ? - Needs testing

### TieredZ
- Items (Swords/Axes/..) that are placed in item frames on generation (BetterDungeons / BetterDesertTemples / ..) are vanilla , they dont have tiers - Done
- same for armor in armor stands on generation - Done
- Extra slot in Anvil (Addition Slot -> items for rarity that get used once when place in (1 item always makes rare on upgrade, other always epic, etc..))

### SpoiledZ
- \(Cooking folder) - Bowl use on Blocks - Stuffed Pumpkin Block from Farmer's Delight not spoiled
- Food Blocks you place down ( Cake , Apple Pie(Vinery Mod) , other modded ) dont get spoiled
- Crash with [Farmers Respite "Rose Hip Pie"](https://beta.curseforge.com/minecraft/mc-mods/farmers-respite-fabric) -> [latest.log](https://gist.github.com/SpigotDE/1d055f0e746194d5c284b9ef9bd99ef7) -> [updated latest.log with xaero ?](https://gist.github.com/SpigotDE/67ff7c6e4791a89cce6aa7342dce8d23)
- Smelting meat doesnt stack in the smoker / furnace -> NBT Crafting

### Unknown
- give effect comfort on startup
- Allow different mobs in different biomes to spawn \(*Enderman / Endermite / Stray / Skeleton / Soul Reaper / Withered Necromancer / Wither Puppet / ..*)

```
{
    "entitys_in_other_biomes": {
        "modid:biome_id": [
            {
                "entity": "minecraft:stray",
                "weight": 8,
                "idk": ...
            },
            {
                "entity": "",
                "weight": .,
                "idk": ...
            }
        ]
    }
}
```
*****
## Datapack

- lower Grapes propability (punching grass)

- update aged guide book

- which mod adds 3D leaves?

*****
## Others

- Disable Phantoms / Gamerule
- No permission for openpac-parties command

### On update

change version numbers in
- Main Menu x2
- Loading Screen x2
- Aged Window

change Changelog in
- Loading Screen
- Main Menu

is LICENSE.md there?

## Only Server configs
- numismaticclaim.json
- voicechat/voicechat-server.properties
- time-and-wind/time-data.json
- seasons.json

*****
### Mods for Aged

- null

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

### Mod Ideas
- Potion that takes you to your last death

- If you die X times in a X period of time you get a health boost or armor boost or both for a x amount of time (like a status effect maybe)

- Continue Breaking a Block when you shortly lift \(~3sec)

- Take Fall Damage while in a Boat \(cause in vanilla boats are OP af)

- Ice Boat Nerf

- Campfires get unlit when it rains

- Schriftrollen \(*teleport zum spawn nach 10 sec ohne damage*)

- Juwlery ( Rings / Necklace / Gloves / .. ) - Different Sets: Farmer , Boat Speed , Dodge Chance , Walk Speed

- Time Control Mod \(*Change the length of day/night time individually*)

- Elfs

- Dwarfs

- Lord of the Rings

- Horses

- Goblins

- Campfire scare agressive wolfs ( maybe such a mechanic for other entitys as well )

- Max Iron Golem from the same Villagers

- chew on bark ( willow ) to get medical benefits

### Mods which Globox does not like in the modpack
- Better Ladders
- Better Statistics Screen
- Better Than Mending
- Craftable Invisible Item Frames
- Experience Bottler
- Horse Expert
- Ice Boat Nerf
- On Soul Fire
- Suggestion Tweaker

### Mods which Globox disables
- Smooth Swapping
- Legendary Tooltips
- EquipmentCompare
- AdvancementPlaques
- DynamicCrossair
- DynamicCrosshairCompat
- ExtraSounds

### Aged 2.0.0 Bugs
## General
- Breaking Animation of 3D leaves is to big
- if you break 3D leaves connection to wood source, the rest has no 3D textures

## Server
- luckperms promote doesnt work?
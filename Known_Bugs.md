*****
# Known Bugs / To Do
*****
## Mods

### AdditionZ
- Normal Oxidization (when placed normal 1 next to another 1 should be same speed as vanilla 1 block 3 air 1 block)
- Fast Oxidization (with lava & water - should be 4x of the vanilla 1 block 3 space 1 block speed)
- **[Idea]** TNT Tennis (2023 April Fools update)
- Shield Cooldown compatible with the mod Guarding ? - Needs testing

### Another World
- Disable Nether Portal creation (diable flint/steel on portal frame, disable creation (from nether to another:world))
- deny outgoing nether portal connection
- deny incoming nether portal connection

### BackSlot
- Backslot overlaps with environmentz (move Backslot HUD x coordinate)

### Dehydration without Z
- [IDEA] combine purified water bottle & flask to fill the flask in crafting table -> bottle gets destroyed

### Early Stage
- [IDEA] Clay Bucket (Clay Brick Bucket for lava one time use)
- [IDEA] Fire Starting Sticks with durability and chance to lit the campfire

### InmisAddon
- Inmis Addon tab centers mouse when clicked on

### DungeonZ
- **[Idea]** Boss phases (Boss is damage 2/3 , monsters spawn & you have to kill all mobs first to damage the Boss again) (like different stages for the boss fight)
- **[Idea]** Add barrels as separate loot table \(eg. *Food Supply*)

### Medieval Weapons
- Give Rapier downsides (currently by far the best item in this mod (by damage per minute))

### LevelZ
- Max Mobs kill drops in a chunk (exlude some mobs (ender dragon / bosses / ...))
- add hoe in github readme (3.Item (5 different not 4 different, you forgot the hoe))
- clicking in sub categorys on the name (upper left) takes you back to the main levelz screen (same as pressing "E")
- mining locked xp blocks (like calcite coal ore), they don't drop items but xp

### TieredZ
- Items (Swords/Axes/..) that are placed in item frames on generation (BetterDungeons / BetterDesertTemples / ..) are vanilla , they dont have tiers - Done
- same for armor in armor stands on generation - Done
- Extra slot in Anvil (Addition Slot -> items for rarity that get used once when place in (1 item always makes rare on upgrade, other always epic, etc..))
- TieredZ aint working with Crafting Rock
- Shields don't get modifiers
- if inventory is full you can see the output modifiers of items before crafting (https://discord.com/channels/745451299713056791/745454651536834630/1108890383594836012)

### SpoiledZ
- \(Cooking folder) - Bowl use on Blocks - Stuffed Pumpkin Block from Farmer's Delight not spoiled
- Food Blocks you place down ( Cake , Apple Pie(Vinery Mod) , other modded ) dont get spoiled
- Crash with [Farmers Respite "Rose Hip Pie"](https://beta.curseforge.com/minecraft/mc-mods/farmers-respite-fabric) -> [latest.log](https://gist.github.com/SpigotDE/1d055f0e746194d5c284b9ef9bd99ef7) -> [updated latest.log with xaero ?](https://gist.github.com/SpigotDE/67ff7c6e4791a89cce6aa7342dce8d23)
- Smelting meat doesnt stack in the smoker / furnace -> NBT Crafting
- Crash with vinery

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
- Villager Trade dark texture
- Change polymorph position (asked on their dc)
- change hide to leather (with salt & sugar)

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

is LICENSE.md there?

## Only Server configs
- numismaticclaim.json
- voicechat/voicechat-server.properties
- time-and-wind/time-data.json
- seasons.json
- another world rpgdifficulty datapack

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
- null

## Server
- null
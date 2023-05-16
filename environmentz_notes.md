## Items

change heating_stones and ice_packs to 120 durability instead of 60

Cooling Effect doesn't work with ice_pack over 1 durabiltiy
Heating Effect doesn't work with heating_stones over 1 durability


## End

in the end you can't go over +240 or under -240
it's both bound to "hot_body_temperature": 240, & "cold_body_temperature": -240,
otherwise in the nether the cold is hardcoded (no acclimatization for too cold in the nether)
would be neat to make it so the end too hot is hardcoded or the nether is handled with acclimatization

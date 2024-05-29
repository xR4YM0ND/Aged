README
Fzzy Core
------------------

This Readme is for config options related to the Fzzy Core library. To learn more about the functionality of Fzzy Core, go to the github Wiki or check out the codes KDoc


Flavors Config:
The flavors config sets how advanced flavor descriptions will appear in-game. For library users, advanced flavor descriptions are used to describe in plain words what a flavor text is inferring.

> showFlavorDesc: when set to true, flavor descriptions will always show in tooltips directly below the flavor text
> showFlavorDescOnAdvanced: when set to true, flavor descriptions will show when advanced tooltips are selected. NOTE: showFlavorDesc overrides this functionality and will show the desc. no matter what.

To always show flavor descriptions: showFlavorDesc: true; showFlavorDescOnAdvanced: any
To show descriptions only on advanced tooltips (default): showFlavorDesc: false; showFlavorDescOnAdvanced: false
To never show descriptions: showFlavorDesc: false; showFlavorDescOnAdvanced: false

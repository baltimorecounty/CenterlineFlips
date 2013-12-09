CenterlineFlips
===============

The CenterlineFlips repo is part of a Baltimore County project to make a routable centerline layer. In order to be routable, centerlines address ranges must be in ascending order. This repo encompasses the need to make those changes.

Centerlines that have descending addresses need to be flipped, and have their attributes rearranged. The process prior to the custom tool development in this repo was very manual:

1. The centerline is selected
2. Editor -> Flip
3. Update the 8 attributes for left/right ranges, and potential/actual ranges.

## Tool

The tool developed by @talllguy for the task flips the centerline, and then swaps all eight attributes, in one click. The base scripts are in the /scripts directory, and the tool is in the CenterlineButton directory.

### Requirements

- Built and tested in ArcGIS 10.2
- ArcMap 10.2
- Centerline layer named "FACILITIES.Centerline"

### Installation

1. [Download the latest release](https://github.com/baltimorecounty/CenterlineFlips/releases/latest) in this repository
2. Uncompress and execute the add-in
3. A toolbar will be added to ArcMap
4. Start an editing session
5. Select the centerline to be flipped
6. Click the custom *Flip Centerlines and Swap Attributes* button
7. Quality check the new data
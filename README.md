CenterlineFlips
===============

The CenterlineFlips repo is part of a Baltimore County project to make a routable centerline layer. In order to be routable, centerlines address ranges must be in ascending order. This repo encompasses the need to make those changes.

Centerlines that have descending addresses need to be flipped, and have their attributes rearranged. The process prior to the custom tool development in this repo was very manual:

1. The centerline is selected
2. Editor -> Flip
3. Update the 8 attributes for left/right ranges, and potential/actual ranges.

## Tool

The tool developed to flip the centerline, and then swap all eight attributes in one click. The base scripts are in the /scripts directory, and the tool is in the /CenterlineButton directory.

### Requirements

- Built and tested in ArcGIS 10.2
- ArcMap 10.2
- Windows
- Editing privileges
- Centerline layer named "FACILITIES.Centerline"
- SDE connection named: "5160Facilities.sde"

### Features

- Executes all steps of flipping street centerline in one click!
- Flips the direction of the centerline feature class
- Swaps the address range attributes from the left to right side, and reorders them.
- Swaps both actual and potential ranges
- Changes the direction (one way) if set
- Updates the change tracking shapefile that centerline is flipped

### Installation

1. [Download the latest release](https://github.com/baltimorecounty/CenterlineFlips/releases/latest)
2. Execute the .esriaddin file
3. A toolbar will be added to ArcMap
4. Start an editing session
5. Select the centerline to be flipped
6. Click the custom *Flip Centerlines and Swap Attributes* button
7. Quality check the new data

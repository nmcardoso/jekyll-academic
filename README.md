# Configurations

## Dimensions citations

- Scope: page
- Fallback: hardcoded defaults
- Documentation: https://badge.dimensions.ai/?identifier=pub.1139635042

Key|Type|Description
---|---|---
dimensions.enabled|`boolean`|Enable badge. Default: `true`
dimensions.hide_uncited|`boolean`|Hide badge if no citations. Default: `true`
dimensions.style|`enum`|Badge style. Options: `medium_circle`, `small_circle`, `large_circle`, `small_rectangle`, `large_rectangle`. Default: `medium_circle`
dimensions.legend|`enum`|Legend display mode. Options: `hover-top`, `hover-right`, `hover-bottom`, `hover-left`, `always`, or `never`. Default: `always`


## Altmetric citations

- Scope: page
- Fallback: hardcoded defaults
- Documentation: https://docs.altmetric.com/badges/customizations/

Key|Type|Description
---|---|---
altmetric.enabled|`boolean`|Enable badge. Default: `true`
altmetric.hide_uncited|`boolean`|Hide badge if no citations. Default: `true`
altmetric.style|`enum`|Badge style. Options: `default`, `donut`, `medium-donut`, `large-donut`, `1`, `4`, `bar`, `medium-bar`, or `large-bar`
altmetric.popover|`enum`|Legend popover location. Options: `top`, `right`, `bottom`, `left`. Default: `nil`
altmetric.details|`boolean`|Permanent legend display. Default: `nil`
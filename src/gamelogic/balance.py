__author__="Yves Adler"
__date__ ="$Nov 5, 2009 3:09:20 PM$"

import goods

# General:
MAX_GOODS_AT_BUILDING = 8
PERCENT_UNTIL_FLATTENED = 20

WALKSPEED_PEOPLE = 1

# Flattener:
WORKSPEED_FLATTENER = 500

# Builder:
WORKSPEED_BUILDER = 500

# Lumberjack:
WORKSPEED_LUMBERJACK = 500

# LumberjackHouse:
BUILDTIME_LUMBERJACK_HOUSE = 100
COSTS_LUMBERJACK_HOUSE = [goods.Plank, goods.Plank, goods.Stone, goods.Stone]

# Warehouse:
BUILDTIME_WAREHOUSE = 200
COSTS_WAREHOUSE = [goods.Plank, goods.Plank, goods.Stone, goods.Stone]

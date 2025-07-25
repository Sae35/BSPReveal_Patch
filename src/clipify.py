import os

from valvebsp.lumps import *
from totcommon.logger import stdout

def clipify(bsp):

    clip_brush_count = grate_brush_count = block_brush_count = 0

    for brush in bsp[LUMP_BRUSHES]:
        brush_side = bsp[LUMP_BRUSHSIDES][brush.firstSide]
        texinfo = bsp[LUMP_TEXINFO][brush_side.texInfo]
        texdata = bsp[LUMP_TEXDATA][texinfo.texData]
        texname = bsp[LUMP_TEXDATA_STRING_DATA][texdata.nameStringTableID]

        if brush.contents.CONTENTS_MONSTERCLIP and \
           brush.contents.CONTENTS_PLAYERCLIP:
            # Retag clip brushes as playerclip brushes
            brush.contents.CONTENTS_MONSTERCLIP = False
            clip_brush_count += 1
        elif brush.contents.CONTENTS_GRATE:
            # Retag grate solidity as clip brushes
            brush.contents.CONTENTS_MONSTERCLIP = True
            brush.contents.CONTENTS_PLAYERCLIP = True
            grate_brush_count += 1
        elif texname.startswith('TOOLS/TOOLSBLOCKBULLETS') or \
            texname.startswith('TOOLS_CONCRETE-ROCK/TOOLS_BLOCKBULLET_CONCRETE-ROCK_BOULDER') or \
            texname.startswith('TOOLS_CONCRETE-ROCK/TOOLS_BLOCKBULLET_CONCRETE-ROCK_BRICK') or \
            texname.startswith('TOOLS_CONCRETE-ROCK/TOOLS_BLOCKBULLET_CONCRETE-ROCK_CONCRETE') or \
            texname.startswith('TOOLS_CONCRETE-ROCK/TOOLS_BLOCKBULLET_CONCRETE-ROCK_GRAVEL') or \
            texname.startswith('TOOLS_CONCRETE-ROCK/TOOLS_BLOCKBULLET_CONCRETE-ROCK_ROCK') or \
            texname.startswith('TOOLS_FROZEN/TOOLS_BLOCKBULLET_FROZEN_ICE') or \
            texname.startswith('TOOLS_FROZEN/TOOLS_BLOCKBULLET_FROZEN_SNOW') or \
            texname.startswith('TOOLS_MANUFACTURED/TOOLS_BLOCKBULLET_MANUFACTURED_CARDBOARD') or \
            texname.startswith('TOOLS_MANUFACTURED/TOOLS_BLOCKBULLET_MANUFACTURED_GLASS') or \
            texname.startswith('TOOLS_MANUFACTURED/TOOLS_BLOCKBULLET_MANUFACTURED_PLASTER') or \
            texname.startswith('TOOLS_MANUFACTURED/TOOLS_BLOCKBULLET_MANUFACTURED_PLASTIC') or \
            texname.startswith('TOOLS_MANUFACTURED/TOOLS_BLOCKBULLET_MANUFACTURED_PORCELAIN') or \
            texname.startswith('TOOLS_MANUFACTURED/TOOLS_BLOCKBULLET_MANUFACTURED_RUBBER') or \
            texname.startswith('TOOLS_MANUFACTURED/TOOLS_BLOCKBULLET_MANUFACTURED_RUBBERTIRE') or \
            texname.startswith('TOOLS_MANUFACTURED/TOOLS_BLOCKBULLET_MANUFACTURED_TILE') or \
            texname.startswith('TOOLS_METAL/TOOLS_BLOCKBULLET_METAL_CANISTER') or \
            texname.startswith('TOOLS_METAL/TOOLS_BLOCKBULLET_METAL_CHAIN') or \
            texname.startswith('TOOLS_METAL/TOOLS_BLOCKBULLET_METAL_CHAINLINK') or \
            texname.startswith('TOOLS_METAL/TOOLS_BLOCKBULLET_METAL_METAL') or \
            texname.startswith('TOOLS_METAL/TOOLS_BLOCKBULLET_METAL_METAL-BARREL') or \
            texname.startswith('TOOLS_METAL/TOOLS_BLOCKBULLET_METAL_METAL-BOX') or \
            texname.startswith('TOOLS_METAL/TOOLS_BLOCKBULLET_METAL_METALGRATE') or \
            texname.startswith('TOOLS_METAL/TOOLS_BLOCKBULLET_METAL_METALPANEL') or \
            texname.startswith('TOOLS_METAL/TOOLS_BLOCKBULLET_METAL_METALVENT') or \
            texname.startswith('TOOLS_MISCELLANEOUS/TOOLS_BLOCKBULLET_MISCELLANEOUS_CARPET') or \
            texname.startswith('TOOLS_MISCELLANEOUS/TOOLS_BLOCKBULLET_MISCELLANEOUS_CEILING-TILE') or \
            texname.startswith('TOOLS_MISCELLANEOUS/TOOLS_BLOCKBULLET_MISCELLANEOUS_COMPUTER') or \
            texname.startswith('TOOLS_MISCELLANEOUS/TOOLS_BLOCKBULLET_MISCELLANEOUS_POTTERY') or \
            texname.startswith('TOOLS_TERRAIN/TOOLS_BLOCKBULLET_TERRAIN_DIRT') or \
            texname.startswith('TOOLS_TERRAIN/TOOLS_BLOCKBULLET_TERRAIN_GRASS') or \
            texname.startswith('TOOLS_TERRAIN/TOOLS_BLOCKBULLET_TERRAIN_MUD') or \
            texname.startswith('TOOLS_TERRAIN/TOOLS_BLOCKBULLET_TERRAIN_SAND') or \
            texname.startswith('TOOLS_WOOD/TOOLS_BLOCKBULLET_WOOD_WOOD') or \
            texname.startswith('TOOLS_WOOD/TOOLS_BLOCKBULLET_WOOD_WOOD-BOX') or \
            texname.startswith('TOOLS_WOOD/TOOLS_BLOCKBULLET_WOOD_WOOD-CRATE') or \
            texname.startswith('TOOLS_WOOD/TOOLS_BLOCKBULLET_WOOD_WOOD-FURNITURE') or \
            texname.startswith('TOOLS_WOOD/TOOLS_BLOCKBULLET_WOOD_LOWDENSITY') or \
            texname.startswith('TOOLS_WOOD/TOOLS_BLOCKBULLET_WOOD-PANEL') or \
            texname.startswith('TOOLS_WOOD/TOOLS_BLOCKBULLET_WOOD_PLANK') or \
            texname.startswith('TOOLS_WOOD/TOOLS_BLOCKBULLET_WOOD_SOLID'):
            # Tag blobkbullet and npcclip brushes, plus Entropy's Block Bullets Pack.
            brush.contents.CONTENTS_MONSTERCLIP = True
            block_brush_count += 1

    if clip_brush_count:
        stdout('{} clip brushes modified.'.format(clip_brush_count))
    if block_brush_count:
        stdout('{} blockbullet brushes modified.'.format(block_brush_count))
    if grate_brush_count:
        stdout('{} grate brushes modified.'.format(grate_brush_count))

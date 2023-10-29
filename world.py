import os, json, random

CHUNK_SIZE = 16
CHUNK_MARGIN = 3
GEN_DISTANCE = 2

class World():
    def __init__(self,name,textures):
        self.name = name
        self.textures = textures
        self.tiles = self.generate_map()

    def save(self):
        with open("worlds/"+self.name+".json", "w") as f:            
            f.write(json.dumps({
                "tiles": []
                }))

    def generate_map(self):
        tiles = []
        for x in range(-GEN_DISTANCE,GEN_DISTANCE+1):
            for y in range(-GEN_DISTANCE,GEN_DISTANCE+1):
                tiles.extend(self.generate_chunk((x,y)))
        return tiles

    def generate_chunk(self, chunk_pos):
        gen_tiles = []
        tiles = []
        for x in range(0,CHUNK_SIZE-CHUNK_MARGIN):
            for y in range(0,CHUNK_SIZE-CHUNK_MARGIN):
                gen_tiles.append({"image": None, "position": (x+16*chunk_pos[0],y+16*chunk_pos[1]), "possibilities": ["grass", "water", "sand"]})

        while len(gen_tiles) > 0:
            lowest = {"s": 0,"d": 0,"possibilities": []}
            for tile in gen_tiles:
                if len(tile["possibilities"]) < len(lowest["possibilities"]) or len(lowest["possibilities"]) == 0:
                    lowest = tile
            
            gen_tiles.pop(gen_tiles.index(lowest))
            lowest["image"] = lowest["possibilities"][random.randint(0,len(lowest["possibilities"])-1)]
            lowest.pop("possibilities")
            tiles.append(lowest)

        return tiles

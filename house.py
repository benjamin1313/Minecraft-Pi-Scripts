from mcpi import minecraft
import time

mc = minecraft.Minecraft.create()

#materials i'm going to use
wood = 5
log = 17
glass = 102
stone = 4
door = 324
air = 0

x, y, z = mc.player.getPos()

mc.postToChat("starting building.")

time.sleep(2)

mc.setBlocks(x-5, y, z, x+5, y, z-12, air)

#changes y and z so i have a center to work from
z = z-5
y = y-1


x = x-3 #sets x a little if to the side to then i loop though the floor
#generates the floor
count = 0
mc.postToChat("Building the floor")  
while count < 7:
    mc.setBlocks(x, y, z-1, x, y, z+1, wood)
    x = x+1
    count = count+1
    time.sleep(1)

#sets x back to the center block
x = x-4


#resets count and builds the log pillars
count = 0
mc.postToChat("Building pillars.")  
while count < 4:
    
    mc.setBlock(x-5, y, z-2, log)
    mc.setBlock(x-5, y, z+2, log)
    mc.setBlock(x+5, y, z-2, log)
    mc.setBlock(x+5, y, z+2, log)

    mc.setBlock(x-4, y, z-3, log)
    mc.setBlock(x-4, y, z+3, log)
    mc.setBlock(x+4, y, z-3, log)
    mc.setBlock(x+4, y, z+3, log)

    mc.setBlock(x, y, z-3, log)
    mc.setBlock(x, y, z+3, log)
    
    count = count+1
    y = y+1
    time.sleep(1)
y = y-4


#resets the counter and builds the walls
count = 0
x = x-4
z = z-2
mc.postToChat("Building walls.")  
while count < 4:
    Fside = 0
    Bside = 0
    Lside = 0
    Rside = 0
    while Bside < 8:
        mc.setBlock(x, y, z, stone)
        x = x+1
        Bside = Bside+1
        time.sleep(0.5)
    while Rside < 4:
        mc.setBlock(x, y, z, stone)
        z = z+1
        Rside = Rside+1
        time.sleep(0.5)
    while Fside < 8:
        mc.setBlock(x, y, z, stone)
        x = x-1
        Fside = Fside+1
        time.sleep(0.5)
    while Lside < 4:
        mc.setBlock(x, y, z, stone)
        z = z-1
        Lside = Lside+1
        time.sleep(0.5)
    y = y+1
    count = count+1

x = x+4
z = z+2
y = y-4

#making windows and space for a door.
#but the pi api does not suport doors as a block so no door is placed
mc.postToChat("putting in a door and window.")
mc.setBlock(x+2, y+1, z+2, air)
mc.setBlock(x+2, y+2, z+2, air)
time.sleep(1)
mc.setBlock(x-1, y+2, z+2, glass)
time.sleep(1)
mc.setBlock(x-2, y+2, z+2, glass)
time.sleep(1)
mc.setBlock(x-3, y+2, z+2, glass)
time.sleep(1)

#builds the roof
mc.postToChat("Building roof.")
mc.setBlocks(x-6, y+4, z-4, x+6, y+4, z+4, wood)
time.sleep(1)
mc.setBlocks(x-5, y+5, z-3, x+5, y+5, z+3, wood)
time.sleep(1)
mc.setBlocks(x-4, y+6, z-2, x+4, y+6, z+2, wood)
time.sleep(1)
mc.setBlocks(x-3, y+7, z-1, x+3, y+7, z+1, wood)
time.sleep(1)
mc.setBlocks(x-2, y+8, z, x+2, y+8, z, wood)
time.sleep(1)

mc.postToChat("Done!")    

import cklib
import scipy

def testBlasts():
    #create power supply
    psu = cklib.PowerSupply("10.32.0.96")

    #create lights and attach them to the powersupply
    psu.addLight(cklib.ColorBlast(psu,1))
    psu.addLight(cklib.ColorBlast(psu,4))
    psu.addLight(cklib.ColorBlast(psu,7))

    #write data to the lights
    for light in psu.lights:
        light.state = [255,255,0]

    psu.write()

def testFlex():
    #create power supply
    psu = cklib.PowerSupply("10.32.0.96")

    #create lights and attach them to the powersupply
    psu.addLight(cklib.Flex(psu,0x01))
    psu.addLight(cklib.Flex(psu,0x02))

    #write data to the lights
    for light in psu.lights:
        light.state = 255*scipy.ones(light.numChannels)

    for light in psu.lights:
        psu.write(channel=light.channel)
import asyncio
from kasa import SmartPlug

async  def main():
    dev=SmartPlug("192.168.0.30")
    while True:
        await dev.update()
        print(dev.alias)
        await dev.turn_off()
        await asyncio.sleep(2)
        print(dev.location)
        await dev.turn_on()
        await asyncio.sleep(2)

if __name__=="__main__":
    asyncio.run(main())



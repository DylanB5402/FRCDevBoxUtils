import asyncio
import websockets
import json

async def test():
    url = "wss://5810-ptyxzawozcodzdjn.daytonaproxy01.net/nt/FRCDevBox"
    async with websockets.connect(url, subprotocols=["networktables.first.wpi.edu"]) as ws:
        print("Connected!")

        # Just send subscribe without timestamp sync
        sub = json.dumps([
            {"method": "subscribe", "params": {"topics": [""], "subuid": -1, "options": {"prefix": True}}}
        ])
        await ws.send(sub)
        print("Sent subscribe")

        for _ in range(20):
            try:
                msg = await asyncio.wait_for(ws.recv(), timeout=5)
                if isinstance(msg, bytes):
                    import msgpack
                    try:
                        print(f"Binary: {msgpack.unpackb(msg)}")
                    except:
                        print(f"Binary raw: {msg.hex()}")
                else:
                    print(f"Text: {msg}")
            except asyncio.TimeoutError:
                print("No more messages")
                break

asyncio.run(test())
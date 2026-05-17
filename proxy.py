import asyncio
import websockets

DAYTONA_HOST = "5810-ptyxzawozcodzdjn.daytonaproxy01.net"
LOCAL_PORT = 5810

async def handle(local_ws):
    print(f"Client connected, opening tunnel to {DAYTONA_HOST}")
    try:
        async with websockets.connect(
            f"wss://{DAYTONA_HOST}/nt/AdvantageScope",
            subprotocols=["networktables.first.wpi.edu"],
        ) as remote_ws:
            print("Tunnel established")

            async def local_to_remote():
                async for msg in local_ws:
                    await remote_ws.send(msg)

            async def remote_to_local():
                async for msg in remote_ws:
                    await local_ws.send(msg)

            await asyncio.gather(local_to_remote(), remote_to_local())
    except Exception as e:
        print(f"Tunnel error: {e}")

async def main():
    print(f"NT4 proxy: ws://localhost:{LOCAL_PORT} -> wss://{DAYTONA_HOST}")
    async with websockets.serve(handle, "localhost", LOCAL_PORT,
                                subprotocols=["networktables.first.wpi.edu"]):
        await asyncio.Future()

asyncio.run(main())
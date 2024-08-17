import asyncio
from bleak import BleakClient, BleakScanner
import sys

CHARACTERISTIC_UUID_PROGRAM_STARTSTOP = "d343bfc1-5a21-4f05-bc7d-af01f617b664"
CHARACTERISTIC_UUID_PROGRAM_KEY = "d343bfc2-5a21-4f05-bc7d-af01f617b664"
CHARACTERISTIC_UUID_PROGRAM_VALUE = "d343bfc3-5a21-4f05-bc7d-af01f617b664"


async def write(client, characteristic, value):
    await client.write_gatt_char(characteristic, value)
    print("Value written")


async def program_code(
    client,
    key,
    value,
):
    await write(client, CHARACTERISTIC_UUID_PROGRAM_KEY, key)
    await write(client, CHARACTERISTIC_UUID_PROGRAM_VALUE, bytes.fromhex(value))


async def program_start(client):
    await write(client, CHARACTERISTIC_UUID_PROGRAM_STARTSTOP, b"\x01")


async def program_stop(client):
    await write(client, CHARACTERISTIC_UUID_PROGRAM_STARTSTOP, b"\x00")


async def run(address):
    async with BleakClient(address) as client:
        print(f"Connected: {client.is_connected}")

        codes_to_program = [
            [
                # vol up button on remote
                b"\x00\x18",
                # denon receiver vol up
                "0221017c0020123c000c001a000c0040000c001a000c001a000c001a000c0040000c001a000c001a000c001a000c0040000c0040000c0040000c0040000c001a000c001a000c05f4000c001a000c0040000c001a000c001a000c001a000c001a000c0040000c0040000c0040000c001a000c001a000c001a000c001a000c0040000c0040000c05f4",
            ],
            [
                # vol down button on remote
                b"\x00\x19",
                # denon receiver vol down
                "0221017c0020123c000c001a000c0040000c001a000c001a000c001a000c001a000c0040000c001a000c001a000c0040000c0040000c0040000c0040000c001a000c001a000c05f4000c001a000c0040000c001a000c001a000c001a000c0040000c001a000c0040000c0040000c001a000c001a000c001a000c001a000c0040000c0040000c05f4",
            ],
            [
                # mute button on remote
                b"\x00\xa4",
                # denon receiver mute
                "0221017c0020123c000c001a000c0040000c001a000c001a000c001a000c001a000c001a000c001a000c001a000c0040000c0040000c0040000c0040000c001a000c001a000c05f4000c001a000c0040000c001a000c001a000c001a000c0040000c0040000c0040000c0040000c001a000c001a000c001a000c001a000c0040000c0040000c05f4",
            ],
            [
                # power button on remote
                b"\x00\x1a",
                # denon receiver power
                "0221017c0020123c000c001a000c0040000c001a000c001a000c001a000c0040000c001a000c001a000c001a000c001a000c001a000c0040000c0040000c001a000c001a000c05f4000c001a000c0040000c001a000c001a000c001a000c001a000c0040000c0040000c0040000c0040000c0040000c001a000c001a000c0040000c0040000c05f4",
            ],
            [
                # input select button on remote
                b"\x00\xb2",
                # lg tv power
                "0321017c00220002015700ab0016001600160016001600410016001600160016001600160016001600160016001600410016004100160016001600410016004100160041001600410016004100160016001600160016001600160041001600160016001600160016001600160016004100160041001600410016001600160041001600410016004100160041001605f50157005600160e60",
            ],
        ]

        await program_start(client)
        for idx in range(len(codes_to_program)):
            await program_code(
                client, codes_to_program[idx][0], codes_to_program[idx][1]
            )
        await program_stop(client)


async def main():
    # Scan for devices and select the correct one
    devices = await BleakScanner.discover()
    for device in devices:
        print(f"Device: {device.name}, Address: {device.address}")

    # Replace with the actual address of your BLE device
    device_address = sys.argv[1]

    # Run the BLE operations
    await run(device_address)


if __name__ == "__main__":
    asyncio.run(main())

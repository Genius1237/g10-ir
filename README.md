# Program IR Buttons on Google G10/G20 Remote
This script allows you to program the 5 IR programmable buttons on the Google G10 remote (G20 also maybe, not tested) with custom IR codes (still WIP, see below) on any device, not just the Android TV devices running the custom Google programming app.

Make sure that the remote is already paired to the device and get it's MAC address. 

Follow instructions below to setup and run the command. As soon as your hit enter to start the command, press and hold the power and back buttons to put the remote in pairing mode. The `bleak` library is only able to identify the remote when in pairing mode

## Running on Desktop Linux
Install dependencies with `pip install bleak`
Then run the script with `python run.py "REMOTE_MAC_ADDRESS"`

## Running on LibreELEC/CoreELEC
Make sure `script.module.typing_extensions` python dependency is installed. The rest of the dependencies can be pulled in by running `./setup.sh`

Then the script can be run with `./run.sh "REMOTE_MAC_ADDRESS"`

## Modifying IR Codes
The IR Codes hardcoded in `run.py` were determined by enabling bluetooth HCI snopping on an onn android device, programming the IR buttons via the inbuilt app and inspecting the packets in wireshark. The IR codes sent seem to be different from what you can see online.

For example, the denon vol up code mentioned online is 
```
0000006c00000020000a001e000a001e000a001e000a0046000a001e000a0046000a001e000a0046000a001e000a0046000a001e000a0046000a0046000a001e000a001e000a06aa000a001e000a001e000a001e000a0046000a001e000a001e000a0046000a001e000a0046000a001e000a0046000a001e000a001e000a0046000a0046000a06aa
```
but the one sent in the packet capture is this
```

0221017c0020123c000c001a000c0040000c001a000c001a000c001a000c0040000c001a000c001a000c001a000c0040000c0040000c0040000c0040000c001a000c001a000c05f4000c001a000c0040000c001a000c001a000c001a000c001a000c0040000c0040000c0040000c001a000c001a000c001a000c001a000c0040000c0040000c05f4
```

Not sure why it is different. The remote seems to reject the first IR code if sent and the button doesn't go into IR mode. Someone needs to figure out what the difference is.

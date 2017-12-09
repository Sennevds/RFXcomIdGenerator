# RFXcomIdGenerator

Generate RFXcom IDs for Home Assistant

As great as Home Assistant is, the RFXcom detection can be a little tricky. For example the remote that comes with the Energenie Wireless Sockets (4 pack) does not get picked up by the RFX. So when the docs say to set `automatic_add` to `True` and press the button on the remote, this doesn't do anything. Because the remote signal is not being received by RFX, there is no way it can be passed to Home Assistant.

To get around this you have to create a new switch in Hass and then pair the device to the new switch as if it was a new remote control. Usually this involves pressing and holding a button on the recieving device untill it goes into pairing mode, then "turn on" the new switch using the Hass UI.

This excellent script by [Sennevds](https://github.com/Sennevds) helps generate the the IDs required by Hass when adding the new switches.

## Usage

`generateId.py -t type -s subtype -p parameters`

e.g.

to generate a code for a Lighting1 type device using ARC subtype, set to housecode A unit code 3

`python generateId.py -t Lighting1 -s ARC -p A,3`

### Supported types:

- Lighting1
- Lighting5

### Supported subtypes:

  - X10
  - AC
  - LightwaveRF
  - ARC
  - HomeEasy EU
  - EMW100
  - AB400D
  - ANSLUT
  - BBSB
  - Waveman
  - MDREMOTE
  - EMW200
  - Conrad RSL2
  - IMPULS
  - Livolo
  - RisingSun
  - RGB TRC02
  - Philips SBC
  - Energenie
  - GDR2
  - ProMax
  - IT


### Parameters are a comma separated list (no spaced) depending on type:

Lighting1: housecode,unitID

e.g. `-p A,3` or `-p A,1`

Lighting5: id,unit_code

## For more details

https://community.home-assistant.io/t/how-to-define-id-for-rfxcom-s-component/7788

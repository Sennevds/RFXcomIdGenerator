# RFXcomIdGenerator
Generate RFXcom ID for Home Assistant

# usage
generateId.py -t type -s subtype -p parameters

types supported at this moment:
	-Lighting1
	-Lighting5

subtypes supported:
	-X10
  -AC
  -LightwaveRF
  -ARC
  -HomeEasy EU
  -EMW100
  -AB400D
  -ANSLUT
  -BBSB
  -Waveman
  -MDREMOTE
  -EMW200
  -Conrad RSL2
  -IMPULS
  -Livolo
  -RisingSun
  -RGB TRC02
  -Philips SBC
  -Energenie
  -GDR2
  -ProMax
  -IT

parameters are a comma separated list depending on type:
	-Lighting1:
		- housecode
		- unit ID
	-Lighting5:
		- id
		- unit code

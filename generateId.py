import sys


TYPES = {'X10':         '00',
         'AC':          '00',
         'LightwaveRF': '00',
         'ARC':         '01',
         'HomeEasy EU': '01',
         'EMW100':      '01',
         'AB400D':      '02',
         'ANSLUT':      '02',
         'BBSB':        '02',
         'Waveman':     '03',
         'MDREMOTE':    '03',
         'EMW200':      '04',
         'Conrad RSL2': '04',
         'IMPULS':      '05',
         'Livolo':      '05',
         'RisingSun':   '06',
         'RGB TRC02':   '06',
         'Philips SBC': '07',
         'Energenie':   '08',
         'Energenie5':  '09',
         'GDR2':        '0a',
         'ProMax':      '0f',
         'IT':          '0f' }

HOUSECODES = {
                'A': '41',
                'B': '42',
                'C': '43',
                'D': '44',
                'E': '45',
                'F': '46',
                'G': '47',
                'H': '48',
                'I': '49',
                'J': '4A',
                'K': '4B',
                'L': '4C',
                'M': '4D',
                'N': '4E',
                'O': '4F',
                'P': '50'}

def generate_id(type, subType, args):
    if type == 'Lighting1':
        if len(args) == 2:
            Lighting1(subType, args)
        else:
            print ('Wrong arguments')

    elif type == 'Lighting2':
        Lighting2(subType, args)
    elif type == 'Lighting3':
        id = '812'
    elif type == 'Lighting4':
        id = '913'
    elif type == 'Lighting5':
        if len(args) == 2:
            Lighting5(subType, args)
        else:
            print ('Wrong arguments')
    elif type == 'Lighting6':
        id = '0b15'


def Lighting1(subType, args):
    id = '0710' + TYPES[subType] + '00' + HOUSECODES[args[0]] + '0' + args[1] + '00' + '00'
    print (id)

def Lighting2(subType, args):
    id = '0b11'

def Lighting5(subType, args):
    id_combined = int(args[0])
    id1 = id_combined >> 16
    id2 = id_combined >> 8 & 0xff
    id3 = id_combined & 0xff
    id = '0a14' + TYPES[subType] + '00' + str(id1) + str(id2) + str(id3) + args[1] + '00' + '00'
    print (id)


#generate_id('Lighting5','Livolo',['2827','4'])

import sys, getopt

def main(argv):
   type = ''
   subtype = ''
   params = ''
   try:
      opts, args = getopt.getopt(argv,"ht:s:p:",["type=","subtype=", "params="])
   except getopt.GetoptError:
      print ('generateId.py -t <type> -s <subtype> -p <parameters>')
      sys.exit(2)
   for opt, arg in opts:
      if opt == '-h':
         print ('generateId.py -t <type> -s <subtype> -p <parameters>')
         sys.exit()
      elif opt in ("-t", "--type"):
         type = arg
      elif opt in ("-s", "--subtype"):
         subtype = arg
      elif opt in ("-p", "--params"):
         params = arg
   list = params.split(",")

   generate_id(type,subtype, list)

if __name__ == "__main__":
   main(sys.argv[1:])

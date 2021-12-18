import sys
from functools import reduce

class BinaryParser:
    def __init__(self, hexstr):
        self.binary = hex2binstr(hexstr)
        self.parsed = []
        self.ind = 0
        self.maxind = len(self.binary)

    def parse_literal(self) -> int:
        """ parse AAAAA BBBBB CCCCC to int """
        has_zgroup = False
        final_bin = ""
        while not has_zgroup:
            if self.binary[self.ind] == '0':
                has_zgroup = True
            self.ind += 1
            bin_group = self.binary[self.ind: self.ind + 4]
            self.ind += 4
            final_bin += bin_group
        literal_value = bin2int(final_bin)
        return literal_value

    def parse_operator(self) -> list:
        """ parse I L...L """
        len_type = self.binary[self.ind]
        #print("LT", len_type)
        self.ind += 1
        if len_type == '0':
            num = 15
            # startbit num offset
            startbit = self.ind + num
        elif len_type == '1':
            num = 11
        len_argb = self.binary[self.ind: self.ind + num]
        self.ind += num
        len_argc = bin2int(len_argb)

        count = 0
        subpackets = []
       # print()
        while count < len_argc:
            #print(count, len_argc, end=" ... ")
            subpacket = self.parse_data()
            if len_type == '0':
                count = self.ind - startbit
            elif len_type == '1':
                count += 1
            #print(count, len_argc)
            subpackets.append(subpacket)
        return subpackets

    def parse_data(self) -> list:
        """ parse VVV TTT ... """
        version = bin2int(self.binary[self.ind: self.ind + 3])
        self.ind += 3
        type_id = bin2int(self.binary[self.ind: self.ind + 3])
        self.ind += 3
        if type_id == 4:
            subpacket = self.parse_literal()
        else:
            subpacket = self.parse_operator()
        return version, type_id, subpacket

    def parse_all(self) -> list:
        subpackets = []
        while self.ind < self.maxind - 11:
            subpacket = self.parse_data()
            subpackets.append(subpacket)
        return subpackets

    def flatten(self, lst):
        for group in lst:
            if isinstance(group, tuple):
                if isinstance(group[2], list):
                    yield group[:2]
                    yield from self.flatten(group[2])
                else:
                    yield group

    def version_sum(self, data):
        flattened = self.flatten(data)
        vsum = 0
        for subpacket in flattened:
            vsum += subpacket[0]
        return vsum


def eval_operator(packet):
    """ evaluates an operator expression """
    operator = packet[1]
    if operator == 5:   # GT
        value = eval_packet(packet[2][0]) > eval_packet(packet[2][1])
    elif operator == 6: # LT
        value = eval_packet(packet[2][0]) < eval_packet(packet[2][1])
    elif operator == 7: # EQ
        value = eval_packet(packet[2][0]) == eval_packet(packet[2][1])
    elif operator == 0: # SUM
        value = reduce(lambda i, j: i + j, map(eval_packet, packet[2]))
    elif operator == 1: # PRODUCT
        value = reduce(lambda i, j: i * j, map(eval_packet, packet[2]))
    elif operator == 2: # MIN
        value = min(map(eval_packet, packet[2]))
    elif operator == 3: # MAX
        value = max(map(eval_packet, packet[2]))
    else:
        print("?", packet, operator)
    return value

def eval_packet(packet):
    """ evaluates a packet to an int literal """
    if packet[1] == 4:
        # return on literal
        return packet[2]
    else:
        return eval_operator(packet)

def hex2binstr(hexstr):
    return "".join(map(lambda bit: bin(int(bit, 16))[2:].zfill(4), hexstr))

def bin2int(binstr):
    return int(binstr, 2)

def main(arg):
    #tests = ["D2FE28", # LITERAL 2021
    #         "38006F45291200", # LT 0, 2 SP LITERALS
    #         "EE00D40C823060"] # LT 1, 3 SP LITERALS
    #tests2 = {"8A004A801A8002F478": 16, # OP [OP [OP [LITERAL]]] : V = 16
    #        "620080001611562C8802118E34": 12, # OP [OP [2 LIT] * 2] V = 23
    #        "C0015000016115A2E0802F182340": 23, # same structure as above v = 23
    #        "A0016C880162017C3686B18A3D4780": 31, # OP [LIT * 5] v = 31
    #        }
    with open(arg) as raw_data:
        hexstr = raw_data.read().strip()
        parser = BinaryParser(hexstr)
        data = parser.parse_all()
        print(data)
        solution1 = parser.version_sum(data)
        print(solution1)
        # 1002
   # for hexcase in tests2:
   #     parser = BinaryParser(hexcase)
   #     data = parser.parse_all()
   #     print(parser.version_sum(data), data)

def main2(arg):
    tests = {"C200B40A82": 3,
             "04005AC33890": 54,
             "880086C3E88112": 7,
             "CE00C43D881120": 9,
             "D8005AC2A8F0": 1,
             "F600BC2D8F": 0,
             "9C005AC2F8F0": 0,
             "9C0141080250320F1802104A08": 1
             }
    for hexcase in tests:
        parser = BinaryParser(hexcase)
        data = parser.parse_all()
        part2 = eval_packet(data[0])
    
    with open(arg) as raw_data:
        hexstr = raw_data.read().strip()
        parser = BinaryParser(hexstr)
        data = parser.parse_all()
        solution2 = eval_packet(data[0])
        print(solution2)
        # 1673210814091

if __name__ == "__main__":
    #main(sys.argv[1])
    main2(sys.argv[1])

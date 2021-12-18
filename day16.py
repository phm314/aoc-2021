class BinaryParser:
    def __init__(self, hexstr):
        self.binary = hex2binstr(hexstr)
        self.parsed = []
        self.ind = 0
        self.maxind = len(self.binary)

    def parse_literal(self):
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
        self.ind += 1
        if len_type == '0':
            num = 15
            startbit = self.ind
        elif len_type == '1':
            num = 11
        len_argb = self.binary[self.ind: self.ind + num]
        self.ind += num
        len_argc = bin2int(len_argb)

        count = 0
        subpackets = []
        while count < len_argc:
            subpacket = self.parse_data()
            if len_type == '0':
                count = self.ind - startbit
            elif len_type == '1':
                count += 1
            subpackets.append(subpacket)
        return subpackets

    def parse_data(self) -> list:
        """ parse VVV TTT ... """
        version = bin2int(self.binary[self.ind: self.ind + 3])
        self.ind += 3
        type_id = bin2int(self.binary[self.ind: self.ind + 3])
        self.ind += 3
        subpackets = []
        # print("v, t:", version, type_id)
        if type_id == 4:
            subpacket = self.parse_literal()
        else:
            subpacket = self.parse_operator()
        subpackets.append((version, type_id, subpacket))
        return subpackets

    def parse_all(self) -> list:
        subpackets = []
        while self.ind < self.maxind - 11:
            subpacket = self.parse_data()
            subpackets.append(subpacket)
            # self.skip_zeros()
        return subpackets

    def skip_zeros(self):
        while self.ind < self.maxind and self.binary[self.ind] == '0':
            self.ind += 1
def hex2binstr(hexstr):
    return "".join(map(lambda bit: bin(int(bit, 16))[2:].zfill(4), hexstr))

def bin2int(binstr):
    return int(binstr, 2)

def main():
    tests = ["D2FE28", # LITERAL 2021
             "38006F45291200", # LT 0, 2 SP LITERALS
             "EE00D40C823060", # LT 1, 3 SP LITERALS
             "8A004A801A8002F478", # OP [OP [OP [LITERAL]]] : V = 16
             "620080001611562C8802118E34", # OP [OP [2 LIT] * 2] V = 23
             "C0015000016115A2E0802F182340", # same structure as above v = 23
             "A0016C880162017C3686B18A3D4780", # OP [LIT * 5] v = 31
            ]
    for hexcase in tests:
        print(hexcase)
        print(hex2binstr(hexcase))
        parser = BinaryParser(hexcase)
        data = parser.parse_all()
        print(data)

if __name__ == "__main__":
    main()

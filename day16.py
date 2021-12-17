import sys
with open(sys.argv[1]) as raw_data:
    hex_packet = raw_data.read().strip()
bits = hex_packet
# bits = "D2FE28"
PACKET = "".join(map(lambda bit: bin(int(bit, 16))[2:].zfill(4), bits))

def read_literal(subpack):
    """
    VVV TTT AAAAA BBBBB CCCCC
    version = subpack[:3]
    type_id = subpack[3:6]
    d1 = subpack[6:11]
    d2 = subpack[11:16]
    d3 = subpack[16:21]
    extra = [21:]

    print(version, type_id, d1, d2, d3, extra)
    """
    return

def parse_operator(pack, ind, version, type_id, len_type_id):
    """
    len_type_id 0 : -> 15 - total length of bits in subpacket
    len_type_id 1 : -> 11 - number of subpackets immediately contained
    """
    c_ind = ind + 7 + (11 if len_type_id else 15)
    if len_type_id == 0:
        total_bits = int(pack[ind + 7: ind + 22], 2)
        while total_bits:
            s_vers = pack[c_ind: c_ind+3]
            s_type = pack[c_ind + 3: c_ind + 6]
            if s_type == 4:
                c_ind += 21
                total_bits -= 21
                yield [s_vers, s_type] 
            else:
                s_lti = pack[c_ind + 6]
                parse_operator(pack, c_ind, s_vers, s_type, s_lti)

    else:
        subpackets_remaining = int(pack[ind + 7: ind + 18], 2)


def parse_packet(pack):
    """
    type 4: literal
    type _: operator
        length_type 0: 15
        length_type 1: 11
    """
     # oper = {0: len("VVVTTTILLLLLLLLLLLLLLLAAAAAAAAAAABBBBBBBBBBBBBBBB"),
            # 1: len("VVVTTTILLLLLLLLLLLAAAAAAAAAAABBBBBBBBBBBCCCCCCCCCCC")}
    print("!", pack, "!")
    ind = 0
    while ind < len(pack):
        print(pack[ind:])
        version = int(pack[ind: ind + 3], 2)
        type_id = int(pack[ind + 3: ind + 6], 2)
        jump = 0

        if type_id == 4:
            jump = 21
            print("literal")
            read_literal(pack[ind: ind + jump])
        else:
            len_type_id = int(pack[ind + 6])
            parse_operator(pack, ind, version, type_id, len_type_id)

        if jump:
            ind += jump
            while ind < len(pack) and pack[ind] == "0":
                ind += 1
        break

    # print(solution1)
    # 597 (low)

test_1 = "D2FE28" # literal : (2021)
test_2 = "38006F45291200" # operator : LT 0, 2 SP
test_3 = "EE00D40C823060" # operator : LT 1, 3 SP
# parse_packet(PACKET)
def h2b(h):
    return "".join(map(lambda bit: bin(int(bit, 16))[2:].zfill(4), h))

parse_packet(h2b(test_2))


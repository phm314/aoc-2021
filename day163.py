import sys

def hex2binstr(hexstr):
    return "".join(map(lambda bit: bin(int(bit, 16))[2:].zfill(4), hexstr))

def bin2int(binstr):
    return int(binstr, 2)

def flatten(data):
    for group in data:
        if isinstance(group, list):
            yield flatten(group)
        else:
            yield group

def parse_data(PACKET, ind):
    while ind < len(PACKET):
        print(ind)
        version = bin2int(PACKET[ind: ind + 3])
        type_id = bin2int(PACKET[ind + 3: ind + 6])

        if type_id == 4:
            sub_data = [parse_literal(PACKET, ind + 6)]
        else:
            sub_data = [parse_operator(PACKET, ind + 6)]
        return sub_data

def parse_literal(PACKET, ind):
    has_zgroup = False
    num_groups = 0
    group_ind = ind
    final_bin = ""
    while not has_zgroup:
        bin_group = PACKET[group_ind + 1: group_ind + 5]
        final_bin += bin_group
        num_groups += 1
        if PACKET[group_ind] == "0":
            has_zgroup = True
        group_ind += 5
    literal_value = bin2int(final_bin)
    return (num_groups, literal_value)

def parse_operator(PACKET, ind):
    len_type = PACKET[ind]
    if len_type == '0':
        num = 15
    elif len_type == '1':
        num = 11
    len_argb = PACKET[ind + 1: ind + 1 + num]
    len_argc = bin2int(len_argb)
    counter = 0
    while counter < len_argc:
        parse_data(PACKET, ind + 1 + num + 1)
        break

def main(data):
    binstr = hex2binstr(data)
    ind = 0
    hierarchy = []
    while ind < len(binstr):
        sub_data = parse_data(binstr, ind)
        for x in sub_data:
            ind += x[0] * 5
        while ind < len(binstr) and binstr[ind] == '0':
            ind += 1
        hierarchy.append(sub_data)

tests = ["D2FE28", # LITERAL 2021
         "38006F45291200", # LT 2, 2 SP LITERALS
         ]

# BINARY_PACKET = hex2binstr(hex_packet)

main(tests[0])

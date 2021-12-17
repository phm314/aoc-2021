import sys

def hex2binstr(hexstr):
    return "".join(map(lambda bit: bin(int(bit, 16))[2:].zfill(4), hexstr))

def bin2int(binstr):
    return int(binstr, 2)

def parse_literal(PACKET, ind):
    """ return num_groups, int value, assumes start at [V]VVTTT... """
    has_zgroup = False
    num_groups = 0
    group_ind = ind + 6
    final_bin = ""
    while not has_zgroup:
        bin_group = PACKET[group_ind + 1: group_ind + 5]
        final_bin += bin_group
        num_groups += 1
        if PACKET[group_ind] == '0':
            has_zgroup = True
        group_ind += 5
    literal_value = bin2int(final_bin)
    return num_groups, literal_value

def parse_operator(PACKET, ind):
    """ 0: L=15 BITS, 1: L=11 SUBGROUPS """
    len_type = PACKET[ind + 6]
    # print(PACKET[ind:])
    # print("?", len_type)
    operator_data = []
    if len_type == 1:
        total_subpackets = bin2int(PACKET[ind + 7: ind + 7 + 11])
        count_subpackets = 0
        s_ind = ind + 7 + 11
        while count_subpackets < total_subpackets:
            s_vers = PACKET[s_ind: s_ind + 3]
            s_type = PACKET[s_ind + 3: s_ind + 6]
            if s_type == 4:
                literal_data = parse_literal(PACKET, s_ind)
                s_ind += literal_data[0] * 5 + 6
                operator_data.append((s_vers, s_type, literal_data))
                count_subpackets += 1
            else:
                op_info = parse_operator(PACKET, s_ind)
                operator_data.append(op_info)
    else:
        total_bits = bin2int(PACKET[ind + 7: ind + 7 + 15])
        count_bits = 0
        s_ind = ind + 7 + 15
        # print(PACKET[s_ind:])
        while count_bits < total_bits:
            s_vers = PACKET[s_ind: s_ind + 3]
            s_type = PACKET[s_ind + 3: s_ind + 6]
            if s_type == 4:
                literal_data = parse_literal(PACKET, s_ind)
                jump = literal_data[0] * 5 + 6
                s_ind += jump
                count_bits += jump
                operator_data.append((s_vers, s_type, literal_data))
            else:
                op_info = parse_operator(PACKET, s_ind)
                print(op_info)
                operator_data.append(op_info)

            break
    return operator_data



def parse_data(PACKET):
    """ READS NEXT 6 BITS for VVV TTT info, pass to literal/ operator.
        skips to start of next subpacket """
    solution1 = 0
    ind = 0
    # print("st: ", PACKET)
    while ind < len(PACKET):
        # print("c: ", ind, len(PACKET))
        version = bin2int(PACKET[ind: ind + 3])
        type_id = bin2int(PACKET[ind + 3: ind + 6])

        # print(version, type_id)
        if type_id == 4:
            solution1 += version
            literal_data = parse_literal(PACKET, ind)
            print("l: ", literal_data)
            ind += literal_data[0] * 5 + 6
            # jump ?
        else:
            op_info = parse_operator(PACKET, ind)
            flat_info = flatten_op(op_info)
            print(op_info)
            print(list(flat_info))

        while ind < len(PACKET) and PACKET[ind] == '0':
            ind += 1

        break

def flatten_op(op):
    for group in op:
        if isinstance(group, list):
            flatten_op(group)
        else:
            yield group


with open(sys.argv[1]) as raw_data:
    hex_packet = raw_data.read().strip()
tests = ["D2FE28", # LITERAL 2021
         "38006F45291200", # LT 2, 2 SP LITERALS
         ]

BINARY_PACKET = hex2binstr(hex_packet)

parse_data(hex2binstr(tests[1]))

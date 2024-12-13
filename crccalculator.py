import crcmod
test_string = "55 66 01 01 00 00 00 0c 00"
def crc_calculator(hex_commands):

    data_bytes = bytes.fromhex(hex_commands)
    crc16_xmodem = crcmod.mkCrcFun(poly=0x11021, initCrc=0, xorOut=0, rev=False)
    crc_value = crc16_xmodem(data_bytes)
    print(f"CRC-16 (XMODEM) for '{hex_commands}': {hex(crc_value)}")
    output_string=hex(crc_value)
    list_banavi=list(hex(crc_value))
    
    lsb_bit=output_string[-2:]
    msb_bit=output_string[-4:-2]
    print(f' msb bit:{msb_bit}')
    print(f' lsb bit:{lsb_bit}')
    return hex_commands+ " "+lsb_bit+" " +msb_bit
crc_output=crc_calculator(test_string)
print(f'this is the output command:{crc_output}')

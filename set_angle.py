import socket
bits=16
yaw=int(input('provide the yaw angle '))
pitch=int(input(' provide the pitch angle'))
def twos_complement(value, bit_width):
    """Convert a signed integer to its two's complement hexadecimal representation."""
    if value < 0:
        # Two's complement for negative values
        value = (1 << bit_width) + value  # Add the value to 2^bit_width
    return hex(value)

pitchhex=twos_complement(pitch,bits)
yawhex=twos_complement(yaw,bits)
final_pitchhex=pitchhex[2:].zfill(bits // 4)
final_yawhex=yawhex[2:].zfill(bits // 4)
print(final_pitchhex)
print(final_yawhex)
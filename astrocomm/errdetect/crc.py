class CRC:
    def __init__(self, polynomial=0b1101):
        self.polynomial = polynomial

    def compute_crc(self, data):
        crc = 0
        for byte in data:
            crc ^= byte
            for _ in range(8):
                if (crc & 0x80) != 0:  # Check if the highest bit is set
                    crc = (crc << 1) ^ self.polynomial
                else:
                    crc <<= 1
                crc &= 0xFF  # Keep CRC to 8 bits
        return crc

    def verify_crc(self, data):
        crc_received = data[-1]
        computed_crc = self.compute_crc(data[:-1])
        return computed_crc == crc_received

if __name__ == "__main__":
    data = [0b11010101, 0b01101011]  # Example data
    crc_instance = CRC()
    computed_crc = crc_instance.compute_crc(data)
    data.append(computed_crc)  # Append CRC to data
    print("Data with CRC:", data)

    if crc_instance.verify_crc(data):
        print("CRC Check: Data is valid.")
    else:
        print("CRC Check: Data is corrupted.")

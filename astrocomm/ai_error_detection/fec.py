import random
""""
 improve bitt error rate off communication link by adding reduntant info
"""
class FEC:
    def __init__(self, parity_bits=2):
        self.parity_bits = parity_bits

    def encode(self, data):
        # Prepare a list to hold encoded data
        encoded = data.copy()
        # Calculate parity bits
        for i in range(self.parity_bits):
            parity = sum(data[j] for j in range(len(data)) if j % (2 ** (i + 1)) < (2 ** i)) % 2
            encoded.append(parity)
        return encoded

    def decode(self, encoded):
        # Extract data and parity bits
        data = encoded[:-self.parity_bits]
        parity = encoded[-self.parity_bits:]
        
        # Error detection
        error_indices = []
        for i in range(self.parity_bits):
            parity_check = sum(data[j] for j in range(len(data)) if j % (2 ** (i + 1)) < (2 ** i)) % 2
            if parity_check != parity[i]:
                error_indices.append(i)
        
        # If errors are detected, correct them
        if error_indices:
            # Find the index to correct based on parity errors
            error_position = 0
            for idx in error_indices:
                error_position += 2 ** idx
        
            if error_position < len(data):
                data[error_position] ^= 1  # Flip the bit at the error position
        
        return data, not error_indices  # Return decoded data and validity

    def simulate_error(self, encoded):
        # Randomly introduce an error in the encoded data
        error_index = random.randint(0, len(encoded) - 1)
        encoded[error_index] ^= 1  # Flip the bit to simulate an error
        return encoded, error_index

if __name__ == "__main__":
    data = [1, 0, 1, 1]  # Sample data
    fec_instance = FEC(parity_bits=2)

    # Encode the data
    encoded_data = fec_instance.encode(data)
    print("Encoded Data:", encoded_data)

    # Simulate an error
    encoded_with_error, error_position = fec_instance.simulate_error(encoded_data.copy())
    print(f"Encoded Data with Simulated Error at Position {error_position}: {encoded_with_error}")

    # Decode the data
    decoded_data, is_valid = fec_instance.decode(encoded_with_error)
    print("Decoded Data:", decoded_data, "Valid:", is_valid)

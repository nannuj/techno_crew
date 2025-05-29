import numpy as np
""""
to provide realiable information optimal error ratwes

"""
class TurboCodes:
    def __init__(self, constraint_length=3, rate=1/2):
        self.constraint_length = constraint_length
        self.rate = rate  # Rate of the convolutional code

    def convolutional_encode(self, data):
        # Simplified convolutional encoding
        n = len(data)
        encoded = []

        # First encoder
        for i in range(n):
            if i == 0:
                encoded.append(data[i])  # Initial input
                encoded.append(data[i])  # First bit
            else:
                encoded.append(data[i] ^ data[i-1])  # XOR with previous bit for first encoder
                encoded.append(data[i])  # Second bit

        return encoded

    def interleave(self, data):
        # Simple interleaving
        n = len(data)
        interleaved = [0] * n
        for i in range(n):
            interleaved[i] = data[(i * 2) % n]  # Simple pattern for interleaving
        return interleaved

    def encode(self, data):
        # Perform Turbo encoding
        first_encoded = self.convolutional_encode(data)
        interleaved_data = self.interleave(data)
        second_encoded = self.convolutional_encode(interleaved_data)

        # Combine both encoded streams
        encoded = first_encoded + second_encoded
        return encoded

    def decode(self, encoded):
        # Simplified Turbo decoding (placeholder for iterative decoding)
        n = len(encoded) // 2
        decoded = encoded[:n]  # Just return the first half as a naive approach
        return decoded

    def simulate_error(self, encoded, error_rate=0.1):
        # Randomly introduce errors based on the error rate
        noisy_encoded = encoded.copy()
        for i in range(len(noisy_encoded)):
            if np.random.rand() < error_rate:
                noisy_encoded[i] ^= 1  # Flip the bit to introduce an error
        return noisy_encoded

if __name__ == "__main__":
    data = [1, 0, 1, 1]
    turbo_instance = TurboCodes()

    # Encode the data
    encoded_data = turbo_instance.encode(data)
    print("Turbo Encoded Data:", encoded_data)

    # Simulate transmission with errors
    noisy_encoded_data = turbo_instance.simulate_error(encoded_data, error_rate=0.2)
    print("Noisy Encoded Data (with errors):", noisy_encoded_data)

    # Decode the data
    decoded_data = turbo_instance.decode(noisy_encoded_data)
    print("Turbo Decoded Data:", decoded_data)

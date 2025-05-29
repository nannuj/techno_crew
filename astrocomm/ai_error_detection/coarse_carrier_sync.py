import numpy as np
""""
used frequency stability check

"""
class LDPC:
    def __init__(self):
        # Example parity-check matrix for LDPC
        self.H = np.array([[1, 1, 0, 0, 1],
                           [0, 1, 1, 0, 1],
                           [0, 0, 1, 1, 1]])
        self.n = self.H.shape[1]  # Number of columns (codeword length)
        self.m = self.H.shape[0]  # Number of rows (parity-check equations)

    def encode(self, data):
        # Padding data to match the codeword length
        padded_data = np.concatenate([data, np.zeros(self.n - len(data), dtype=int)])
        # Generate the codeword using the parity-check matrix
        codeword = (padded_data @ self.H.T) % 2  # Using modulo 2 for binary operations
        return codeword

    def decode(self, received):
        # Initialize messages
        messages = np.zeros((self.m, self.n), dtype=int)
        
        # Iterative decoding (Belief Propagation)
        for iteration in range(10):  # Number of iterations can be adjusted
            # Calculate messages from variable nodes to check nodes
            for j in range(self.n):
                involved_rows = np.where(self.H[:, j] == 1)[0]
                messages[:, j] = (1 - np.prod(1 - messages[involved_rows, j])) % 2
            
            # Update received based on messages
            for i in range(self.m):
                involved_columns = np.where(self.H[i, :] == 1)[0]
                received[i] = (received[i] + np.sum(messages[i, involved_columns])) % 2
        
        return received

    def simulate_error(self, encoded, error_rate=0.1):
        # Introduce random errors into the encoded message
        noisy_encoded = encoded.copy()
        for i in range(len(noisy_encoded)):
            if np.random.rand() < error_rate:
                noisy_encoded[i] ^= 1  # Flip the bit to introduce an error
        return noisy_encoded

if __name__ == "__main__":
    ldpc_instance = LDPC()
    data = np.array([1, 0, 1, 1])
    encoded_data = ldpc_instance.encode(data)
    print("LDPC Encoded Data:", encoded_data)

    # Simulate transmission with errors
    noisy_encoded_data = ldpc_instance.simulate_error(encoded_data, error_rate=0.2)
    print("Noisy Encoded Data (with errors):", noisy_encoded_data)

    # Decode the data
    decoded_data = ldpc_instance.decode(noisy_encoded_data)
    print("LDPC Decoded Data:", decoded_data[:len(data)])

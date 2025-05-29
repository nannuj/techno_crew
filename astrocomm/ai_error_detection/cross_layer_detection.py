class CrossLayerDetection:

    def detect_errors(self, data):
        """
        Detects errors in the given data.
        
        Returns:
            tuple: A boolean indicating if the data is valid, 
                   the count of errors, and the indices of erroneous bits.
                   //used diffrent para metters  diff type of protocols accross the communication stack
        """
        is_valid = True
        error_indices = []
        
        # Check if all bits are either 0 or 1
        for i, bit in enumerate(data):
            if bit not in (0, 1):
                is_valid = False
                error_indices.append(i)

        # Check for specific patterns (for example: [1, 0, 0] should not occur)
        if [1, 0, 0] in self.sliding_window(data, 3):
            is_valid = False
            error_indices.extend([i for i in range(len(data) - 2) if data[i:i+3] == [1, 0, 0]])

        error_count = len(error_indices)

        if not is_valid:
            print(f"Detected {error_count} error(s) at indices: {error_indices}")
        
        return is_valid, error_count, error_indices

    def sliding_window(self, data, window_size):
        """Generates sliding windows of specified size."""
        for i in range(len(data) - window_size + 1):
            yield data[i:i + window_size]

if __name__ == "__main__":
    cld_instance = CrossLayerDetection()
    
    # Example data input (can be altered for testing)
    data = [1, 0, 1, 1, 1, 0, 0, 1, 0]
    
    # Detect errors in the data
    valid, error_count

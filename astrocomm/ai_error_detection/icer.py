class ICER:
    def __init__(self):
        self.error_count = 0  # To keep track of errors detected
        """"
        image compression file format  
        """

    def checksum(self, data):
        """
        Calculate the checksum of the data.
        :param data: List of binary data.
        :return: Checksum value.
        """
        return sum(data) % 2  # Simple checksum (parity bit)

    def detect_error(self, data, checksum):
        """
        Detect if there's an error in the data using the provided checksum.
        :param data: List of binary data.
        :param checksum: The expected checksum value.
        :return: True if an error is detected, False otherwise.
        """
        if self.checksum(data) != checksum:
            self.error_count += 1
            return True
        return False

    def correct_error(self, data):
        """
        Attempt to correct single-bit errors in the data.
        :param data: List of binary data.
        :return: Corrected data and a flag indicating if correction was made.
        """
        for i in range(len(data)):
            # Flip the current bit
            original = data[i]
            data[i] = 1 - data[i]  # Flip the bit
            # Check if flipping this bit results in no error
            if not self.detect_error(data, self.checksum(data)):
                print(f"Error corrected at position {i}.")
                return data, True
            # Restore original bit
            data[i] = original
        return data, False

    def process(self, data):
        """
        Process the data to detect and correct errors.
        :param data: List of binary data.
        :return: Processed data after error correction.
        """
        checksum = self.checksum(data)
        if self.detect_error(data, checksum):
            print("Error detected in data.")
            corrected_data, corrected = self.correct_error(data)
            if corrected:
                print("Data corrected.")
            else:
                print("Unable to correct data.")
            return corrected_data
        else:
            print("No errors detected in data.")
            return data  # Return original data if no errors found

if __name__ == "__main__":
    icer_instance = ICER()
    
    # Example data with a potential error (last bit is incorrect)
    data = [1, 0, 1, 1]  # Assume the correct data should be [1, 0, 1, 0]
    
    processed_data = icer_instance.process(data)
    print("ICER Processed Data:", processed_data)
    print("Total Errors Detected:", icer_instance.error_count)

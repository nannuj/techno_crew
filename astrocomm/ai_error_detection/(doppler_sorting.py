class DopplerSorting:
    def __init__(self, speed_of_light=299792458):
        self.speed_of_light = speed_of_light  # Speed of light in meters per second

    def simulate_doppler_shift(self, frequency, velocity):
        """
        
        """
        # Formula for the Doppler effect (for sound in air)
        shifted_frequency = frequency * ((self.speed_of_light) / (self.speed_of_light - velocity))
        return shifted_frequency

    def sort(self, data, velocities):
        """
   
        """
        if len(data) != len(velocities):
            raise ValueError("Data and velocities must be of the same length.")

        shifted_frequencies = [self.simulate_doppler_shift(frequency, velocity) 
                                for frequency, velocity in zip(data, velocities)]
        sorted_data = [frequency for _, frequency in sorted(zip(shifted_frequencies, data))]
        return sorted_data

    def visualize_results(self, original_data, sorted_data):
        """
        Visualize the original and sorted data.
        :param original_data: Original data.
        :param sorted_data: Sorted data.
        """
        print("\nOriginal Frequencies: ", original_data)
        print("Sorted Frequencies:   ", sorted_data)

if __name__ == "__main__":
    doppler_instance = DopplerSorting()
    
    # Example frequencies (in Hz) and corresponding velocities (in m/s)
    original_data = [300, 400, 500, 600]  # Original frequencies
    velocities = [50, -30, 20, 10]  # Observer velocities (m/s)
    
    sorted_data = doppler_instance.sort(original_data, velocities)
    doppler_instance.visualize_results(original_data, sorted_data)

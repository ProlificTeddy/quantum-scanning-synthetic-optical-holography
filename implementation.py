import numpy as np
import torch
import torch.nn.functional as F

class SyntheticOpticalHolography:
    def __init__(self, image_size, wavelength, phase_step):
        self.image_size = image_size
        self.wavelength = wavelength
        self.phase_step = phase_step
        self.k = 2 * np.pi / wavelength  # Wave number

    def generate_synthetic_phase_carrier(self):
        x = np.linspace(-1, 1, self.image_size)
        y = np.linspace(-1, 1, self.image_size)
        X, Y = np.meshgrid(x, y)
        phase_carrier = np.sin(self.k * X) + np.cos(self.k * Y)
        return torch.tensor(phase_carrier, dtype=torch.float32)

    def holographic_reconstruction(self, intensity_measurements):
        # Perform Fourier-based holographic reconstruction
        intensity_measurements = torch.stack(intensity_measurements, dim=0)
        phase_shifts = torch.arange(0, len(intensity_measurements)) * self.phase_step
        phase_shifts = phase_shifts.view(-1, 1, 1)

        # Apply synthetic phase carrier
        synthetic_phase = torch.exp(1j * phase_shifts)
        hologram = torch.sum(intensity_measurements * synthetic_phase, dim=0)

        # Perform inverse Fourier transform to reconstruct the image
        reconstructed_field = torch.fft.ifft2(hologram)
        amplitude = torch.abs(reconstructed_field)
        phase = torch.angle(reconstructed_field)
        return amplitude, phase

if __name__ == '__main__':
    # Parameters
    image_size = 128
    wavelength = 0.5  # Arbitrary units
    phase_step = np.pi / 4

    # Initialize the Synthetic Optical Holography system
    soh = SyntheticOpticalHolography(image_size, wavelength, phase_step)

    # Generate synthetic phase carrier
    phase_carrier = soh.generate_synthetic_phase_carrier()

    # Simulate intensity measurements with phase shifts
    num_measurements = 8
    intensity_measurements = []
    for i in range(num_measurements):
        phase_shift = i * phase_step
        object_field = torch.exp(1j * (phase_carrier + phase_shift))
        intensity = torch.abs(object_field) ** 2
        intensity_measurements.append(intensity)

    # Perform holographic reconstruction
    amplitude, phase = soh.holographic_reconstruction(intensity_measurements)

    # Display results
    print("Reconstructed Amplitude:")
    print(amplitude)
    print("Reconstructed Phase:")
    print(phase)
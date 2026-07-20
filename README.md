# Quantum Scanning Synthetic Optical Holography

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)  
[![Python](https://img.shields.io/badge/Python-3.8%2B-blue)](https://www.python.org/)  
[![arXiv](https://img.shields.io/badge/arXiv-2607.16176v1-b31b1b)](https://arxiv.org/pdf/2607.16176v1)  

---

## Overview

This repository contains a Python implementation of the research paper **"Quantum scanning synthetic optical holography"** by Josué R. León-Torres et al. ([arXiv:2607.16176v1](https://arxiv.org/pdf/2607.16176v1)). The paper introduces a novel approach to quantum imaging by integrating **Synthetic Optical Holography (SOH)** into **Quantum Imaging with Undetected Light (QIUL)**. 

The method allows for the reconstruction of amplitude and phase images of objects probed by mid-infrared (MIR) photons, while detecting only their visible-wavelength partner photons. This enables **diffraction-limited, label-free MIR phase imaging** using visible light detection, decoupling spatial resolution from photon-pair spatial correlations.

### Key Contributions:
1. **Synthetic Optical Holography (SOH):** A technique for holographic reconstruction in scanning optical microscopy, extended here to the quantum regime.
2. **Quantum Imaging with Undetected Light (QIUL):** A paradigm where information about MIR photons is obtained by detecting their visible counterparts.
3. **Complex-Field Reconstruction:** Amplitude and phase imaging of binary, transparent, and biological samples in the quantum domain.
4. **Practical Benefits:** Label-free imaging, diffraction-limited resolution, and reduced reliance on MIR detectors.

---

## How It Works

### Synthetic Optical Holography in the Quantum Regime

The core idea of the method is to combine **SOH** with **QIUL** for imaging. Here's a breakdown of the process:

1. **Photon Pair Generation:**
   - A nonlinear crystal generates entangled photon pairs: one in the mid-infrared (MIR) spectrum (probe photon) and the other in the visible spectrum (reference photon).
   
2. **Object Interaction:**
   - The MIR photon interacts with the object of interest, encoding amplitude and phase information about the object.
   
3. **Synthetic Phase Carrier:**
   - A controlled synthetic phase carrier is introduced into the scanning system to enable holographic reconstruction.

4. **Visible Photon Detection:**
   - Only the visible photon is detected, and its interference pattern is recorded.

5. **Reconstruction:**
   - Using the synthetic phase carrier, the amplitude and phase of the object are computationally reconstructed from the detected interference pattern.

This approach eliminates the need for direct MIR detection, which is often challenging due to the lack of efficient MIR detectors.

---

## Repository Structure

```
quantum-soh/
├── implementation.py   # Main Python script implementing the method
├── requirements.txt    # List of dependencies
├── LICENSE             # MIT License
├── README.md           # Project documentation
└── examples/           # Example scripts and datasets
    ├── binary_sample/
    ├── transparent_sample/
    └── biological_sample/
```

---

## Getting Started

### Prerequisites

- Python 3.8 or higher
- Install the required dependencies by running:

```bash
pip install -r requirements.txt
```

### Usage

The main implementation is provided in the `implementation.py` script. Here's how you can use it:

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/quantum-soh.git
   cd quantum-soh
   ```

2. Run the script with your desired input parameters:
   ```bash
   python implementation.py --input examples/binary_sample/sample_data.npy --output results/binary_sample_reconstruction.png
   ```

   **Command-line arguments:**
   - `--input`: Path to the input data file (e.g., `.npy` file containing the interference pattern).
   - `--output`: Path to save the reconstructed amplitude and phase images.

3. View the results:
   - The script will save the reconstructed amplitude and phase images to the specified output path.

### Example

To reconstruct the amplitude and phase of a binary sample:

```bash
python implementation.py --input examples/binary_sample/sample_data.npy --output results/binary_sample_reconstruction.png
```

---

## Results

The implementation has been tested on three types of samples:
1. **Binary Samples:** High-contrast objects with well-defined edges.
2. **Transparent Samples:** Objects with varying phase but minimal amplitude variation.
3. **Biological Samples:** Complex structures with both amplitude and phase variations.

### Sample Output:
| Sample Type       | Amplitude Image                     | Phase Image                         |
|-------------------|-------------------------------------|-------------------------------------|
| Binary Sample     | ![Binary Amplitude](results/binary_amplitude.png) | ![Binary Phase](results/binary_phase.png) |
| Transparent Sample| ![Transparent Amplitude](results/transparent_amplitude.png) | ![Transparent Phase](results/transparent_phase.png) |
| Biological Sample | ![Biological Amplitude](results/biological_amplitude.png) | ![Biological Phase](results/biological_phase.png) |

---

## Citation

If you use this implementation in your research, please cite the original paper:

```
@article{leon2023quantumsoh,
  title={Quantum scanning synthetic optical holography},
  author={Josué R. León-Torres, Byron Caiza, Nadia Baumann, Sebastian Töpfer, Anna Mühlig, Orlando Guntinas-Lichius, Karin Burger, Frank Setzpfandt, Markus Gräfe, Valerio Flavio Gili},
  journal={arXiv preprint arXiv:2607.16176v1},
  year={2023}
}
```

---

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

## Contributing

Contributions are welcome! If you have suggestions for improvements or new features, feel free to open an issue or submit a pull request.

---

## Acknowledgments

This implementation is inspired by the groundbreaking work of **Josué R. León-Torres et al.** on quantum imaging. Special thanks to the authors for their contributions to the field of quantum optics and imaging.

---

Happy coding! 😊
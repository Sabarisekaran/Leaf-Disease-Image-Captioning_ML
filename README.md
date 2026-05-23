# Leaf Disease Image Captioning ML

A machine learning project for classifying and captioning plant leaf diseases using image processing and deep learning models.

## Project Structure

```
├── src/                    # Source code modules
├── data/
│   ├── raw/               # Original, unprocessed data
│   └── processed/         # Processed data for modeling
├── models/
│   └── trained/           # Trained model checkpoints
├── notebooks/             # Jupyter notebooks for exploration and experimentation
├── config/                # Configuration files
├── results/               # Output predictions and results
├── tests/                 # Unit tests
├── docs/                  # Documentation
├── requirements.txt       # Project dependencies
└── README.md             # This file
```

## Installation

1. Create a virtual environment (if not already done):
```bash
python -m venv .venv
```

2. Activate the virtual environment:
```bash
# On Windows:
.venv\Scripts\activate
# On macOS/Linux:
source .venv/bin/activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

## Usage

```python
from src.predict import predict_caption

image_paths = ["path/to/image1.jpg", "path/to/image2.jpg"]
captions = predict_caption(image_paths)

for i, caption in enumerate(captions):
    print(f"Image {i+1}: {caption}")
```

## Model Information

- **Model Type**: Image Classification with Hugging Face Transformers
- **Input**: Plant leaf images (RGB)
- **Output**: Disease classification/caption

## Contributing

Please follow these guidelines when contributing to this project:
- Create feature branches for new work
- Add tests for new functionality
- Update documentation as needed

## License

MIT License

## Authors

- Your Name

## Contact

[Your contact information]

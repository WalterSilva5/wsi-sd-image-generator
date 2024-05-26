# Image Generator Application

This is a simple image generator application built with Tkinter, leveraging the `diffusers` library to generate pixel art sprite sheet images using a pre-trained Stable Diffusion model. The application follows the MVC (Model-View-Controller) design pattern for better organization and maintainability.

## Table of Contents
- [Installation](#installation)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [License](#license)

## Installation

### Prerequisites
- Python 3.7 or later
- CUDA-compatible GPU (for running the model)

### Dependencies
1. Clone the repository:
    ```bash
    git clone https://github.com/yourusername/image-generator-app.git
    cd image-generator-app
    ```

2. Create a virtual environment and activate it:
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. Install the required packages:
    ```bash
    pip install -r requirements.txt
    ```

### `requirements.txt`
Ensure your `requirements.txt` contains the following:
```
diffusers
torch
transformers
Pillow
tk
```

## Usage

To run the application, execute the `main.py` file:
```bash
python main.py
```

### Features
- **Generate Image**: Enter a prompt and click "Generate" to create an image based on the prompt.
- **Open Image**: Open and display an existing image file.

## Project Structure

```
.
├── src
│   ├── controllers
│   │   └── image_generator_controller.py   # Controller code to handle user input and update the view
│   ├── models
│   │   └── image_generator_model.py        # Contains the model for generating images
│   └── views
│       └── image_generator_view.py         # Contains the GUI code
├── main.py                                 # Main file to initiate the application
├── requirements.txt                        # List of required Python packages
├── README.md                               # Project README file
```

### Model (`src/models/image_generator_model.py`)
Handles the image generation logic using the `StableDiffusionPipeline`.

### View (`src/views/image_generator_view.py`)
Defines the GUI elements and layout using Tkinter.

### Controller (`src/controllers/image_generator_controller.py`)
Connects the Model and View, handles user inputs, and updates the GUI accordingly.

### Main (`main.py`)
Initiates the application by creating an instance of the controller.


## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

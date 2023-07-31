# Storage Space Calculator

This web application is a storage space calculator built with Flask and Bootstrap. The calculator provides an estimation of how much storage space would be required for various types of files like photos, videos, MP3 files, documents, and PowerPoint presentations.

The application allows users to input the number of each file type and calculates the estimated total storage space required based on predetermined average file sizes.

## Installation

1. Clone the repository:

```bash
git clone https://github.com/yourusername/StorageCalculator.git
cd StorageCalculator
```

1. Create and activate a virtual environment

```bash
python3 -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
```

1. Install the dependencies:

```bash
pip install -r requirements.txt
```

1. Run the development server:

```bash
python app.py
```

Then open a web browser and go to [http://127.0.0.1:5000/](http://127.0.0.1:5000/) to see the application in action.

## Assumptions

The calculation is based on the following average file sizes:

Photos: 5 MB each
Videos: 11.67 MB per minute
MP3 files: 5 MB per 5-minute song
Documents: 0.1 MB each
PowerPoint presentations: 2 MB each
Please note that these are rough estimations and actual file sizes may vary.

## License

This project is licensed under the terms of the MIT license.
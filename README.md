# PDF to Images Converter

This project converts a PDF file into individual images, saving each page as a separate PNG file. It utilizes the `pdf2image` library, which requires Poppler to be installed on your system.

## Requirements

- Python 3.6+
- `pdf2image` library
- Poppler (must be installed and accessible in the system `PATH`)

## Installation

### Install Python Dependencies

Create a virtual environment (optional but recommended):
```bash
python -m venv venv
source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
```

Install required packages:
```bash
pip install pdf2image
```

### Install Poppler

#### **Ubuntu/Debian**:
```bash
sudo apt update
sudo apt install poppler-utils
```

#### **macOS (using Homebrew)**:
```bash
brew install poppler
```

#### **Windows**:
1. Download the latest Poppler binaries from: [Poppler Windows Releases](https://github.com/oschwartz10612/poppler-windows/releases)
2. Extract the downloaded zip file.
3. Add the `bin` folder inside the extracted directory to your system `PATH`.
4. Verify installation by running:
   ```bash
   pdfinfo -v
   ```

## Usage

Run the script to convert a PDF file into images:
```bash
python convert.py -i path/to/yourfile.pdf
```

### Output

The converted images will be saved in the `./output` directory with filenames in the format:
```
output/<pdf_filename>_page_<page_number>.png
```

## Troubleshooting

### Error: `pdf2image.exceptions.PDFInfoNotInstalledError`
- Ensure Poppler is installed and added to the system `PATH`.
- Run `pdfinfo -v` to check if it is correctly installed.

### Error: `FileNotFoundError: [Errno 2] No such file or directory: 'pdfinfo'`
- This means Poppler is missing. Install it using the steps in the **Installation** section.

## License
This project is licensed under the MIT License.

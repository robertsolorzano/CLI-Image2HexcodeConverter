# HexConvert [![MIT License](https://img.shields.io/badge/License-MIT-blue.svg)](https://opensource.org/licenses/MIT)


HexConvert is a simple Python CLI utility that converts the first pixel of an image file to Hex color code. Inspired when I needed to obtain a hex color code from an image when styling for a school project and thought this can be streamlined.

![Preview image](/assets/preview.png)

## Installation

1. Clone this repository:
```bash
git clone https://github.com/robertsolorzano/HexConvert.git
```
2. Navigate to the project directory & run the script:
```bash
python main.py
```

### Usage

- **Open File Explorer**: Press 'O' to open the file explorer, allowing you to browse and select an image file.
- **Paste File Path**: Press 'P' to directly paste the file path from the clipboard, then press Enter to confirm.
- **Display Hex Color**: After the file is selected or the path is pasted, the hex color of the first pixel will be displayed on the screen.


## Create an alias and add file to path
Navigate to the directory containing the script: 
```bash
cd /path/to/image-to-hexcode-converter
```

Open ~/.bashrc or ~/.bash_profile:
```bash
nano ~/.bashrc
```
Or:
```bash
nano ~/.bash_profile
```

Add the following line to your ~/.bashrc or ~/.bash_profile:
```bash
alias hexconvert="python /path/to/image-to-hexcode-converter/main.py"
```

Apply changes:
```bash
source ~/.bashrc
```

Now you can use the ```hexconvert``` alias anywhere in your terminal to run the utility easily ✅

### Contributions
Feel free to customize it further to better fit your project's need.

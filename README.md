# Image to Hexcode Converter

This is a simple Python utility that converts the hex color of the first pixel of an image file. Inspired when I needed to obtain an exact color from an image when styling for a project. 

This is a command line interface script that can be used as a quick utility within your workflow.

## Installation

1. Clone this repository:
```bash
git clone https://github.com/your_username/image-to-hexcode-converter.git
```
2. Navigate to the project directory & run the script:
```bash
python main.py
```

### Usage

- Press 'O' to open the file explorer and select an image file.
- Press 'P' to paste the file path from the clipboard and press Enter.
- The hex color of the first pixel will be displayed.

## Adding to Path and Creating an Alias

Navigate to the directory containing the script: 
```bash
cd /path/to/image-to-hexcode-converter
```
### Add the directory to your system's PATH

For Gitbash open your config file:
```bash
nano ~/.bashrc
```

Add the following line to your ~/.bashrc:
```bash
export PATH="$PATH:/path/to/image-to-hexcode-converter"
```

## Create an alias for easy use
Add the following line to your ~/.bashrc or ~/.bash_profile:
```bash
alias hexconvert="python /path/to/image-to-hexcode-converter/main.py"
```

Apply Changes:
```bash
source ~/.bashrc
```

Now you can use the 'hexconvert' alias in your terminal to run the utility easily.
### Contributions
Feel free to customize it further to better fit your project's need.

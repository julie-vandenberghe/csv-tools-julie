# My Package
filter and join functionalities on csv files

## Installation
You can install the package using pip:
```bash
pip install julie_package
```

## Tests
To run the tests, execute:
```bash
python3 script_test_julie
```
This script:
- Creates sample CSV files for testing
- Displays the original CSV in the terminal
- Applies a filter on a column and displays the result
- Joins two CSV files on a common key and displays the result


## Project structure
Algo_Julie/
│
├── julie_package/                # Code folder (the actual package)
│   ├── __init__.py               # Makes the folder importable as a module
│   ├── testalgo_julie.py         # Your file containing the pandas functions
│
├── script_test_julie.py          # Unit tests
│
├── README.md                     # Project documentation
├── setup.py                      # Installation script
└── cardata.csv                   # Sample data file
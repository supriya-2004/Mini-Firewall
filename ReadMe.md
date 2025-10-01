# Mini-Firewall

A command-line tool written in Python that simulates a simple firewall's packet processing logic. It reads packet data (serial number and priority) from a file, sorts them in configurable batches based on priority and serial number, and prints the ordered result to standard output.
The tool is designed to be robust, handling various input formats and providing clear warnings for invalid data while keeping the final output clean and predictable.

---

## Features ✨
- **Batch Processing**: Processes packets in batches of 10 to simulate firewall queue processing.

- **Two-Level Sorting**: Sorts packets first by priority (ascending, 1=highest) and then by serial number (ascending) to resolve ties.

- **Robust Parser**: Tolerant to different delimiters (commas, spaces, tabs) and extra whitespace in the input file.

- **Input Validation**: Validates that packet priorities are within the required range of 1-10 and safely skips malformed or invalid lines with clear warnings.

- **Clean Output**: Produces a simple, clean list of sorted packets, suitable for scripting or automated checking. Warnings and errors are sent to `stderr` to avoid polluting the results.

- **Error Handling**: Provides user-friendly messages for common issues like a missing input file.

---

## Usage
1. **Prepare the Input File**
- Modify the `input.txt` file to include your packet data. Each line should contain a serial number and a priority, separated by a comma, space, or tab.
```bash
# input.txt
# Each line: <serial_number> <priority>

3,1
10,1
2	3
4 3
1,   5
```

2. **Run the Script**
- Execute the script from your terminal:
```bash

python firewall_v2.py
```
3. **View the Output**
- The script will print the sorted list of packets directly to the console (standard output). Any warnings or errors will be printed to the standard error stream, keeping the primary output clean.

---

## Example
This example demonstrates how the script handles a mixed-format input file and produces a clean, sorted output.
1. `input.txt`
```bash

# This input file tests the robust parser.
# The script will correctly parse all valid lines and skip invalid ones.

# Valid data with standard comma delimiter
3,1
10,1

# Test for lines separated by tabs and spaces
2	3
4 3

# Test for adversarial spacing
 1,   5
 9 ,5

# More valid data
5,7
6,10

# Invalid data that should be skipped with a warning
16,11
this is not a packet

# Another valid packet to complete the first batch of 10
11,2
12,8

# This packet will start the second batch
13,1
```
2. **Running the Command**
```bash
python firewall_v2.py
```
3. **Output**
The script processes the 11 valid packets in two batches (one of 10, one of 1) and prints the following sorted result to standard output:
```bash
3,1
10,1
11,2
2,3
4,3
1,5
9,5
5,7
12,8
6,10
13,1
```
Simultaneously, it prints the following warnings for the invalid lines to standard error:
```bash
Warning: Skipping line #16 due to invalid priority (11). Must be 1-10.
Warning: Skipping malformed line #17: 'this is not a packet'
```




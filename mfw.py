# firewall_v2.py
import re
import sys

def process_firewall_packets(file_content, batch_size=10):
    """
    Processes and sorts firewall packets with a robust parser and clean output.

    Args:
        file_content (str): A string containing the packet data.
        batch_size (int): The number of packets to process at a time.
    """
    all_packets = []
    
    # Iterate through each line to parse packet data.
    for line_num, line in enumerate(file_content.strip().split('\n'), 1):
        clean_line = line.strip()
        
        # Skip empty lines or lines that are comments (starting with #)
        if not clean_line or clean_line.startswith('#'):
            continue
            
        # 1. Use regex to split by comma or any whitespace, making the parser robust.
        parts = re.split(r'[,\s]+', clean_line)
        
        if len(parts) != 2:
            print(f"Warning: Skipping malformed line #{line_num}: '{line}'", file=sys.stderr)
            continue
            
        try:
            serial_str, priority_str = parts
            serial_no = int(serial_str)
            priority = int(priority_str)
            
            # 2. Add validation for the priority range [1..10].
            if not (1 <= priority <= 10):
                print(f"Warning: Skipping line #{line_num} due to invalid priority ({priority}). Must be 1-10.", file=sys.stderr)
                continue
                
            all_packets.append((priority, serial_no))
            
        except ValueError:
            print(f"Warning: Skipping non-numeric data on line #{line_num}: '{line}'", file=sys.stderr)

    # Process the valid packets in batches.
    for i in range(0, len(all_packets), batch_size):
        batch = all_packets[i : i + batch_size]
        batch.sort()
        
        # 3. Print only the clean, sorted packet data as required.
        for priority, serial_no in batch:
            print(f"{serial_no},{priority}")

def main():
    """
    Main function to read the input file and run the firewall processing.
    """
    input_filename = "input.txt"
    try:
        with open(input_filename, 'r') as f:
            file_content = f.read()
        process_firewall_packets(file_content)
    except FileNotFoundError:
        # Print errors to stderr to separate them from standard output.
        print(f"Error: The file '{input_filename}' was not found.", file=sys.stderr)
    except Exception as e:
        print(f"An unexpected error occurred: {e}", file=sys.stderr)

if __name__ == "__main__":
    main()
# filter_duplicate_lines.py

def remove_duplicates(input_file, output_file):
    unique_lines = set()
    output_lines = []
    total_lines = 0
    distinct_lines = 0
    duplicates = 0

    # Specify UTF-8 encoding for reading the file
    with open(input_file, 'r', encoding='utf-8') as f:
        for line in f:
            total_lines += 1
            stripped_line = line.strip()
            if stripped_line == "":
                # Maintain empty lines to preserve grouping
                output_lines.append("")
            elif line not in unique_lines:
                unique_lines.add(line)
                distinct_lines += 1
                output_lines.append(line.rstrip())
            else:
                duplicates += 1

    # Write the unique lines to the output file, maintaining the structure
    # Specify UTF-8 encoding for writing the file
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write("\n".join(output_lines) + "\n")

    # Calculate total lines in the output file
    output_total_lines = len(output_lines)

    # Print statistics
    # print(f"Input file statistics:")
    # print(f"  Total lines: {total_lines}")
    # print(f"  Distinct lines: {distinct_lines}")
    # print(f"  Duplicate lines: {duplicates}")
    # print(f"Output file statistics:")
    # print(f"  Total lines: {output_total_lines}")
    # print(f"  Distinct lines: {distinct_lines}")

def remove_extra_empty_lines(input_file, output_file):
    output_lines = []
    previous_line_empty = False

    # Specify UTF-8 encoding for reading the file
    with open(input_file, 'r', encoding='utf-8') as f:
        for line in f:
            stripped_line = line.strip()
            if stripped_line == "":
                if not previous_line_empty:
                    output_lines.append("")
                previous_line_empty = True
            else:
                output_lines.append(line.rstrip())
                previous_line_empty = False

    # Write the cleaned lines to the output file
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write("\n".join(output_lines) + "\n")

if __name__ == "__main__":
    input_file = "url_list.txt"
    intermediate_file = "dups_removed.txt"
    final_output_file = "cleaned_output.txt"

    # First, remove duplicates
    remove_duplicates(input_file, intermediate_file)
    
    # Then, remove extra empty lines
    remove_extra_empty_lines(intermediate_file, final_output_file)

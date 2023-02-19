import json
import csv

# Load the spec from the JSON file
with open("spec.json", "r") as spec_file:
    spec = json.load(spec_file)

# Define the input and output file names
input_file = "input.txt"
output_file = "output/output.csv"

# Generate the fixed-width file using the spec
with open(input_file, "w") as f:
    if spec["IncludeHeader"] == "True":
        # Write the header line if IncludeHeader is True
        header = "".join([col.ljust(int(offset)) for col, offset in zip(spec["ColumnNames"], spec["Offsets"])])
        f.write(header + "\n")
    
    # Generate some fake data
    data = []
    dic = {}
    for i in range(len(spec["ColumnNames"])):
        dic[spec["ColumnNames"][i]] = 'v' + str(i)
    ## generate sample data like [{'f1':'v1'}]
    data.append(dic)

    for row in data:
        line = "".join([str(row[col]).ljust(int(spec["Offsets"][i])) for i, col in enumerate(spec["ColumnNames"])])
        f.write(line + "\n")

def parse_fixed_width_file(input_file, output_file, spec):
    # Parse the fixed-width file and generate the delimited CSV file
    with open(input_file, "r", encoding=spec["FixedWidthEncoding"]) as f:
        with open(output_file, "w", newline="", encoding=spec["DelimitedEncoding"]) as output:
            writer = csv.DictWriter(output, fieldnames=spec["ColumnNames"])
            if spec["IncludeHeader"] == "True":
                writer.writeheader()
                next(f)
            for line in f:
                # Parse the fixed-width line into a dictionary
                row = {col: line[int(sum(map(int, spec["Offsets"][:i]))):int(sum(map(int, spec["Offsets"][:i+1])))].strip() for i, col in enumerate(spec["ColumnNames"])}
                # Write the row to the CSV file
                writer.writerow(row)

parse_fixed_width_file(input_file, output_file, spec)
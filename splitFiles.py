import os
import pandas as pd

def split_csv(input_file, num_splits, output_dir):
    try:
        # Read the input CSV file
        df = pd.read_csv(input_file)
        
        # Calculate the number of rows per split
        total_rows = len(df)
        rows_per_split = total_rows // num_splits
        remainder = total_rows % num_splits
        
        # Create the output directory if it doesn't exist
        os.makedirs(output_dir, exist_ok=True)
        
        # Create the split files
        for i in range(num_splits):
            start_idx = i * rows_per_split
            end_idx = (i + 1) * rows_per_split
            if i == num_splits - 1:
                end_idx += remainder
            split_df = df.iloc[start_idx:end_idx]
            output_file = os.path.join(output_dir, f"{os.path.splitext(os.path.basename(input_file))[0]}_split_{i+1}.csv")
            split_df.to_csv(output_file, index=False)
        
        print(f"{num_splits} CSV files created in '{output_dir}' with approximately {rows_per_split} rows each.")
    except FileNotFoundError:
        print("Error: Input file not found.")

def main():
    input_file = input("Enter the path to the input CSV file: ")
    num_splits = int(input("Enter the number of splits: "))
    output_dir = input("Enter the output directory: ")
    
    split_csv(input_file, num_splits, output_dir)

if __name__ == "__main__":
    main()

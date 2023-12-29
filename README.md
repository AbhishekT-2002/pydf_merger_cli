# PDF Merger

This Python script allows you to merge multiple PDF files into a single PDF. You can either merge all PDFs in a directory or select specific ones for merging.

## Requirements
- Python 3.x
- PyPDF2 library (`pip install PyPDF2`)

## Usage

1. Place the script in the directory containing the PDF files you want to merge.

2. Open a terminal and navigate to the script's directory.

3. Run the script using the following command:
   ```bash
   python script_name.py
   ```

4. Follow the on-screen instructions to select and merge the desired PDF files.

## Script Details

### `merge_selected_pdfs(file_list, output_filepath, skip_sort)`

- `file_list`: List of PDF files to be merged.
- `output_filepath`: Path to the output merged PDF file.
- `skip_sort`: Flag to skip sorting the selected PDFs.

### Running the Script

1. The script lists all available PDF files in the current directory.
2. Enter the indices of the PDFs to merge (comma-separated), or enter '0' to merge all files.
3. If merging all files, confirm the operation.
4. Optionally, choose to sort the selected PDFs by filename.
5. Provide a custom name for the output file (optional).

### Logging

- The script logs errors to a file named `merged.log` in the output directory.

## Example

```bash
python merge_pdfs.py
```

**Note:** Ensure that Python is in your system's PATH, and the PyPDF2 library is installed (`pip install PyPDF2`).

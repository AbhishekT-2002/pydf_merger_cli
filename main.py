import os
import logging
from PyPDF2 import PdfMerger

def merge_selected_pdfs(file_list, output_filepath, skip_sort):
    merger = PdfMerger()

    try:
        if skip_sort == False:
            sort_choice = input("Sort the selected PDFs by filename? (y/n): ").lower()
            if sort_choice == 'y':
                # Sort the selected PDF files
                file_list.sort()
            else:
                print("PDFs will be merged in the order they were selected.")

        for pdf_file in file_list:
            merger.append(pdf_file)

        # Create the output directory if it doesn't exist
        output_directory = os.path.dirname(output_filepath)
        if not os.path.exists(output_directory):
            os.makedirs(output_directory)
        
        # Configure logging with an explicit log file path
        log_filepath = os.path.join(output_directory, "merged.log")
        logging.basicConfig(filename=log_filepath, level=logging.ERROR)

        # Save the merged PDF
        merger.write(output_filepath)
        print(f"Merged selected PDFs into '{output_filepath}'")


    except Exception as e:
        logging.error(f"An error occurred: {e}")

if __name__ == "__main__":
    # Flag to skip sorting the selected PDFs
    skip_sort = False
    # Specify the directory containing your PDFs
    directory = os.getcwd()

    # List all PDF files in the directory for user selection
    pdf_files = [ f for f in os.listdir(directory) if f.endswith(".pdf")]

    print("Available PDF files:")
    for i, pdf_file in enumerate(pdf_files, start=1):
        print(f"{i}. {pdf_file}")

    # Prompt the user to select files by index
    while True:
        selected_indices = input("Enter the indices of the PDFs to merge (comma-separated), or '0' to merge all: ")

        if selected_indices == '0':
            skip_sort = True
            # Confirm with the user before merging all PDFs
            confirm_merge = input("Are you sure you want to merge all PDFs? (y/n): ").lower()
            if confirm_merge == 'y':
                selected_files = [os.path.join(directory, pdf_file) for pdf_file in pdf_files]
                break
            else:
                print("Operation canceled. No files were merged.")
        else:
            try:
                selected_indices = [int(index) for index in selected_indices.split(',')]
                if all(1 <= idx <= len(pdf_files) for idx in selected_indices):
                    selected_files = [os.path.join(directory, pdf_files[idx-1]) for idx in selected_indices]
                    break
                else:
                    print("Invalid index. Please enter a valid integer within the range.")
            except ValueError:
                print("Invalid input. Please enter a valid integer or '0'.")

    if selected_files:
        # Allow the user to input a custom name for the output file
        custom_output_directory = input("Enter a name: ") + " merged"
        output_filename = f"{custom_output_directory}.pdf"

        # Create a full path for the output file within the specified directory
        output_filepath = os.path.join(directory, custom_output_directory, output_filename)

        # Merge selected PDFs
        merge_selected_pdfs(selected_files, output_filepath, skip_sort)

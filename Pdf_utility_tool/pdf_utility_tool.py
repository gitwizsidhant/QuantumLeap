import PyPDF2
import tkinter as tk
from tkinter import filedialog

def select_files():
    global pdfiles
    pdfiles = filedialog.askopenfilenames(filetypes=[("PDF Files", "*.pdf")])
    if pdfiles:
        merge_button.config(state=tk.NORMAL)
        remove_button.config(state=tk.NORMAL)
        extract_button.config(state=tk.NORMAL)

def merge_pdfs():
    if pdfiles:
        pdfMerge = PyPDF2.PdfMerger()
        for filename in pdfiles:
            pdfFile = open(filename, 'rb')
            pdfReader = PyPDF2.PdfReader(pdfFile)
            pdfMerge.append(pdfReader)
            pdfFile.close()

        output_path = filedialog.asksaveasfilename(defaultextension=".pdf", filetypes=[("PDF Files", "*.pdf")])
        if output_path:
            pdfMerge.write(output_path)

def remove_pages():
    global pdfiles
    if pdfiles:
        for filename in pdfiles:
            pdfFile = open(filename, 'rb')
            pdfReader = PyPDF2.PdfFileReader(pdfFile)
            pdfWriter = PyPDF2.PdfFileWriter()

            for page_num in range(pdfReader.numPages):
                if page_num not in pages_to_remove:
                    page = pdfReader.getPage(page_num)
                    pdfWriter.addPage(page)

            output_path = filename.replace('.pdf', '_removed.pdf')
            with open(output_path, 'wb') as output_file:
                pdfWriter.write(output_file)

            pdfFile.close()

def extract_pages():
    global pdfiles
    if pdfiles:
        for filename in pdfiles:
            pdfFile = open(filename, 'rb')
            pdfReader = PyPDF2.PdfFileReader(pdfFile)

            for page_num in pages_to_extract:
                page = pdfReader.getPage(page_num)
                pdfWriter = PyPDF2.PdfFileWriter()
                pdfWriter.addPage(page)

                output_path = filename.replace('.pdf', f'_page_{page_num}.pdf')
                with open(output_path, 'wb') as output_file:
                    pdfWriter.write(output_file)

            pdfFile.close()

def get_pages():
    global pages_to_remove, pages_to_extract
    pages_to_remove = list(map(int, remove_entry.get().split(','))) if remove_entry.get() else []
    pages_to_extract = list(map(int, extract_entry.get().split(','))) if extract_entry.get() else []

pdfiles = []
pages_to_remove = []
pages_to_extract = []

root = tk.Tk()

root.geometry("732x455")
root.title("PDF Tool")

# Buttons
select_button = tk.Button(root, text="Select PDF Files", command=select_files)
select_button.grid(row=0, column=0, pady=10, padx=10)

merge_button = tk.Button(root, text="Merge PDFs", command=merge_pdfs, state=tk.DISABLED)
merge_button.grid(row=1, column=0, pady=10, padx=10)

remove_button = tk.Button(root, text="Remove Pages", command=remove_pages, state=tk.DISABLED)
remove_button.grid(row=2, column=0, pady=10, padx=10)

extract_button = tk.Button(root, text="Extract Pages", command=extract_pages, state=tk.DISABLED)
extract_button.grid(row=3, column=0, pady=10, padx=10)

# Entry fields for page numbers
remove_entry = tk.Entry(root, width=30)
remove_entry.grid(row=2, column=1, pady=10, padx=10)
remove_label = tk.Label(root, text="Remove Pages (comma-separated):")
remove_label.grid(row=2, column=2, pady=10)

extract_entry = tk.Entry(root, width=30)
extract_entry.grid(row=3, column=1, pady=10, padx=10)
extract_label = tk.Label(root, text="Extract Pages (comma-separated):")
extract_label.grid(row=3, column=2, pady=10)

get_pages_button = tk.Button(root, text="Get Pages", command=get_pages)
get_pages_button.grid(row=4, column=1, pady=10)

root.mainloop()

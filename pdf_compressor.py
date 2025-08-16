import subprocess
import os

def compress_pdf(input_path, output_path):
    gs_command = [
        'gswin64c',
        '-sDEVICE=pdfwrite',
        '-dCompatibilityLevel=1.4',
        '-dPDFSETTINGS=/screen', 
        '-dNOPAUSE',
        '-dQUIET',
        '-dBATCH',
        f'-sOutputFile={output_path}',
        input_path
    ]
    
    try:
        subprocess.run(gs_command, check=True)
        print(f"Compressed PDF saved to: {output_path}")
    except subprocess.CalledProcessError as e:
        print(f"Error during compression: {e}")
    except FileNotFoundError:
        print("Error: Ghostscript not found. Please make sure it's installed and in your PATH.")

input_pdf = "ebook2.pdf"
filename = os.path.splitext(input_pdf)[0]
output_pdf = f"{filename} compressed.pdf"

compress_pdf(input_pdf, output_pdf)

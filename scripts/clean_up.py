import os


remove_these = [
    "bytes.bin",
    "chars.txt",
    "data.bin",
    "data.txt",
    "df.csv",
    "dict.tsv",
    "dict.txt",
    "even_lines.txt",
    "finished.txt",
    "fruits.txt",
    "gene_data.txt",
    "headers.txt",
    "log.txt",
    "multi.txt",
    "numbers.dat",
    "numbers.txt",
    "output.txt",
    "pairs.csv",
    "sample.txt",
    "sequences.fasta",
    "table.csv",
    "temp.txt",
    "test.txt",
    "upper.txt",
    "words.txt",
]

for file_name in remove_these:
    try:
        path = os.path.join("io_files_contexts", "practice_solutions", file_name)
        os.remove(path)
    except FileNotFoundError:
        pass

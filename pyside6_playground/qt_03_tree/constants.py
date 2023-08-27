from typing import Union

File = str
Directory = list[Union[File, "Directory"]]
Tree = dict[str, Directory]

# An example file structure
FILES: Tree = {
    "dir 1": ["file1.png", "file2.csv", "file3.pdf"],
    "dir 2": ["file4.docx"],
    "dir 3": [],
}

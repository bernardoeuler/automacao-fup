def createPythonFile(code: str, file_name: str):
    with open(file_name, "w") as code_file:
        code_file.write(code)

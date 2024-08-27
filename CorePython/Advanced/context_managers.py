# context managers handles file processing even if exception occurs in between. if we are performing some operations on a file and if exception occurs, file may not be closed and this may create memory leaks
# to create custom context manager, we need to override enter and exit methods
# custom context manager:

class FileManager:
    def __init__(self, filename, mode):
        self.filename = filename
        self.mode = mode
        self.file = None

    def __enter__(self):
        # open the file
        self.file = open(self.filename, self.mode)
        print(f"Opening file {self.filename}")
        return self.file

    def __exit__(self, exc_type, exc_val, exc_tb):
        # Close the file
        self.file.close()
        print(f"Closing file {self.filename}")
        # Handle exceptions if any
        if exc_type:
            print(f"Exception occured: {exc_val}")
        return True # even if exception occurs, bypass and close the file

if __name__ == "__main__":
    with FileManager("example.txt", "w") as file:
        file.write("Hello world")
        print("File written successfully")

    # If there's an exception within the 'with' block, it will be handled by __exit__.
    with FileManager("example.txt", "r") as file:
        content = file.read()
        raise Exception("xyz")
        print(f"File content: {content}")


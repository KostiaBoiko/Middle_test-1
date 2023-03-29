import os


class Loader:
    def __init__(self):
        self.folder_path = "files"

    def read_files(self):
        for file_name in os.listdir(self.folder_path):
            if file_name.endswith(".txt"):
                with open(os.path.join(self.folder_path, file_name), "r") as f:
                    if file_name == "file_1.txt":
                        file1_lines = f.readlines()
                    elif file_name == "file_2.txt":
                        file2_lines = f.readlines()
        return file1_lines, file2_lines

    def write_same_lines(self, file1, file2):
        same_lines = set(file1).intersection(file2)
        return same_lines

    def write_diff_lines(self, file1, file2):
        diff_lines = set(file1).symmetric_difference(file2)
        return diff_lines

    def write_to_files(self, samelines, difflines):
        with open(os.path.join(self.folder_path, "same.txt"), "w") as same_file:
            for line in samelines:
                same_file.write(line)

        with open(os.path.join(self.folder_path, "diff.txt"), "w") as diff_file:
            for line in difflines:
                diff_file.write(line)


loader = Loader()
file_1, file_2 = loader.read_files()
same_lines = loader.write_same_lines(file_1, file_2)
diff_lines = loader.write_diff_lines(file_1, file_2)
loader.write_to_files(same_lines, diff_lines)

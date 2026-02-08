from typing import List

class Solution:
    def createListFromDict(self, dictionary: dict[str: List[str]]) -> List[List[str]]:
        final_list = []
        for values in dictionary.values():
            if len(values) > 1:
                final_list.append(values)

        return final_list

    def createDirectory(self, path: List[str], path_file: List[str]) -> List[List[str]]:
        path = "".join(path)
        path_file = "".join(path_file)
        return path + "/" +  path_file

    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        duplicates = dict()

        for path in paths:
            file_path = [] # The actual path of the directory excluding the files
            file_found = False  # Boolean to check if file is found
            content_found = False  # Boolean to check if content is found
            path_files = []  # Files extracted from the path
            path_file = []  # A single file 
            content = []  # A single content

            for char in path:
                if char == " ":  # If a space is found it means we got a file
                    file_found = True

                    if path_file:
                        path_files.append("".join(path_file))
                        path_file = []

                elif char == "(":  # If an opening bracket is found it means we found a content
                    content_found = True
                    path_files.append("".join(path_file))
                    path_file = []

                elif char == ")" and content_found:  # If we found a closing bracket, it means we know what our file content is 
                    content_found = False
                    file_content = "".join(content)
                    content = []
                    if file_content in duplicates:
                        duplicates[file_content] += [self.createDirectory(file_path, path_files[-1])]
                    
                    else:
                        duplicates[file_content] = [self.createDirectory(file_path, path_files[-1])]

                else:  # If we find other characters
                    if content_found:  # They maybe a content in a file
                        content.append(char)

                    elif file_found:  # The actual file
                        path_file.append(char)

                    else:  # Or they are just a paths
                        file_path.append(char)

        return self.createListFromDict(duplicates)

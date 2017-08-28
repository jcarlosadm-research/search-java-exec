import javalang

class JavaAst:
    def __init__(self,filePath):
        content = ""
        with open(filePath) as filedata:
            for line in filedata:
                content += line

        self.tree = javalang.parse.parse(content)

    def is_valid(self):

        class_declr_list = []
        for type in self.tree.types:
            if str(type) == "ClassDeclaration":
                class_declr_list.append(type)

        if not class_declr_list:
            return False

        contains_non_empty_methods = False
        for class_declr in class_declr_list:
            for method in class_declr.methods:
                if len(method.body) > 0:
                    contains_non_empty_methods = True
                    break
            if contains_non_empty_methods == True:
                break

        return contains_non_empty_methods
import os
import unittest
from search.java.exec import JavaAst

VALID_FILE = os.path.join("tests","resources","JavaPatternFinder","src","patternFinder","Main.java")
ENUM_FILE = os.path.join("tests","resources","enumConstantOrdinal.java")
INTERFACE_FILE = os.path.join("tests","resources","Interface.java")
EMPTY_METHOD_FILE = os.path.join("tests","resources","MethodClass.java")
EMPTY_CLASS_FILE = os.path.join("tests","resources","EmptyClass.java")

class JavaAstTest(unittest.TestCase):
    def test_is_valid(self):
        java_ast = JavaAst(VALID_FILE)
        self.assertTrue(java_ast.is_valid())

        java_ast = JavaAst(ENUM_FILE)
        self.assertFalse(java_ast.is_valid())

        java_ast = JavaAst(INTERFACE_FILE)
        self.assertFalse(java_ast.is_valid())

        java_ast = JavaAst(EMPTY_METHOD_FILE)
        self.assertFalse(java_ast.is_valid())

        java_ast = JavaAst(EMPTY_CLASS_FILE)
        self.assertFalse(java_ast.is_valid())
